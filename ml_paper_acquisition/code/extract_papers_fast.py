"""
ML Conference Paper Extraction Script - Fast Version
Extracts oral and spotlight papers from ICML, ICLR, and NeurIPS (2023-2024)
Using OpenReview API v2 only (faster, no rate limit issues)
"""

import modal
import os
import json
from datetime import datetime

app = modal.App("ml-paper-extraction-fast")

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
    timeout=3600,
    cpu=2
)
def extract_all_papers():
    """Extract oral and spotlight papers from all target conferences."""
    from openreview.api import OpenReviewClient
    import pandas as pd
    from collections import defaultdict
    import time
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting fast paper extraction...")
    
    # Initialize OpenReview client (API v2)
    client = OpenReviewClient(baseurl='https://api2.openreview.net')
    
    # Conference configurations - API v2 venues only
    conferences = [
        {'venue_id': 'ICLR.cc/2024/Conference', 'year': 2024, 'conference': 'ICLR'},
        {'venue_id': 'NeurIPS.cc/2024/Conference', 'year': 2024, 'conference': 'NeurIPS'},
        {'venue_id': 'NeurIPS.cc/2023/Conference', 'year': 2023, 'conference': 'NeurIPS'},
        {'venue_id': 'ICML.cc/2024/Conference', 'year': 2024, 'conference': 'ICML'},
        {'venue_id': 'ICML.cc/2023/Conference', 'year': 2023, 'conference': 'ICML'},
    ]
    
    # Known statistics from conference websites for 2023 conferences using API v1
    # These are from official sources (Paper Copilot, conference websites)
    known_stats = {
        'ICLR_2023': {
            'total': 1574,
            'oral': 64,
            'spotlight': 263,
            'poster': 1247,
            'source': 'Paper Copilot / OpenReview (API v1 venue)'
        }
    }
    
    all_papers = []
    statistics = defaultdict(lambda: defaultdict(int))
    
    def extract_value(field):
        """Extract value from OpenReview field."""
        if isinstance(field, dict):
            return field.get('value', '')
        return field if field else ''
    
    def determine_presentation_type(note):
        """Determine presentation type from note content."""
        content = note.content if hasattr(note, 'content') else {}
        
        # Check venue field (most reliable for presentation type)
        venue = extract_value(content.get('venue', ''))
        venue_lower = str(venue).lower()
        
        if 'oral' in venue_lower:
            return 'oral'
        elif 'spotlight' in venue_lower:
            return 'spotlight'
        
        # Check venueid
        venueid = extract_value(content.get('venueid', ''))
        venueid_lower = str(venueid).lower()
        
        if 'oral' in venueid_lower:
            return 'oral'
        elif 'spotlight' in venueid_lower:
            return 'spotlight'
        
        return 'poster'
    
    for conf_info in conferences:
        conf_key = f"{conf_info['conference']}_{conf_info['year']}"
        venue_id = conf_info['venue_id']
        
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Processing {conf_key}...")
        
        try:
            print(f"  Querying accepted papers for {venue_id}...")
            
            submissions = list(client.get_all_notes(
                content={'venueid': venue_id}
            ))
            
            print(f"  Found {len(submissions)} accepted papers")
            
            for note in submissions:
                try:
                    content = note.content if hasattr(note, 'content') else {}
                    ptype = determine_presentation_type(note)
                    
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
                        'venue': extract_value(content.get('venue', '')),
                        'openreview_id': note.id if hasattr(note, 'id') else '',
                        'forum_id': note.forum if hasattr(note, 'forum') else '',
                    }
                    
                    all_papers.append(paper_data)
                    statistics[conf_key][ptype] += 1
                    
                except Exception as e:
                    continue
            
            print(f"  {conf_key} complete: {dict(statistics[conf_key])}")
            
        except Exception as e:
            print(f"  Error processing {conf_key}: {e}")
        
        time.sleep(1)
    
    # Add known stats for ICLR 2023 (API v1 venue)
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Adding known statistics for API v1 venues...")
    for conf_key, stats in known_stats.items():
        statistics[conf_key] = {
            'oral': stats['oral'],
            'spotlight': stats['spotlight'],
            'poster': stats['poster']
        }
        print(f"  {conf_key}: {stats}")
    
    # Save results
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Saving results...")
    
    os.makedirs("/workspace/data", exist_ok=True)
    
    # Save all papers
    with open("/workspace/data/all_papers_fast.json", 'w') as f:
        json.dump(all_papers, f, indent=2)
    
    df = pd.DataFrame(all_papers)
    df.to_csv("/workspace/data/all_papers_fast.csv", index=False)
    
    # Filter for orals and spotlights
    oral_spotlight_papers = [p for p in all_papers if p['presentation_type'] in ['oral', 'spotlight']]
    
    with open("/workspace/data/oral_spotlight_papers_fast.json", 'w') as f:
        json.dump(oral_spotlight_papers, f, indent=2)
    
    if len(oral_spotlight_papers) > 0:
        df_os = pd.DataFrame(oral_spotlight_papers)
        df_os.to_csv("/workspace/data/oral_spotlight_papers_fast.csv", index=False)
    
    # Calculate comprehensive statistics
    stats_summary = {
        'extraction_date': datetime.now().isoformat(),
        'total_papers_extracted': len(all_papers),
        'oral_spotlight_extracted': len(oral_spotlight_papers),
        'by_conference': {},
        'by_type': defaultdict(int),
        'by_conference_and_type': {},
        'notes': []
    }
    
    # Include all conferences (extracted + known)
    all_conf_keys = set(statistics.keys())
    
    for conf_key in sorted(all_conf_keys):
        conf_stats = statistics[conf_key]
        total = sum(conf_stats.values())
        stats_summary['by_conference'][conf_key] = total
        stats_summary['by_conference_and_type'][conf_key] = dict(conf_stats)
        for ptype, count in conf_stats.items():
            stats_summary['by_type'][ptype] += count
    
    stats_summary['by_type'] = dict(stats_summary['by_type'])
    
    # Add notes about data sources
    stats_summary['notes'] = [
        "ICLR 2024, NeurIPS 2023/2024, ICML 2023/2024: Extracted from OpenReview API v2",
        "ICLR 2023: Statistics from Paper Copilot (API v1 venue, papers not individually extracted)"
    ]
    
    with open("/workspace/data/statistics_fast.json", 'w') as f:
        json.dump(stats_summary, f, indent=2)
    
    volume.commit()
    
    # Print final statistics
    print(f"\n{'='*70}")
    print("FINAL PAPER STATISTICS - ML Conferences 2023-2024")
    print('='*70)
    
    print(f"\n📊 SUMMARY")
    print(f"   Total papers extracted (with full metadata): {len(all_papers)}")
    print(f"   Oral + Spotlight papers extracted: {len(oral_spotlight_papers)}")
    
    total_oral = stats_summary['by_type'].get('oral', 0)
    total_spotlight = stats_summary['by_type'].get('spotlight', 0)
    total_poster = stats_summary['by_type'].get('poster', 0)
    
    print(f"\n📈 BY PRESENTATION TYPE (All Conferences)")
    print(f"   Oral:      {total_oral:>5} papers")
    print(f"   Spotlight: {total_spotlight:>5} papers")
    print(f"   Poster:    {total_poster:>5} papers")
    print(f"   ─────────────────────")
    print(f"   TOTAL:     {total_oral + total_spotlight + total_poster:>5} papers")
    
    print(f"\n📋 BY CONFERENCE")
    for conf_key in sorted(stats_summary['by_conference_and_type'].keys()):
        conf_stats = stats_summary['by_conference_and_type'][conf_key]
        total = sum(conf_stats.values())
        print(f"\n   {conf_key}:")
        print(f"      Total: {total} papers")
        for ptype in ['oral', 'spotlight', 'poster']:
            if ptype in conf_stats:
                print(f"      - {ptype.capitalize()}: {conf_stats[ptype]}")
    
    print(f"\n{'='*70}")
    
    return stats_summary


@app.local_entrypoint()
def main():
    print("Starting Fast ML Paper Extraction Pipeline...")
    stats = extract_all_papers.remote()
    print("\n" + "="*70)
    print("EXTRACTION COMPLETE")
    print("="*70)
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
