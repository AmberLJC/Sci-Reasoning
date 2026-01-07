# Prior Work Analysis Report

## Target Paper
**Title:** 9ehJCZz4aM
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning** (1999)
- *Authors:* Sutton et al.
- *Connection:* AutoCGP’s manipulation “concepts” are operationalized as temporally extended primitives akin to options, and its Concept Selection Transformer plays the role of an option selector for long-horizon control.

**Learning Latent Plans from Play** (2019)
- *Authors:* Lynch et al.
- *Connection:* AutoCGP adopts the label-free play/unlabeled demonstrations paradigm and the notion of latent plan variables from Play-LMP, but replaces single-shot plan inference with closed-loop concept selection for robust long-horizon execution.

### 💡 Inspiration

**CompILE: Compositional Imitation Learning and Execution** (2019)
- *Authors:* Kipf et al.
- *Connection:* AutoCGP directly builds on the idea of unsupervised decomposition of demonstrations into reusable sub-behaviors, generalizing CompILE’s latent segment discovery to proprioceptive manipulation concepts and coupling it with closed-loop online selection.

**Diversity is All You Need: Learning Diverse Skills without a Reward Function** (2018)
- *Authors:* Eysenbach et al.
- *Connection:* AutoCGP’s automatic concept discovery echoes DIAYN’s unsupervised skill discovery by inducing consistent, distinguishable behaviors, but grounds them in structure present in demonstrations and proprioceptive state rather than pure exploration.

**Concept Bottleneck Models** (2020)
- *Authors:* Koh et al.
- *Connection:* AutoCGP inherits the idea of decision-making through an intermediate concept bottleneck, while removing the reliance on human-annotated concepts by discovering manipulation concepts self-supervised from proprioception.

### 🔍 Gap Identification

**Do As I Can, Not As I Say: Grounding Language in Robotic Affordances** (2022)
- *Authors:* Ahn et al.
- *Connection:* AutoCGP explicitly targets the misalignment and annotation burden in language/label-conditioned policies exemplified by SayCan, replacing human semantics with autonomously discovered manipulation concepts for long-horizon guidance.

### 🔗 Related Problem

**HIRO: Hierarchical Reinforcement Learning with Off-Policy Correction** (2018)
- *Authors:* Nachum et al.
- *Connection:* AutoCGP’s two-level structure (high-level concept selection guiding a low-level controller) parallels HIRO’s hierarchical control, adapting the idea to imitation from unlabeled demos via discovered concept-conditioned policies rather than hand-specified subgoals.

---

## Synthesis

AutoCGP stands at the intersection of temporal abstraction, unsupervised skill discovery, and concept-guided decision making. Its core construct—closed-loop manipulation concepts—rests on the options framework, which formalized temporally extended actions and high-level selection. It directly inherits from CompILE and Play-LMP the central premise that unlabeled demonstrations contain compositional structure: CompILE’s unsupervised segmentation reveals reusable sub-behaviors, and Play-LMP’s latent plans show how such structure can guide low-level control without task labels. AutoCGP fuses these threads into a closed-loop system that continually selects among discovered concepts, rather than committing to a single global plan, enabling robustness over long horizons. 
In form, AutoCGP mirrors hierarchical controllers such as HIRO, but replaces hand-crafted or externally defined subgoals with self-discovered, proprioception-grounded concepts derived from demonstration data. Its concept discovery is philosophically aligned with DIAYN—skills as identifiable, diverse behaviors—yet is tailored to the structure present in manipulation trajectories rather than exploration. Crucially, AutoCGP adopts the interpretability benefits of concept bottlenecks without requiring human annotations, thereby addressing a key limitation of language/label-conditioned approaches like SayCan: semantic misalignment and annotation overhead. The result is a concept-guided, closed-loop policy that preserves compositionality and interpretability while operating entirely from unlabeled demonstrations.

---
*Generated: 2026-01-06T23:09:26.638892*
