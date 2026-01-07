# Prior Work Analysis Report

## Target Paper

**Title:** Learning Randomized Algorithms with Transformers

**Conference:** ICLR 2025 (oral)

**Authors:** Johannes von Oswald, Seijin Kobayashi, Yassir Akram, Angelika Steger

**Keywords:** Randomized algorithms, Learning under adversarial losses, Adversarial robustness, In-context learning algorithms

**Abstract:** 
> Randomization is a powerful tool that endows algorithms with remarkable properties. For instance, randomized algorithms excel in adversarial settings, often surpassing the worst-case performance of deterministic algorithms with large margins. Furthermore, their success probability can be amplified by simple strategies such as repetition and majority voting. In this paper, we enhance deep neural networks, in particular transformer models, with randomization. We demonstrate for the first time that...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Probabilistic Computations: Toward a Unified Measure of Complexity** (1977)
- *Authors:* Andrew C.-C. Yao
- *Direct Connection:* Yao’s minimax principle formalizes why randomized algorithms can strictly outperform deterministic ones against adversaries, providing the theoretical backbone for training transformers to exploit injected randomness on adversarial objectives.

**A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting** (1997)
- *Authors:* Yoav Freund et al.
- *Direct Connection:* The Weighted Majority/Hedge framework demonstrates that randomized prediction is essential to avoid adversarial exploitation and that repetition/majority voting amplifies success—precisely the properties the transformer is trained to learn and leverage.

**The Nonstochastic Multiarmed Bandit Problem** (2002)
- *Authors:* Peter Auer et al.
- *Direct Connection:* EXP3 and related adversarial bandit formulations establish canonical loss settings where deterministic strategies fail and randomization is necessary, directly informing the adversarial objectives used to elicit learned randomized behavior.

**What Can Transformers Learn In-Context? A Case Study of Simple Function Classes** (2022)
- *Authors:* Pratyush Garg et al.
- *Direct Connection:* This study established that transformers can learn algorithmic procedures purely from data and objectives, laying the methodological groundwork that is here extended from deterministic routines to randomized algorithms.

### 💡 Inspiration

**What Learning Algorithm Is In-Context Learning? Investigations with Linear Models** (2023)
- *Authors:* Hadi Akyürek et al.
- *Direct Connection:* By showing transformers can implement specific learning rules (e.g., gradient-descent-like updates) in-context, this work directly inspires training transformers to implement randomized procedures when furnished with a randomness source.

### 🔗 Related Problem

**Certified Adversarial Robustness via Randomized Smoothing** (2019)
- *Authors:* Jeremy M. Cohen et al.
- *Direct Connection:* Randomized smoothing shows how injecting noise and using majority vote yields adversarial robustness, motivating this work’s shift from fixed noise heuristics to learning how a model should use provided randomness and amplification.

**Neural Algorithmic Reasoning** (2021)
- *Authors:* Petar Veličković et al.
- *Direct Connection:* Demonstrating that neural networks can learn to execute algorithmic primitives provides the immediate precursor for extending from learned deterministic routines to learned randomized algorithms within transformer architectures.

---

## Synthesis: How Prior Work Led to This Paper

Foundational theory established that randomization can yield decisive advantages against adversaries: Yao’s minimax principle formalized how randomized strategies outperform deterministic ones in worst-case settings. In online learning, Weighted Majority/Hedge made this concrete by showing that randomized prediction is necessary to avoid adversarial exploitation and that simple repetition plus majority voting amplifies reliability. Adversarial bandits, via the EXP3 framework, provided canonical loss formulations where any deterministic policy is exploitable, making randomization essential for low regret. Randomized smoothing demonstrated in supervised learning that injecting noise and aggregating predictions by majority vote can confer adversarial robustness, highlighting a practical template for leveraging randomness during inference. In parallel, work on in-context learning showed that transformers can learn algorithmic procedures purely from data and objectives, with studies characterizing when such models implement simple function classes and even gradient-descent-like update rules. Neural Algorithmic Reasoning further showed neural networks can acquire algorithmic primitives, underscoring the viability of end-to-end learning of procedural computation.
Together, these strands revealed a gap: while classical theory and practice show the power of randomization and amplification, neural models largely relied on fixed heuristics (e.g., smoothing noise) rather than learning how to use randomness algorithmically. By marrying in-context algorithm learning with adversarial formulations where randomization is provably beneficial, the current work naturally emerges: supply transformers with a source of randomness and train them—via standard objectives—to implement randomized algorithms whose success can be further amplified by repetition and majority vote.

---

*Analysis generated on: 2026-01-06T17:13:41.386456*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
