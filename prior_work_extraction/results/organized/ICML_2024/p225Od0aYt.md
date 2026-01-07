# Prior Work Analysis Report

## Target Paper
**Title:** p225Od0aYt
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning** (1999)
- *Authors:* Richard S. Sutton et al.
- *Connection:* This options framework formalized temporally extended actions and terminations, providing the theoretical basis that PRISE instantiates by learning data-driven, variable-duration macro-actions from demonstrations.

**Neural Discrete Representation Learning (VQ-VAE)** (2017)
- *Authors:* Aaron van den Oord et al.
- *Connection:* Provided the vector quantization paradigm for mapping continuous signals to discrete codebooks; PRISE’s first stage—quantizing continuous actions into discrete primitives—follows this idea before applying BPE.

### 💡 Inspiration

**Neural Machine Translation of Rare Words with Subword Units** (2016)
- *Authors:* Rico Sennrich et al.
- *Connection:* Introduced byte pair encoding (BPE) for subword tokenization; PRISE directly adapts BPE to compress action sequences into a variable-length action vocabulary, the paper’s core innovation.

**CompILE: Compositional Imitation Learning and Execution** (2019)
- *Authors:* Tobias Kipf et al.
- *Connection:* Demonstrated unsupervised, variable-length segmentation of demonstrations into reusable sub-tasks; PRISE pursues the same goal but replaces latent-variable segmentation with lightweight BPE-style compression of action sequences.

### 🔍 Gap Identification

**Trajectory Transformer: Offline Reinforcement Learning as Sequence Modeling** (2021)
- *Authors:* Michael Janner et al.
- *Connection:* Showed that discretized trajectories can be modeled as token sequences, but tokens are fixed at step-level granularity; PRISE addresses this gap by using BPE to merge frequent action n-grams into variable-duration skills.

**SPiRL: Learning Skill Priors for Reinforcement Learning** (2020)
- *Authors:* Karl Pertsch et al.
- *Connection:* Learns skill priors from offline demonstrations using fixed-length segments; PRISE explicitly overcomes this fixed-horizon limitation by discovering variable-span skills via BPE-style sequence compression.

---

## Synthesis

PRISE’s core idea—casting temporal action abstraction as sequence compression—stands on two pillars: the options framework from reinforcement learning and subword tokenization from NLP. Sutton, Precup, and Singh’s options formalized temporally extended actions and terminations, supplying the theoretical scaffold for learning skills of variable duration. From the language side, Sennrich et al.’s introduction of BPE showed how data-driven merging of frequent symbol pairs yields compact, variable-length vocabularies; PRISE directly imports this mechanism to actions, defining skills as compressed action n-grams. To make action sequences tokenizable, PRISE first discretizes continuous actions, drawing on van den Oord et al.’s VQ-VAE paradigm for converting continuous signals into discrete codebooks. The work also responds to concrete gaps in sequence-modeling for control and prior skill-learning. Trajectory Transformer established that discretized trajectories can be modeled as token sequences but retained fixed step-level granularity, offering no temporal abstraction; PRISE’s BPE merges address this by inducing variable-span skills. In demonstration-driven hierarchical learning, SPiRL learns skill priors from fixed-length segments, a rigidity PRISE removes by discovering skills whose durations adapt to data statistics. Finally, CompILE’s variable-length segmentation of demonstrations provided evidence that compositional, data-driven decomposition is useful, while PRISE achieves a similar end with a simpler, scalable compression algorithm. Together, these works directly shape PRISE’s method: quantize actions, compress with BPE, and realize options as learned, variable-duration action tokens.

---
*Generated: 2026-01-06T23:09:26.438190*
