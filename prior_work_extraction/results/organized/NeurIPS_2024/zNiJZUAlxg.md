# Prior Work Analysis Report

## Target Paper
**Title:** zNiJZUAlxg
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

ResAD’s central insight—modeling residual feature distributions rather than raw feature distributions—sits at the intersection of two trajectories in anomaly detection: (1) density/memory modeling in pre-trained feature spaces, and (2) leveraging residual signals as robust anomaly evidence. PaDiM and CFLOW-AD crystallized the effectiveness of learning probability models over deep patch features (Gaussian modeling and normalizing flows, respectively), yet both operate on class-dependent raw features, which impedes cross-class generalization. PatchCore further highlighted the strength of generic pre-trained features for AD, but its nearest-neighbor search still inherits inter-class feature drift. These works collectively motivate ResAD’s pivot: keep the successful idea of modeling normality in feature space, but reduce class-specific variance before modeling.

Concurrently, DRAEM and RD4AD showed that residuals—either input–reconstruction differences or teacher–student feature discrepancies—are highly informative for anomaly detection. ResAD abstracts and generalizes this notion by residualizing features themselves and then learning the distribution over these residuals, targeting a representation whose normal distribution is more stationary across categories. Finally, the classical Deep SVDD perspective underscores the challenge of learning compact normal regions that transfer; ResAD’s residualization can be viewed as an invariance-inducing transformation that makes a single compact/density model viable across unseen classes. Together, these prior works directly shaped ResAD’s shift from modeling raw features to modeling residual feature distributions to achieve class-generalizable anomaly detection without target-time adaptation.

---
*Generated: 2026-01-07T00:02:04.764619*
