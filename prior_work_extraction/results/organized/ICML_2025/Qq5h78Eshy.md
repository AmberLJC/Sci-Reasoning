# Prior Work Analysis Report

## Target Paper
**Title:** Qq5h78Eshy
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—showing that multi-pass SGD can rapidly overfit in non-smooth stochastic convex optimization and quantifying a sharp phase transition—rests on three interlocking strands of prior work. First, foundational SCO and subgradient analyses (Nemirovski et al., Shamir & Zhang) characterize the optimization-error side, including the 1/(ηT) decay and the one-pass step-size choice η≈1/√n that yields optimal excess risk. Second, statistical limits for SCO (Agarwal et al.) establish that Θ(1/√n) is the minimax-optimal generalization rate under Lipschitz convex losses, framing one-pass SGD as already statistically optimal and leaving no headroom for multi-pass improvements in the general case. Third, algorithmic stability theory (Bousquet & Elisseeff) and its modern instantiation for SGD (Hardt, Recht & Singer) link the number of updates and step size to out-of-sample error, highlighting how additional iterations can worsen generalization—especially pertinent when smoothness is absent.

Building on these, the present paper targets the practically dominant multi-epoch regime (Shamir, 2016, without-replacement sampling), and precisely balances optimization progress against instability to derive a population loss of order Θ(1/(ηT)+η√T) from the second pass onward. This crystallizes a phase transition: the η that is optimal for one pass triggers overfitting as T grows, yielding even Ω(1) population loss after a second pass. The result sharpens stability-based intuitions for the non-smooth setting and echoes early-stopping principles (Yao, Rosasco & Caponnetto), but with tight, distribution-agnostic rates that explain rapid overfitting in multi-pass SGD.

---
*Generated: 2026-01-07T00:04:09.155513*
