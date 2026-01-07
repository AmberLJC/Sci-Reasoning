# Prior Work Extraction Pipeline - TODO

## Phase 1: Pipeline Development ✅
- [x] Create base pipeline with GPT-5 integration
- [x] Implement arXiv metadata fetching
- [x] Design analysis prompt for prior work extraction
- [x] Add JSON and Markdown output formats
- [x] Refine prompt for direct intellectual lineage focus
- [x] Test on sample paper (Andes - 2404.16283)
- [x] Get user approval on pipeline quality

## Phase 2: Batch Processing 🔄
- [x] Create batch processor with checkpointing
- [x] Implement rate limiting (40 req/min)
- [x] Add parallel conference processing (2 at a time)
- [x] Create progress monitoring script
- [ ] Run batch processing on all 3,451 papers
- [ ] Monitor and handle any failures
- [ ] Generate final summary report

## Phase 3: Analysis & Delivery
- [ ] Analyze batch processing results
- [ ] Create summary statistics
- [ ] Package final deliverables

## Data Summary
- **2023-2024 Oral/Spotlight**: 1,775 papers
  - ICLR 2024: 453
  - ICML 2023: 155
  - ICML 2024: 335
  - NeurIPS 2023: 445
  - NeurIPS 2024: 387

- **2025 Oral/Spotlight**: 1,676 papers
  - ICLR 2025: 593
  - ICML 2025: 319
  - NeurIPS 2025: 764

- **TOTAL**: 3,451 papers across 8 conference-years

## Commands

### Start batch processing:
```bash
cd projects/prior_work_extraction
nohup python3 code/batch_processor.py \
    --api-key "API_KEY" \
    --output-dir results/batch \
    --max-parallel 2 \
    > logs/batch_processing.log 2>&1 &
```

### Monitor progress:
```bash
python3 code/monitor_progress.py --output-dir results/batch
python3 code/monitor_progress.py --output-dir results/batch --watch  # Continuous
```

### Resume after interruption:
```bash
# Just run the same command - checkpoint handles resume automatically
python3 code/batch_processor.py --api-key "API_KEY" --output-dir results/batch
```
