# Prior Work Analysis Report

## Target Paper

**Title:** Amortizing intractable inference in large language models

**Conference:** ICLR 2024 (oral)

**Authors:** Edward J Hu, Moksh Jain, Eric Elmoznino, Younesse Kaddar, Guillaume Lajoie, Yoshua Bengio, Nikolay Malkin

**Keywords:** large language models, LLMs, Bayesian inference, chain-of-thought reasoning, latent variable models, generative flow networks, GFlowNets

**Abstract:** 
> Autoregressive large language models (LLMs) compress knowledge from their training data through next-token conditional distributions. This limits tractable querying of this knowledge to start-to-end autoregressive sampling. However, many tasks of interest---including sequence continuation, infilling, and other forms of constrained generation---involve sampling from intractable posterior distributions. We address this limitation by using amortized Bayesian inference to sample from these intractab...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Flow Network based Generative Models for Non-Iterative Diverse Candidate Generation** (2021)
- *Authors:* Yoshua Bengio et al.
- *Direct Connection:* Introduces Generative Flow Networks (GFlowNets), the core paradigm of learning a policy that samples objects proportional to an unnormalized target, which this paper adopts to realize posterior sampling for LLMs.

**Auto-Encoding Variational Bayes** (2013)
- *Authors:* Diederik P. Kingma et al.
- *Direct Connection:* Introduces amortized variational inference—learning an inference network to approximate intractable posteriors—which this paper adapts conceptually by fine-tuning LLMs to amortize posterior sampling via GFlowNets.

**Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (2022)
- *Authors:* Jason Wei et al.
- *Direct Connection:* Establishes explicit reasoning traces (rationales) in LMs, enabling this paper’s formulation of chain-of-thought as latent variables whose posterior should be sampled.

### 💡 Inspiration

**Bayesian Structure Learning with Generative Flow Networks** (2022)
- *Authors:* Tristan Deleu et al.
- *Direct Connection:* Demonstrates GFlowNets as amortized samplers of complex Bayesian posteriors in discrete spaces, directly motivating their use here to sample intractable posteriors over language sequences and rationales.

### 🔍 Gap Identification

**Self-Consistency Improves Chain of Thought Reasoning in Language Models** (2023)
- *Authors:* Xuezhi Wang et al.
- *Direct Connection:* Shows that aggregating multiple diverse reasoning paths improves accuracy but relies on heuristic sampling and voting, highlighting the need for a principled posterior sampler over rationales addressed here.

### 📊 Baseline

**Training language models to follow instructions with human feedback** (2022)
- *Authors:* Long Ouyang et al.
- *Direct Connection:* Represents the dominant reward-maximizing RL fine-tuning approach (RLHF) that this work contrasts with a distribution-matching, diversity-seeking alternative using GFlowNets.

### 🔧 Extension

**Trajectory Balance: Improved Credit Assignment in GFlowNets** (2022)
- *Authors:* Nikolay Malkin et al.
- *Direct Connection:* Provides the trajectory balance objective and credit assignment scheme that this work leverages to train sequence-level GFlowNets over token trajectories when amortizing posterior inference.

---

## Synthesis: How Prior Work Led to This Paper

Generative Flow Networks introduced a learning paradigm in which a stochastic policy samples structured objects in proportion to an unnormalized target, making diversity not a byproduct but the objective of training. The Trajectory Balance objective refined this framework with a stable credit assignment scheme for long, compositional trajectories, enabling practical training on sequence-like objects. Building on these ideas, Bayesian Structure Learning with GFlowNets demonstrated that GFlowNets can act as amortized samplers for complex posteriors in discrete domains, showing their suitability for Bayesian inference beyond synthetic settings. Auto-Encoding Variational Bayes established the principle of amortized inference—learning an inference model that approximates intractable posteriors—which provides the conceptual template for learning to sample posteriors across many inputs. Chain-of-Thought Prompting defined explicit intermediate rationales in language models, while Self-Consistency revealed that exploring multiple diverse reasoning paths and marginalizing improves performance, albeit with heuristic sampling and voting. Finally, InstructGPT (RLHF) exemplified reward-maximizing fine-tuning, aligning outputs but often collapsing diversity and not targeting a posterior distribution.
Taken together, these works expose a clear opportunity: treat reasoning traces and constrained generations as latent-variable posteriors and learn a policy that samples from them directly. By marrying the amortization principle of variational methods with the diversity-seeking, unnormalized distribution-matching of GFlowNets—and operationalizing it via trajectory-balance training on token trajectories—the current work naturally emerges as a principled alternative to MLE and RLHF, providing posterior-consistent sampling over rationales and constraints rather than reward-maximizing point solutions.

---

*Analysis generated on: 2026-01-06T19:52:28.812102*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
