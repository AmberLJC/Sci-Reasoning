# Prior Work Analysis Report

## Target Paper

**Title:** Views Can Be Deceiving: Improved SSL Through Feature Space Augmentation

**Conference:** ICLR 2024 (spotlight)

**Authors:** Kimia Hamidieh, Haoran Zhang, Swami Sankaranarayanan, Marzyeh Ghassemi

**Keywords:** Representation Learning, Spurious Correlations, Self-supervised Learning

**Abstract:** 
> Supervised learning methods have been found to exhibit inductive biases favoring simpler features. When such features are spuriously correlated with the label, this can result in suboptimal performance on minority subgroups. Despite the growing popularity of methods which learn from unlabeled data, the extent to which these representations rely on spurious features for prediction is unclear. In this work, we explore the impact of spurious features on Self-Supervised Learning (SSL) for visual rep...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Domain-Adversarial Training of Neural Networks** (2016)
- *Authors:* Yaroslav Ganin et al.
- *Direct Connection:* DANN established the adversarial principle for removing specific nuisance/domain information from representations, a principle LateTVG leverages to regularize late-layer features so that spurious attributes become uninformative during SSL pretraining.

### 💡 Inspiration

**Manifold Mixup: Better Representations by Interpolating Hidden States** (2019)
- *Authors:* Vikas Verma et al.
- *Direct Connection:* By showing that augmentations performed in hidden feature space can improve generalization, Manifold Mixup directly inspires LateTVG’s strategy of augmenting late-layer embeddings rather than relying solely on pixel-space transformations.

### 🔍 Gap Identification

**What makes for good views for contrastive learning?** (2020)
- *Authors:* Yonglong Tian et al.
- *Direct Connection:* This paper formalized how augmentations define the invariances learned by contrastive SSL, motivating the current work’s focus on identifying and correcting undesired invariances by generating targeted feature-space views.

**Distributionally Robust Neural Networks for Group Shifts: On the Importance of Regularization for Worst-Group Generalization** (2020)
- *Authors:* Shiori Sagawa et al.
- *Direct Connection:* GroupDRO popularized group-aware reweighting/resampling to mitigate spurious correlations, and the current work explicitly shows that analogous resampling during SSL fails to induce true invariance, motivating its feature-space regularization approach.

### 📊 Baseline

**A Simple Framework for Contrastive Learning of Visual Representations** (2020)
- *Authors:* Ting Chen et al.
- *Direct Connection:* LateTVG is designed to plug into contrastive SSL pipelines like SimCLR, using the same InfoNCE objective and standard view-augmentation setup while regularizing the learned representations via feature-space view generation to counteract augmentation-induced spurious invariances.

### 🔗 Related Problem

**Robust Pre-Training by Adversarial Contrastive Learning** (2020)
- *Authors:* Jiang et al.
- *Direct Connection:* Adversarial contrastive learning demonstrated that learned (hard) views can harden SSL, and the present work adapts this idea by generating feature-space perturbations targeted to remove spurious attributes rather than indiscriminately perturbing images.

---

## Synthesis: How Prior Work Led to This Paper

Contrastive self-supervised learning frameworks showed that representation quality hinges on the definition of positive/negative pairs and the augmentations that produce them; SimCLR in particular crystallized the InfoNCE pipeline where view augmentations dictate what invariances are learned. Subsequent analysis clarified that these views effectively specify the invariance class, with theory and experiments demonstrating that mismatched or overly aggressive augmentations can encode undesirable invariances that harm transfer. Independently, feature-space augmentation work established that manipulating hidden states—rather than images—can yield stronger inductive biases and better generalization, suggesting a lever to target specific information in learned representations. Adversarial contrastive pretraining further revealed that learned or adversarially generated views can harden SSL, albeit with largely indiscriminate perturbations in pixel space. In supervised settings, domain-adversarial training provided a mechanism to explicitly remove domain or attribute information from features, offering a blueprint for targeted invariance. Finally, group-robust optimization highlighted practical mitigation via reweighting/resampling, but with limitations that can fail to enforce the desired invariances.
Taken together, these works identify a gap: while augmentations control invariance in SSL, existing image-space or adversarial approaches are not targeted to spurious attributes, and group-based resampling does not reliably yield invariant representations. The natural next step is to generate views in feature space—where specific nuisance factors can be suppressed—and to regularize late-layer embeddings so spurious information is actively removed during pretraining, yielding SSL representations that retain task-relevant content without encoding shortcut cues.

---

*Analysis generated on: 2026-01-06T14:28:08.891578*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
