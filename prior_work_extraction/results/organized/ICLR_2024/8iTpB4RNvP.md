# Prior Work Analysis Report

## Target Paper

**Title:** Poisoned Forgery Face: Towards Backdoor Attacks on Face Forgery Detection

**Conference:** ICLR 2024 (spotlight)

**Authors:** Jiawei Liang, Siyuan Liang, Aishan Liu, Xiaojun Jia, Junhao Kuang, Xiaochun Cao

**Keywords:** Deepfake Detection, Backdoor Attack

**Abstract:** 
> The proliferation of face forgery techniques has raised significant concerns within society, thereby motivating the development of face forgery detection methods. These methods aim to distinguish forged faces from genuine ones and have proven effective in practical applications. However, this paper introduces a novel and previously unrecognized threat in face forgery detection scenarios caused by backdoor attack. By embedding backdoors into models and incorporating specific trigger patterns into...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain** (2017)
- *Authors:* Tianyu Gu et al.
- *Direct Connection:* BadNets established the backdoor attack formulation of poisoning training data so a learned trigger flips predictions at test time, which Poisoned Forgery Face adopts in the face forgery detection setting.

**Poison Frogs! Targeted Clean-Label Poisoning Attacks on Neural Networks** (2018)
- *Authors:* Amirhossein Shafahi et al.
- *Direct Connection:* The clean-label poisoning paradigm introduced in Poison Frogs directly underpins PFF’s threat model of implanting a backdoor without altering ground-truth labels of forged/real faces.

**FaceForensics++: Learning to Detect Manipulated Facial Images** (2019)
- *Authors:* Andreas Rössler et al.
- *Direct Connection:* FaceForensics++ defined the canonical face forgery detection problem and face-aligned preprocessing, which PFF exploits via landmark-relative trigger embedding to ensure consistent placement across samples.

### 💡 Inspiration

**Trojaning Attack on Neural Networks** (2018)
- *Authors:* Yuntao Liu et al.
- *Direct Connection:* The idea of optimizing a universal trigger pattern and mask across many inputs to achieve scalable backdoor implantation motivates PFF’s scalable trigger generator for face images.

### 🔍 Gap Identification

**A Sinusoidal Signal Based Backdoor Attack** (2019)
- *Authors:* Mauro Barni et al.
- *Direct Connection:* Global, translation-invariant sinusoidal triggers like SIG highlight a limitation for detectors relying on localized artifacts, which PFF addresses by crafting translation-sensitive triggers via convolution.

### 🔧 Extension

**Hidden Trigger Backdoor Attacks** (2020)
- *Authors:* Aniruddha Saha et al.
- *Direct Connection:* Saha et al. showed how to realize stealthy clean-label backdoors via feature collisions, a mechanism PFF generalizes to a binary forgery-detection task with task-tailored trigger synthesis.

### 🔗 Related Problem

**WaNet: Imperceptible Warping-based Backdoor Attack** (2021)
- *Authors:* Anh Nguyen et al.
- *Direct Connection:* WaNet demonstrated spatial-domain, transformation-based triggers, informing PFF’s design of a convolving process to produce translation-sensitive, imperceptible patterns suited to face regions.

---

## Synthesis: How Prior Work Led to This Paper

Backdoor learning was crystallized by BadNets, which showed that injecting a small pattern into a poisoned subset of training images causes models to rely on that pattern at test time. Poison Frogs extended this into the clean-label regime by demonstrating targeted poisoning with feature collisions while keeping ground-truth labels intact. Hidden Trigger Backdoor Attacks refined this stealthy, clean-label mechanism, crafting poisons that implant a hidden association between a trigger and a target outcome without relabeling. Trojaning Attack further showed that optimizing a universal pattern and mask across many training samples yields scalable trigger synthesis that generalizes across inputs. In parallel, WaNet introduced imperceptible, spatial warping triggers, indicating that location-dependent transformations can be more natural and harder to notice than pasted patches. Conversely, sinusoidal-signal backdoors exemplified global, translation-invariant patterns—effective in classification but ill-suited when decisions hinge on localized facial evidence. On the data side, FaceForensics++ standardized face forgery detection with aligned facial crops, implicitly providing stable landmark geometry across images.
Together, these works expose the opportunity to implant a stealthy, clean-label backdoor into deepfake detectors by combining scalable trigger generation with spatially aware placement. Building on universal trigger optimization while avoiding global, translation-invariant cues, a convolving process can produce translation-sensitive patterns that interact with the localized evidence detectors use. Leveraging consistent face alignment from forgery datasets, landmark-relative embedding stabilizes trigger placement across identities and detectors. This synthesis naturally yields a clean-label backdoor framework tailored to face forgery detection that is scalable, imperceptible, and effective under realistic preprocessing.

---

*Analysis generated on: 2026-01-06T18:23:03.077365*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
