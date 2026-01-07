#!/usr/bin/env python3
"""
Monitor batch processing progress.

Usage:
    python monitor_progress.py --output-dir results/batch
    python monitor_progress.py --output-dir results/batch --watch  # Continuous monitoring
"""

import os
import sys
import json
import time
import argparse
from pathlib import Path
from datetime import datetime

def load_checkpoint(output_dir):
    """Load checkpoint file."""
    checkpoint_path = Path(output_dir) / "checkpoint.json"
    if not checkpoint_path.exists():
        return None
    
    with open(checkpoint_path) as f:
        return json.load(f)

def count_output_files(output_dir):
    """Count output files by conference."""
    output_path = Path(output_dir)
    counts = {}
    
    for conf_dir in output_path.iterdir():
        if conf_dir.is_dir() and not conf_dir.name.startswith('.'):
            json_files = list(conf_dir.glob("*.json"))
            md_files = list(conf_dir.glob("*.md"))
            counts[conf_dir.name] = {
                "json": len(json_files),
                "md": len(md_files)
            }
    
    return counts

def display_progress(output_dir):
    """Display current progress."""
    checkpoint = load_checkpoint(output_dir)
    file_counts = count_output_files(output_dir)
    
    print("\n" + "="*70)
    print("BATCH PROCESSING PROGRESS")
    print("="*70)
    
    if checkpoint:
        print(f"\nStarted: {checkpoint.get('started_at', 'Unknown')}")
        print(f"Last Updated: {checkpoint.get('last_updated', 'Unknown')}")
        print(f"\nTotal Processed: {checkpoint.get('total_processed', 0)}")
        print(f"Total Failed: {checkpoint.get('total_failed', 0)}")
        
        print("\n" + "-"*70)
        print("CONFERENCE PROGRESS")
        print("-"*70)
        print(f"{'Conference':<20} {'Total':<10} {'Completed':<12} {'Failed':<10} {'Progress':<15}")
        print("-"*70)
        
        conf_progress = checkpoint.get('conference_progress', {})
        for conf in sorted(conf_progress.keys()):
            stats = conf_progress[conf]
            total = stats.get('total', 0)
            completed = stats.get('completed', 0)
            failed = stats.get('failed', 0)
            
            if total > 0:
                pct = (completed / total) * 100
                bar_len = int(pct / 5)  # 20 char bar
                bar = "█" * bar_len + "░" * (20 - bar_len)
                progress = f"{pct:.1f}% {bar}"
            else:
                progress = "0%"
            
            print(f"{conf:<20} {total:<10} {completed:<12} {failed:<10} {progress}")
        
        # Calculate overall progress
        total_all = sum(s.get('total', 0) for s in conf_progress.values())
        completed_all = sum(s.get('completed', 0) for s in conf_progress.values())
        
        if total_all > 0:
            overall_pct = (completed_all / total_all) * 100
            print("-"*70)
            print(f"{'OVERALL':<20} {total_all:<10} {completed_all:<12} {'':<10} {overall_pct:.1f}%")
    else:
        print("\nNo checkpoint found. Processing may not have started yet.")
    
    print("\n" + "-"*70)
    print("OUTPUT FILES")
    print("-"*70)
    
    if file_counts:
        for conf in sorted(file_counts.keys()):
            counts = file_counts[conf]
            print(f"  {conf}: {counts['json']} JSON, {counts['md']} MD files")
    else:
        print("  No output files yet.")
    
    print("="*70 + "\n")

def watch_progress(output_dir, interval=30):
    """Continuously monitor progress."""
    print(f"Watching progress every {interval} seconds. Press Ctrl+C to stop.")
    
    try:
        while True:
            os.system('clear' if os.name == 'posix' else 'cls')
            display_progress(output_dir)
            print(f"Next update in {interval} seconds...")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopped monitoring.")

def main():
    parser = argparse.ArgumentParser(description="Monitor batch processing progress")
    parser.add_argument("--output-dir", default="results/batch", help="Output directory")
    parser.add_argument("--watch", action="store_true", help="Continuous monitoring")
    parser.add_argument("--interval", type=int, default=30, help="Watch interval in seconds")
    
    args = parser.parse_args()
    
    if args.watch:
        watch_progress(args.output_dir, args.interval)
    else:
        display_progress(args.output_dir)

if __name__ == "__main__":
    main()
