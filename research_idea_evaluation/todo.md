# Research Idea Generation Evaluation

## Objective
Evaluate whether GPT-5.2 can generate research ideas that align with real published papers, given only prior work as context.

## Task Breakdown

### Phase 1: Data Preparation
- [x] Explore NeurIPS 2025 Oral data structure
- [ ] Extract all papers with their intellectual_predecessors
- [ ] Build paper title → content mapping

### Phase 2: Paper Content Acquisition
- [ ] For each predecessor paper title, search and find the paper
- [ ] Crawl first 3 pages of content from each paper
- [ ] Store crawled content for idea generation

### Phase 3: Idea Generation Pipeline
- [ ] Create prompt for GPT-5.2 to generate k=10 research ideas
- [ ] Feed predecessor content to GPT-5.2
- [ ] Generate candidate ideas for each target paper

### Phase 4: Similarity Judgment
- [ ] Create prompt for GPT-5.2 to judge similarity
- [ ] Compare each generated idea against ground truth paper
- [ ] Record binary match decisions

### Phase 5: Evaluation & Reporting
- [ ] Calculate Hit@k metric across all papers
- [ ] Track API costs (Input: $2/1M, Output: $14/1M)
- [ ] Generate final report

## Configuration
- Model: gpt-5.2 (no temperature or other parameters)
- k = 10 candidate ideas
- Dataset: NeurIPS 2025 Oral papers (77 papers)
- API Pricing: Input $2/1M tokens, Output $14/1M tokens
