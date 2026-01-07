# Prior Work Analysis Report

## Target Paper

**Title:** Steering Protein Family Design through Profile Bayesian Flow

**Conference:** ICLR 2025 (oral)

**Authors:** Jingjing Gong, Yu Pei, Siyu Long, Yuxuan Song, Zhe Zhang, Wenhao Huang, Ziyao Cao, Shuyi Zhang, Hao Zhou, Wei-Ying Ma

**Keywords:** protein family generation, homologous protein generation, protein design, bayesian flow

**Abstract:** 
> Protein family design emerges as a promising alternative by combining the advantages of de novo protein design and mutation-based directed evolution.In this paper, we propose ProfileBFN, the Profile Bayesian Flow Networks, for specifically generative modeling of protein families. ProfileBFN extends the discrete Bayesian Flow Network from an MSA profile perspective, which can be trained on single protein sequences by regarding it as a degenerate profile, thereby achieving efficient protein family...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Profile hidden Markov models** (1998)
- *Authors:* Sean R. Eddy
- *Direct Connection:* The notion of protein families as position-specific residue distributions (profiles) is the conceptual basis that ProfileBFN adopts and generalizes into a learnable flow over profiles, with single sequences as degenerate profiles.

**Deep generative models of genetic variation capture mutation effects** (2018)
- *Authors:* Riesselman et al.
- *Direct Connection:* This VAE trained on family MSAs established family-specific generative modeling for proteins, which ProfileBFN targets while removing the need for large MSAs by learning in profile space from single sequences.

### 💡 Inspiration

**Generative Flow Networks** (2021)
- *Authors:* Bengio et al.
- *Direct Connection:* The flow-based construction for sampling in discrete spaces inspired ProfileBFN’s use of forward–backward flow factorization to model combinatorial sequence spaces without autoregressive decoding.

### 🔍 Gap Identification

**Mutation effects predicted from sequence co-variation** (2017)
- *Authors:* Hopf et al.
- *Direct Connection:* Potts/EVmutation showed MSA-derived pairwise couplings capture family constraints but depend on deep MSAs; ProfileBFN addresses this limitation by replacing explicit MSA dependence with profile-guided Bayesian flows.

**MSA Transformer** (2021)
- *Authors:* Rao et al.
- *Direct Connection:* While MSA Transformer exploits multiple-sequence alignments to capture coevolutionary structure, its reliance on large MSAs motivates ProfileBFN’s design to capture family structure without building or training on MSAs.

### 📊 Baseline

**Large language models generate functional protein sequences** (2023)
- *Authors:* Madani et al.
- *Direct Connection:* This LLM-based generator conditions on global tags to bias function/family, a coarse control that ProfileBFN improves upon by conditioning generation on per-position profile priors to steer family design more precisely.

### 🔧 Extension

**Discrete Bayesian Flow Networks** (2024)
- *Authors:* Zhang et al.
- *Direct Connection:* ProfileBFN directly extends the discrete Bayesian Flow Network objective from token-level sequences to position-wise profile distributions, enabling training on single sequences by treating them as degenerate profiles and steering generation with profile priors.

---

## Synthesis: How Prior Work Led to This Paper

Profile hidden Markov models introduced the core idea that a protein family can be represented as a position-specific distribution over residues, providing a profile that summarizes permissible amino acids at each site. DeepSequence demonstrated that training generative models directly on MSAs yields family-specific distributions that capture mutational constraints and predict fitness effects. EVmutation further showed that pairwise couplings extracted from MSAs encode family constraints, underscoring the utility and limitations of MSA-derived statistics. MSA Transformer leveraged multiple sequences to learn coevolutionary structure via attention, validating that family information is richly encoded in aligned sets but at the cost of constructing large MSAs. In parallel, Generative Flow Networks established a flow-based paradigm for sampling in discrete combinatorial spaces by learning consistent forward and backward flows, offering a non-autoregressive route to discrete generation. Building on this line, Discrete Bayesian Flow Networks introduced a training objective that makes flow-based generation practical for categorical sequences by estimating transitions consistent with a target posterior over discrete states. Recent LLM-based protein generators such as ProGen2 showed that global conditioning can bias function across families, while revealing the need for finer, position-wise control. Taken together, these works pointed to a gap: family-aware generative modeling benefits from profile-level constraints but is bottlenecked by MSA construction and lacks precise steering. ProfileBFN naturally emerges by marrying the profile representation with Bayesian flow objectives, lifting flows from tokens to per-position distributions so that single sequences act as degenerate profiles, thereby eliminating MSA requirements while enabling precise, profile-driven control over family design.

---

*Analysis generated on: 2026-01-06T12:01:14.683293*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
