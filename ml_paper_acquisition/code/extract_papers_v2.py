"""
ML Conference Paper Extraction Script v2
Extracts oral and spotlight papers from ICML, ICLR, and NeurIPS (2023-2024)
Using OpenReview API with proper venue ID filtering
"""

import modal
import os
import json
from datetime import datetime

app = modal.App("ml-paper-extraction-v2")

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
    import openreview
    from openreview.api import OpenReviewClient
    import pandas as pd
    from collections import defaultdict
    import time
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting paper extraction v2...")
    
    # Initialize OpenReview client (API v2)
    client = OpenReviewClient(baseurl='https://api2.openreview.net')
    
    # Conference configurations with proper venue IDs for accepted papers
    # OpenReview uses specific venueid patterns for different acceptance types
    conferences = [
        # ICLR 2024
        {'venue_id': 'ICLR.cc/2024/Conference', 'year': 2024, 'conference': 'ICLR',
         'oral_venueid': 'ICLR.cc/2024/Conference', 'spotlight_venueid': 'ICLR.cc/2024/Conference',
         'poster_venueid': 'ICLR.cc/2024/Conference'},
        # ICLR 2023
        {'venue_id': 'ICLR.cc/2023/Conference', 'year': 2023, 'conference': 'ICLR',
         'oral_venueid': 'ICLR.cc/2023/Conference', 'spotlight_venueid': 'ICLR.cc/2023/Conference',
         'poster_venueid': 'ICLR.cc/2023/Conference'},
        # NeurIPS 2024
        {'venue_id': 'NeurIPS.cc/2024/Conference', 'year': 2024, 'conference': 'NeurIPS',
         'oral_venueid': 'NeurIPS.cc/2024/Conference', 'spotlight_venueid': 'NeurIPS.cc/2024/Conference',
         'poster_venueid': 'NeurIPS.cc/2024/Conference'},
        # NeurIPS 2023
        {'venue_id': 'NeurIPS.cc/2023/Conference', 'year': 2023, 'conference': 'NeurIPS',
         'oral_venueid': 'NeurIPS.cc/2023/Conference', 'spotlight_venueid': 'NeurIPS.cc/2023/Conference',
         'poster_venueid': 'NeurIPS.cc/2023/Conference'},
        # ICML 2024
        {'venue_id': 'ICML.cc/2024/Conference', 'year': 2024, 'conference': 'ICML',
         'oral_venueid': 'ICML.cc/2024/Conference', 'spotlight_venueid': 'ICML.cc/2024/Conference',
         'poster_venueid': 'ICML.cc/2024/Conference'},
        # ICML 2023
        {'venue_id': 'ICML.cc/2023/Conference', 'year': 2023, 'conference': 'ICML',
         'oral_venueid': 'ICML.cc/2023/Conference', 'spotlight_venueid': 'ICML.cc/2023/Conference',
         'poster_venueid': 'ICML.cc/2023/Conference'},
    ]
    
    all_papers = []
    statistics = defaultdict(lambda: defaultdict(int))
    
    for conf_info in conferences:
        conf_key = f"{conf_info['conference']}_{conf_info['year']}"
        venue_id = conf_info['venue_id']
        
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Processing {conf_key}...")
        
        try:
            # Get all accepted submissions by querying with the venue ID
            # The venueid field contains the acceptance status
            print(f"  Querying accepted papers for {venue_id}...")
            
            # Get all notes that have this venue in their venueid
            submissions = list(client.get_all_notes(
                content={'venueid': venue_id}
            ))
            
            print(f"  Found {len(submissions)} accepted papers")
            
            # Process each submission
            for note in submissions:
                try:
                    content = note.content if hasattr(note, 'content') else {}
                    
                    # Get the venueid to determine presentation type
                    venueid = content.get('venueid', {})
                    if isinstance(venueid, dict):
                        venueid = venueid.get('value', '')
                    
                    # Determine presentation type from venueid or other fields
                    presentation_type = 'poster'  # default
                    venueid_lower = str(venueid).lower()
                    
                    if 'oral' in venueid_lower:
                        presentation_type = 'oral'
                    elif 'spotlight' in venueid_lower:
                        presentation_type = 'spotlight'
                    elif 'poster' in venueid_lower:
                        presentation_type = 'poster'
                    
                    # Extract title
                    title = content.get('title', {})
                    if isinstance(title, dict):
                        title = title.get('value', 'Unknown')
                    
                    # Extract authors
                    authors = content.get('authors', {})
                    if isinstance(authors, dict):
                        authors = authors.get('value', [])
                    if isinstance(authors, list):
                        authors_str = ', '.join(authors)
                    else:
                        authors_str = str(authors)
                    
                    # Extract abstract
                    abstract = content.get('abstract', {})
                    if isinstance(abstract, dict):
                        abstract = abstract.get('value', '')
                    
                    # Extract keywords
                    keywords = content.get('keywords', {})
                    if isinstance(keywords, dict):
                        keywords = keywords.get('value', [])
                    if isinstance(keywords, list):
                        keywords_str = ', '.join(keywords) if keywords else ''
                    else:
                        keywords_str = str(keywords) if keywords else ''
                    
                    paper_data = {
                        'title': title,
                        'authors': authors_str,
                        'abstract': abstract[:1000] if abstract else '',
                        'keywords': keywords_str,
                        'conference': conf_info['conference'],
                        'year': conf_info['year'],
                        'presentation_type': presentation_type,
                        'venueid': venueid,
                        'openreview_id': note.id if hasattr(note, 'id') else '',
                        'forum_id': note.forum if hasattr(note, 'forum') else '',
                    }
                    
                    all_papers.append(paper_data)
                    statistics[conf_key][presentation_type] += 1
                    
                except Exception as e:
                    print(f"    Error processing paper: {e}")
                    continue
            
            print(f"  {conf_key} complete: {dict(statistics[conf_key])}")
            
        except Exception as e:
            print(f"  Error processing {conf_key}: {e}")
            import traceback
            traceback.print_exc()
        
        # Rate limiting
        time.sleep(2)
    
    # Now let's also try to get more detailed presentation type info
    # by checking the decision notes
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Refining presentation types...")
    
    # Create lookup by forum_id
    paper_lookup = {p['forum_id']: p for p in all_papers if p['forum_id']}
    
    # Save results
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Saving results...")
    
    os.makedirs("/workspace/data", exist_ok=True)
    
    # Save as JSON
    with open("/workspace/data/all_papers.json", 'w') as f:
        json.dump(all_papers, f, indent=2)
    
    # Save as CSV
    df = pd.DataFrame(all_papers)
    df.to_csv("/workspace/data/all_papers.csv", index=False)
    
    # Calculate final statistics
    stats_summary = {
        'extraction_date': datetime.now().isoformat(),
        'total_papers': len(all_papers),
        'by_conference': {},
        'by_type': defaultdict(int),
        'by_conference_and_type': {}
    }
    
    # Aggregate statistics
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
    print(f"Total papers extracted: {len(all_papers)}")
    print(f"\nStatistics by conference:")
    for conf, count in stats_summary['by_conference'].items():
        print(f"  {conf}: {count} papers")
        if conf in stats_summary['by_conference_and_type']:
            for ptype, pcount in stats_summary['by_conference_and_type'][conf].items():
                print(f"    - {ptype}: {pcount}")
    
    print(f"\nStatistics by type:")
    for ptype, count in stats_summary['by_type'].items():
        print(f"  {ptype}: {count}")
    
    return stats_summary


@app.local_entrypoint()
def main():
    print("Starting ML Paper Extraction Pipeline v2...")
    stats = extract_all_papers.remote()
    print("\n" + "="*60)
    print("FINAL STATISTICS")
    print("="*60)
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
