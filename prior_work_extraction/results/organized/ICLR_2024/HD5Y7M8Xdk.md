# Prior Work Analysis Report

## Target Paper

**Title:** Forward $\chi^2$ Divergence Based Variational Importance Sampling

**Conference:** ICLR 2024 (spotlight)

**Authors:** Chengrui Li, Yule Wang, Weihan Li, Anqi Wu

**Keywords:** Importance sampling, $\chi^2$ divergence, latent variable models

**Abstract:** 
> Maximizing the marginal log-likelihood is a crucial aspect of learning latent variable models, and variational inference (VI) stands as the commonly adopted method. However, VI can encounter challenges in achieving a high marginal log-likelihood when dealing with complicated posterior distributions. In response to this limitation, we introduce a novel variational importance sampling (VIS) approach that directly estimates and maximizes the marginal log-likelihood. VIS leverages the optimal propos...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Rényi Divergence Variational Inference** (2016)
- *Authors:* Yingzhen Li et al.
- *Direct Connection:* This work introduced the α-divergence family for VI and showed that α>1 (including α=2 which corresponds to χ^2) yields mass-covering behavior and an upper bound (CUBO), laying the divergence-theoretic basis for VIS’s choice of the forward χ^2 objective.

**The sample size required in importance sampling** (2018)
- *Authors:* Sourav Chatterjee et al.
- *Direct Connection:* This paper formalized that IS efficiency and required sample size are governed by the forward χ^2 divergence χ^2(p||q), directly motivating VIS’s proposal training objective as a principled way to control weight degeneracy when estimating the marginal likelihood.

### 💡 Inspiration

**Black-box alpha divergence minimization** (2016)
- *Authors:* José Miguel Hernández-Lobato et al.
- *Direct Connection:* BB-α demonstrated practical optimization of α-divergences (including forward-direction choices) for fitting variational posteriors, motivating VIS’s use of a specific α (χ^2) to learn proposals aligned with posterior mass while connecting directly to IS variance.

### 📊 Baseline

**Importance Weighted Autoencoders** (2016)
- *Authors:* Yuri Burda et al.
- *Direct Connection:* IWAE framed variational learning around an importance-sampling-based multi-sample objective, providing the main baseline that VIS departs from by directly maximizing the marginal likelihood and optimizing the proposal via forward χ^2 rather than tightening a lower bound.

### 🔧 Extension

**Reweighted Wake-Sleep** (2015)
- *Authors:* Jörg Bornschein et al.
- *Direct Connection:* RWS trains the inference network by minimizing the inclusive (forward) KL to the true posterior using importance weights, a mechanism VIS extends by replacing inclusive KL with forward χ^2 to explicitly target variance-optimal proposals for evidence estimation.

### 🔗 Related Problem

**Variational Sequential Monte Carlo** (2017)
- *Authors:* Jimmy Naesseth et al.
- *Direct Connection:* VSMC established that one can train latent variable models by maximizing a stochastic estimator of the marginal likelihood while learning proposals, a strategy VIS adopts in the simpler IS setting with χ^2-trained proposals to reduce estimator variance.

**Auto-Encoding Sequential Monte Carlo** (2017)
- *Authors:* Tuan Anh Le et al.
- *Direct Connection:* AESMC used unbiased SMC estimators of the marginal likelihood as training objectives and optimized proposal distributions, providing the template that VIS follows using plain importance sampling coupled with χ^2-driven proposal optimization.

---

## Synthesis: How Prior Work Led to This Paper

Importance Weighted Autoencoders established a multi-sample variational objective derived from importance sampling, showing that learning generative models can benefit from Monte Carlo estimators but still optimizes a lower bound. Reweighted Wake-Sleep trained inference networks with the inclusive KL using importance weights, highlighting the utility of forward-direction divergences for making proposals mass-covering toward the true posterior. Rényi Divergence Variational Inference generalized VI to α-divergences and showed that α>1—including α=2 corresponding to χ2—induces mass-covering behavior and yields an upper bound on log evidence (CUBO), clarifying the role of χ2 within a unified framework. Black-box α divergence minimization provided practical tools to optimize α-divergences, demonstrating that forward-divergence objectives can be stably trained for flexible variational families. Complementing these, the sample size required in importance sampling proved that IS efficiency and weight degeneracy are controlled by the forward χ2 divergence between target and proposal, pinpointing χ2 as the quantity to minimize for low-variance estimators. Variational/Auto-Encoding SMC showed that one can directly train models by maximizing stochastic estimators of the marginal likelihood while learning proposal distributions. Together, these works reveal a gap: lower-bound objectives or generic α-divergences do not directly minimize IS variance for evidence estimation. The natural next step is to use importance sampling with a proposal trained by forward χ2 minimization—precisely the divergence that governs IS efficiency—and to optimize the resulting marginal likelihood estimator end-to-end. VIS synthesizes these ideas, replacing bound-tightening with direct likelihood maximization and aligning proposal learning with the variance-optimal criterion.

---

*Analysis generated on: 2026-01-06T23:33:41.884371*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
