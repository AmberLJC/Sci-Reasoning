# Thinking Patterns Analysis - LLM-Based Pattern Discovery

## Objective
Analyze ~3000 synthesis_narrative texts from top ML papers (ICML, ICLR, NeurIPS 2023-2025) to discover recurring thinking patterns using GPT-5-mini.

## Dataset
- Source: projects/synthesis_graph_pipeline/results/conferences/
- ~3466 JSON files across 17 conference directories
- Focus field: `synthesis_narrative` (describes intellectual journey)

## Strategy: Multi-Phase LLM Pattern Discovery

### Phase 1: Data Loading & Initial Sampling ✅
- [ ] Load all synthesis_narratives from JSON files
- [ ] Create stratified sample (by conference, year, presentation type)
- [ ] Validate data quality

### Phase 2: Pattern Discovery via LLM (Large Initial Sampling)
- [ ] Sample 200+ papers for initial pattern discovery (avoid bias)
- [ ] Use GPT-5-mini to identify patterns in batches
- [ ] Aggregate discovered patterns across batches
- [ ] Consolidate into canonical pattern taxonomy

### Phase 3: Pattern Refinement
- [ ] Use LLM to refine and merge similar patterns
- [ ] Create clear pattern definitions with examples
- [ ] Validate pattern taxonomy is comprehensive

### Phase 4: Full Dataset Classification
- [ ] Classify ALL papers using discovered patterns
- [ ] Track pattern frequencies and co-occurrences
- [ ] Analyze by conference/year/presentation type

### Phase 5: Analysis & Insights
- [ ] Statistical analysis of pattern distributions
- [ ] Temporal trends (2023 vs 2024 vs 2025)
- [ ] Conference-specific patterns
- [ ] Generate actionable insights for researchers

### Phase 6: Reporting
- [ ] Create visualizations
- [ ] Write comprehensive report
- [ ] Track total API costs

## Cost Tracking
- Model: gpt-5-mini
- Input: $0.25 / 1M tokens
- Output: $2 / 1M tokens
- Running total: $0.00

## Notes
- NO regex-based classification
- Use LLM for ALL pattern detection
- Large initial sampling to avoid bias
