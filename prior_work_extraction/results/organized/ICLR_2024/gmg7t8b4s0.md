# Prior Work Analysis Report

## Target Paper

**Title:** Can LLMs Keep a Secret? Testing  Privacy  Implications of Language Models  via Contextual Integrity Theory

**Conference:** ICLR 2024 (spotlight)

**Authors:** Niloofar Mireshghallah, Hyunwoo Kim, Xuhui Zhou, Yulia Tsvetkov, Maarten Sap, Reza Shokri, Yejin Choi

**Keywords:** Contextual Integrity, Privacy, Theory of Mind

**Abstract:** 
> Existing efforts on quantifying privacy implications for large language models (LLMs) solely focus on measuring leakage of training data. In this work, we shed light on the often-overlooked interactive settings where an LLM receives information from multiple sources and generates an output to be shared with other entities, creating the potential of exposing sensitive input data in inappropriate contexts. In these scenarios, humans nat- urally uphold privacy by choosing whether or not to disclose...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Privacy in Context: Technology, Policy, and the Integrity of Social Life** (2010)
- *Authors:* Helen Nissenbaum
- *Direct Connection:* The benchmark’s scenarios and labeling schema instantiate contextual integrity’s five parameters (subject, sender, recipient, attribute, transmission principle) and its norm-violation criterion, which directly structure CONFAIDE’s tiers.

**Membership Inference Attacks Against Machine Learning Models** (2017)
- *Authors:* Reza Shokri et al.
- *Direct Connection:* By formalizing privacy risk measurement via adversarial querying, this paper provides the methodological backbone that the current work extends from training-data membership to context-appropriate disclosure judgments.

### 💡 Inspiration

**Theory of Mind May Have Spontaneously Emerged in Large Language Models** (2023)
- *Authors:* Michal Kosinski
- *Direct Connection:* Findings that LLMs can track beliefs and perspectives inspire the inclusion of tasks requiring theory-of-mind-style reasoning about who knows what for privacy-appropriate disclosure.

**Social Chemistry 101: Learning to Reason about Everyday Morality** (2020)
- *Authors:* Maarten Sap et al.
- *Direct Connection:* By operationalizing everyday social norms as structured rules with crowdsourced judgments, this work informs the methodology of building a norm-grounded evaluation set, here adapted to privacy norms via contextual integrity.

### 🔍 Gap Identification

**Extracting Training Data from Large Language Models** (2021)
- *Authors:* Nicholas Carlini et al.
- *Direct Connection:* This work’s focus on memorization-driven leakage from static training corpora marks the limitation that the present paper explicitly addresses by shifting to interactive, multi-party contextual leakage of user-provided inputs.

**Not What You’ve Signed Up For: Compromising LLMs via Prompt Injection** (2023)
- *Authors:* Jonas Greshake et al.
- *Direct Connection:* Evidence that LLMs can be induced to exfiltrate secrets across contexts directly motivates a principled, norm-grounded benchmark to test whether models withhold sensitive inputs from unintended recipients.

**Large Language Models Fail on Trivial Alterations to Theory-of-Mind Tasks** (2023)
- *Authors:* Tomer D. Ullman
- *Direct Connection:* Documented brittleness of LLMs’ ToM under minimal contextual changes motivates stress-testing privacy reasoning under subtle variations in roles, recipients, and transmission principles.

---

## Synthesis: How Prior Work Led to This Paper

Contextual integrity articulates privacy as appropriate information flows governed by five parameters—subject, sender, recipient, attribute, and transmission principle—and evaluates violations against context-specific norms; this theoretical structure, laid out by Nissenbaum, offers a directly operationalizable schema for judging when disclosure is acceptable. Membership inference introduced a concrete, query-based methodology to quantify privacy risk in ML, establishing that model behavior can be probed adversarially to reveal sensitive associations. Subsequent work showed that large language models can emit verbatim training data, crystallizing a memorization-centric framing of privacy leakage. In parallel, prompt-injection studies revealed that LLMs can be manipulated to exfiltrate secrets across role boundaries, highlighting vulnerabilities that arise precisely from contextual shifts rather than mere memorization. On the reasoning side, findings that LLMs may exhibit theory-of-mind capabilities suggested they might track who knows what, while counterevidence showed such capabilities are brittle under minor contextual perturbations. Separately, Social Chemistry 101 demonstrated how to construct norm-grounded evaluation datasets by structuring scenarios and aggregating judgments about appropriateness. Together, these strands expose a gap: existing privacy evaluations fixate on training data leakage and miss interactive, multi-party contexts where normative appropriateness of disclosure is the core question. The current work synthesizes CI’s formal parameters with norm-grounded dataset construction and ToM-informed scenario design to create a tiered benchmark that probes whether instruction-tuned LLMs can withhold sensitive inputs when context deems it inappropriate, directly addressing injection-style exfiltration risks and the brittleness of belief-tracking in nuanced, real-world settings.

---

*Analysis generated on: 2026-01-06T14:19:21.606210*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
