# Prior Work Analysis Report

## Target Paper

**Title:** Variational Bayesian Last Layers

**Conference:** ICLR 2024 (spotlight)

**Authors:** James Harrison, John Willes, Jasper Snoek

**Keywords:** bayesian deep learning, variational methods, bayesian last layers, neural linear models

**Abstract:** 
> We introduce a deterministic variational formulation for training Bayesian last layer neural networks. This yields a sampling-free, single-pass model and loss that effectively improves uncertainty estimation. Our variational Bayesian last layer (VBLL) can be trained and evaluated with only quadratic complexity in last layer width, and is thus (nearly) computationally free to add to standard architectures. We experimentally investigate VBLLs, and show that they improve predictive accuracy, calibr...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Deep Bayesian Bandits Showdown: An Empirical Comparison of Bayesian Deep Networks for Thompson Sampling** (2018)
- *Authors:* Carlos Riquelme et al.
- *Direct Connection:* VBLL builds directly on the neural-linear/Bayesian last-layer formulation introduced by Riquelme et al., generalizing Bayesian linear heads on learned features to a deterministic variational objective that handles both regression and classification with quadratic cost in head width.

### 💡 Inspiration

**Conjugate-Computation Variational Inference: Converting Inference in Non-Conjugate Models to Inference in Conjugate Models** (2017)
- *Authors:* Mohammad Emtiyaz Khan et al.
- *Direct Connection:* CCVI showed how auxiliary variational bounds can recover conjugacy and enable collapsed, deterministic updates in nonconjugate models; VBLL applies this principle to collapse the last layer and, when paired with feature-layer VI, yields a lower-variance collapsed VI for BNNs.

### 🔍 Gap Identification

**Weight Uncertainty in Neural Networks** (2015)
- *Authors:* Charles Blundell et al.
- *Direct Connection:* Bayes by Backprop popularized Monte Carlo–based variational inference in BNNs, whose gradient variance and multiple-sample costs motivate VBLL’s sampling-free, deterministic treatment of the last layer via analytic expectations.

**Variational Dropout and the Local Reparameterization Trick** (2015)
- *Authors:* Diederik P. Kingma et al.
- *Direct Connection:* The local reparameterization trick reduces but does not eliminate Monte Carlo variance in stochastic VI, directly motivating VBLL’s further step of removing sampling entirely for the last layer by exploiting Gaussian identities and variational bounds.

### 📊 Baseline

**Laplace Redux: Effortless Bayesian Deep Learning** (2021)
- *Authors:* Jakob D. Daxberger et al.
- *Direct Connection:* Laplace Redux established last-layer Laplace (LLLA) as a strong, cheap Bayesian head baseline using local Hessians around the MAP, which VBLL targets and improves upon by replacing post-hoc second-order approximations with a principled variational posterior and closed-form loss without sampling.

### 🔧 Extension

**A variational approach to Bayesian logistic regression** (1997)
- *Authors:* Tommi S. Jaakkola et al.
- *Direct Connection:* VBLL directly uses the Jaakkola–Jordan quadratic variational bound on the logistic sigmoid to obtain a deterministic, conjugate-form objective for binary classification under a Gaussian last-layer posterior.

**Efficient bounds for the softmax function, with applications to approximate inference in CRFs** (2007)
- *Authors:* Guillaume Bouchard
- *Direct Connection:* For multiclass classification, VBLL leverages Bouchard’s convex quadratic bound on the softmax log-partition to compute closed-form expectations under a Gaussian last-layer, yielding a single-pass variational loss.

---

## Synthesis: How Prior Work Led to This Paper

Neural-linear methods established a practical blueprint for uncertainty in deep networks by placing a Bayesian linear model on top of learned features, demonstrating that a probabilistic last layer can deliver strong exploration and calibrated predictions with minimal overhead. Laplace-based approaches later showed that last-layer posteriors could be approximated extremely cheaply by fitting a Gaussian around the MAP using local curvature, making last-layer Bayesianization a de facto baseline for scalable uncertainty. Variational Bayes for neural networks, popularized via reparameterized Monte Carlo estimators, exposed a key limitation of sampling-based training: gradient variance and multi-sample cost. Local reparameterization mitigated this variance by moving randomness to activations but still required stochastic sampling. Classic variational bounds for logistic/softmax likelihoods—Jaakkola–Jordan’s quadratic bound for the sigmoid and Bouchard’s convex bound for the softmax—provide deterministic quadratic surrogates that render nonconjugate classification nearly conjugate under Gaussian posteriors. Conjugate-Computation VI generalized this idea, showing how auxiliary bounds can convert nonconjugate models into conjugate ones to enable collapsed, deterministic updates. Together, these works reveal a path: retain the neural-linear structure for scalability, replace post-hoc Laplace and stochastic VI with analytic expectations enabled by convex quadratic bounds, and exploit conjugacy to collapse nuisance variables. The natural next step is a sampling-free, single-pass variational objective for the Bayesian last layer that handles both regression and multiclass classification with quadratic cost, and that can be combined with variational feature learning to produce a lower-variance, collapsed VI procedure for full Bayesian neural networks.

---

*Analysis generated on: 2026-01-06T11:08:29.106776*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
