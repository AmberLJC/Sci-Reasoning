# Prior Work Analysis Report

## Target Paper

**Title:** A Second-Order Perspective on Model Compositionality and Incremental Learning

**Conference:** ICLR 2025 (spotlight)

**Authors:** Angelo Porrello, Lorenzo Bonicelli, Pietro Buzzega, Monica Millunzi, Simone Calderara, Rita Cucchiara

**Keywords:** Continual Learning, Model Compositionality, Ensemble Learning, Task Arithmetic

**Abstract:** 
> The fine-tuning of deep pre-trained models has revealed compositional properties, with multiple specialized modules that can be arbitrarily composed into a single, multi-task model. However, identifying the conditions that promote compositionality remains an open issue, with recent efforts concentrating mainly on linearized networks. We conduct a theoretical study that attempts to demystify compositionality in standard non-linear networks through the second-order Taylor approximation of the loss...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Overcoming catastrophic forgetting in neural networks** (2017)
- *Authors:* Kirkpatrick et al.
- *Direct Connection:* We adapt EWC’s Fisher‑weighted quadratic penalty, originally used to retain past tasks, into a mechanism for staying near the pre‑trained optimum so that incrementally learned modules remain mutually compatible for composition.

### 💡 Inspiration

**Editing Models with Task Arithmetic** (2023)
- *Authors:* Ilharco et al.
- *Direct Connection:* This work’s task‑vector view—treating fine‑tuning as additive weight updates that can be linearly combined—directly motivates our analysis, which generalizes beyond linearized assumptions via a second‑order Taylor model to state when and how such compositions remain valid.

### 🔍 Gap Identification

**TIES-Merging: Resolving Interference When Merging Models** (2023)
- *Authors:* Yadav et al.
- *Direct Connection:* We address the interference that TIES mitigates via sign‑pruning heuristics by providing principled second‑order criteria for safe composition and training procedures that avoid creating conflicting directions in the first place.

### 📊 Baseline

**Model Soups: Averaging weights of multiple fine-tuned models improves accuracy without additional training** (2022)
- *Authors:* Wortsman et al.
- *Direct Connection:* Their finding that simple parameter averaging works when fine‑tuned models lie in the same loss basin informs our formalization of the pre‑training basin condition and motivates training rules that explicitly keep modules in‑basin to enable composability.

### 🔧 Extension

**Merging Models with Fisher-Weighted Averaging** (2022)
- *Authors:* Matena and Raffel
- *Direct Connection:* We extend the Fisher‑weighted merging principle—derived from a local quadratic (second‑order) loss approximation—by using the same second‑order lens not only for post‑hoc merging but to design dual incremental optimization procedures for modules and their composition.

### 🔗 Related Problem

**Git Re-Basin: Merging Models modulo Permutation Symmetries** (2023)
- *Authors:* Ainsworth et al.
- *Direct Connection:* Where they resolve permutation symmetries to enable model merging, our theory explains when such re‑basining is unnecessary—namely when updates remain within the pre‑training basin—and our algorithms enforce this during training.

---

## Synthesis: How Prior Work Led to This Paper

Task arithmetic introduced the idea that fine-tuning creates task vectors—parameter offsets from a common pre-trained model—that can be additively combined to edit capabilities, an effect largely justified by local linearity around the pre-training point. Model soups then showed that simple weight averaging of fine-tuned models can improve performance, but only when the models reside in a shared basin of the loss landscape, hinting at geometric conditions for successful composition. Merging models with Fisher-weighted averaging grounded composition in a second-order Taylor expansion of the loss, using Fisher information to weight parameters during post-hoc merging. Elastic Weight Consolidation further established the practical power of second-order (Fisher-based) quadratic approximations by constraining updates to remain near previous optima to prevent forgetting. Git Re-Basin revealed that when models drift into different symmetry-equivalent basins, permutation alignment is required before merging. Finally, TIES-Merging highlighted interference between fine-tuned updates and proposed heuristic sign-pruning to reduce destructive interactions when combining models.

Together, these works expose a gap: empirical weight-space composition is effective but fragile, with success tied to implicit basin proximity and ad hoc fixes for interference, and theory often limited to linearized regimes or post-hoc merging. Building on their insights, a second-order perspective naturally emerges to formalize the pre-training basin as the safe region for compositionality and to transform Fisher-based quadratic reasoning into training-time, dual incremental procedures that keep modules compatible while also directly optimizing their composed model.

---

*Analysis generated on: 2026-01-06T11:53:34.464727*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
