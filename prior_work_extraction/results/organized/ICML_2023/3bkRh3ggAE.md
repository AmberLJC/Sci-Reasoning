# Prior Work Analysis Report

## Target Paper
**Title:** 3bkRh3ggAE
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (5 papers)

### 🏗️ Foundation

**Without-replacement sampling for Stochastic Gradient Methods** (2016)
- *Authors:* Ohad Shamir
- *Connection:* Introduced the without-replacement (random reshuffling) SGD framework and posed its theoretical advantages and open questions, providing the exact problem formulation and setting that this paper studies and tightens with κ-tight lower bounds.

**Tight Complexity Bounds for Optimizing Finite Sums** (2016)
- *Authors:* Alon Woodworth et al.
- *Connection:* Developed the modern finite-sum optimization lower-bound machinery used to construct hard instances and reason about iterate averaging, which this paper adapts to the without-replacement setting to obtain tight bounds in n, K, and κ.

**Acceleration of stochastic approximation by averaging** (1992)
- *Authors:* B. T. Polyak et al.
- *Connection:* Introduced iterate averaging (and weighted averaging) as a central principle in stochastic approximation; the current paper’s focus on lower bounds for arbitrary weighted average iterates builds directly on this averaging paradigm.

### 📊 Baseline

**Why Random Reshuffling Beats Stochastic Gradient Descent** (2019)
- *Authors:* Osman Gürbüzbalaban et al.
- *Connection:* Established leading upper bounds for Random Reshuffling on smooth (strongly) convex finite sums, which this paper directly targets with matching lower bounds—tightening the κ dependence and closing the gap for weighted-average iterates.

**SGD Without Replacement: Sharper Rates for General Smooth Convex Functions** (2019)
- *Authors:* Dheeraj Nagaraj et al.
- *Connection:* Provided sharper convergence upper bounds for without-replacement SGD in smooth convex settings; the present work supplies κ-tight lower bounds for weighted averages that align with and clarify the limits of such upper bounds.

---

## Synthesis

This work delivers κ-tight lower bounds for without-replacement SGD (random reshuffling and broader permutation-based schemes) on smooth (strongly) convex finite-sum problems, specifically for arbitrary weighted average iterates. The direct intellectual lineage begins with Shamir (2016), which formalized the without-replacement/reshuffling sampling model and highlighted theoretical gaps relative to with-replacement SGD. On the upper-bound side, Gürbüzbalaban–Ozdaglar–Parrilo (2019) and Nagaraj–Jain–Netrapalli (2019) provided the strongest convergence guarantees for Random Reshuffling in convex and strongly convex regimes. Their bounds—especially the dependencies on the condition number κ and the role of averaging—set the concrete targets this paper aims to match from below; Cha–Lee–Yun close these gaps by constructing lower bounds that exactly meet those upper rates for weighted averages, including improved κ dependencies. Methodologically, the paper’s lower-bound constructions and the emphasis on the finite-sum structure are rooted in the techniques of Woodworth–Srebro (2016), which established tight finite-sum oracle lower bounds and hard-instance design patterns that this work tailors to the without-replacement sampling dynamics. Finally, the paper’s focus on arbitrary weighted average iterates is anchored in the averaging paradigm introduced by Polyak–Juditsky (1992), with Cha–Lee–Yun showing that, even with optimally chosen weights and permutations, one cannot beat the presented bounds—thereby precisely delineating the limits of reshuffling and permutation-based SGD.

---
*Generated: 2026-01-06T23:09:26.529964*
