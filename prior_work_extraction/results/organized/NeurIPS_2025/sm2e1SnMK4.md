# Prior Work Analysis Report

## Target Paper
**Title:** sm2e1SnMK4
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The Bayesian Data Scheduler (BDS) reframes defense against harmful fine-tuning as per-example Bayesian inference, drawing on and unifying strands from alignment, adversarial robustness, and robust training. Alignment methods such as RLHF (Ouyang et al.) and Constitutional AI (Bai et al.) provide structured harmlessness signals and datasets; BDS treats these alignment corpora as evidence to calibrate a posterior over each fine-tuning example’s latent safety attribute. In contrast to attack-simulation defenses popularized by jailbreak studies (e.g., Zou et al.), which rely on bounded adversarial prompt sets and struggle with unknown threats, BDS sidesteps red teaming entirely by estimating safety directly from data distributions.
Conceptually, BDS inherits the effectiveness of example-level control from robust training with noisy data: meta-learned reweighting (Ren et al.) and selective sampling (Co-teaching; Han et al.) demonstrate that per-example weighting/selection can resist corruption. BDS advances this line by replacing heuristic or meta-learned weights with a principled Bayesian posterior that captures both estimated safety and uncertainty. Its adaptive scheduler further leverages Bayesian decision-making: inspired by BALD, it uses posterior information to guide which data to emphasize, and, akin to Thompson sampling (Russo & Van Roy), it samples from the posterior to stochastically weight data, naturally balancing caution and coverage. Together, these influences yield a tuning-stage defense that is simulation-free, uncertainty-aware, and adaptable across varying attack settings.

---
*Generated: 2026-01-07T00:21:32.349011*
