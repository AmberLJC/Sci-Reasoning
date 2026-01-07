# Prior Work Analysis Report

## Target Paper
**Title:** I6tBNcJE2F
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s two core contributions—(1) a cooperative unfolding network that jointly models atmospheric scattering and scene content, and (2) a coherence-based, iterative mean-teacher pseudo-labeling pipeline—are grounded in complementary lines of prior work. On the physics side, the atmospheric scattering model and priors from DCP (He et al., 2011) define the variables (airlight, transmission) and motivate emphasizing reliable, haze-free regions. Non-Local Dehazing (Berman & Avidan, 2016) provides a global color-line coherence perspective, which the authors adapt into global/local coherence cues to assess pseudo-label quality. DehazeNet (Cai et al., 2016) demonstrated how to embed scattering physics into CNNs, while DCPDN (Zhang & Patel, 2018) showed the benefit of jointly modeling haze variables and content—both ideas the authors synthesize into a cooperative, physically grounded restoration pipeline. The architectural mechanism for this synthesis comes from deep unfolding, exemplified by ISTA-Net (Zhang & Ghanem, 2018), which informs how iterative, interpretable updates to scattering and scene estimates can be unrolled into a trainable network. On the supervision side, Mean Teacher (Tarvainen & Valpola, 2017) supplies the consistency-based teacher–student backbone, and Noisy Student (Xie et al., 2020) motivates iterative self-training and teacher refresh. The authors adapt these to restoration by creating a label pool and selecting/weighting pseudo-labels via coherence, aligning supervision with physics-driven reliability, thereby advancing real-world dehazing without paired data.

---
*Generated: 2026-01-07T00:02:04.770907*
