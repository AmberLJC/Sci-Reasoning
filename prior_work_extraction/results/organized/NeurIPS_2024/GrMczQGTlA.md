# Prior Work Analysis Report

## Target Paper
**Title:** GrMczQGTlA
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core idea—casting humanoid locomotion as next-token prediction with a causal transformer over modality-aligned sensorimotor sequences—stands on a clear lineage of sequence modeling for control and multimodal generalist agents. Decision Transformer and Trajectory Transformer provided the decisive methodological shift: treat control as autoregressive sequence modeling, with discretization/tokenization strategies that make continuous sensorimotor streams amenable to next-token prediction. Building on this, Gato established that a single transformer can operate on interleaved, modality-tagged tokens across vision, language, and action, directly informing the paper’s modality-aligned autoregression and its ability to train on heterogeneous inputs.
RT-2 showed that augmenting robot data with internet-scale visual-language corpora and action vocabularies materially improves real-world generalization, an insight mirrored here by mixing prior policy/controller rollouts, mocap, and YouTube human videos. DeepMimic contributed the blueprint for exploiting motion capture as a rich supervision source for humanoid skills, legitimizing mocap as a key component of the training set. VPT demonstrated a practical path to leverage web videos where action labels are absent, conceptually supporting the paper’s objective that predicts the next token within each modality and thus tolerates missing modalities. Finally, Rapid Motor Adaptation highlighted strategies for robust real-world locomotion and zero-shot transfer, shaping the paper’s emphasis on deployment in the wild and generalization from limited hours of data. Together, these works converge on a unified, autoregressive, multimodal paradigm that this paper extends to real humanoid walking.

---
*Generated: 2026-01-06T23:39:42.952893*
