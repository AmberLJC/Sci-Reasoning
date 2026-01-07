# ML Paper Acquisition Pipeline - Task Breakdown

## Objective
Compile a definitive dataset of all oral and spotlight papers from ICML, ICLR, and NeurIPS for 2023 and 2024, enriched with metadata and peer-review context.

---

## Phase 1: Surgical Data Acquisition and Enrichment

### Step 1.1: Source Identification and Extraction
- [ ] 1.1.1 Research and compile target URLs for each conference/year combination
  - ICML 2023, ICML 2024
  - ICLR 2023, ICLR 2024
  - NeurIPS 2023, NeurIPS 2024
- [ ] 1.1.2 Identify the structure of each conference's accepted papers page
- [ ] 1.1.3 Determine best extraction approach (API vs scraping) for each source
- [ ] 1.1.4 Extract oral/spotlight paper lists from each source
- [ ] 1.1.5 Consolidate into unified schema: (paper_title, authors, conference, year, presentation_type)

### Step 1.2: Metadata Enrichment and Verification
- [ ] 1.2.1 Set up Semantic Scholar API integration
- [ ] 1.2.2 For each paper, fetch: paperId, affiliations, abstract, publication date, URL
- [ ] 1.2.3 Set up OpenReview API integration
- [ ] 1.2.4 Cross-reference papers with OpenReview for peer reviews and meta-reviews
- [ ] 1.2.5 Create enriched dataset with all metadata

---

## Phase 2: Feature Engineering and Lineage Graph Construction

### Step 2.1: Citation and Reference Extraction
- [ ] 2.1.1 For each paper, fetch reference list (papers it cites)
- [ ] 2.1.2 For each paper, fetch citing papers (papers that cite it)
- [ ] 2.1.3 Construct directed citation graph with oral/spotlight papers as central nodes

### Step 2.2: Impact Metrics Computation
- [ ] 2.2.1 Calculate citation velocity (citations per time since publication)
- [ ] 2.2.2 Calculate influential citation count (citations from top-tier venues)
- [ ] 2.2.3 Gather community engagement proxies (GitHub, HuggingFace mentions)

---

## Deliverables
- [ ] Comprehensive dataset of oral/spotlight papers (CSV/JSON)
- [ ] Citation graph data structure
- [ ] Impact metrics for each paper
- [ ] Final report with methodology and findings
