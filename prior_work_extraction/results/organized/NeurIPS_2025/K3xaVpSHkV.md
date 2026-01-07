# Prior Work Analysis Report

## Target Paper
**Title:** K3xaVpSHkV
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Learning in the Presence of Malicious Errors** (1993)
- *Authors:* Michael Kearns et al.
- *Connection:* Introduced the malicious-noise/poisoning model (adversarially corrupting an η-fraction of examples) that underlies the corruption formalism refined by instance-targeted poisoning and used in the present agnostic analysis.

**Toward Efficient Agnostic Learning** (1994)
- *Authors:* Michael Kearns et al.
- *Connection:* Established the agnostic PAC framework and excess-risk viewpoint that the new paper adopts to pin down the minimax optimal excess error under instance-targeted poisoning as ẐΘ(√(d·η)).

### 💡 Inspiration

**VC Dimension of Adversarially Robust Classifiers** (2019)
- *Authors:* Omar Montasser et al.
- *Connection:* Established that randomization/improperness can be essential in adversarially robust learning, directly informing the present work’s emphasis on randomized learners to overcome deterministic impossibility under targeted poisoning.

### 📊 Baseline

**Learning Under Instance-Targeted Poisoning Attacks** (2022)
- *Authors:* Steve Hanneke et al.
- *Connection:* This NeurIPS 2022 work formalized instance-targeted poisoning in the realizable PAC setting, proved optimal error Θ(d·η), showed deterministic learners can be forced to near-1 error, and explicitly posed the agnostic-rate question that the present paper resolves.

### 🔗 Related Problem

**Certified Defenses for Data Poisoning Attacks** (2017)
- *Authors:* Jacob Steinhardt et al.
- *Connection:* Provided a formal worst-case poisoning framework with fraction-η corruptions for standard (untargeted) objectives, informing the present paper’s adversarial-budget modeling and contrast with the targeted objective.

**Poison Frogs! Targeted Clean-Label Poisoning Attacks on Neural Networks** (2018)
- *Authors:* Amir Shafahi et al.
- *Connection:* Demonstrated targeted poisoning against a specific test instance in practice, motivating the theoretical instance-targeted formulation that the current work analyzes to optimal rates.

**The Reusable Holdout: Preserving Validity in Adaptive Data Analysis** (2015)
- *Authors:* Cynthia Dwork et al.
- *Connection:* Showed how algorithmic randomness can preserve statistical guarantees against adaptive adversaries with visibility into random bits, conceptually supporting the paper’s result that randomized learners achieve optimal rates even with public randomness.

---

## Synthesis

The core innovation of this paper—tight agnostic rates for instance-targeted poisoning and the decisive role of randomized learners—rests on a precise lineage. The starting point is Hanneke et al. (NeurIPS 2022), which introduced and analyzed instance-targeted poisoning in the realizable PAC setting, proved optimal Θ(d·η) error, and showed that deterministic learners can be driven to near-1 error—while explicitly leaving the agnostic rate as a main open problem. The present paper answers that challenge, delivering the ẐΘ(√(d·η)) excess-error rate in the agnostic regime.
This development sits atop two foundational pillars: Kearns–Li’s malicious-noise model formalized the η-fraction adversarial corruption paradigm that instance-targeted poisoning refines, and Kearns–Schapire–Sellie’s agnostic PAC framework provides the excess-risk lens and minimax perspective used to state and prove optimality. Broader poisoning theory, typified by Steinhardt–Koh–Liang’s certified defenses for (untargeted) poisoning, shaped the fraction-η adversarial-budget formalism and clarifies how the targeted objective departs from standard robust learning goals. From the empirical side, Shafahi et al.’s clean-label targeted attacks on specific test points motivated the instance-targeted objective that the theory now characterizes sharply. Finally, two strands underscore the centrality of randomness: Montasser–Hanneke–Srebro’s results on the necessity of randomized/improper learners for adversarial robustness, and Dwork et al.’s demonstration that public randomness can still protect against adaptive adversaries. Together, these works directly enable the new agnostic-rate characterization and its surprising robustness to an adversary who observes the learner’s random bits.

---
*Generated: 2026-01-06T23:08:23.964577*
