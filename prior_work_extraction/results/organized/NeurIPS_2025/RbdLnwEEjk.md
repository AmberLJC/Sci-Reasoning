# Prior Work Analysis Report

## Target Paper
**Title:** RbdLnwEEjk
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

SEEK builds directly on the canonical greenlist/redlist watermark of Kirchenbauer et al., where a keyed partition of the vocabulary within sliding windows yields a z-statistic for detection. That framework exposes a structural trade-off: smaller windows better survive scrubbing (e.g., paraphrasing and token deletions) but are easier to reverse-engineer, enabling low-cost spoofing. Two contemporaneous strands informed SEEK’s solution. First, soft and semantic watermarks such as SWEET and SemStamp demonstrated that distributing signal across many candidate tokens or semantics-preserving alternatives enhances edit resilience—an idea SEEK generalizes by introducing equivalent texture keys: multiple tokens inside each window that independently contribute to the same detection statistic. Second, recent spoofing work (e.g., reverse engineering and likelihood shaping attacks) showed that naively increasing redundancy or shrinking windows can leak the keyed partition, enabling counterfeit watermarked text. SEEK counters this by decomposing the vocabulary into keyed sub-vocabularies that preserve high entropy per window, hindering inversion while keeping multiple equivalent supports.
Coding-theoretic insights from Tardos codes and Boneh–Shaw fingerprinting underlie SEEK’s redundancy design: robustness to deletions and tampering comes from spreading evidence across independently valid symbols, while secrecy hinges on a strong key and randomized assignment. Evaluations like WaterBench framed the Pareto frontier between scrubbing and spoofing; SEEK’s sub-vocabulary equivalent keys expand that frontier, achieving higher scrubbing resilience without compromising spoofing robustness.

---
*Generated: 2026-01-07T00:21:32.357494*
