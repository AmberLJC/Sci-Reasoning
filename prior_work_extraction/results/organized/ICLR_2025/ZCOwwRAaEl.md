# Prior Work Analysis Report

## Target Paper

**Title:** Latent Bayesian Optimization via Autoregressive Normalizing Flows

**Conference:** ICLR 2025 (oral)

**Authors:** Seunghun Lee, Jinyoung Park, Jaewon Chu, Minseo Yoon, Hyunwoo J. Kim

**Keywords:** Bayesian optimization, normalizing flow

**Abstract:** 
> Bayesian Optimization (BO) has been recognized for its effectiveness in optimizing expensive and complex objective functions.
Recent advancements in Latent Bayesian Optimization (LBO) have shown promise by integrating generative models such as variational autoencoders (VAEs) to manage the complexity of high-dimensional and structured data spaces.
However, existing LBO approaches often suffer from the value discrepancy problem, which arises from the reconstruction gap between input and latent spa...

---

## Key Prior Works (5 papers with direct influence)

### 🏗️ Foundation

**Automatic Chemical Design Using a Data-Driven Continuous Representation of Molecules** (2018)
- *Authors:* Gómez-Bombarelli et al.
- *Direct Connection:* This work established the latent-space Bayesian optimization paradigm using VAEs (optimize in z, decode to x), whose encoder–decoder non-invertibility causes the reconstruction/value mismatch that NF-BO eliminates by switching to a bijective flow.

**Bayesian Optimization of Combinatorial Structures** (2018)
- *Authors:* Baptista and Poloczek
- *Direct Connection:* They formalized BO over learned continuous embeddings for high-dimensional, structured/discrete domains via autoencoders, a setup directly adopted by NF-BO but addressed with an invertible mapping to avoid latent–input discrepancies.

**Density Estimation Using Real NVP** (2017)
- *Authors:* Dinh et al.
- *Direct Connection:* Real NVP introduced tractable, exactly invertible normalizing flows with explicit left-inverses, providing the core mechanism NF-BO leverages to remove the reconstruction gap in latent Bayesian optimization.

### 💡 Inspiration

**Masked Autoregressive Flow for Density Estimation** (2017)
- *Authors:* Papamakarios et al.
- *Direct Connection:* MAF’s autoregressive, invertible parameterization directly inspires NF-BO’s SeqFlow design, enabling expressive bijections that preserve exact encode–decode consistency during BO.

### 🔍 Gap Identification

**Junction Tree Variational Autoencoder for Molecular Graph Generation** (2018)
- *Authors:* Jin et al.
- *Direct Connection:* As a leading VAE-based latent optimization model for molecules, JT-VAE highlights persistent reconstruction errors and non-bijective mappings in LBO, the precise limitation NF-BO targets by enforcing a one-to-one encoder/decoder.

---

## Synthesis: How Prior Work Led to This Paper

Early work showed that expensive objective optimization could be carried out in a learned latent space: Gómez-Bombarelli et al. mapped molecules into a VAE’s continuous latent variables, optimized properties with a surrogate, and decoded candidates back to molecules. Baptista and Poloczek generalized this idea to high-dimensional, structured combinatorial domains by training autoencoders to provide the continuous embedding on which BO operates. Despite architectural advances like Junction Tree VAE, which improved molecular graph reconstruction via a structured decoder, these approaches retained a fundamental issue: the encoder–decoder mapping was not bijective, so optimizing in latent space did not guarantee that decoded designs faithfully reflected the optimized latent values. In parallel, normalizing flows provided a principled solution for exact, learnable bijections. Real NVP demonstrated tractable, invertible transformations with explicit left-inverses, and Masked Autoregressive Flow introduced highly expressive autoregressive, invertible parameterizations capable of modeling complex, high-dimensional distributions while guaranteeing exact forward and inverse maps.

Together, these lines of work revealed both the promise and the bottleneck of latent-space BO: autoencoder-based embeddings enabled search over complex domains, but non-invertibility induced a value discrepancy between latent and input spaces. Normalizing flows, and especially autoregressive flows, offered the missing ingredient—an expressive, one-to-one mapping with an exact inverse. The current paper synthesizes these insights by replacing VAEs with an autoregressive normalizing flow (SeqFlow), maintaining encode–decode consistency and thereby eliminating the reconstruction gap that previously propagated errors through the BO loop.

---

*Analysis generated on: 2026-01-06T10:56:13.344719*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
