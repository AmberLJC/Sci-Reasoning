# Prior Work Analysis Report

## Target Paper
**Title:** DkeeXVdQyu
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

How to Scale Your EMA tackles a gap left by the well-established practice of preserving optimization dynamics across batch sizes. Goyal et al. introduced the linear learning-rate scaling rule, and Smith et al. sharpened the intuition that batch size and step-wise learning-rate schedules are interchangeable when viewed in units of samples processed. McCandlish et al. further tied batch size to the effective stochastic dynamics via the gradient-noise scale, providing a principled motivation to preserve behavior when the number of parameter updates per epoch changes. In parallel, model-parameter averaging—rooted in Polyak and Juditsky’s iterate averaging—has become central to modern training practice. Mean Teacher formalized EMA of weights as a teacher with a tunable momentum, while BYOL and MoCo embedded EMA targets/momentum encoders at the heart of state-of-the-art self-supervised pipelines, where performance is highly sensitive to the momentum hyperparameter.

Despite this reliance on EMA, prior work lacked a rule for how to adjust EMA momentum when batch size alters the cadence of parameter updates. This paper unifies the two threads: it treats the EMA as a discrete-time low-pass filter with a per-sample time constant (or half-life), then derives the mapping from that invariant quantity to the per-step momentum under different batch sizes. In effect, it extends the linear-scaling philosophy from learning rate to EMA momentum, so that EMA-driven teacher/target dynamics remain stable across batch regimes, benefiting supervised robustness, semi-supervised pseudo-labeling, and self-supervised learning alike.

---
*Generated: 2026-01-07T00:02:04.774773*
