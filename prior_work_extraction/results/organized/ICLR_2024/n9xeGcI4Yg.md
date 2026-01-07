# Prior Work Analysis Report

## Target Paper

**Title:** The Consensus Game: Language Model Generation via Equilibrium Search

**Conference:** ICLR 2024 (spotlight)

**Authors:** Athul Paul Jacob, Yikang Shen, Gabriele Farina, Jacob Andreas

**Keywords:** language models, decoding, planning, game theory

**Abstract:** 
> When applied to question answering and other text generation tasks, language models (LMs) may be queried generatively (by sampling answers from their output distribution) or discriminatively (by using them to score or rank a set of candidate answers). These procedures sometimes yield very different predictions. How do we reconcile mutually incompatible scoring procedures to obtain coherent LM predictions? We introduce a new, a training-free, game-theoretic procedure for language model decoding. ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Predicting pragmatic reasoning in language games** (2012)
- *Authors:* Michael C. Frank and Noah D. Goodman
- *Direct Connection:* This work introduced the speaker–listener (signaling) framework underlying pragmatic communication, which the consensus game instantiates with an LM generator and LM-based discriminator to model decoding as cooperative signaling.

**Quantal Response Equilibria for Normal Form Games** (1995)
- *Authors:* Richard D. McKelvey and Thomas R. Palfrey
- *Direct Connection:* The use of entropy-regularized (noisy) best responses and equilibrium concepts in this work motivates the regularized equilibrium notion and smoothed dynamics used to compute the consensus game’s decoding fixed point.

**Regret Minimization in Games with Incomplete Information** (2007)
- *Authors:* Martin Zinkevich et al.
- *Direct Connection:* Counterfactual regret minimization for extensive-form games supplies the computational blueprint the paper adapts to find approximate equilibria in its sequential signaling game for decoding.

**Language Models (Mostly) Know What They Know** (2022)
- *Authors:* Saurav Kadavath et al.
- *Direct Connection:* Its finding that LMs can estimate their own correctness provides the discriminative scoring signal the paper formalizes as the listener’s utility and reconciles with generative decoding via equilibrium search.

### 💡 Inspiration

**Training Verifiers to Solve Math Word Problems** (2021)
- *Authors:* Karl Cobbe et al.
- *Direct Connection:* This work established the generate-then-verify paradigm where a (learned) verifier ranks candidate solutions, directly inspiring the paper’s LM-as-discriminator setup while highlighting the need for a training-free, principled coupling with generation.

### 📊 Baseline

**Self-Consistency Improves Chain of Thought Reasoning in Language Models** (2023)
- *Authors:* Xuezhi Wang et al.
- *Direct Connection:* As a primary decoding baseline that aggregates multiple generations by voting without a principled coupling to verification, it motivates and is directly improved upon by the equilibrium-ranking procedure that jointly links generation and evaluation.

### 🔧 Extension

**Reasoning about Pragmatics with Neural Listeners and Speakers** (2016)
- *Authors:* Jacob Andreas and Dan Klein
- *Direct Connection:* By coupling neural speakers and listeners for pragmatic generation, this paper provides the concrete neural instantiation that is directly extended to LM-based generator/discriminator roles and equilibrium-driven decoding.

---

## Synthesis: How Prior Work Led to This Paper

Work on pragmatic communication formalized language use as cooperative signaling between a speaker and listener, where utterances are chosen to shape a listener’s beliefs (Frank and Goodman), and subsequent neural implementations showed how to couple trainable speakers and listeners to improve generation via pragmatic inference (Andreas and Klein). In parallel, game theory introduced smooth, entropy-regularized equilibria via quantal response (McKelvey and Palfrey) and practical equilibrium-finding in sequential, imperfect-information settings via regret minimization in extensive-form games (Zinkevich et al.), providing algorithms for computing stable profiles of interacting agents. Within language modeling, generate-then-verify pipelines demonstrated that verifiers can reliably score candidate rationales or answers (Cobbe et al.), while separate findings showed LMs can estimate their own correctness, enabling a training-free, discriminative scoring signal (Kadavath et al.). Decoding methods like self-consistency highlighted the gains from aggregating diverse generations, but operated by unweighted voting rather than principled coupling between generation and evaluation (Wang et al.). Together, these threads revealed an opportunity: cast decoding as a cooperative signaling game where a generator’s utterances and a discriminator’s correctness assessments influence one another. By adopting pragmatic speaker–listener structure, using LM-based correctness estimates as utilities, and importing regularized equilibrium concepts and equilibrium-finding dynamics from game theory, the paper synthesizes a training-free equilibrium-ranking procedure that reconciles generative sampling and discriminative scoring into coherent, fixed-point LM predictions.

---

*Analysis generated on: 2026-01-06T06:40:19.638946*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
