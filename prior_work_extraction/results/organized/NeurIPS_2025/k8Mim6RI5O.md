# Prior Work Analysis Report

## Target Paper
**Title:** k8Mim6RI5O
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

EMPO’s key contribution—fully unsupervised incentivization of LLM reasoning by minimizing semantic entropy—rests on fusing classic entropy-minimization from semi-supervised learning with modern policy optimization for language models. The core theoretical impetus comes from Grandvalet and Bengio’s entropy minimization, which prescribes pushing model predictions on unlabeled inputs toward confident, low-entropy distributions. EMPO translates this to open-ended reasoning by leveraging the Self-Consistency finding that agreement among multiple sampled chains correlates with correctness; disagreement becomes a measurable, label-free proxy for uncertainty that the algorithm seeks to reduce.
Algorithmically, EMPO adopts the KL-regularized policy optimization scaffolding established by PPO and RLHF (Ziegler et al.), ensuring stable updates to an LLM policy while constraining divergence from a reference model. Where RLHF relies on preference or reward models, EMPO replaces the reward with a semantic-entropy signal computed over generations, paralleling SSL methods like FixMatch that couple consistency regularization with confidence-driven training to exploit unlabeled data. Relative to prior self-improvement approaches for reasoning such as STaR—which still leverage answer labels—EMPO removes external supervision entirely, optimizing only on unlabeled questions. Finally, its philosophical alignment with Constitutional AI underscores a broader shift from human-intensive supervision toward intrinsic or AI-mediated signals; EMPO advances this trajectory by demonstrating that semantic agreement alone can drive sizable reasoning gains without labels or reward models.

---
*Generated: 2026-01-07T00:21:32.344183*
