#!/usr/bin/env python3
"""
Push the organized prior work extraction dataset to HuggingFace.
Uses git clone + add + push approach for reliable upload.
"""

import sys
sys.path.insert(0, '/tmp/hf_libs')

import os
import shutil
from pathlib import Path

# Set HuggingFace cache to a writable location BEFORE importing huggingface_hub
os.environ['HF_HOME'] = '/tmp/hf_cache'
os.environ['HUGGINGFACE_HUB_CACHE'] = '/tmp/hf_cache'
os.makedirs('/tmp/hf_cache', exist_ok=True)

from huggingface_hub import HfApi, login

# Configuration
HF_TOKEN = "YOUR_HF_TOKEN"
REPO_ID = "AmberLJC/ml-conference-papers"
LOCAL_DATA_PATH = "results/organized"

def main():
    print("🔐 Logging into HuggingFace...")
    login(token=HF_TOKEN)
    
    api = HfApi()
    
    # Get list of all conference directories
    data_path = Path(LOCAL_DATA_PATH)
    
    # Count files
    json_count = len(list(data_path.rglob("*.json")))
    md_count = len(list(data_path.rglob("*.md")))
    
    print(f"📊 Found {json_count} JSON files and {md_count} MD files")
    
    # List directories
    conference_dirs = [d for d in data_path.iterdir() if d.is_dir()]
    print(f"📁 Conference directories: {[d.name for d in sorted(conference_dirs)]}")
    
    # Create a temp directory with the correct structure
    temp_upload_dir = Path("/tmp/hf_upload")
    if temp_upload_dir.exists():
        shutil.rmtree(temp_upload_dir)
    
    target_dir = temp_upload_dir / "prior_work_extraction"
    print(f"\n📁 Creating temporary upload structure at {temp_upload_dir}...")
    
    # Copy the organized folder to the temp location with correct structure
    shutil.copytree(data_path, target_dir)
    print(f"   ✅ Copied {json_count + md_count + 1} files")
    
    # Upload using upload_large_folder
    print(f"\n📤 Uploading to HuggingFace using upload_large_folder...")
    print(f"   Repository: {REPO_ID}")
    print(f"   This may take several minutes...")
    
    try:
        api.upload_large_folder(
            repo_id=REPO_ID,
            folder_path=str(temp_upload_dir),
            repo_type="dataset",
            num_workers=4,
            print_report=True,
            print_report_every=30,
        )
        print("\n✅ Upload complete!")
        print(f"📊 View at: https://huggingface.co/datasets/{REPO_ID}/tree/main/prior_work_extraction")
    except Exception as e:
        print(f"\n❌ Upload failed: {e}")
        raise
    finally:
        # Cleanup
        if temp_upload_dir.exists():
            shutil.rmtree(temp_upload_dir)
            print("🧹 Cleaned up temporary files")

if __name__ == "__main__":
    main()
