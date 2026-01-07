# Prior Work Analysis Report

## Target Paper
**Title:** ktpG37Dzh5
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

BMRS fuses two strands of prior work to deliver a principled, end-to-end Bayesian method for structured pruning. From the pruning side, Neklyudov et al. introduced Bayesian structured pruning via log-normal multiplicative noise, establishing the idea of learnable stochastic gates at the neuron/filter level. This builds upon variational dropout and sparsity-inducing priors (Molchanov et al.) and relies on the local reparameterization trick (Kingma et al.) to obtain low-variance gradients for multiplicative noise, making group-wise stochastic gating scalable and effective. Conceptually related stochastic gating ideas from L0 regularization (Louizos et al.) further shaped the modern view of end-to-end trainable, structured sparsity mechanisms.
From the Bayesian model selection side, BMRS directly incorporates Bayesian Model Reduction (Friston et al.), which provides a mechanism to efficiently recompute model evidence under changes to priors without retraining. This enables BMRS to tighten priors on specific gates—corresponding to potential neuron/filter removals—and rapidly assess the marginal likelihood of pruned variants. The overall rationale follows MacKay’s evidence framework and ARD principles (Tipping), where structures with weak posterior support under sparsity-promoting priors are deemed irrelevant and can be removed. By uniting multiplicative-noise structured gating with BMR-based evidence evaluation, BMRS yields practical, theoretically grounded pruning that can instantiate different behaviors via alternative priors (e.g., truncated log-normal), achieving reliable compression without repeated costly retraining.

---
*Generated: 2026-01-06T23:33:36.290739*
