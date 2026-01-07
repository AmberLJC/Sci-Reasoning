# Prior Work Analysis Report

## Target Paper

**Title:** RetroBridge: Modeling Retrosynthesis with Markov Bridges

**Conference:** ICLR 2024 (spotlight)

**Authors:** Ilia Igashov, Arne Schneuing, Marwin Segler, Michael M. Bronstein, Bruno Correia

**Keywords:** Retrosynthesis, Reactions, Chemistry, Drug Discovery, Markov Bridge

**Abstract:** 
> Retrosynthesis planning is a fundamental challenge in chemistry which aims at designing multi-step reaction pathways from commercially available starting materials to a target molecule. Each step in multi-step retrosynthesis planning requires accurate prediction of possible precursor molecules given the target molecule and confidence estimates to guide heuristic search algorithms. We model single-step retrosynthesis as a distribution learning problem in a discrete state space. First, we introduc...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Diffusion Schrödinger Bridge** (2021)
- *Authors:* Louis De Bortoli et al.
- *Direct Connection:* This work establishes generative modeling via bridges conditioned on endpoints, providing the theoretical template of connecting two intractable distributions that RetroBridge adapts to discrete Markov chains for retrosynthesis.

**Retro*: Learning Retrosynthetic Planning with Neural Guided A*** (2020)
- *Authors:* Xianggen Liu et al. (often cited as Chen et al.)
- *Direct Connection:* Retro* frames multi‑step retrosynthesis as heuristic search driven by calibrated single‑step likelihoods, directly motivating RetroBridge’s focus on probabilistic single‑step modeling with confidence estimates.

### 💡 Inspiration

**Denoising Diffusion Bridges** (2023)
- *Authors:* Michael S. Albergo et al.
- *Direct Connection:* By introducing learning objectives along diffusion bridges to transport between endpoint distributions, this paper directly inspires RetroBridge’s endpoint‑conditioned denoising objective while motivating a bridge‑based alternative to standard diffusion.

**Stochastic Interpolants: A Unifying Framework for Flows and Diffusions** (2022)
- *Authors:* Michael S. Albergo et al.
- *Direct Connection:* Stochastic interpolants formalize paths pinned at endpoints, a key insight RetroBridge adopts by parameterizing discrete Markov bridges that interpolate between product and precursor molecules.

### 🔍 Gap Identification

**Structured Denoising Diffusion Models in Discrete State Spaces (D3PM)** (2021)
- *Authors:* Jacob Austin et al.
- *Direct Connection:* D3PM highlights the core limitation of discrete diffusion—needing a hand‑designed, tractable corruption/noise process—which RetroBridge explicitly avoids by learning a Markov bridge pinned at data endpoints instead of relying on a simple noise prior.

### 📊 Baseline

**RetroXpert: Decompose Retrosynthesis Prediction via Reaction Center Identification and Synthon-Based Editing** (2020)
- *Authors:* Chao Yan et al.
- *Direct Connection:* As a leading template‑free single‑step method, RetroXpert serves as a primary competitor that RetroBridge targets, contrasting a deterministic edit pipeline with a learned Markov bridge over discrete molecular states.

### 🔗 Related Problem

**Generative Flow Networks** (2021)
- *Authors:* Yoshua Bengio et al.
- *Direct Connection:* GFlowNets show how to learn stochastic policies over discrete trajectories to match target terminal distributions, informing RetroBridge’s use of a learned multi‑step Markov process in discrete chemical state spaces.

---

## Synthesis: How Prior Work Led to This Paper

Work on discrete diffusion models such as D3PM established that denoising in token spaces hinges on a prescribed, tractable corruption process, an assumption that can distort discrete structures like molecular graphs. Schrödinger-bridge formulations subsequently introduced generative modeling as learning a process that connects two endpoint distributions; the Diffusion Schrödinger Bridge made this concrete by conditioning dynamics on both endpoints to transport mass between complex marginals. Denoising Diffusion Bridges refined this perspective with training objectives defined along the bridge path, demonstrating that endpoint-conditioned denoising can replace reliance on simple priors. Stochastic Interpolants unified flows and diffusions through endpoint-pinned paths, clarifying how to construct learnable interpolations between paired samples. In discrete domains, Generative Flow Networks showed that one can learn stochastic multi-step policies to realize target terminal distributions via Markovian trajectories, highlighting the practicality of trajectory-based generative modeling in combinatorial state spaces. In retrosynthesis, Retro* formulated multi-step planning as heuristic search that depends critically on calibrated single-step probabilities, and RetroXpert provided a strong template-free baseline for single-step reactant prediction via synthon edits. Together, these works revealed a gap: while bridges enable endpoint-conditioned transport, existing methods largely target continuous spaces or require simple priors, and discrete diffusion imposes unnatural noise. The natural next step is a discrete, endpoint-conditioned Markov process that learns directly from paired (product, precursor) data, yielding calibrated conditional likelihoods for search. RetroBridge synthesizes bridge-based generative transport with discrete, trajectory-based modeling to connect product molecules to plausible precursors without a tractable noise distribution.

---

*Analysis generated on: 2026-01-06T19:09:18.025720*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
