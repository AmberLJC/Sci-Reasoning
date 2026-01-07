# Prior Work Analysis Report

## Target Paper

**Title:** TRAM: Bridging Trust Regions and Sharpness Aware Minimization

**Conference:** ICLR 2024 (spotlight)

**Authors:** Tom Sherborne, Naomi Saphra, Pradeep Dasigi, Hao Peng

**Keywords:** sharpness-aware minimization, sam, trust region, optimization, cross-lingual transfer, language modeling

**Abstract:** 
> Sharpness-aware minimization (SAM) reports improving domain generalization by
reducing the loss surface curvature in the parameter space. However,
generalization during _fine-tuning_ is often more dependent on the
transferability of _representations_ in the function space. Trust-region
methods (TR) target this goal by regularizing representation curvature to reduce
catastrophic forgetting of pre-trained task-agnostic information while adopting
task-specific skills. We consider unifying these str...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Trust Region Policy Optimization** (2015)
- *Authors:* John Schulman et al.
- *Direct Connection:* TRPO introduced KL-divergence trust-region constraints to limit function changes per update, and TRAM adapts this KL-based bound to regulate how far SAM perturbs parameters so as to preserve representation stability.

### 💡 Inspiration

**Virtual Adversarial Training: A Regularization Method for Supervised and Semi-Supervised Learning** (2018)
- *Authors:* Takeru Miyato et al.
- *Direct Connection:* VAT’s core idea of enforcing local prediction smoothness via adversarial perturbations and a KL-based stability term informs TRAM’s use of a function-space (KL) bound to shape the SAM adversarial neighborhood.

**Better Fine-Tuning by Reducing Representational Collapse** (2020)
- *Authors:* Armen Aghajanyan et al.
- *Direct Connection:* R3F demonstrated that constraining representation drift during fine-tuning via prediction-consistency (KL) regularization improves OOD transfer, a principle TRAM operationalizes by imposing a trust-region bound when computing SAM perturbations.

### 🔍 Gap Identification

**GSAM: Rethinking Sharpness-Aware Minimization** (2022)
- *Authors:* Zhuang et al.
- *Direct Connection:* GSAM showed that purely parameter-space flatness objectives can conflict with descent directions and do not guarantee better generalization, motivating TRAM to introduce explicit function-space curvature control via a trust-region bound.

### 📊 Baseline

**Sharpness-Aware Minimization for Efficiently Improving Generalization** (2021)
- *Authors:* Pierre Foret et al.
- *Direct Connection:* TRAM directly modifies SAM’s inner maximization by constraining its adversarial neighborhood with a trust-region bound, turning SAM’s parameter-space flatness objective into one that is explicitly aware of function-space curvature.

### 🔗 Related Problem

**Overcoming catastrophic forgetting in neural networks** (2017)
- *Authors:* James Kirkpatrick et al.
- *Direct Connection:* EWC’s Fisher-based penalty approximates a local KL trust region to preserve pre-trained knowledge, motivating TRAM’s use of a trust-region perspective to protect task-agnostic structure while seeking flatter minima.

---

## Synthesis: How Prior Work Led to This Paper

Sharpness-Aware Minimization (SAM) frames generalization as minimizing worst-case loss in a small parameter-space neighborhood, operationalized by an inner maximization step that seeks sharper directions and a descent step that prefers flatter minima. Trust Region Policy Optimization (TRPO) formalized using a KL-divergence trust-region to limit functional change per update, establishing a principled way to bound representation drift. Virtual Adversarial Training (VAT) brought adversarial smoothing to supervised learning by enforcing local prediction consistency under worst-case perturbations measured with KL, directly targeting function-space smoothness. In fine-tuning, R3F showed that penalizing representational collapse via KL consistency under noise preserves pre-trained structure and improves out-of-domain transfer. EWC further connected preservation of pre-trained knowledge to an approximate KL trust-region through a Fisher-weighted quadratic penalty, demonstrating how trust-region ideas mitigate catastrophic forgetting. Meanwhile, GSAM dissected SAM’s gradient conflicts and highlighted that optimizing only parameter-space flatness can misalign with generalization, especially when representation transfer is critical. Taken together, these works reveal a gap: SAM variants succeed at parameter-space flatness, while trust-region and consistency methods control function-space drift, yet they remain separate. The natural next step is to couple them—use a trust-region (KL) bound to inform SAM’s adversarial neighborhood so the inner maximization becomes representation-aware. TRAM synthesizes these strands, co-optimizing for flat minima and controlled function curvature to preserve pre-trained structure during fine-tuning, yielding better OOD and cross-lingual generalization.

---

*Analysis generated on: 2026-01-06T11:19:23.712125*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
