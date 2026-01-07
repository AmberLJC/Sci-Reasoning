# Prior Work Analysis Report

## Target Paper

**Title:** A Hierarchical Bayesian Model for Few-Shot Meta Learning

**Conference:** ICLR 2024 (spotlight)

**Authors:** Minyoung Kim, Timothy Hospedales

**Keywords:** Bayesian models, Meta learning, Few-shot learning

**Abstract:** 
> We propose a novel hierarchical Bayesian model for the few-shot meta learning problem. We consider episode-wise random variables to model episode-specific generative processes, where these local random variables are governed by a higher-level global random variable. The global variable captures information shared across episodes, while controlling how much the model needs to be adapted to new episodes in a principled Bayesian manner. Within our  framework, prediction on a novel episode/task can ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Recasting Gradient-Based Meta-Learning as Hierarchical Bayes** (2018)
- *Authors:* Erin Grant et al.
- *Direct Connection:* It formalized meta-learning as hierarchical Bayesian inference with task-specific parameters drawn from a shared prior, directly motivating the paper’s global–local latent variable formulation.

**Meta-Learning Probabilistic Inference for Prediction** (2018)
- *Authors:* Jonathan Gordon et al.
- *Direct Connection:* By framing meta-learning as learning to perform Bayesian inference and output posterior predictive distributions, it underpins the paper’s view of novel-episode prediction as Bayesian inference under a learned hierarchical prior.

### 💡 Inspiration

**Towards a Neural Statistician** (2017)
- *Authors:* Harrison Edwards et al.
- *Direct Connection:* It introduced dataset/episode-level latent variables governed by global variables, inspiring the explicit episode-wise random variables controlled by a global prior in the proposed hierarchical model.

### 🔍 Gap Identification

**Probabilistic Model-Agnostic Meta-Learning** (2018)
- *Authors:* Chelsea Finn et al.
- *Direct Connection:* By introducing a Bayesian treatment of task-specific parameters via variational/SG-MCMC approximations, it highlighted the lack of tractable conjugate updates that the new NIW-based model addresses with approximate closed-form local posteriors.

### 📊 Baseline

**Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks** (2017)
- *Authors:* Chelsea Finn et al.
- *Direct Connection:* This work’s gradient-based inner-loop adaptation is the primary baseline whose costly unrolled computational graph the new hierarchical Bayesian NIW approach replaces with closed-form episode-level Bayesian updates.

### 🔧 Extension

**Prototypical Networks for Few-shot Learning** (2017)
- *Authors:* Jake Snell et al.
- *Direct Connection:* Its class-mean (Gaussian-like) assumption connects directly to conjugate Gaussian modeling, which the new work generalizes by placing an NIW prior over class means and covariances to obtain principled Bayesian predictive distributions.

---

## Synthesis: How Prior Work Led to This Paper

Gradient-based meta-learning established a dominant template in which a model quickly adapts to new tasks via inner-loop updates, but doing so requires unrolling costly computational graphs (Finn et al., 2017). A pivotal perspective then showed that such procedures can be understood as hierarchical Bayesian inference, with task-specific parameters drawn from a shared prior that is learned across tasks (Grant et al., 2018). Pushing this further, probabilistic MAML introduced an explicit Bayesian treatment of task parameters, but relied on variational sampling or SG-MCMC to approximate intractable posteriors, revealing the need for tractable per-task Bayesian updates (Finn et al., 2018). In parallel, the Neural Statistician demonstrated that dataset/episode-level latent variables governed by a global variable can capture across-episode regularities in a principled hierarchical generative model (Edwards & Storkey, 2017). Meta-learning as probabilistic inference was further crystallized by ML-PIP, which emphasized learning to compute posterior predictives for new tasks (Gordon et al., 2018). Finally, Prototypical Networks exposed the practical value of Gaussian-like class-conditional assumptions in embedding space, hinting at conjugate Bayesian treatments when moving beyond point estimates of class means (Snell et al., 2017).
Together these works suggested a natural opportunity: retain the hierarchical Bayesian view with explicit episode-level variables and global priors, but replace approximate, gradient-heavy inner loops with conjugate Bayesian updates. The present work synthesizes these strands by adopting a Normal–Inverse–Wishart prior over Gaussian episode-level parameters, yielding approximate closed-form local posteriors and posterior predictives. This preserves the hierarchical sharing and Bayesian task adaptation of prior probabilistic meta-learners while avoiding MAML’s expensive unrolled computation, realizing a principled and efficient few-shot meta-learning algorithm.

---

*Analysis generated on: 2026-01-06T18:59:03.917320*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
