# Prior Work Analysis Report

## Target Paper

**Title:** Fair Clustering in the Sliding Window Model

**Conference:** ICLR 2025 (spotlight)

**Authors:** Vincent Cohen-Addad, Shaofeng H.-C. Jiang, Qiaoyuan Yang, Yubo Zhang, Samson Zhou

**Keywords:** fair clustering, sliding window model

**Abstract:** 
> We study streaming algorithms for proportionally fair clustering, a notion originally suggested by Chierichetti et al. (2017), in the sliding window model. We show that although there exist efficient streaming algorithms in the insertion-only model, surprisingly no algorithm can achieve finite ratio without violating the fairness constraint in sliding window. Hence, the problem of fair clustering is a rare separation between the insertion-only streaming model and the sliding window model. On the...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Fair Clustering Through Fairlets** (2017)
- *Authors:* Chierichetti et al.
- *Direct Connection:* This paper formalized proportional fairness for clustering and introduced the fairlet framework that the current work adopts as the fairness constraint it analyzes in streaming and sliding-window settings.

**Smooth Histograms and Streaming Algorithms** (2007)
- *Authors:* Braverman and Ostrovsky
- *Direct Connection:* The smooth histogram framework underpins sliding-window summarization, which the present paper adapts to maintain near-fair cluster quality with poly(k, ε⁻¹, log n) space once fairness is relaxed by (1+ε).

**Turning Big Data into Tiny Data: Coresets for k-Means, k-Median, and k-Center** (2013)
- *Authors:* Feldman et al.
- *Direct Connection:* Coreset constructions enabling small-space approximations for k-clustering directly inform the paper’s streaming design, serving as the cost-approximation primitive combined with sliding-window maintenance under relaxed fairness.

### 💡 Inspiration

**Fair Algorithms for Clustering** (2019)
- *Authors:* Bera et al.
- *Direct Connection:* It established bicriteria approaches that allow a small multiplicative violation of fairness to obtain good cost approximations, directly motivating the current paper’s (1+ε)-fairness relaxation to overcome sliding-window impossibility.

### 🔧 Extension

**Coresets for k-Median and k-Means and Their Applications in Dynamic and Streaming Settings** (2011)
- *Authors:* Braverman et al.
- *Direct Connection:* This work’s coreset and streaming toolkit for insertion-only clustering provides the insertion-only baseline the new paper separates from, and its techniques are adapted to the sliding-window regime when allowing (1+ε)-fairness.

### 🔗 Related Problem

**Scalable Fair Clustering** (2019)
- *Authors:* Backurs et al.
- *Direct Connection:* By operationalizing fairlet-based and local-search techniques at scale for proportionally fair clustering in the offline setting, this work provided algorithmic primitives and baselines that the present paper must match in a streaming context.

---

## Synthesis: How Prior Work Led to This Paper

Proportional fairness in clustering was crystallized by the fairlet framework, which encoded demographic-parity-style constraints into a combinatorial structure that could be paired with classical k-clustering objectives. Subsequent progress showed that exact fairness is often too restrictive, and that permitting a controlled multiplicative violation can recover efficient approximations; in particular, bicriteria designs demonstrated that a (1+ε) slack in group proportions can dramatically simplify algorithmic design while preserving utility. On the algorithmic side, fair clustering techniques were scaled in the offline setting, combining fairlets with local search to achieve practical performance and to clarify which parts of the pipeline bore the computational burden. Orthogonally, sliding-window stream processing introduced smooth histograms as a general blueprint to maintain summaries over the active window, and coreset constructions for k-means/k-median provided compact surrogates with strong cost guarantees suitable for streaming maintenance. Dynamic-and-streaming coreset frameworks further showed how to realize insertion-only k-clustering approximations in small space.
Bringing these strands together highlights a tension: insertion-only streaming approximations benefit from coresets, but the windowed, adversarial nature of sliding windows undermines strict proportional fairness. The natural synthesis—implied by bicriteria fairness—relaxes fairness by (1+ε) and then marries smooth-histogram window maintenance with coreset-based k-clustering summaries. This yields near-optimal poly(k, ε⁻¹, log n)-space algorithms while the impossibility of finite approximation under exact fairness explains the sharp separation from the insertion-only model.

---

*Analysis generated on: 2026-01-06T12:40:24.961955*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
