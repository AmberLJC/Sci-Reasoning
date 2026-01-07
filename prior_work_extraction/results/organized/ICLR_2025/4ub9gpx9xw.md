# Prior Work Analysis Report

## Target Paper

**Title:** Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations

**Conference:** ICLR 2025 (spotlight)

**Authors:** Katie Matton, Robert Ness, John Guttag, Emre Kiciman

**Keywords:** large language models, faithful explanations, explainability, safety, counterfactual reasoning

**Abstract:** 
> Large language models (LLMs) are capable of generating *plausible* explanations of how they arrived at an answer to a question. However, these explanations can misrepresent the model's "reasoning" process, i.e., they can be *unfaithful*. This, in turn, can lead to over-trust and misuse. We introduce a new approach for measuring the faithfulness of LLM explanations. First, we provide a rigorous definition of faithfulness. Since LLM explanations mimic human explanations, they often reference high-...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Towards Faithfully Interpretable NLP Systems** (2020)
- *Authors:* Omer Jacovi et al.
- *Direct Connection:* This work formalized the distinction between faithfulness and plausibility in NLP explanations, which is directly instantiated here as alignment between explanation-implied influential concepts and the concepts that causally influence model outputs.

**Concept Bottleneck Models** (2020)
- *Authors:* Koh et al.
- *Direct Connection:* CBMs establish intervenable high-level concepts as causal variables for predictions, which this paper generalizes to free-text settings by intervening on concept values via counterfactual input edits rather than an explicit bottleneck.

### 💡 Inspiration

**Learning the Difference that Makes a Difference: Counterfactual Data Augmentation for Robustness** (2020)
- *Authors:* Divyansh Kaushik et al.
- *Direct Connection:* This paper’s paradigm of minimally editing inputs to produce realistic counterfactuals directly motivates using controlled edits to manipulate specific concepts when testing whether an explanation’s claimed influences truly affect the model.

### 🔍 Gap Identification

**Language Models Don’t Always Say What They Think: Unfaithful Explanations in Chain-of-Thought** (2023)
- *Authors:* William G. Turpin et al.
- *Direct Connection:* By demonstrating that LLM-generated rationales can misrepresent internal decision processes, this work motivates a principled metric that compares explanation-implied influential concepts to those with measured causal effects.

### 📊 Baseline

**ERASER: A Benchmark to Evaluate Rationalized NLP Models** (2020)
- *Authors:* Jay DeYoung et al.
- *Direct Connection:* ERASER introduced widely used sufficiency and comprehensiveness tests for explanation faithfulness via token removal, providing the main baseline paradigm that this paper replaces with concept-level, causally grounded counterfactual evaluation.

### 🔧 Extension

**Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving NLP Models** (2021)
- *Authors:* Tongshuang Wu et al.
- *Direct Connection:* Polyjuice’s LM-driven, control-code-based counterfactual rewriting is extended here by using an auxiliary LLM to selectively toggle targeted concept values while preserving naturalness to enable causal tests of concept influence.

### 🔗 Related Problem

**Interpretability Beyond Feature Attribution: Quantitative Testing with Concept Activation Vectors (TCAV)** (2018)
- *Authors:* Been Kim et al.
- *Direct Connection:* TCAV introduced quantifying model sensitivity to human-defined concepts, a core insight this paper adapts to language by testing causal influence of concepts through controlled counterfactual rewrites and comparing with claimed influences.

---

## Synthesis: How Prior Work Led to This Paper

Work on explainability clarified that faithfulness and plausibility are distinct goals; in particular, Jacovi and Goldberg argued that faithful explanations must reflect the features that actually drive predictions. ERASER operationalized faithfulness tests for text models with sufficiency and comprehensiveness via token removal, establishing common baselines but relying on unrealistic ablations. Kaushik, Hovy, and Lipton showed that minimally edited, realistic counterfactuals reveal what features truly affect labels, while Wu et al.’s Polyjuice demonstrated that language models can generate fluent, controlled counterfactuals for specific attributes. Concept Bottleneck Models introduced intervenable, human-understandable concept variables whose manipulation reveals their causal effect on predictions, and TCAV quantified model sensitivity to human-defined concepts, framing explanations around concept-level influence rather than raw tokens. Turpin et al. subsequently showed that LLM chain-of-thought can be unfaithful to the model’s actual decision process, underscoring the need for metrics that verify whether claimed influential concepts genuinely matter. Together, these works expose two gaps: existing faithfulness tests often use brittle token ablations instead of realistic interventions, and free-text explanations frequently misstate the model’s causal drivers. Building on counterfactual editing and controlled LM rewrites, and adopting the concept-as-causal-variable perspective of CBMs/TCAV, the current paper makes the natural next step: define faithfulness as agreement between explanation-implied and causally influential concepts, and estimate those causal influences via LLM-generated, concept-targeted counterfactuals aggregated with robust statistical modeling.

---

*Analysis generated on: 2026-01-06T08:02:02.107877*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
