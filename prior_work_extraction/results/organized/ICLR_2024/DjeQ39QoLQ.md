# Prior Work Analysis Report

## Target Paper

**Title:** Robustifying State-space Models for Long Sequences via Approximate Diagonalization

**Conference:** ICLR 2024 (spotlight)

**Authors:** Annan Yu, Arnur Nigmetov, Dmitriy Morozov, Michael W. Mahoney, N. Benjamin Erichson

**Keywords:** state-space models, sequence models, Long-Range Arena, recurrent neural networks

**Abstract:** 
> State-space models (SSMs) have recently emerged as a framework for learning long-range sequence tasks. An example is the structured state-space sequence (S4) layer, which uses the diagonal-plus-low-rank structure of the HiPPO initialization framework. However, the complicated structure of the S4 layer poses challenges; and, in an effort to address these challenges, models such as S4D and S5 have considered a purely diagonal structure. This choice simplifies the implementation, improves computati...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**HiPPO: Recurrent Memory with Optimal Polynomial Projections** (2020)
- *Authors:* Albert Gu et al.
- *Direct Connection:* Introduces the non-normal Legendre HiPPO operators and the SSM initialization that diagonal SSMs attempt to diagonalize—whose ill-posedness the PTD method explicitly targets.

**Efficiently Modeling Long Sequences with Structured State Spaces** (2022)
- *Authors:* Albert Gu et al.
- *Direct Connection:* Establishes the S4 layer and the diagonal-plus-low-rank (NPLR) formulation built on HiPPO, defining the core SSM framework and motivating the search for simpler (diagonal) parameterizations that PTD robustifies.

**Matrix Perturbation Theory** (1990)
- *Authors:* G. W. Stewart et al.
- *Direct Connection:* Supplies the backward error and eigen-structure perturbation bounds that justify PTD’s backward-stable approach to approximate diagonalization of ill-conditioned non-normal matrices like HiPPO.

### 💡 Inspiration

**Spectra and Pseudospectra: The Behavior of Nonnormal Matrices and Operators** (2005)
- *Authors:* Lloyd N. Trefethen et al.
- *Direct Connection:* Provides the pseudospectral theory of non-normal operators that underpins the insight that small perturbations can yield well-conditioned approximate diagonalizations, directly motivating PTD’s perturb-then-diagonalize strategy.

### 🔍 Gap Identification

**S4D: Simple State-Space Models for Sequence Modeling** (2022)
- *Authors:* Albert Gu et al.
- *Direct Connection:* Proposes using a purely diagonal state matrix by diagonalizing HiPPO for efficiency and channel mixing, but implicitly inherits the ill-posed diagonalization that PTD directly addresses with backward-stable approximate diagonalization.

### 📊 Baseline

**S5: Simplified State Space Models for Sequence Modeling** (2023)
- *Authors:* First author et al.
- *Direct Connection:* Adopts a diagonal SSM parameterization to simplify S4-style models, serving as a primary baseline whose diagonalization step is made robust by the proposed perturb-then-diagonalize methodology.

---

## Synthesis: How Prior Work Led to This Paper

HiPPO: Recurrent Memory with Optimal Polynomial Projections defined continuous-time state-space memory operators (notably the non-normal Legendre matrices) and an initialization scheme that made SSMs practical for long-range dependencies; crucially, these operators are difficult to diagonalize stably. Efficiently Modeling Long Sequences with Structured State Spaces (S4) built on HiPPO to create a state-space layer using a diagonal-plus-low-rank (NPLR) structure, showing that long convolutions can be realized efficiently but at the cost of implementation complexity. S4D simplified this by forcing a purely diagonal state matrix via diagonalization of HiPPO, yielding efficiency and channel communication but implicitly relying on a diagonalization that can be numerically ill-posed. Similarly, S5 advanced simplified diagonal SSMs as strong sequence models, but its reliance on diagonalization inherits the same fragility. Outside of modeling, Spectra and Pseudospectra by Trefethen and Embree established how non-normal operators possess sensitive spectra, where small perturbations can dramatically alter eigen-structure yet yield more numerically stable diagonalizations. Matrix Perturbation Theory by Stewart and Sun formalized backward-stability and eigen-perturbation bounds that guide principled perturbation-based algorithms.
Together, these works reveal a tension: diagonal SSMs promise simplicity and speed but rest on an unstable diagonalization of non-normal HiPPO operators. The pseudospectral and perturbation theories suggest a remedy—inject controlled perturbations to obtain a nearby, well-conditioned operator and only then diagonalize. The present work synthesizes these insights into a backward-stable perturb-then-diagonalize procedure that robustifies diagonal SSMs like S4D/S5 while preserving their efficiency, providing a principled approximate diagonalization tailored to the HiPPO-driven SSM setting.

---

*Analysis generated on: 2026-01-06T14:14:56.615032*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
