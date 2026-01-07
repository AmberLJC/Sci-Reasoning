# Prior Work Analysis Report

## Target Paper

**Title:** MOS: Model Synergy for Test-Time Adaptation on LiDAR-Based 3D Object Detection

**Conference:** ICLR 2025 (oral)

**Authors:** Zhuoxiao Chen, Junjie Meng, Mahsa Baktashmotlagh, Yonggang Zhang, Zi Huang, Yadan Luo

**Keywords:** Test-Time Adaptation, 3D Object Detection

**Abstract:** 
> LiDAR-based 3D object detection is crucial for various applications but often experiences performance degradation in real-world deployments due to domain shifts. While most studies focus on cross-dataset shifts, such as changes in environments and object geometries, practical corruptions from sensor variations and weather conditions remain underexplored. In this work, we propose a novel online test-time adaptation framework for 3D detectors that effectively tackles these shifts, including a chal...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Tent: Fully Test-Time Adaptation by Entropy Minimization** (2021)
- *Authors:* Dequan Wang et al.
- *Direct Connection:* MOS builds its online adaptation loop on the entropy-minimization paradigm introduced by TENT, using unsupervised test-time optimization to update 3D detectors without labels.

**Robo3D: Towards Robust and Reliable 3D Object Detection in Open-World Environments** (2024)
- *Authors:* Wang et al.
- *Direct Connection:* MOS explicitly targets the LiDAR corruption and weather-induced robustness issues characterized in Robo3D’s benchmark, extending the setting to cross-corruption and using it as a primary evaluation context.

### 💡 Inspiration

**Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time** (2022)
- *Authors:* Mitchell Wortsman et al.
- *Direct Connection:* MOS generalizes the model-soups insight by assembling a batch-dependent weighted combination of diverse historical checkpoints rather than a static greedy average, enabling distribution-aware integration at test time.

**Snapshot Ensembles: Train 1, Get M for Free** (2017)
- *Authors:* Gao Huang et al.
- *Direct Connection:* MOS operationalizes the checkpoint-diversity idea from snapshot ensembles at test time by selecting and combining past snapshots whose complementary knowledge best matches the current batch via synergy weights.

### 🔍 Gap Identification

**EATA: Efficient Test-Time Adaptation** (2022)
- *Authors:* Niu et al.
- *Direct Connection:* MOS addresses EATA’s reliance on per-sample filtering and a single adapted model—which can be brittle on severe or compound corruptions—by leveraging long-term checkpoint memory and synergy weighting across models.

### 📊 Baseline

**CoTTA: Continual Test-Time Adaptation** (2022)
- *Authors:* Wang et al.
- *Direct Connection:* MOS targets the continual TTA scenario formalized by CoTTA but replaces its single EMA teacher and augmentation-averaging with dynamic assembly of diverse historical checkpoints to mitigate catastrophic forgetting under evolving corruptions.

---

## Synthesis: How Prior Work Led to This Paper

Entropy-minimization test-time adaptation established that models can be updated on unlabeled test streams by minimizing predictive uncertainty, defining a practical objective for label-free adaptation in deployment. Continual test-time adaptation introduced a streaming-shift setting with methods that maintain an EMA teacher and leverage augmentation-averaging to reduce drift, but they still operate a single evolving model and are vulnerable to catastrophic forgetting across long sequences. Efficient TTA proposals further curbed instability by filtering unreliable samples and regularizing updates, though these approaches remain brittle under severe or compound corruptions when one adapted model must serve all domains. In parallel, model soups demonstrated that aggregating weights from multiple fine-tuned checkpoints yields stronger out-of-distribution generalization than any single model, and snapshot ensembles showed that checkpoints capture complementary hypotheses that can be combined effectively. Robustness work in LiDAR-based 3D detection, exemplified by Robo3D, documented performance collapses under sensor/weather corruptions and provided concrete corruption taxonomies and evaluation protocols. Integrating these strands, the next step was to fuse the stability of TTA with the complementary knowledge in multiple checkpoints. Rather than continually pushing a single model to fit every shift, dynamically selecting and assembling historical checkpoints offers a principled way to retain long-term knowledge. By guiding selection and combination with batch-dependent synergy weights atop an entropy-minimization objective, the approach addresses continual TTA’s forgetting and EATA-style brittleness, aligning with evidence from soups and snapshot ensembles that diversity across checkpoints is a powerful lever for robustness—now exploited online for LiDAR 3D detection, including cross-corruption scenarios.

---

*Analysis generated on: 2026-01-06T18:52:34.435949*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
