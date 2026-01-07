# Prior Work Analysis Report

## Target Paper

**Title:** Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book?

**Conference:** ICLR 2025 (spotlight)

**Authors:** Seth Aycock, David Stap, Di Wu, Christof Monz, Khalil Sima'an

**Keywords:** llms, translation, low-resource, grammar, long-context, linguistics

**Abstract:** 
> Extremely low-resource (XLR) languages lack substantial corpora for training NLP models, motivating the use of all available resources such as dictionaries and grammar books. Machine Translation from One Book (Tanzer et al., 2024) suggests that prompting long-context LLMs with one grammar book enables English–Kalamang translation, an XLR language unseen by LLMs—a noteworthy case of linguistics helping an NLP task. We investigate the source of this translation ability, finding almost all improvem...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Machine Translation from One Book** (2024)
- *Authors:* Tanzer et al.
- *Direct Connection:* This work introduced the one-grammar-book prompting setup for English–Kalamang and claimed that grammatical descriptions enable translation in an unseen XLR language, providing the exact problem formulation and primary baseline that this paper dissects and re-evaluates.

**ODIN: A Database of Interlinear Glossed Text** (2010)
- *Authors:* William D. Lewis and Fei Xia
- *Direct Connection:* ODIN established interlinear glossed text as structured supervision for morphosyntax, informing this paper’s gloss-prediction diagnostic to assess what linguistic knowledge grammar books actually inject into models.

**URIEL and lang2vec: Representing languages as typological, genealogical, and geographical vectors** (2017)
- *Authors:* Patrick Littell et al.
- *Direct Connection:* URIEL’s typological representations provide the conceptual and practical basis for this paper’s typology-driven analysis of which grammatical properties in a book are likely to help models.

### 💡 Inspiration

**Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?** (2022)
- *Authors:* Sewon Min et al.
- *Direct Connection:* Their finding that in-context performance often stems from the presence and properties of examples rather than task instructions directly motivates this paper’s isolation of grammar-book parallel examples versus grammatical prose to locate the true source of translation gains.

### 🔍 Gap Identification

**Is ChatGPT a Good Translator? A Preliminary Study** (2023)
- *Authors:* Wenxiang Jiao et al.
- *Direct Connection:* By showing that LLM translation quality depends heavily on data coverage and benefits notably from few-shot examples, this study highlights limitations in low-resource and unseen settings that this paper probes within the one-book scenario.

**Large Language Models are State-of-the-Art for Translation? Not Yet** (2023)
- *Authors:* Tom Kocmi and Christian Federmann
- *Direct Connection:* Their evidence that fine-tuned encoder–decoder NMT remains highly competitive with LLM prompting directly motivates this paper’s comparison showing that a simply fine-tuned MT model can match the one-book LLM setup.

---

## Synthesis: How Prior Work Led to This Paper

Machine Translation from One Book framed the striking claim that a single grammar book, fed to a long-context LLM, can unlock translation for an unseen, extremely low-resource language, establishing the concrete one-book prompting protocol and Kalamang evaluation. Min et al. showed that in-context learning’s gains often arise from example demonstrations rather than the textual instructions themselves, suggesting a precise methodological lever to separate the influence of parallel examples from explanatory prose. Jiao et al. documented that LLM translation quality is sensitive to language coverage and benefits substantially from few-shot exemplars, especially in low-resource regimes, underscoring the importance of example-driven signal. Kocmi and Federmann argued that fine-tuned encoder–decoder MT remains competitive with prompted LLMs, motivating a rigorous NMT baseline when only tiny parallel supervision is available. ODIN established interlinear glossed text as a structured source of morphosyntactic supervision, enabling diagnostics like gloss prediction to test what linguistic information is actually learned. URIEL’s typological vectors offered a principled scaffold to relate specific grammatical properties to cross-lingual generalization. Together, these works reveal a tension: dramatic claims about grammar-book prompting, clear evidence that demonstrations drive in-context performance, and the competitiveness of small-data NMT. Building on this, the present study dissects the one-book setting to show that parallel examples—not grammatical exposition—drive gains, extends the analysis beyond Kalamang, demonstrates a simple fine-tuned encoder–decoder can match performance, and uses grammaticality judgment and gloss prediction under a typological lens to pinpoint what kinds of grammatical information, if any, actually help.

---

*Analysis generated on: 2026-01-06T10:04:31.993091*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
