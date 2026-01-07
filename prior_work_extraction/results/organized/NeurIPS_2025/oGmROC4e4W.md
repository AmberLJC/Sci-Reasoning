# Prior Work Analysis Report

## Target Paper
**Title:** oGmROC4e4W
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—adapting surrogate gradient slopes for sequential reinforcement learning in SNNs—sits at the intersection of two lines of prior work. First, the surrogate-gradient lineage originates with straight-through estimators (Bengio et al., 2013), which established the usefulness of biased gradients for non-differentiable units and highlighted bias–variance trade-offs central to slope selection. Within SNNs, SuperSpike (Zenke & Ganguli, 2017) and SLAYER (Shrestha & Orchard, 2018) operationalized surrogate derivatives through spikes and exposed the practical role of slope in controlling gradient flow and alignment, while Neftci et al. (2019) systematized these design choices and their optimization properties. The present work builds directly on this foundation by quantifying how slope affects gradient magnitude in depth and alignment with true gradients, and by making slope a quantity to schedule or adapt.
Second, the sequential RL aspect draws from recurrent RL practice. R2D2 (Kapturowski et al., 2019) showed that burn-in and sufficient unroll length are critical for credit assignment, a problem exacerbated in SNNs with stateful dynamics; Tallec & Ollivier (2018) analyzed how time-scale mismatch and truncated BPTT distort learning, motivating mechanisms that modulate effective timescales. The proposed adaptive slope acts as a learning-time control knob to bridge warm-up under limited sequence lengths. Finally, e-prop (Bellec et al., 2020) offers a contrasting local-credit paradigm in SNNs; positioning against it clarifies the contribution: preserve the performance benefits of BPTT-based training while gaining robustness to sequential RL constraints via adaptive surrogate gradients.

---
*Generated: 2026-01-07T00:21:33.142354*
