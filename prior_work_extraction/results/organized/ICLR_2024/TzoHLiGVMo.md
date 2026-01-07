# Prior Work Analysis Report

## Target Paper

**Title:** ODEFormer: Symbolic Regression of Dynamical Systems with Transformers

**Conference:** ICLR 2024 (spotlight)

**Authors:** Stéphane d'Ascoli, Sören Becker, Philippe Schwaller, Alexander Mathis, Niki Kilbertus

**Keywords:** symbolic regression, dynamical systems, differential equations, transformer

**Abstract:** 
> We introduce ODEFormer, the first transformer able to infer multidimensional ordinary differential equation (ODE) systems in symbolic form from the observation of a single solution trajectory. We perform extensive evaluations on two datasets: (i) the existing ‘Strogatz’ dataset featuring two-dimensional systems; (ii) ODEBench, a collection of one- to four-dimensional systems that we carefully curated from the literature to provide a more holistic benchmark. ODEFormer consistently outperforms exi...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Discovering governing equations from data by sparse identification of nonlinear dynamical systems** (2016)
- *Authors:* Steven L. Brunton et al.
- *Direct Connection:* This work formalized the problem of recovering an ODE’s right-hand side from observed trajectories (SINDy), which ODEFormer tackles while removing SINDy’s reliance on hand-crafted libraries and numerical differentiation.

**Discovering symbolic models from deep learning with inductive biases** (2020)
- *Authors:* Miles Cranmer et al.
- *Direct Connection:* This work popularized symbolic discovery for dynamical systems and curated the 2D ‘Strogatz’ ODE benchmark, which defines the evaluation setting ODEFormer targets and extends.

### 💡 Inspiration

**Deep Learning for Symbolic Mathematics** (2020)
- *Authors:* Guillaume Lample et al.
- *Direct Connection:* This paper demonstrated that sequence-to-sequence Transformers trained on synthetic corpora can manipulate and generate formal mathematical expressions, directly inspiring ODEFormer’s autoregressive generation of symbolic ODEs.

**SymbolicGPT: A Generative Transformer Model for Symbolic Regression** (2021)
- *Authors:* Shayan G. Valipour et al.
- *Direct Connection:* SymbolicGPT showed that conditioning Transformers on sampled input–output data enables end-to-end symbolic regression, an idea ODEFormer adapts to condition on time-series trajectories to recover vector-field expressions.

### 📊 Baseline

**AI Feynman: A Physics-Inspired Method for Symbolic Regression** (2020)
- *Authors:* Silviu-Marian Udrescu et al.
- *Direct Connection:* AI Feynman is a primary symbolic-regression baseline that requires supervised (x, y) pairs—applied to ODEs via estimated derivatives—whose noise sensitivity and derivative dependence ODEFormer explicitly addresses.

**PySR: Fast & Parallelized Symbolic Regression in Python/Julia** (2023)
- *Authors:* Miles Cranmer
- *Direct Connection:* PySR is a state-of-the-art evolutionary symbolic regression baseline against which ODEFormer is directly compared, highlighting gains in robustness when derivatives are unavailable or noisy.

### 🔧 Extension

**Inferring biological networks by sparse identification of nonlinear dynamics** (2016)
- *Authors:* N. M. Mangan et al.
- *Direct Connection:* Implicit-SINDy extended SINDy to rational forms via implicit sparse regression, a capability ODEFormer generalizes by learning symbolic forms without pre-specifying function libraries.

---

## Synthesis: How Prior Work Led to This Paper

Sparse Identification of Nonlinear Dynamics (SINDy) established the blueprint for discovering ODE right-hand sides from trajectories by selecting a few terms from a hand-crafted function library, and Implicit-SINDy broadened that formulation to rational dynamics via implicit sparse regression. AI Feynman advanced general-purpose symbolic regression with physics-inspired heuristics and noise-aware procedures, typically applied to ODEs by first estimating derivatives from data. In parallel, Deep Learning for Symbolic Mathematics showed that Transformers trained on synthetic corpora can learn to parse and generate formal mathematical expressions with strong generalization, while SymbolicGPT demonstrated conditioning generative Transformers on input–output samples to recover concise closed-form expressions end-to-end. Complementing these methodological advances, work on discovering symbolic models with inductive biases curated the widely used two-dimensional ‘Strogatz’ ODE benchmark, crystallizing evaluation practices for symbolic modeling of dynamical systems. PySR then provided a fast evolutionary baseline for symbolic regression that is competitive on noiseless supervised settings but typically operates on (state, derivative) pairs derived from numeric differentiation. Together, these works highlight a gap: library- or derivative-dependent methods struggle with noise and irregular sampling, while Transformer-based symbolic regression had not targeted vector-field discovery from a single trajectory. ODEFormer naturally synthesizes these strands by conditioning a Transformer on raw trajectories to autoregressively generate symbolic ODE systems, thereby bypassing derivative estimation and hand-crafted libraries while aligning with established dynamical-system benchmarks.

---

*Analysis generated on: 2026-01-06T17:53:45.133921*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
