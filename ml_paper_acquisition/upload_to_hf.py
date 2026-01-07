#!/usr/bin/env python3
"""
Upload ML Paper Acquisition dataset to HuggingFace Hub
"""

import os
import json
from huggingface_hub import HfApi, create_repo, upload_folder

# Configuration
HF_TOKEN = "YOUR_HF_TOKEN"
REPO_NAME = "ml-conference-papers"  # Will be created under your username
DATA_DIR = "results/data"

def main():
    # Initialize HuggingFace API
    api = HfApi(token=HF_TOKEN)
    
    # Get username
    user_info = api.whoami()
    username = user_info["name"]
    repo_id = f"{username}/{REPO_NAME}"
    
    print(f"Username: {username}")
    print(f"Repository ID: {repo_id}")
    
    # Create the repository (dataset type)
    try:
        create_repo(
            repo_id=repo_id,
            token=HF_TOKEN,
            repo_type="dataset",
            private=False,  # Public dataset
            exist_ok=True   # Don't fail if exists
        )
        print(f"✅ Repository created/verified: https://huggingface.co/datasets/{repo_id}")
    except Exception as e:
        print(f"Repository creation: {e}")
    
    # Create README for the dataset
    readme_content = """---
license: mit
task_categories:
  - text-classification
  - feature-extraction
language:
  - en
tags:
  - machine-learning
  - research-papers
  - NeurIPS
  - ICML
  - ICLR
  - academic
  - deep-learning
size_categories:
  - 10K<n<100K
---

# ML Conference Papers Dataset

A comprehensive collection of machine learning research papers from top-tier conferences.

## Dataset Description

This dataset contains metadata and abstracts from papers published at major machine learning conferences:

- **ICLR** (International Conference on Learning Representations)
- **NeurIPS** (Neural Information Processing Systems)
- **ICML** (International Conference on Machine Learning)

### Coverage

**2023-2024 Papers:**
- Total: ~14,000 papers
- ICLR 2024: 2,260 papers
- NeurIPS 2024: 4,035 papers
- NeurIPS 2023: 3,218 papers
- ICML 2024: 2,610 papers
- ICML 2023: 1,828 papers

**2025 Papers:**
- Total: ~12,247 papers
- ICLR 2025: 3,703 papers
- ICML 2025: 3,257 papers
- NeurIPS 2025: 5,287 papers
- Includes oral and spotlight presentations

## Data Fields

| Field | Description |
|-------|-------------|
| `title` | Paper title |
| `authors` | List of authors |
| `abstract` | Paper abstract |
| `keywords` | Paper keywords |
| `conference` | Conference name (ICLR, NeurIPS, ICML) |
| `year` | Publication year |
| `presentation_type` | Type (poster, oral, spotlight) |
| `venueid` | OpenReview venue ID |
| `openreview_id` | OpenReview paper ID |
| `forum_id` | OpenReview forum ID |

## File Structure

```
├── 2023-2024/
│   ├── all_papers.csv
│   ├── all_papers.json
│   ├── oral_spotlight_papers_fast.csv
│   ├── oral_spotlight_papers_fast.json
│   └── statistics.json
├── 2025/
│   ├── all_papers_2025.csv
│   ├── all_papers_2025.json
│   ├── oral_spotlight_papers_2025.csv
│   ├── oral_spotlight_papers_2025.json
│   └── statistics_2025.json
```

## Usage

```python
import pandas as pd
from huggingface_hub import hf_hub_download

# Download specific file
file_path = hf_hub_download(
    repo_id="YOUR_USERNAME/ml-conference-papers",
    filename="2025/all_papers_2025.csv",
    repo_type="dataset"
)

# Load with pandas
df = pd.read_csv(file_path)
print(f"Total papers: {len(df)}")
```

Or load directly:

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("YOUR_USERNAME/ml-conference-papers", data_files="2025/all_papers_2025.csv")
```

## Use Cases

- **Literature Review**: Search and filter papers by topic, conference, or year
- **Trend Analysis**: Analyze research trends across conferences and years
- **NLP Training**: Use abstracts for text classification or embedding models
- **Citation Analysis**: Study paper metadata and keywords
- **Research Discovery**: Find relevant papers in your area of interest

## License

MIT License

## Citation

If you use this dataset, please cite:

```bibtex
@dataset{ml_conference_papers,
  title={ML Conference Papers Dataset},
  year={2025},
  publisher={HuggingFace},
  note={Collection of papers from ICLR, NeurIPS, and ICML conferences}
}
```

## Acknowledgments

Data extracted from OpenReview.net
"""
    
    # Write README to data directory
    readme_path = os.path.join(DATA_DIR, "README.md")
    with open(readme_path, "w") as f:
        f.write(readme_content)
    print(f"✅ README.md created")
    
    # Upload the entire data folder
    print(f"\n📤 Uploading data to HuggingFace...")
    print(f"   Source: {DATA_DIR}")
    print(f"   Destination: {repo_id}")
    
    api.upload_folder(
        folder_path=DATA_DIR,
        repo_id=repo_id,
        repo_type="dataset",
        token=HF_TOKEN,
        commit_message="Upload ML conference papers dataset (2023-2025)"
    )
    
    print(f"\n✅ Upload complete!")
    print(f"🔗 Dataset URL: https://huggingface.co/datasets/{repo_id}")

if __name__ == "__main__":
    main()
