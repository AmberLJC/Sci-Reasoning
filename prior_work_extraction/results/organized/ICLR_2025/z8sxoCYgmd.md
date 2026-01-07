# Prior Work Analysis Report

## Target Paper
**Title:** z8sxoCYgmd
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

LOKI’s central contribution—a unified, multimodal benchmark that probes large multimodal models’ ability to detect synthetic data and articulate reasons—emerges from two converging lines of prior work. First, the visual and audio deepfake community established the value of standardized, diverse, and challenging corpora with clear protocols. FaceForensics++ and DFDC defined large-scale, category-aware evaluation for manipulated faces, while Celeb-DF raised the bar by curating high-quality, low-artifact forgeries that stress fine-grained perception. In audio, ASVspoof 2019 provided rigorous tracks and metrics for spoofing countermeasures. LOKI inherits these lessons—diversity, protocol clarity, difficulty calibration—and generalizes them into a single framework spanning image, video, audio, text, and 3D.
Second, the text-AIGC literature underscored both robust detection approaches and the importance of interpretability. GLTR showed that detectors should offer human-understandable evidence, and DetectGPT introduced strong, generator-agnostic baselines. LOKI integrates this ethos by requiring LMMs not only to classify authenticity but also to justify their decisions in natural language. Finally, the rise of instruction-tuned LMMs such as LLaVA provided the practical interface—QA with rationales—through which a single model can be evaluated uniformly across modalities. Together, these works directly shaped LOKI’s design: a comprehensive, difficulty-aware, QA-based benchmark that tests perception, knowledge, and reasoning for synthetic data detection with explainable outputs across modalities.

---
*Generated: 2026-01-06T23:42:48.100466*
