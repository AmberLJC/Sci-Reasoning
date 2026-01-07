#!/usr/bin/env python3
"""
Prior Work Extraction Pipeline

This pipeline analyzes AI research papers to identify key prior works
and document their relationships to the current paper.

Uses GPT-5 for analysis.
"""

import os
import json
import re
import requests
from typing import Optional, Dict, List, Any
from dataclasses import dataclass, asdict
from datetime import datetime
import time

# OpenAI API configuration
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

# Role classifications
VALID_ROLES = [
    "Baseline",
    "Inspiration", 
    "Gap Identification",
    "Foundation",
    "Extension",
    "Related Problem"
]

@dataclass
class PriorWork:
    """Represents a prior work paper and its relationship to the current paper."""
    title: str
    authors: str
    year: Optional[int]
    role: str
    relationship_sentence: str
    arxiv_id: Optional[str] = None
    url: Optional[str] = None

@dataclass
class PriorWorkAnalysis:
    """Complete analysis of prior works for a paper."""
    paper_title: str
    paper_arxiv_id: str
    paper_abstract: str
    prior_works: List[PriorWork]
    synthesis_narrative: str
    analysis_timestamp: str


def fetch_arxiv_metadata(arxiv_id: str) -> Dict[str, Any]:
    """Fetch paper metadata from arXiv API."""
    # Clean the arxiv_id
    arxiv_id = arxiv_id.replace("https://arxiv.org/abs/", "").replace("https://www.arxiv.org/abs/", "")
    arxiv_id = arxiv_id.rstrip('/')
    
    api_url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    
    print(f"[INFO] Fetching metadata for arXiv:{arxiv_id}")
    response = requests.get(api_url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch arXiv metadata: {response.status_code}")
    
    # Parse the XML response
    import xml.etree.ElementTree as ET
    root = ET.fromstring(response.content)
    
    # Define namespace
    ns = {
        'atom': 'http://www.w3.org/2005/Atom',
        'arxiv': 'http://arxiv.org/schemas/atom'
    }
    
    entry = root.find('atom:entry', ns)
    if entry is None:
        raise Exception(f"No entry found for arXiv:{arxiv_id}")
    
    title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
    abstract = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
    
    authors = []
    for author in entry.findall('atom:author', ns):
        name = author.find('atom:name', ns).text
        authors.append(name)
    
    published = entry.find('atom:published', ns).text
    year = int(published[:4]) if published else None
    
    # Get PDF link
    pdf_link = None
    for link in entry.findall('atom:link', ns):
        if link.get('title') == 'pdf':
            pdf_link = link.get('href')
            break
    
    return {
        'arxiv_id': arxiv_id,
        'title': title,
        'abstract': abstract,
        'authors': authors,
        'year': year,
        'pdf_url': pdf_link
    }


def download_and_extract_pdf(pdf_url: str, max_words: int = 8000, max_pages: int = 15) -> str:
    """Download PDF and extract text content using multiple methods."""
    print(f"[INFO] Downloading PDF from {pdf_url}")
    
    response = requests.get(pdf_url)
    if response.status_code != 200:
        raise Exception(f"Failed to download PDF: {response.status_code}")
    
    # Save temporarily
    temp_path = "/tmp/temp_paper.pdf"
    with open(temp_path, 'wb') as f:
        f.write(response.content)
    
    text = ""
    
    # Method 1: Try PyMuPDF (fitz) - best quality
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(temp_path)
        for page_num in range(min(max_pages, len(doc))):
            page = doc[page_num]
            text += page.get_text() + "\n"
        doc.close()
        print(f"[INFO] Extracted text using PyMuPDF")
    except Exception as e:
        print(f"[WARN] PyMuPDF failed: {e}")
    
    # Method 2: Try PyPDF2 as fallback
    if not text.strip():
        try:
            import PyPDF2
            with open(temp_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                for page_num in range(min(max_pages, len(reader.pages))):
                    text += reader.pages[page_num].extract_text() + "\n"
            print(f"[INFO] Extracted text using PyPDF2")
        except Exception as e:
            print(f"[WARN] PyPDF2 failed: {e}")
    
    # Method 3: Try pdftotext command line tool
    if not text.strip():
        try:
            import subprocess
            result = subprocess.run(
                ['pdftotext', '-layout', '-l', str(max_pages), temp_path, '-'],
                capture_output=True,
                text=True,
                timeout=60
            )
            if result.returncode == 0:
                text = result.stdout
                print(f"[INFO] Extracted text using pdftotext")
        except Exception as e:
            print(f"[WARN] pdftotext failed: {e}")
    
    # Truncate to max_words
    words = text.split()
    if len(words) > max_words:
        text = ' '.join(words[:max_words])
        print(f"[INFO] Truncated text to {max_words} words (from {len(words)})")
    else:
        print(f"[INFO] Extracted {len(words)} words from PDF")
    
    # Clean up
    if os.path.exists(temp_path):
        os.remove(temp_path)
    
    return text


def call_gpt5(messages: List[Dict], api_key: str) -> str:
    """Call GPT-5 API with the given messages."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "gpt-5",  # GPT-5 model
        "messages": messages
    }
    
    print("[INFO] Calling GPT-5 API...")
    response = requests.post(
        OPENAI_API_URL,
        headers=headers,
        json=payload,
        timeout=300
    )
    
    if response.status_code != 200:
        raise Exception(f"GPT-5 API error: {response.status_code} - {response.text}")
    
    result = response.json()
    return result['choices'][0]['message']['content']


def analyze_prior_works(paper_metadata: Dict, paper_text: str, api_key: str) -> Dict:
    """Use GPT-5 to analyze prior works and their relationships."""
    
    system_prompt = """You are an expert AI research analyst. Your task is to identify the KEY PRIOR WORKS that DIRECTLY led to a research paper's core innovation.

## CRITICAL: Focus on DIRECT Intellectual Lineage

You must identify papers that are **directly responsible** for the current paper's main contributions. Ask yourself:
- "Without this prior work, would the current paper's core idea exist?"
- "Did this prior work directly inspire, enable, or motivate the KEY INNOVATION?"
- "Is this paper cited in the Introduction or Related Work as a PRIMARY influence?"

### ❌ DO NOT INCLUDE:
- Generic infrastructure/tools (e.g., PyTorch, CUDA, standard attention mechanisms)
- Complementary optimizations that are orthogonal to the main contribution
- Papers that share the same domain but don't directly influence the core idea
- Standard baselines that are just compared against without deeper connection
- Well-known foundational works that everyone cites but aren't specific to this innovation

### ✅ DO INCLUDE:
- Papers whose specific IDEAS, METHODS, or FINDINGS directly shaped the current work
- Papers whose LIMITATIONS or GAPS the current paper explicitly addresses
- Papers that introduced the PROBLEM FORMULATION the current paper builds on
- Papers whose TECHNIQUES are directly extended or modified
- Papers that provide the KEY INSIGHT that the current paper leverages

## Role Classifications (assign ONE per paper):

1. **Baseline**: The primary system/method this paper improves upon or compares against as its main competitor
2. **Inspiration**: Paper whose specific idea/approach directly sparked the current paper's key innovation  
3. **Gap Identification**: Paper whose explicit limitations/failures motivated this research direction
4. **Foundation**: Paper that introduced the core problem formulation, dataset, or theoretical framework used
5. **Extension**: Paper whose specific method is directly extended, modified, or generalized
6. **Related Problem**: Paper solving a closely related problem whose solution approach informed this work

## Output Requirements:

For each prior work (identify 5-7 papers, quality over quantity):
1. **Role**: One of the six classifications above
2. **Relationship Sentence**: ONE specific sentence explaining the DIRECT connection to the current paper's innovation. Be concrete about WHAT was borrowed/extended/addressed.

## Synthesis Narrative (200-300 words):
Write a cohesive narrative that flows naturally (NO explicit "Part 1" / "Part 2" labels):

**First ~150 words - Prior Work with Relevant Details:**
Describe each prior work, but FOCUS ONLY on the specific aspects/details that relate to the current paper's innovation. For each prior work, highlight:
- The specific technique, insight, or finding that is relevant (not a general summary)
- How this specific detail connects to what the current paper does
- Do NOT mention the current paper yet - just establish what relevant knowledge existed

**Remaining ~100 words - How They Collectively Inspired Current Work:**
Transition naturally to explain:
- What gap or opportunity emerged from the combination of these prior works
- How the current paper synthesizes or builds upon these specific relevant details
- Why this was a natural next step given the prior work landscape

The narrative should read as one flowing paragraph, not two separate sections.

## Output Format (JSON):
```json
{
  "prior_works": [
    {
      "title": "Exact paper title",
      "authors": "First author et al.",
      "year": 2023,
      "arxiv_id": "if known",
      "role": "One of six roles",
      "relationship_sentence": "Specific sentence about DIRECT connection to core innovation"
    }
  ],
  "synthesis_narrative": "200-300 word flowing narrative: describe prior works focusing on details relevant to current paper, then show how they collectively inspired this work"
}
```

Remember: Every paper you include should pass the test: "This paper DIRECTLY influenced the core innovation, not just the general research area."
"""

    user_prompt = f"""Analyze this research paper and identify the prior works that DIRECTLY led to its core innovation.

## Paper Title:
{paper_metadata['title']}

## Authors:
{', '.join(paper_metadata['authors'])}

## Abstract:
{paper_metadata['abstract']}

## Paper Content (first ~8000 words / 15 pages):
{paper_text if paper_text.strip() else "[PDF extraction unavailable - analyze based on title and abstract]"}

---

TASK: Identify 5-7 prior works that DIRECTLY influenced this paper's KEY CONTRIBUTION. 

Focus on papers that:
1. Introduced ideas/methods this paper directly builds on
2. Had limitations this paper explicitly addresses  
3. Defined the problem formulation used here
4. Are the primary baselines being improved upon

DO NOT include generic tools, orthogonal optimizations, or tangentially related work.

Return your analysis as valid JSON."""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    response_text = call_gpt5(messages, api_key)
    
    # Parse JSON from response
    try:
        # Try to find JSON in the response (handle markdown code blocks)
        json_match = re.search(r'```(?:json)?\s*(\{[\s\S]*?\})\s*```', response_text)
        if json_match:
            analysis = json.loads(json_match.group(1))
        else:
            # Try direct JSON parsing
            json_match = re.search(r'\{[\s\S]*\}', response_text)
            if json_match:
                analysis = json.loads(json_match.group())
            else:
                raise ValueError("No JSON found in response")
    except json.JSONDecodeError as e:
        print(f"[WARN] Failed to parse JSON: {e}")
        print(f"[DEBUG] Response preview: {response_text[:1500]}...")
        raise
    
    return analysis


def run_pipeline(arxiv_url: str, api_key: str, output_dir: str = "results") -> PriorWorkAnalysis:
    """Run the complete prior work extraction pipeline."""
    
    print("=" * 70)
    print("PRIOR WORK EXTRACTION PIPELINE (v2 - Direct Lineage Focus)")
    print("=" * 70)
    
    # Step 1: Fetch paper metadata
    print("\n[STEP 1] Fetching paper metadata from arXiv...")
    metadata = fetch_arxiv_metadata(arxiv_url)
    print(f"  Title: {metadata['title']}")
    print(f"  Authors: {', '.join(metadata['authors'][:3])}{'...' if len(metadata['authors']) > 3 else ''}")
    print(f"  Year: {metadata['year']}")
    
    # Step 2: Download and extract PDF text
    print("\n[STEP 2] Downloading and extracting PDF content...")
    paper_text = ""
    if metadata['pdf_url']:
        try:
            paper_text = download_and_extract_pdf(metadata['pdf_url'])
        except Exception as e:
            print(f"[WARN] PDF extraction failed: {e}")
            print("[INFO] Will analyze based on abstract only")
    else:
        print("[WARN] No PDF URL found, using abstract only")
    
    # Step 3: Analyze prior works using GPT-5
    print("\n[STEP 3] Analyzing prior works with GPT-5...")
    analysis = analyze_prior_works(metadata, paper_text, api_key)
    
    # Step 4: Format results
    print("\n[STEP 4] Formatting results...")
    prior_works = []
    for pw in analysis.get('prior_works', []):
        prior_works.append(PriorWork(
            title=pw.get('title', 'Unknown'),
            authors=pw.get('authors', 'Unknown'),
            year=pw.get('year'),
            role=pw.get('role', 'Foundation'),
            relationship_sentence=pw.get('relationship_sentence', ''),
            arxiv_id=pw.get('arxiv_id'),
            url=pw.get('url')
        ))
    
    result = PriorWorkAnalysis(
        paper_title=metadata['title'],
        paper_arxiv_id=metadata['arxiv_id'],
        paper_abstract=metadata['abstract'],
        prior_works=prior_works,
        synthesis_narrative=analysis.get('synthesis_narrative', ''),
        analysis_timestamp=datetime.now().isoformat()
    )
    
    # Step 5: Save results
    print("\n[STEP 5] Saving results...")
    os.makedirs(output_dir, exist_ok=True)
    
    safe_arxiv_id = metadata['arxiv_id'].replace('/', '_').replace('.', '_')
    output_file = os.path.join(output_dir, f"prior_work_analysis_{safe_arxiv_id}.json")
    with open(output_file, 'w') as f:
        json.dump(asdict(result), f, indent=2)
    print(f"  Saved JSON to: {output_file}")
    
    # Also create a markdown report
    md_report = generate_markdown_report(result)
    md_file = os.path.join(output_dir, f"prior_work_analysis_{safe_arxiv_id}.md")
    with open(md_file, 'w') as f:
        f.write(md_report)
    print(f"  Saved Markdown to: {md_file}")
    
    print("\n" + "=" * 70)
    print("PIPELINE COMPLETE")
    print("=" * 70)
    
    return result


def generate_markdown_report(analysis: PriorWorkAnalysis) -> str:
    """Generate a markdown report from the analysis."""
    
    report = f"""# Prior Work Analysis Report

## Target Paper

**Title:** {analysis.paper_title}

**arXiv ID:** [{analysis.paper_arxiv_id}](https://arxiv.org/abs/{analysis.paper_arxiv_id})

**Abstract:** 
> {analysis.paper_abstract}

---

## Key Prior Works ({len(analysis.prior_works)} papers with direct influence)

"""
    
    # Group by role
    roles_order = ["Foundation", "Inspiration", "Gap Identification", "Baseline", "Extension", "Related Problem"]
    by_role = {}
    for pw in analysis.prior_works:
        role = pw.role
        if role not in by_role:
            by_role[role] = []
        by_role[role].append(pw)
    
    for role in roles_order:
        if role in by_role:
            report += f"### 🏷️ {role}\n\n"
            for pw in by_role[role]:
                year_str = f" ({pw.year})" if pw.year else ""
                arxiv_str = f" [[arXiv](https://arxiv.org/abs/{pw.arxiv_id})]" if pw.arxiv_id else ""
                report += f"""**{pw.title}**{year_str}{arxiv_str}
- *Authors:* {pw.authors}
- *Direct Connection:* {pw.relationship_sentence}

"""
    
    report += f"""---

## Synthesis: How Prior Work Led to This Paper

{analysis.synthesis_narrative}

---

*Analysis generated on: {analysis.analysis_timestamp}*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
"""
    
    return report


def print_analysis_summary(analysis: PriorWorkAnalysis):
    """Print a summary of the analysis to console."""
    
    print("\n" + "=" * 70)
    print("ANALYSIS SUMMARY")
    print("=" * 70)
    
    print(f"\n📄 Paper: {analysis.paper_title}")
    print(f"🔗 arXiv: {analysis.paper_arxiv_id}")
    
    print(f"\n📚 Identified {len(analysis.prior_works)} Key Prior Works (Direct Lineage):")
    print("-" * 50)
    
    for i, pw in enumerate(analysis.prior_works, 1):
        year_str = f" ({pw.year})" if pw.year else ""
        print(f"\n{i}. {pw.title}{year_str}")
        print(f"   📌 Role: [{pw.role}]")
        print(f"   → {pw.relationship_sentence}")
    
    print("\n" + "-" * 50)
    print("\n📝 SYNTHESIS NARRATIVE:")
    print("-" * 50)
    
    # Word wrap the narrative for better display
    words = analysis.synthesis_narrative.split()
    lines = []
    current_line = []
    for word in words:
        current_line.append(word)
        if len(' '.join(current_line)) > 80:
            lines.append(' '.join(current_line[:-1]))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
    
    print('\n'.join(lines))


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Prior Work Extraction Pipeline")
    parser.add_argument("--arxiv", type=str, required=True, help="arXiv URL or ID")
    parser.add_argument("--api-key", type=str, help="OpenAI API key")
    parser.add_argument("--output-dir", type=str, default="results", help="Output directory")
    
    args = parser.parse_args()
    
    api_key = args.api_key or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Please provide OpenAI API key via --api-key or OPENAI_API_KEY env var")
    
    result = run_pipeline(args.arxiv, api_key, args.output_dir)
    print_analysis_summary(result)
