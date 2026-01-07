# Prior Work Analysis Report

## Target Paper

**Title:** Enhancing Group Fairness in Online Settings Using Oblique Decision Forests

**Conference:** ICLR 2024 (spotlight)

**Authors:** Somnath Basu Roy Chowdhury, Nicholas Monath, Ahmad Beirami, Rahul Kidambi, Kumar Avinava Dubey, Amr Ahmed, Snigdha Chaturvedi

**Keywords:** Fairness, Online Learning, Oblique Decision Trees

**Abstract:** 
> Fairness, especially group fairness, is an important consideration in the context of machine learning systems. The most commonly adopted group fairness-enhancing techniques are in-processing methods that rely on a mixture of a fairness objective (e.g., demographic parity) and a task-specific objective (e.g., cross-entropy) during the training process. However, when data arrives in an online fashion – one instance at a time – optimizing such fairness objectives poses several challenges. In partic...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Equality of Opportunity in Supervised Learning** (2016)
- *Authors:* Moritz Hardt et al.
- *Direct Connection:* This work formalized group fairness notions (demographic parity and equality of opportunity/odds) that are the target constraints Aranyani operationalizes via online-computable surrogates.

**Online Convex Optimization with Long Term Constraints** (2012)
- *Authors:* M. Mahdavi et al.
- *Direct Connection:* Aranyani adopts the primal–dual, long-term constraints perspective to update fairness Lagrange multipliers online while optimizing accuracy in the stream.

### 💡 Inspiration

**Learning Fair Classifiers: A Regularization Approach** (2017)
- *Authors:* Yossi Bechavod et al.
- *Direct Connection:* The idea of training with a joint objective that mixes task loss with a fairness regularizer directly motivates Aranyani’s in-processing objective at each node and across the forest.

### 🔍 Gap Identification

**A Reductions Approach to Fair Classification** (2018)
- *Authors:* Alekh Agarwal et al.
- *Direct Connection:* This constrained-reduction framework requires repeated access to global group statistics and costly inner-loop optimization, highlighting the computational bottleneck that Aranyani resolves with a single-pass, per-instance fairness update.

### 🔧 Extension

**Fairness Constraints: Mechanisms for Fair Classification** (2017)
- *Authors:* Muhammad Bilal Zafar et al.
- *Direct Connection:* Aranyani extends Zafar et al.’s covariance-based surrogate (linking the sensitive attribute to the signed distance to a linear decision boundary) by embedding it at oblique splits and updating it online with streaming moment estimates.

### 🔗 Related Problem

**Mondrian Forests: Efficient Online Random Forests** (2014)
- *Authors:* Balaji Lakshminarayanan et al.
- *Direct Connection:* The online forest paradigm for incremental tree growth and ensemble updates informs Aranyani’s streaming architecture, which replaces axis-aligned splits with learnable oblique, fairness-regularized splits.

---

## Synthesis: How Prior Work Led to This Paper

Group fairness criteria such as demographic parity and equality of opportunity were precisely formulated by Hardt et al., establishing the population-level rates that fairness-aware learners seek to control. Bechavod and Ligett showed how to incorporate fairness into learning by adding a regularization term to the task loss, introducing differentiable proxies that enable in-processing optimization. Zafar et al. proposed covariance-based surrogates that connect sensitive attributes to linear decision boundaries, yielding tractable constraints and penalties for demographic parity and error-rate disparities in linear models. Agarwal et al. reframed fair classification as a constrained reduction to cost-sensitive classification, but their method relies on repeated estimation of group-wide statistics and solver calls, making it ill-suited to per-instance online learning. From the optimization side, Mahdavi et al. developed online convex optimization with long-term constraints via primal–dual updates, enabling constraint satisfaction over time rather than per-step. In online modeling, Lakshminarayanan et al. introduced Mondrian forests, demonstrating how to incrementally grow and update tree ensembles on streams.
Collectively, these works revealed a gap: fairness objectives are defined over expectations and are computationally heavy in streaming settings, while online forests lack mechanisms to control group rates. The natural next step was to marry linear fairness surrogates with online tree architectures: use oblique (linear) splits so covariance-based fairness penalties apply locally, maintain streaming moment estimates to avoid global passes, and regulate fairness via lightweight dual updates across an online forest—precisely the synthesis operationalized by Aranyani.

---

*Analysis generated on: 2026-01-06T13:12:27.365464*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
