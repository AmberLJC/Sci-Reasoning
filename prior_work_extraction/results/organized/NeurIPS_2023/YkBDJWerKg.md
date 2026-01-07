# Prior Work Analysis Report

## Target Paper
**Title:** YkBDJWerKg
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

STEVE-1’s core contribution is to reframe text-to-behavior as unCLIP-style generation in a task-relevant latent space, eliminating the need for large, instruction-labeled trajectories. The design fuses three strands of prior work. First, unCLIP (Ramesh et al.) provides the two-stage blueprint: learn a text-to-embedding prior, then decode from that embedding. STEVE-1 instantiates this by training a text→MineCLIP prior and using a pretrained behavior decoder. Second, CLIP’s cross-modal alignment, realized in Minecraft by MineDojo’s MineCLIP, supplies a semantic video–text latent that is both instruction-expressive and behavior-relevant; STEVE-1 conditions the policy on MineCLIP latents and uses them to relabel trajectories. Third, hindsight relabeling and goal-conditioned learning (HER, RIG, GCSL) show how to turn unlabeled experience into goal-conditioned supervision. STEVE-1 applies this by relabeling collected trajectories with achieved MineCLIP codes, enabling self-supervised behavioral cloning without reward or dense language annotation.
Crucially, VPT provides the behavior backbone trained from web-scale videos; STEVE-1 adapts VPT to accept MineCLIP commands, casting it as the decoder in the unCLIP analogy. The combination—unCLIP-style prior+decoder, MineCLIP latent semantics, VPT behavior capacity, and hindsight goal relabeling—directly yields a low-cost, instruction-following policy that aligns short-horizon text and visual commands with executable behavior in Minecraft.

---
*Generated: 2026-01-06T23:33:36.296073*
