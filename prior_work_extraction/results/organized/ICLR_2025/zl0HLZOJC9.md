# Prior Work Analysis Report

## Target Paper
**Title:** zl0HLZOJC9
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s key contribution—a probabilistic learning-to-defer framework that handles missing expert annotations and explicitly controls workload among an AI model and multiple human experts—sits at the intersection of three lines of work. First, learning-to-defer (Madras et al.) and its statistical formalization (Mozannar & Sontag) define the core objective of jointly optimizing prediction and deferral decisions to improve system-level performance. However, these approaches typically presume full supervision of expert responses and lack mechanisms to distribute workload across multiple experts. Second, selective classification (Geifman & El-Yaniv) provides risk–coverage principles that the present work adapts to regulate coverage not only for an abstain action but across AI and several human experts, turning coverage constraints into actionable workload controls. Third, probabilistic modeling of annotators (Dawid–Skene; Raykar et al.) introduces latent true labels and expert-specific confusion/reliability parameters, along with EM-style estimation, enabling learning when many expert annotations are missing or noisy. The proposed method synthesizes these strands through a mixture-of-experts perspective (Jacobs et al.), using a probabilistic gate to route instances to the AI or particular humans while regularizing the gate to meet workload targets. Chow’s reject-option decision theory underlies the defer-versus-predict trade-off that the model generalizes to deferral to specific experts. Together, these prior works directly enable the paper’s central advance: a unified probabilistic L2D model that is identifiable and trainable under partial expert labels, and that enforces controllable, balanced allocation of cases across AI and multiple human experts.

---
*Generated: 2026-01-06T23:42:48.098217*
