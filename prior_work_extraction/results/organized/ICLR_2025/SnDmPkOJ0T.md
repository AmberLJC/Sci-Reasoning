# Prior Work Analysis Report

## Target Paper
**Title:** SnDmPkOJ0T
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Similarity of Neural Network Representations Revisited** (2019)
- *Authors:* Simon Kornblith et al.
- *Connection:* REEF’s core fingerprint is the linear centered kernel alignment (CKA) between activations, directly adopting Kornblith et al.’s representation-similarity metric for its invariance to isotropic scaling and orthogonal reparameterizations, which underpins REEF’s robustness to fine-tuning, pruning, and permutations.

**Algorithms for learning kernels based on centered alignment** (2012)
- *Authors:* Corinna Cortes et al.
- *Connection:* REEF explicitly relies on centered kernel alignment as the fundamental similarity notion; Cortes et al. formalized centered alignment and its normalization, which REEF uses to compare models’ representation Gram matrices in a training-free manner.

### 🔍 Gap Identification

**Turning Your Weakness Into a Strength: Watermarking Deep Neural Networks by Backdooring** (2018)
- *Authors:* Yossi Adi et al.
- *Connection:* Backdoor-based watermarking demonstrates ownership but can be brittle to fine-tuning/pruning and may affect behavior; REEF directly addresses these limitations by using representation similarity without triggers or retraining.

**A Watermark for Large Language Models** (2023)
- *Authors:* Johannes Kirchenbauer et al.
- *Connection:* LLM output watermarking targets text provenance rather than model lineage and can trade off generation quality; REEF fills this gap by establishing model-level relationship detection via internal representations, independent of decoding or output watermarks.

### 📊 Baseline

**Embedding Watermarks into Deep Neural Networks** (2017)
- *Authors:* Yusuke Uchida et al.
- *Connection:* As a primary ownership-verification baseline that embeds watermarks into weights during training, Uchida et al.’s approach motivates REEF’s training-free alternative that avoids model modification while aiming for robustness under post-processing.

### 🔗 Related Problem

**SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability** (2017)
- *Authors:* Maithra Raghu et al.
- *Connection:* SVCCA established the paradigm of comparing internal representations across networks on shared inputs; REEF follows this setup but chooses CKA over CCA-based metrics for the invariances needed to make a robust representation fingerprint.

---

## Synthesis

REEF’s key contribution—training-free identification of lineage between a suspect and victim LLM via internal representations—stands on two pillars: representation similarity and model IP protection. On the representation side, Kornblith et al. introduced CKA as a principled, robust metric for comparing neural representations, highlighting invariances to isotropic scaling and orthogonal transformations. Cortes et al. provided the theoretical basis for centered kernel alignment and its normalization, which REEF operationalizes by comparing centered Gram matrices from the suspect and victim on the same inputs. Earlier work such as SVCCA by Raghu et al. defined the practical protocol of comparing hidden activations across networks on shared samples; REEF follows this setup but adopts CKA specifically for the invariances crucial to survive fine-tuning, pruning, permutation, and even model merging.
On the IP side, classic watermarking approaches like Uchida et al. embed signals into weights during training, while Adi et al. proposed backdoor-based watermarks. These methods either require modifying training, can degrade utility, or are vulnerable to post-processing—gaps REEF explicitly aims to overcome with a non-invasive, training-free fingerprint derived from representations. For LLMs, output watermarking by Kirchenbauer et al. secures text provenance, not model lineage. REEF addresses this unmet need by leveraging CKA-based representational fingerprints to directly infer whether a suspect model is derived from a victim model, without altering either model or its outputs.

---
*Generated: 2026-01-06T23:09:26.637014*
