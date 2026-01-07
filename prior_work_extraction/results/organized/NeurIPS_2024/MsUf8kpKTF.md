# Prior Work Analysis Report

## Target Paper
**Title:** MsUf8kpKTF
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—a systematic characterization of plasticity loss in on-policy deep RL under domain shift and the identification of “regenerative” interventions as robust remedies—rests on three intellectual pillars. First, the on-policy RL substrate is defined by PPO, the standard algorithmic context where the authors measure plasticity degradation and test interventions. Second, prior evidence that deep RL can become biased toward early experiences (primacy bias) directly motivates probing plasticity specifically in the on-policy regime, while classic continual learning methods such as EWC and policy consolidation (Progress & Compress) provide natural baselines for stability–plasticity trade-offs. The paper shows that these regularization/distillation approaches, successful in other regimes, often fail to recover plasticity on-policy under domain shift, sharpening the problem statement.
Third, a line of work on rejuvenation and restarts—Lottery Ticket Hypothesis/rewinding, SGDR warm restarts, and Population Based Training—establishes that reinitialization and periodic resets can restore trainability and exploration. Building on this, the authors identify a class of regenerative methods (e.g., parameter/optimizer resets or partial reinitialization) that consistently mitigate plasticity loss in on-policy training. Together, these works frame the phenomenon, supply rigorous baselines, and inspire the key insight: in on-policy deep RL, plasticity is better recovered by regeneration-style interventions than by conventional regularization-based continual learning methods.

---
*Generated: 2026-01-06T23:33:35.549275*
