# Prior Work Analysis Report

## Target Paper

**Title:** Joint Gradient Balancing for Data Ordering in Finite-Sum Multi-Objective Optimization

**Conference:** ICLR 2025 (spotlight)

**Authors:** Hansi Yang, James Kwok

**Keywords:** multi-objective optimization

**Abstract:** 
> In finite-sum optimization problems, the sample orders for parameter updates can significantly influence the convergence rate of optimization algorithms. While numerous sample ordering techniques have been proposed in the context of single-objective optimization, the problem of sample ordering in finite-sum multi-objective optimization has not been thoroughly explored. To address this gap, we propose a sample ordering method called JoGBa, which finds the sample orders for multiple objectives by ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Multiple-Gradient Descent Algorithm (MGDA) for Multiobjective Optimization** (2012)
- *Authors:* Jean-Antoine Désidéri
- *Direct Connection:* JoGBa preserves the MGDA update rule from this paper and builds its convergence analysis around how sample ordering can reduce inter-objective gradient discrepancy to speed MGDA.

**Without-Replacement Sampling for Stochastic Gradient Methods** (2016)
- *Authors:* Ohad Shamir
- *Direct Connection:* By showing that without-replacement (ordered) sampling can improve finite-sum optimization, this work directly motivates seeking principled, non-random sample orders—generalized here to the multi-objective setting.

### 💡 Inspiration

**Gradient Surgery for Multi-Task Learning (PCGrad)** (2020)
- *Authors:* Tongzhou Yu et al.
- *Direct Connection:* PCGrad’s core insight that mitigating conflicting task gradients accelerates training directly inspires JoGBa’s strategy to balance gradients across objectives via sample ordering rather than per-step projection.

**The Gram-Schmidt Walk: A Cure for the Banaszczyk Problem** (2018)
- *Authors:* Nikhil Bansal et al.
- *Direct Connection:* This discrepancy-minimization method for balancing vector sums inspires JoGBa’s framing of per-sample multi-objective gradients as vectors and using online vector balancing to keep cumulative inter-objective gradient discrepancy small during training.

### 🔍 Gap Identification

**Why Random Reshuffling Beats SGD? A Theoretical Explanation with Larger Step Sizes** (2019)
- *Authors:* Mert Gürbüzbalaban et al.
- *Direct Connection:* This paper establishes random reshuffling as a strong baseline in single-objective finite-sum problems, highlighting a gap—lack of analogous ordering theory and methods for multi-objective optimization—that JoGBa addresses and theoretically surpasses.

### 📊 Baseline

**Multi-Task Learning as Multi-Objective Optimization** (2018)
- *Authors:* Ozan Sener et al.
- *Direct Connection:* JoGBa’s analysis and experiments target accelerating MGDA-style updates introduced for deep multi-task learning in this work, and it explicitly proves faster convergence for MGDA under principled data ordering.

---

## Synthesis: How Prior Work Led to This Paper

MGDA was first formalized for multiobjective optimization with a principled multiple-gradient descent rule, providing a convergence framework tied to how gradients from different objectives are aggregated. Its adaptation to deep multi-task learning established MGDA as a practical baseline for neural networks, highlighting the role of gradient geometry in driving multiobjective progress. In parallel, the finite-sum optimization literature showed that sampling without replacement, and in particular random reshuffling, can significantly improve convergence over i.i.d. sampling, thereby elevating sample order from an implementation detail to a provably impactful design choice. Theoretical analyses made random reshuffling a de facto baseline in single-objective regimes and mapped how ordering can enable larger steps and faster rates. Separately, multi-task methods like PCGrad demonstrated that explicitly reducing gradient conflict between tasks yields practical gains, crystallizing the idea that balancing gradients—however achieved—is beneficial. From discrepancy theory, the Gram-Schmidt Walk provided a constructive way to balance sequences of vectors by keeping partial sums small, offering an algorithmic lens for controlling cumulative vector imbalance. Together, these works expose a clear opportunity: while ordering boosts finite-sum optimization and balancing mitigates multiobjective conflicts, there was no principled mechanism to order data in multiobjective settings by directly balancing objective gradients. The current work synthesizes these threads by formulating sample ordering as an online vector balancing problem over per-sample, per-objective gradients and proving that such ordering provably accelerates MGDA, while empirically improving convergence across multiobjective optimizers.

---

*Analysis generated on: 2026-01-06T10:53:55.552036*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
