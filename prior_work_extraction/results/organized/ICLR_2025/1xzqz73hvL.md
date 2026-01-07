# Prior Work Analysis Report

## Target Paper

**Title:** High-dimensional Analysis of Knowledge Distillation: Weak-to-Strong Generalization and Scaling Laws

**Conference:** ICLR 2025 (spotlight)

**Authors:** Muhammed Emrullah Ildiz, Halil Alperen Gozeten, Ege Onur Taga, Marco Mondelli, Samet Oymak

**Keywords:** empirical risk minimization, high-dimensional statistics, scaling laws, weak to strong generalization, knowledge distillation

**Abstract:** 
> A growing number of machine learning scenarios rely on knowledge distillation where one uses the output of a surrogate model as labels to supervise the training of a target model. In this work, we provide a sharp characterization of this process for ridgeless, high-dimensional regression, under two settings: *(i)* model shift, where the surrogate model is arbitrary, and *(ii)* distribution shift, where the surrogate model is the solution of empirical risk minimization with out-of-distribution da...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Distilling the Knowledge in a Neural Network** (2015)
- *Authors:* Geoffrey Hinton et al.
- *Direct Connection:* This work formalized the teacher–student paradigm of training on surrogate (soft) labels, which the current paper analyzes sharply in the high-dimensional ridgeless regression regime.

**Surprises in High-Dimensional Ridgeless Least Squares Interpolation** (2019)
- *Authors:* Trevor Hastie et al.
- *Direct Connection:* The ridgeless least-squares framework and its high-dimensional risk behavior from this paper serve as the base estimator the current work analyzes under surrogate-label supervision and shift.

**Benign Overfitting in Linear Regression** (2020)
- *Authors:* Peter L. Bartlett et al.
- *Direct Connection:* Techniques and insights on when minimum-norm interpolants generalize underpin the non-asymptotic risk control that this paper adapts to the teacher-labeled (distilled) regression setting with model/distribution shift.

### 💡 Inspiration

**Self-Training With Noisy Student Improves ImageNet Classification** (2020)
- *Authors:* Qizhe Xie et al.
- *Direct Connection:* By showing student training on teacher-generated labels drawn from extra out-of-distribution data, this work motivates the paper’s distribution-shift setting where the surrogate is an ERM solution on OOD data.

### 🔍 Gap Identification

**Scaling Laws for Neural Language Models** (2020)
- *Authors:* Jared Kaplan et al.
- *Direct Connection:* This empirical discovery of power-law performance vs. scale highlights a lack of theory for scaling behavior in distillation that the present paper addresses with explicit risk scaling laws.

**Training Compute-Optimal Large Language Models** (2022)
- *Authors:* Jordan Hoffmann et al.
- *Direct Connection:* Their compute-optimal scaling observations motivate the paper’s theoretical characterization of how sample size and surrogate quality trade off in distillation to yield optimal scaling.

### 🔧 Extension

**Towards Understanding Knowledge Distillation** (2019)
- *Authors:* Mary Phuong and Christoph H. Lampert
- *Direct Connection:* Their theoretical analysis of when distillation helps provided a first principles view that the present paper extends by deriving precise, non-asymptotic, distribution-aware risk bounds in overparameterized regression.

---

## Synthesis: How Prior Work Led to This Paper

Knowledge distillation was crystallized by Hinton et al., who proposed training a student on a teacher’s soft outputs, establishing the surrogate-label training paradigm. Phuong and Lampert advanced this by analyzing when distillation improves generalization, identifying structural conditions under which teacher guidance is beneficial. In parallel, high-dimensional learning theory explained overparameterized regression: Hastie et al. characterized ridgeless least squares’ risk and double-descent behavior, while Bartlett et al. showed when minimum-norm interpolants can still generalize (“benign overfitting”), providing tools for non-asymptotic risk control. On the applied side, Xie et al.’s Noisy Student demonstrated that training students on teacher labels produced using additional, out-of-distribution data can yield substantial gains, concretely highlighting a distribution-shifted distillation regime. Meanwhile, Kaplan et al. and Hoffmann et al. revealed empirical scaling laws and compute-optimal tradeoffs, underscoring the need for theory that predicts how performance scales with data, model size, and supervision quality. Together, these works left a clear opportunity: unify teacher–student supervision with modern high-dimensional risk analyses, especially under model and distribution shift, and connect the resulting theory to observed scaling behavior. The present paper takes this step by deriving sharp, non-asymptotic risk bounds for ridgeless regression under distillation, identifying the optimal surrogate form (including when to discard weak features), and translating these bounds into scaling laws that explain when and how weak-to-strong training can provably help or hurt across shifts.

---

*Analysis generated on: 2026-01-06T15:00:39.048339*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
