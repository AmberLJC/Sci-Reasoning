# Prior Work Analysis Report

## Target Paper
**Title:** EmYWJsyad4
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—using conditional mutual information (CMI) as an auxiliary objective to learn disentangled representations that remain robust under correlation shifts—emerges from two converging threads: disentanglement via information-theoretic penalties and generalization under spurious correlations in RL. Beta-VAE established that constraining mutual information between latents and data can induce disentanglement, while FactorVAE and β-TCVAE sharpened this by directly penalizing total correlation among latents. However, these methods implicitly assume independent generative factors and tend to collapse when factors are correlated, a failure mode central to the motivation of the present work. In RL, DARLA showed the practical value of disentangled representations for transfer and robustness, motivating an RL-specific auxiliary loss that targets the causes of generalization failure.

Methodologically, the feasibility of optimizing information-theoretic objectives in deep models is grounded in variational machinery from the Deep Variational Information Bottleneck and neural MI estimation (MINE), which provide tractable bounds and estimators for MI-based losses. The NeurIPS paper adapts this toolbox to conditional dependencies, replacing unconditional MI/TC penalties with CMI so that latent features become conditionally independent given others—precisely the criterion needed when observed correlations arise from shared confounders or limited coverage. Finally, the broader objective aligns with Invariant Risk Minimization’s aim to avoid spurious correlations across environments; here, invariance is achieved not by reweighting environments but by shaping the representation itself via CMI minimization. Together, these prior works directly inform the paper’s insight and its practical CMI-based auxiliary task for RL.

---
*Generated: 2026-01-06T23:42:49.124428*
