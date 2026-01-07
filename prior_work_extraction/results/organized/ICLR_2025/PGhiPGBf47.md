# Prior Work Analysis Report

## Target Paper

**Title:** DailyDilemmas: Revealing Value Preferences of LLMs with Quandaries of Daily Life

**Conference:** ICLR 2025 (spotlight)

**Authors:** Yu Ying Chiu, Liwei Jiang, Yejin Choi

**Keywords:** language model, moral dilemma, model alignment, machine ethics, value alignment

**Abstract:** 
> As users increasingly seek guidance from LLMs for decision-making in daily life, many of these decisions are not clear-cut and depend significantly on the personal values and ethical standards of people. We present DailyDilemmas, a dataset of 1,360 moral dilemmas encountered in everyday life. Each dilemma presents two possible actions, along with affected parties and relevant human values for each action. Based on these dilemmas, we gather a repository of human values covering diverse everyday t...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Social Chemistry 101: Learning to Reason about Social and Moral Norms** (2020)
- *Authors:* Maarten Sap et al.
- *Direct Connection:* By framing everyday situations in terms of social and moral rules-of-thumb, it established the everyday normative context that DailyDilemmas extends into explicit two-action dilemmas with annotated affected parties and value trade-offs.

**SCRUPLES: A Corpus of Community Ethical Judgments** (2021)
- *Authors:* Nicholas Lourie et al.
- *Direct Connection:* By surfacing ambiguity and disagreement in community ethical judgments on everyday narratives, it highlighted the need for datasets that capture contested choices, which DailyDilemmas formalizes via paired actions and explicit value dimensions.

**The Moral Machine experiment** (2018)
- *Authors:* Edmond Awad et al.
- *Direct Connection:* It established large-scale pairwise moral dilemmas and cross-cultural analysis, a paradigm DailyDilemmas adapts from trolley settings to quotidian life with value tags for each option and identified affected parties.

**World Values Survey: Round 7 (2017–2021) Cross-National Data-Set** (2020)
- *Authors:* Ronald Inglehart et al.
- *Direct Connection:* It provides a canonical taxonomy of human values that DailyDilemmas explicitly uses to code actions and aggregate model preferences along sociological value dimensions.

**Moral Foundations Theory: The Pragmatic Validity of Moral Pluralism** (2013)
- *Authors:* Jesse Graham et al.
- *Direct Connection:* Its psychologically grounded moral dimensions supply one of the key lenses through which DailyDilemmas annotates and analyzes the values implicated by each action choice.

### 💡 Inspiration

**Delphi: Towards Machine Ethics and Norms** (2021)
- *Authors:* Liwei Jiang et al.
- *Direct Connection:* Delphi showed that LMs can make normative judgments over everyday scenarios but are brittle and opaque about underlying values, directly motivating DailyDilemmas’ controlled dilemma design and explicit value labeling to diagnose model value preferences.

### 🔍 Gap Identification

**Constitutional AI: Harmlessness from AI Feedback** (2022)
- *Authors:* Yuntao Bai et al.
- *Direct Connection:* By aligning models to a fixed set of stated principles, it raised the question of which values models actually prioritize in practice, which DailyDilemmas directly probes by mapping choices to value frameworks across everyday dilemmas.

---

## Synthesis: How Prior Work Led to This Paper

Social Chemistry 101 showed that everyday situations can be represented by compact social and moral rules-of-thumb, making normative reasoning over daily life a tractable modeling target. Delphi then demonstrated that language models can render such judgments but often do so opaquely and inconsistently, revealing the need for structured probes that expose the value trade-offs behind model outputs. SCRUPLES surfaced ambiguity and community disagreement in ethical judgments, underscoring that many real decisions are contested rather than clear-cut and thus require formulations that capture competing, legitimate values. The Moral Machine experiment pioneered large-scale pairwise moral dilemmas with cross-cultural analysis, validating pairwise choice as a vehicle to elicit preferences, albeit within stylized trolley scenarios. In parallel, the World Values Survey articulated sociological value dimensions suitable for aggregating preferences across topics and populations, while Moral Foundations Theory provided psychologically grounded moral dimensions for coding what values a choice implicates. Constitutional AI reframed alignment as adherence to an explicit set of principles, highlighting a gap between declared constitutions and the values models actually enact under pressure. Together, these works reveal a missing diagnostic: everyday, two-sided dilemmas with explicit affected parties and value tags that allow principled aggregation across established value taxonomies. DailyDilemmas synthesizes these insights by pairing quotidian choices, annotating their implicated values, and analyzing model selections through WVS and MFT lenses (among others), thereby turning opaque moral judgments into measurable value preferences and exposing how aligned models prioritize values in practice.

---

*Analysis generated on: 2026-01-06T06:56:11.462734*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
