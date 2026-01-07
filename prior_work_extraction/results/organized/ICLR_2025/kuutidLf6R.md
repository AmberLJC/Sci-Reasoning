# Prior Work Analysis Report

## Target Paper

**Title:** Diffusion Attribution Score: Evaluating Training Data Influence in Diffusion Models

**Conference:** ICLR 2025 (spotlight)

**Authors:** Jinxu Lin, Linwei Tao, Minjing Dong, Chang Xu

**Keywords:** Diffusion Model; Data Attribution; Training Data Influence

**Abstract:** 
> As diffusion models become increasingly popular, the misuse of copyrighted and private images has emerged as a major concern. One promising solution to mitigate this issue is identifying the contribution of specific training samples in generative models, a process known as data attribution. Existing data attribution methods for diffusion models typically quantify the contribution of a training sample by evaluating the change in diffusion loss when the sample is included or excluded from the trai...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Denoising Diffusion Probabilistic Models** (2020)
- *Authors:* Jonathan Ho et al.
- *Direct Connection:* This work formalized the standard diffusion training objective as MSE on noise prediction across timesteps, whose loss formulation (comparing predictions to ground-truth noise) is exactly the objective prior attribution methods optimized and that this paper argues is mismatched for measuring sample influence.

**Estimation of Non-Normalized Statistical Models by Score Matching** (2005)
- *Authors:* Aapo Hyvärinen
- *Direct Connection:* Score matching connects training to Fisher divergence with the data distribution, clarifying that diffusion losses measure divergence to ground-truth distributions rather than directly contrasting two models’ predictive behaviors—the precise conceptual gap this paper addresses by proposing a direct model-to-model distribution comparison.

**Understanding Black-box Predictions via Influence Functions** (2017)
- *Authors:* Pang Wei Koh et al.
- *Direct Connection:* Influence functions define training-sample contribution via leave-one-out effects on loss, a paradigm adopted by diffusion data attribution that this paper retains in spirit while replacing the loss with a direct predictive-distribution discrepancy between models.

**Data Shapley: Equitable Valuation of Data for Machine Learning** (2019)
- *Authors:* Amirata Ghorbani et al.
- *Direct Connection:* Data Shapley formalizes per-sample contribution as marginal utility measured via a task loss; this paper keeps the marginal-contribution framing but substitutes utility with a direct comparison of predicted distributions to better capture differences in model behavior for diffusion models.

### 🔍 Gap Identification

**Extracting Training Data from Diffusion Models** (2023)
- *Authors:* Nicholas Carlini et al.
- *Direct Connection:* By demonstrating concrete training data memorization and privacy risks in diffusion models, this work motivates the need for precise per-sample attribution beyond loss-based proxies, directly prompting the development of a more behavior-faithful attribution score.

### 📊 Baseline

**Estimating Training Data Influence by Tracing Gradient Descent** (2020)
- *Authors:* Garima Pruthi et al.
- *Direct Connection:* TracIn provides a practical, loss-based influence approximation widely used as a baseline; the proposed Diffusion Attribution Score improves on this class of methods by replacing diffusion-loss dependence with a direct divergence between model predictive distributions.

---

## Synthesis: How Prior Work Led to This Paper

The core loss used to train diffusion models was established by Denoising Diffusion Probabilistic Models, which framed training as timestep-weighted MSE on noise prediction; this objective compares predictions to ground-truth noise rather than contrasting two models’ behaviors. Score matching theory further clarifies that such training minimizes Fisher divergence to the data distribution, reinforcing that diffusion loss is a model-to-data discrepancy rather than a direct model-to-model comparison. In parallel, influence functions framed training-sample contribution as the leave-one-out effect on loss, and Data Shapley formalized sample valuation as marginal utility, both cementing the loss-centric view of data attribution. TracIn operationalized this paradigm with a scalable approximation based on gradient-trajectory inner products, becoming a practical baseline for influence estimation. Meanwhile, work on extracting training data from diffusion models exposed real privacy and copyright stakes, underscoring the importance of accurate attribution beyond coarse loss-based measures.
Taken together, these strands revealed a mismatch: diffusion attribution inherited loss-based utilities that inherently compare models to ground-truth distributions, not to each other, obscuring differences in model behavior attributable to specific samples. The natural next step is to retain the leave-one-out/marginal-contribution framing while redefining the utility to directly compare predicted distributions of models trained with versus without a sample. By grounding attribution in model-to-model predictive divergence instead of diffusion loss, the proposed approach directly targets behavioral variance, yielding a more faithful measure of training data influence in diffusion models.

---

*Analysis generated on: 2026-01-06T18:03:27.471588*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
