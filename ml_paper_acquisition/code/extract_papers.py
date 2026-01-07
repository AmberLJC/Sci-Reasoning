"""
ML Conference Paper Extraction Script
Extracts oral and spotlight papers from ICML, ICLR, and NeurIPS (2023-2024)
Using OpenReview API
"""

import modal
import os
import json
from datetime import datetime

app = modal.App("ml-paper-extraction")

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
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting paper extraction...")
    
    # Initialize OpenReview client (API v2)
    client = OpenReviewClient(baseurl='https://api2.openreview.net')
    
    # Conference configurations
    conferences = {
        'ICLR_2023': {
            'venue_id': 'ICLR.cc/2023/Conference',
            'year': 2023,
            'conference': 'ICLR'
        },
        'ICLR_2024': {
            'venue_id': 'ICLR.cc/2024/Conference', 
            'year': 2024,
            'conference': 'ICLR'
        },
        'NeurIPS_2023': {
            'venue_id': 'NeurIPS.cc/2023/Conference',
            'year': 2023,
            'conference': 'NeurIPS'
        },
        'NeurIPS_2024': {
            'venue_id': 'NeurIPS.cc/2024/Conference',
            'year': 2024,
            'conference': 'NeurIPS'
        },
        'ICML_2023': {
            'venue_id': 'ICML.cc/2023/Conference',
            'year': 2023,
            'conference': 'ICML'
        },
        'ICML_2024': {
            'venue_id': 'ICML.cc/2024/Conference',
            'year': 2024,
            'conference': 'ICML'
        }
    }
    
    all_papers = []
    statistics = defaultdict(lambda: defaultdict(int))
    
    for conf_key, conf_info in conferences.items():
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Processing {conf_key}...")
        venue_id = conf_info['venue_id']
        
        try:
            # Get all accepted submissions for this venue
            # Different venues use different venueid patterns
            possible_venue_ids = [
                venue_id,
                f"{venue_id}/Accept",
            ]
            
            submissions = []
            
            # Try to get submissions by querying accepted papers
            try:
                # For API v2, we need to check the venue's content structure
                print(f"  Fetching accepted papers from {venue_id}...")
                
                # Get papers with different acceptance statuses
                # OpenReview stores decision in the venueid field for accepted papers
                for accept_type in ['oral', 'spotlight', 'poster', 'Oral', 'Spotlight', 'Poster']:
                    try:
                        venue_pattern = f"{venue_id}/{accept_type}"
                        notes = list(client.get_all_notes(
                            content={'venueid': venue_pattern}
                        ))
                        if notes:
                            print(f"    Found {len(notes)} papers with venueid pattern: {venue_pattern}")
                            for note in notes:
                                submissions.append((note, accept_type.lower()))
                    except Exception as e:
                        pass
                
                # Also try the standard accepted papers query
                if not submissions:
                    print(f"  Trying alternative query method...")
                    # Query by invitation
                    try:
                        all_notes = list(client.get_all_notes(
                            invitation=f"{venue_id}/-/Submission",
                            details='directReplies'
                        ))
                        print(f"    Found {len(all_notes)} total submissions")
                        
                        for note in all_notes:
                            # Check for decision in replies
                            if hasattr(note, 'details') and 'directReplies' in note.details:
                                for reply in note.details['directReplies']:
                                    if 'Decision' in reply.get('invitation', ''):
                                        decision = reply.get('content', {}).get('decision', {})
                                        if isinstance(decision, dict):
                                            decision = decision.get('value', '')
                                        if 'Accept' in str(decision):
                                            if 'oral' in str(decision).lower():
                                                submissions.append((note, 'oral'))
                                            elif 'spotlight' in str(decision).lower():
                                                submissions.append((note, 'spotlight'))
                                            elif 'poster' in str(decision).lower():
                                                submissions.append((note, 'poster'))
                                            else:
                                                submissions.append((note, 'accepted'))
                    except Exception as e:
                        print(f"    Alternative method failed: {e}")
                
            except Exception as e:
                print(f"  Error fetching from {venue_id}: {e}")
            
            # Process submissions
            print(f"  Processing {len(submissions)} submissions...")
            
            for note, presentation_type in submissions:
                try:
                    content = note.content if hasattr(note, 'content') else {}
                    
                    # Extract title
                    title = content.get('title', {})
                    if isinstance(title, dict):
                        title = title.get('value', 'Unknown')
                    
                    # Extract authors
                    authors = content.get('authors', {})
                    if isinstance(authors, dict):
                        authors = authors.get('value', [])
                    if isinstance(authors, list):
                        authors = ', '.join(authors)
                    
                    # Extract abstract
                    abstract = content.get('abstract', {})
                    if isinstance(abstract, dict):
                        abstract = abstract.get('value', '')
                    
                    # Extract keywords
                    keywords = content.get('keywords', {})
                    if isinstance(keywords, dict):
                        keywords = keywords.get('value', [])
                    if isinstance(keywords, list):
                        keywords = ', '.join(keywords)
                    
                    paper_data = {
                        'title': title,
                        'authors': authors,
                        'abstract': abstract[:500] if abstract else '',  # Truncate for storage
                        'keywords': keywords,
                        'conference': conf_info['conference'],
                        'year': conf_info['year'],
                        'presentation_type': presentation_type,
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
        time.sleep(1)
    
    # Save results
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Saving results...")
    
    os.makedirs("/workspace/data", exist_ok=True)
    
    # Save as JSON
    with open("/workspace/data/all_papers.json", 'w') as f:
        json.dump(all_papers, f, indent=2)
    
    # Save as CSV
    df = pd.DataFrame(all_papers)
    df.to_csv("/workspace/data/all_papers.csv", index=False)
    
    # Save statistics
    stats_summary = {
        'extraction_date': datetime.now().isoformat(),
        'total_papers': len(all_papers),
        'by_conference': dict(statistics),
        'by_type': {}
    }
    
    # Aggregate by type
    type_counts = defaultdict(int)
    for conf_stats in statistics.values():
        for ptype, count in conf_stats.items():
            type_counts[ptype] += count
    stats_summary['by_type'] = dict(type_counts)
    
    with open("/workspace/data/statistics.json", 'w') as f:
        json.dump(stats_summary, f, indent=2)
    
    volume.commit()
    
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Extraction complete!")
    print(f"Total papers extracted: {len(all_papers)}")
    print(f"\nStatistics by conference:")
    for conf, stats in statistics.items():
        print(f"  {conf}: {dict(stats)}")
    
    return stats_summary


@app.local_entrypoint()
def main():
    print("Starting ML Paper Extraction Pipeline...")
    stats = extract_all_papers.remote()
    print("\n" + "="*60)
    print("FINAL STATISTICS")
    print("="*60)
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
