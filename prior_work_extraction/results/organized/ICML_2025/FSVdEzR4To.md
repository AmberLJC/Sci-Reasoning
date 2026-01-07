# Prior Work Analysis Report

## Target Paper
**Title:** FSVdEzR4To
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

PARS is rooted in the offline RL literature that pinpointed extrapolation error as the primary failure mode when learning from static datasets. BCQ crystallized this diagnosis and mitigated it through action-space constraints, while BEAR and BRAC formalized behavior support and regularization to keep learned policies within the dataset’s distribution. CQL reframed the solution directly in value-space, penalizing Q-values for out-of-distribution (OOD) actions to counter overestimation. IQL took another angle by avoiding explicit evaluation of OOD actions, extracting policies from value estimates to sidestep extrapolation. These works collectively established that controlling how Q-functions behave on unsupported actions is essential.
PARS advances this line by targeting a specific pathology: linear extrapolation of Q beyond the data range. It introduces two complementary mechanisms. First, RS-LN applies principled reward/Q scaling inspired by Pop-Art’s adaptive target rescaling and stabilized via Layer Normalization, directly shaping the magnitude and curvature of Q so it gradually decreases outside the data range. Second, PA explicitly penalizes infeasible actions—aligning with the conservative/value-space perspective of CQL but refined to focus on actions the dataset deems implausible. The synthesis of adaptive scaling (from normalization literature) with targeted value penalties (from conservative/offline RL) yields a method that both curbs OOD overestimation and actively regularizes extrapolative behavior, enabling strong offline and fine-tuning performance, including on challenging AntMaze Ultra tasks.

---
*Generated: 2026-01-07T00:21:32.393458*
