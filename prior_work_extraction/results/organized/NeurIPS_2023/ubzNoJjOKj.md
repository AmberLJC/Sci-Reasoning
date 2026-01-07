# Prior Work Analysis Report

## Target Paper
**Title:** ubzNoJjOKj
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

HyenaDNA’s core contribution—single-nucleotide, long-range genomic sequence modeling—sits at the intersection of two lines of progress: (1) efficient long-context sequence architectures and (2) domain evidence that distal genomic context matters while fine-grained base resolution must be preserved. On the architectural side, Hyena Hierarchy introduced implicit long convolutions that match attention quality while scaling to far longer contexts; this capability is grounded in the structured state-space lineage exemplified by S4, which formalized subquadratic long-range dependency modeling. Performer provided a practical benchmark for scalable attention, widely adopted in genomics, and sets the efficiency/quality bar HyenaDNA seeks to surpass with Hyena operators.

On the genomics side, Basenji first underscored that regulatory signals span tens to hundreds of kilobases and can be captured with convolutional mechanisms. Enformer cemented this by showing substantial gains from ~200 kb receptive fields, but also exposed attention’s quadratic scaling limits in practice. In parallel, DNABERT showed the utility of large-scale pretraining on genomes, yet its reliance on k-mer tokenization and short contexts sacrifices single-nucleotide fidelity and distal interactions. Insights from ByT5 in NLP strengthened the case for token-free, character-level modeling, directly mirroring HyenaDNA’s choice to operate at nucleotide resolution. Together, these works shaped HyenaDNA’s design: replace attention with Hyena implicit convolutions to unlock longer contexts, and model raw nucleotides to preserve SNP-level signal—advancing both scale and resolution in genomic sequence modeling.

---
*Generated: 2026-01-06T23:42:49.071074*
