# Prior Work Analysis Report

## Target Paper
**Title:** fBNaGVMDD9
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution is a computational lower bound for weak recovery in the symmetric stochastic block model (SBM) that is sensitive to recovery rate and aligns sharply with the Kesten–Stigum (KS) threshold. Two strands of prior work directly feed into this result. First, the KS frontier itself—developed for broadcasting on trees (Evans–Kenyon–Peres–Schulman) and predicted for SBMs via cavity methods (Decelle–Krzakala–Moore–Zdeborová)—established the information-theoretic transition governing detectability. Rigorous algorithmic and threshold analyses around KS (Massoulié; Mossel–Neeman–Sly) showed that polynomial-time methods can achieve positive (constant) correlation above KS, shaping the upper-bound side of the transition this paper seeks to match from below.
Second, the computational lower-bound machinery comes from the low-degree program. The low-degree likelihood ratio framework (Schramm–Wein) ties the failure of low-degree polynomials to the failure of all polynomial-time algorithms under the low-degree conjecture. The present work crucially relies on Moitra et al.’s 2023 formalization of the (extended) low-degree conjecture, which provides a clear assumption under which indistinguishability results can be lifted to unconditional algorithmic limitations. Building on these, the authors show that below KS no polynomial-time algorithm can even achieve n^{-0.49} correlation—offering the first rigorous evidence (under this assumption) of a sharp recovery-rate transition at KS. Moreover, by invoking a stronger variant of the conjecture, they extend the lower bound to settings with a diverging number of blocks, pushing beyond classical fixed-q analyses and aligning computational lower bounds with known algorithmic successes above KS.

---
*Generated: 2026-01-07T00:21:32.289368*
