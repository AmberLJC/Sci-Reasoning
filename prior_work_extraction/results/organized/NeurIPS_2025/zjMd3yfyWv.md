# Prior Work Analysis Report

## Target Paper
**Title:** zjMd3yfyWv
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The key contribution—private hyperparameter tuning with an ex-post (utility-first) guarantee—stands on two pillars: ex-post privacy and private selection. Wu et al. (2019) provide the central blueprint by introducing ex-post DP and a progressive, correlated-noise schedule wherein only the least noisy reveal determines the privacy charge; our method adapts this schedule to validation metrics across candidate hyperparameters, enabling early stopping once a target utility is met. To effectuate the final selection among candidates, we draw on selection primitives: McSherry–Talwar’s Exponential Mechanism offers a utility-aware baseline selector, while Liu–Talwar’s Private Selection from Private Candidates formalizes choosing the best among privately computed models. We integrate these with ex-post accounting to avoid worst-case composition, achieving lower realized privacy when tuning halts early.

Adaptive privacy accounting is critical: Rogers et al.’s privacy odometers/filters supply the pay-as-you-go view we use to certify realized epsilon–delta under adaptive tuning rounds. For the stopping rule, Dwork–Lei’s Propose-Test-Release inspires our release-when-stable criterion, mirroring a utility threshold crossed with correlated noise while preserving privacy. Finally, the reusable holdout framework guides our private validation protocol, supporting many adaptive probes without compromising generalization. Together, these works enable a tuning pipeline that targets a desired utility first, revealing just enough noisy information to certify success and pay only the privacy cost that actually materializes.

---
*Generated: 2026-01-07T00:21:32.230941*
