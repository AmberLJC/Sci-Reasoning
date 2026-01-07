# Prior Work Analysis Report

## Target Paper

**Title:** Variational Inference for SDEs Driven by Fractional Noise

**Conference:** ICLR 2024 (spotlight)

**Authors:** Rembert Daems, Manfred Opper, Guillaume Crevecoeur, Tolga Birdal

**Keywords:** variational inference, neural sdes, stochastic differential equations, brownian motion, fractional noise, fractional brownian motion, markov approximation, markov representation

**Abstract:** 
> We present a novel variational framework for performing inference in (neural) stochastic differential equations (SDEs) driven by Markov-approximate fractional Brownian motion (fBM). SDEs offer a versatile tool for modeling real-world continuous-time dynamic systems with inherent noise and randomness. Combining SDEs with the powerful inference capabilities of variational methods, enables the learning of representative distributions through stochastic gradient descent. However, conventional SDEs t...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Variational Inference for Diffusion Processes** (2007)
- *Authors:* Archambeau et al.
- *Direct Connection:* Their variational framework derives an ELBO for Brownian-driven SDEs, which this paper generalizes to the Markov-augmented representation of fractional Brownian motion.

**Markovian Structure of the Volterra Heston Model** (2019)
- *Authors:* Abi Jaber and El Euch
- *Direct Connection:* They prove that Volterra processes with fractional kernels admit Markovian lifts via Laplace-transform measures, directly underpinning the state augmentation used to render fBM approximately Markov.

### 💡 Inspiration

**Turbocharging Monte Carlo pricing for the rough Bergomi model** (2018)
- *Authors:* McCrickerd and Pakkanen
- *Direct Connection:* They introduce multi-factor (sum-of-exponentials) approximations of fractional kernels that yield finite-dimensional Markov embeddings, the exact Markov approximation strategy adopted to enable VI with fBM.

### 📊 Baseline

**Neural Stochastic Differential Equations: Deep Latent Gaussian Models in the Diffusion Limit** (2019)
- *Authors:* Tzen and Raginsky
- *Direct Connection:* They cast latent SDEs as VAEs with pathwise reparameterization under Brownian noise, providing the core training setup that this work extends to fractional noise.

**Latent SDEs for Irregularly-Sampled Time Series** (2020)
- *Authors:* Li et al.
- *Direct Connection:* This practical VI framework for neural SDEs under Brownian motion motivates the need for a fractional-noise extension to capture long-range dependencies, which this paper provides.

### 🔗 Related Problem

**The Characteristic Function of Rough Heston Models** (2019)
- *Authors:* El Euch and Rosenbaum
- *Direct Connection:* They demonstrate accurate finite-factor Markov approximations and constructive quadrature schemes for fractional kernels, informing the discretization/parameterization choices for the Markov-approximate fBM used here.

---

## Synthesis: How Prior Work Led to This Paper

Archambeau and colleagues developed a variational framework for diffusion processes that yields an evidence lower bound for Brownian-driven SDEs, establishing how to perform tractable inference over continuous-time latent dynamics. Tzen and Raginsky cast neural SDEs as VAE-style latent generative models with pathwise reparameterization under Brownian motion, while Li and co-authors operationalized this setup for irregularly sampled data and scalable training, consolidating Brownian-based neural SDE VI as a practical baseline. In parallel, McCrickerd and Pakkanen proposed multi-factor sum-of-exponentials approximations of fractional kernels, producing finite-dimensional Markov embeddings that mimic long-memory behavior with auxiliary Ornstein–Uhlenbeck factors. Abi Jaber and El Euch formalized the Markovian lift of Volterra processes via Laplace-transform measures, providing theoretical justification for state augmentation that turns fractional dynamics into Markov ones. El Euch and Rosenbaum further demonstrated the practical accuracy of finite-factor approximations and offered constructive quadrature schemes for fractional kernels, validating these Markov embeddings for efficient computation.
Taken together, these works suggest a clear opportunity: marry the proven VI machinery for Brownian SDEs with the Markovian lifts of fractional processes to capture long-range dependence without sacrificing tractability. By adopting multi-factor Markov approximations of fBM grounded in Volterra–Laplace theory, and then plugging this augmented Markov system into the Brownian SDE ELBO and pathwise training pipelines, the present paper naturally extends neural SDE variational inference to fractional noise, overcoming the Brownian baseline’s inability to model long-memory while retaining computational efficiency.

---

*Analysis generated on: 2026-01-06T23:20:17.961307*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
