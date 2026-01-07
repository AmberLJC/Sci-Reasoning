"""
ML Conference Paper Extraction Script - 2025 Conferences
Extracts oral and spotlight papers from ICML, ICLR, and NeurIPS 2025
Using OpenReview API v2
"""

import modal
import os
import json
from datetime import datetime

app = modal.App("ml-paper-extraction-2025")

extraction_image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install("openreview-py", "requests", "pandas", "tqdm")
)

volume = modal.Volume.from_name("ml-paper-data", create_if_missing=True)

@app.function(
    image=extraction_image,
    volumes={"/workspace": volume},
    timeout=3600,
    cpu=2
)
def extract_2025_papers():
    """Extract oral and spotlight papers from 2025 conferences."""
    from openreview.api import OpenReviewClient
    import pandas as pd
    from collections import defaultdict
    import time
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting 2025 paper extraction...")
    
    client = OpenReviewClient(baseurl='https://api2.openreview.net')
    
    conferences = [
        {'venue_id': 'ICLR.cc/2025/Conference', 'year': 2025, 'conference': 'ICLR'},
        {'venue_id': 'NeurIPS.cc/2025/Conference', 'year': 2025, 'conference': 'NeurIPS'},
        {'venue_id': 'ICML.cc/2025/Conference', 'year': 2025, 'conference': 'ICML'},
    ]
    
    all_papers = []
    statistics = defaultdict(lambda: defaultdict(int))
    
    def extract_value(field):
        if isinstance(field, dict):
            return field.get('value', '')
        return field if field else ''
    
    def determine_presentation_type(note):
        content = note.content if hasattr(note, 'content') else {}
        
        venue = extract_value(content.get('venue', ''))
        venue_lower = str(venue).lower()
        
        if 'oral' in venue_lower:
            return 'oral'
        elif 'spotlight' in venue_lower:
            return 'spotlight'
        
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
            
            if len(submissions) == 0:
                print(f"  No accepted papers found. Decisions may not be released yet.")
            
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
    
    # Save results
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Saving results...")
    
    os.makedirs("/workspace/data/2025", exist_ok=True)
    
    with open("/workspace/data/2025/all_papers_2025.json", 'w') as f:
        json.dump(all_papers, f, indent=2)
    
    if len(all_papers) > 0:
        df = pd.DataFrame(all_papers)
        df.to_csv("/workspace/data/2025/all_papers_2025.csv", index=False)
        
        oral_spotlight_papers = [p for p in all_papers if p['presentation_type'] in ['oral', 'spotlight']]
        
        with open("/workspace/data/2025/oral_spotlight_papers_2025.json", 'w') as f:
            json.dump(oral_spotlight_papers, f, indent=2)
        
        if len(oral_spotlight_papers) > 0:
            df_os = pd.DataFrame(oral_spotlight_papers)
            df_os.to_csv("/workspace/data/2025/oral_spotlight_papers_2025.csv", index=False)
    
    stats_summary = {
        'extraction_date': datetime.now().isoformat(),
        'total_papers_extracted': len(all_papers),
        'oral_spotlight_extracted': len([p for p in all_papers if p['presentation_type'] in ['oral', 'spotlight']]),
        'by_conference': {},
        'by_type': defaultdict(int),
        'by_conference_and_type': {},
    }
    
    for conf_key in sorted(statistics.keys()):
        conf_stats = statistics[conf_key]
        total = sum(conf_stats.values())
        stats_summary['by_conference'][conf_key] = total
        stats_summary['by_conference_and_type'][conf_key] = dict(conf_stats)
        for ptype, count in conf_stats.items():
            stats_summary['by_type'][ptype] += count
    
    stats_summary['by_type'] = dict(stats_summary['by_type'])
    
    with open("/workspace/data/2025/statistics_2025.json", 'w') as f:
        json.dump(stats_summary, f, indent=2)
    
    volume.commit()
    
    print(f"\n{'='*70}")
    print("FINAL PAPER STATISTICS - ML Conferences 2025")
    print('='*70)
    
    print(f"\n📊 SUMMARY")
    print(f"   Total papers extracted: {len(all_papers)}")
    print(f"   Oral + Spotlight papers: {stats_summary['oral_spotlight_extracted']}")
    
    if stats_summary['by_type']:
        print(f"\n📈 BY PRESENTATION TYPE")
        for ptype in ['oral', 'spotlight', 'poster']:
            count = stats_summary['by_type'].get(ptype, 0)
            if count > 0:
                print(f"   {ptype.capitalize():>10}: {count:>5} papers")
    
    print(f"\n📋 BY CONFERENCE")
    for conf_key in sorted(stats_summary['by_conference_and_type'].keys()):
        conf_stats = stats_summary['by_conference_and_type'][conf_key]
        total = sum(conf_stats.values())
        print(f"\n   {conf_key}: {total} papers")
        for ptype in ['oral', 'spotlight', 'poster']:
            if ptype in conf_stats:
                print(f"      - {ptype.capitalize()}: {conf_stats[ptype]}")
    
    print(f"\n{'='*70}")
    
    return stats_summary


@app.local_entrypoint()
def main():
    print("Starting 2025 ML Paper Extraction...")
    stats = extract_2025_papers.remote()
    print(json.dumps(stats, indent=2))
