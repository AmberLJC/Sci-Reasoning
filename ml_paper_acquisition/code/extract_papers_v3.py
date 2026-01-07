"""
ML Conference Paper Extraction Script v3
Extracts oral and spotlight papers from ICML, ICLR, and NeurIPS (2023-2024)
Using OpenReview API with decision-based presentation type detection
"""

import modal
import os
import json
from datetime import datetime

app = modal.App("ml-paper-extraction-v3")

# Image with required packages
extraction_image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install("openreview-py", "requests", "pandas", "tqdm")
)

# Volume for storing results
volume = modal.Volume.from_name("ml-paper-data", create_if_missing=True)

@app.function(
    image=extraction_image,
    volumes={"/workspace": volume},
    timeout=7200,
    cpu=2
)
def extract_all_papers():
    """Extract oral and spotlight papers from all target conferences."""
    import openreview
    from openreview.api import OpenReviewClient
    import pandas as pd
    from collections import defaultdict
    import time
    import re
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting paper extraction v3...")
    
    # Initialize OpenReview client (API v2)
    client = OpenReviewClient(baseurl='https://api2.openreview.net')
    
    # Conference configurations
    conferences = [
        {'venue_id': 'ICLR.cc/2024/Conference', 'year': 2024, 'conference': 'ICLR'},
        {'venue_id': 'ICLR.cc/2023/Conference', 'year': 2023, 'conference': 'ICLR'},
        {'venue_id': 'NeurIPS.cc/2024/Conference', 'year': 2024, 'conference': 'NeurIPS'},
        {'venue_id': 'NeurIPS.cc/2023/Conference', 'year': 2023, 'conference': 'NeurIPS'},
        {'venue_id': 'ICML.cc/2024/Conference', 'year': 2024, 'conference': 'ICML'},
        {'venue_id': 'ICML.cc/2023/Conference', 'year': 2023, 'conference': 'ICML'},
    ]
    
    all_papers = []
    statistics = defaultdict(lambda: defaultdict(int))
    
    def extract_value(field):
        """Extract value from OpenReview field which may be dict or direct value."""
        if isinstance(field, dict):
            return field.get('value', '')
        return field if field else ''
    
    def determine_presentation_type(note, decision_notes=None):
        """Determine presentation type from note content and decision."""
        content = note.content if hasattr(note, 'content') else {}
        
        # Check venueid first
        venueid = extract_value(content.get('venueid', ''))
        venueid_lower = str(venueid).lower()
        
        if 'oral' in venueid_lower:
            return 'oral'
        elif 'spotlight' in venueid_lower:
            return 'spotlight'
        
        # Check venue field
        venue = extract_value(content.get('venue', ''))
        venue_lower = str(venue).lower()
        
        if 'oral' in venue_lower:
            return 'oral'
        elif 'spotlight' in venue_lower:
            return 'spotlight'
        
        # Check decision notes if available
        if decision_notes:
            for dec in decision_notes:
                dec_content = dec.get('content', {})
                decision = extract_value(dec_content.get('decision', ''))
                decision_lower = str(decision).lower()
                
                if 'oral' in decision_lower:
                    return 'oral'
                elif 'spotlight' in decision_lower:
                    return 'spotlight'
        
        return 'poster'
    
    for conf_info in conferences:
        conf_key = f"{conf_info['conference']}_{conf_info['year']}"
        venue_id = conf_info['venue_id']
        
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Processing {conf_key}...")
        
        try:
            # Get all accepted submissions
            print(f"  Querying accepted papers for {venue_id}...")
            
            submissions = list(client.get_all_notes(
                content={'venueid': venue_id},
                details='directReplies'
            ))
            
            print(f"  Found {len(submissions)} accepted papers")
            
            # Also try alternative query for ICLR 2023 which uses API v1
            if len(submissions) == 0 and '2023' in venue_id:
                print(f"  Trying API v1 query...")
                try:
                    client_v1 = openreview.Client(baseurl='https://api.openreview.net')
                    submissions_v1 = list(client_v1.get_all_notes(
                        invitation=f"{venue_id}/-/Blind_Submission"
                    ))
                    print(f"  Found {len(submissions_v1)} submissions via API v1")
                    
                    # Filter for accepted papers
                    for note in submissions_v1:
                        # Check if paper was accepted by looking at replies
                        try:
                            replies = client_v1.get_all_notes(forum=note.forum)
                            decision_notes = [r for r in replies if 'Decision' in str(r.invitation)]
                            
                            is_accepted = False
                            ptype = 'poster'
                            
                            for dec in decision_notes:
                                dec_content = dec.content if hasattr(dec, 'content') else {}
                                decision = dec_content.get('decision', '')
                                if 'Accept' in str(decision):
                                    is_accepted = True
                                    if 'oral' in str(decision).lower():
                                        ptype = 'oral'
                                    elif 'spotlight' in str(decision).lower():
                                        ptype = 'spotlight'
                                    break
                            
                            if is_accepted:
                                content = note.content if hasattr(note, 'content') else {}
                                paper_data = {
                                    'title': content.get('title', 'Unknown'),
                                    'authors': ', '.join(content.get('authors', [])) if isinstance(content.get('authors'), list) else str(content.get('authors', '')),
                                    'abstract': str(content.get('abstract', ''))[:1000],
                                    'keywords': ', '.join(content.get('keywords', [])) if isinstance(content.get('keywords'), list) else '',
                                    'conference': conf_info['conference'],
                                    'year': conf_info['year'],
                                    'presentation_type': ptype,
                                    'venueid': venue_id,
                                    'openreview_id': note.id if hasattr(note, 'id') else '',
                                    'forum_id': note.forum if hasattr(note, 'forum') else '',
                                }
                                all_papers.append(paper_data)
                                statistics[conf_key][ptype] += 1
                        except Exception as e:
                            continue
                    
                    print(f"  {conf_key} (API v1) complete: {dict(statistics[conf_key])}")
                    time.sleep(2)
                    continue
                    
                except Exception as e:
                    print(f"  API v1 query failed: {e}")
            
            # Process API v2 submissions
            for note in submissions:
                try:
                    content = note.content if hasattr(note, 'content') else {}
                    
                    # Get decision notes from directReplies
                    decision_notes = []
                    if hasattr(note, 'details') and note.details:
                        replies = note.details.get('directReplies', [])
                        decision_notes = [r for r in replies if 'Decision' in str(r.get('invitation', ''))]
                    
                    # Determine presentation type
                    ptype = determine_presentation_type(note, decision_notes)
                    
                    # Extract fields
                    title = extract_value(content.get('title', 'Unknown'))
                    
                    authors = content.get('authors', {})
                    if isinstance(authors, dict):
                        authors = authors.get('value', [])
                    authors_str = ', '.join(authors) if isinstance(authors, list) else str(authors)
                    
                    abstract = extract_value(content.get('abstract', ''))
                    
                    keywords = content.get('keywords', {})
                    if isinstance(keywords, dict):
                        keywords = keywords.get('value', [])
                    keywords_str = ', '.join(keywords) if isinstance(keywords, list) else ''
                    
                    paper_data = {
                        'title': title,
                        'authors': authors_str,
                        'abstract': abstract[:1000] if abstract else '',
                        'keywords': keywords_str,
                        'conference': conf_info['conference'],
                        'year': conf_info['year'],
                        'presentation_type': ptype,
                        'venueid': extract_value(content.get('venueid', '')),
                        'openreview_id': note.id if hasattr(note, 'id') else '',
                        'forum_id': note.forum if hasattr(note, 'forum') else '',
                    }
                    
                    all_papers.append(paper_data)
                    statistics[conf_key][ptype] += 1
                    
                except Exception as e:
                    print(f"    Error processing paper: {e}")
                    continue
            
            print(f"  {conf_key} complete: {dict(statistics[conf_key])}")
            
        except Exception as e:
            print(f"  Error processing {conf_key}: {e}")
            import traceback
            traceback.print_exc()
        
        time.sleep(2)
    
    # Save results
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Saving results...")
    
    os.makedirs("/workspace/data", exist_ok=True)
    
    # Save all papers
    with open("/workspace/data/all_papers.json", 'w') as f:
        json.dump(all_papers, f, indent=2)
    
    df = pd.DataFrame(all_papers)
    df.to_csv("/workspace/data/all_papers.csv", index=False)
    
    # Filter for orals and spotlights only
    oral_spotlight_papers = [p for p in all_papers if p['presentation_type'] in ['oral', 'spotlight']]
    
    with open("/workspace/data/oral_spotlight_papers.json", 'w') as f:
        json.dump(oral_spotlight_papers, f, indent=2)
    
    df_os = pd.DataFrame(oral_spotlight_papers)
    if len(df_os) > 0:
        df_os.to_csv("/workspace/data/oral_spotlight_papers.csv", index=False)
    
    # Calculate statistics
    stats_summary = {
        'extraction_date': datetime.now().isoformat(),
        'total_papers': len(all_papers),
        'oral_spotlight_papers': len(oral_spotlight_papers),
        'by_conference': {},
        'by_type': defaultdict(int),
        'by_conference_and_type': {}
    }
    
    for conf_key, conf_stats in statistics.items():
        stats_summary['by_conference'][conf_key] = sum(conf_stats.values())
        stats_summary['by_conference_and_type'][conf_key] = dict(conf_stats)
        for ptype, count in conf_stats.items():
            stats_summary['by_type'][ptype] += count
    
    stats_summary['by_type'] = dict(stats_summary['by_type'])
    
    with open("/workspace/data/statistics.json", 'w') as f:
        json.dump(stats_summary, f, indent=2)
    
    volume.commit()
    
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Extraction complete!")
    print(f"\n{'='*60}")
    print("FINAL STATISTICS")
    print('='*60)
    print(f"Total papers extracted: {len(all_papers)}")
    print(f"Oral + Spotlight papers: {len(oral_spotlight_papers)}")
    print(f"\nBy conference:")
    for conf, count in stats_summary['by_conference'].items():
        print(f"  {conf}: {count} papers")
        if conf in stats_summary['by_conference_and_type']:
            for ptype, pcount in stats_summary['by_conference_and_type'][conf].items():
                print(f"    - {ptype}: {pcount}")
    
    print(f"\nBy type:")
    for ptype, count in stats_summary['by_type'].items():
        print(f"  {ptype}: {count}")
    
    return stats_summary


@app.local_entrypoint()
def main():
    print("Starting ML Paper Extraction Pipeline v3...")
    stats = extract_all_papers.remote()
    print("\n" + "="*60)
    print("EXTRACTION COMPLETE")
    print("="*60)
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
