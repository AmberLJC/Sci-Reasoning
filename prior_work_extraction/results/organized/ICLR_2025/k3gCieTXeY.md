# Prior Work Analysis Report

## Target Paper

**Title:** INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge

**Conference:** ICLR 2025 (spotlight)

**Authors:** Angelika Romanou, Negar Foroutan, Anna Sotnikova, Sree Harsha Nelaturu, Shivalika Singh, Rishabh Maheshwary, Micol Altomare, Zeming Chen, Mohamed A. Haggag, Snegha A, Alfonso Amayuelas, Azril Hafizi Amirudin, Danylo Boiko, Michael Chang, Jenny Chim, Gal Cohen, Aditya Kumar Dalmia, Abraham Diress, Sharad Duwal, Daniil Dzenhaliou, Daniel Fernando Erazo Florez, Fabian Farestam, Joseph Marvin Imperial, Shayekh Bin Islam, Perttu Isotalo, Maral Jabbarishiviari, Börje F. Karlsson, Eldar Khalilov, Christopher Klamm, Fajri Koto, Dominik Krzemiński, Gabriel Adriano de Melo, Syrielle Montariol, Yiyang Nan, Joel Niklaus, Jekaterina Novikova, Johan Samir Obando Ceron, Debjit Paul, Esther Ploeger, Jebish Purbey, Swati Rajwal, Selvan Sunitha Ravi, Sara Rydell, Roshan Santhosh, Drishti Sharma, Marjana Prifti Skenduli, Arshia Soltani Moakhar, Bardia soltani moakhar, Ayush Kumar Tarun, Azmine Toushik Wasi, Thenuka Ovin Weerasinghe, Serhan Yilmaz, Mike Zhang, Imanol Schlag, Marzieh Fadaee, Sara Hooker, Antoine Bosselut

**Keywords:** evaluation, multilinguality, large language models

**Abstract:** 
> The performance differential of large language models (LLM) between languages hinders their effective deployment in many regions, inhibiting the potential economic and societal value of generative AI tools in many communities. However, the development of functional LLMs in many languages (i.e., multilingual LLMs) is bottlenecked by the lack of high-quality evaluation resources in languages other than English. Moreover, current practices in multilingual benchmark construction often translate Engl...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Measuring Massive Multitask Language Understanding** (2020)
- *Authors:* Hendrycks et al.
- *Direct Connection:* It established the exam-style, multi-subject, multiple-choice evaluation paradigm for knowledge and reasoning that this work generalizes to multilingual, region-specific contexts.

**MKQA: A Linguistically Diverse Benchmark for Multilingual Open Domain Question Answering** (2021)
- *Authors:* Longpre et al.
- *Direct Connection:* It introduced a multilingual evaluation design with language-native queries and answers, a principle this work adopts at exam scale to measure knowledge and reasoning across many languages.

### 💡 Inspiration

**TyDi QA: A Benchmark for Information-Seeking Question Answering in Typologically Diverse Languages** (2020)
- *Authors:* Clark et al.
- *Direct Connection:* By demonstrating the importance of collecting questions natively in each language rather than translating from English, it directly motivates sourcing local exam questions to avoid translation artifacts and preserve cultural specificity.

**CEval: A Comprehensive Chinese Evaluation Suite for Foundation Models** (2023)
- *Authors:* Huang et al.
- *Direct Connection:* By leveraging diverse real-world Chinese exam questions, it demonstrated that locally sourced exams better reflect cultural and curricular knowledge, inspiring a multilingual extension grounded in regional exam content.

### 🔍 Gap Identification

**MLQA: Evaluating Cross-lingual Extractive Question Answering** (2020)
- *Authors:* Lewis et al.
- *Direct Connection:* As a translation-based multilingual QA benchmark, it exemplifies the limitations (translation artifacts and lack of regional specificity) that this work explicitly addresses by grounding items in local-language sources.

### 🔗 Related Problem

**AGIEval: A Human-Centric Benchmark for Evaluating Foundation Models** (2023)
- *Authors:* Zhong et al.
- *Direct Connection:* It showed that standardized exams provide a rigorous way to assess real-world knowledge and reasoning, informing the choice to use official exam materials while expanding beyond English/Chinese to many languages.

---

## Synthesis: How Prior Work Led to This Paper

Measuring Massive Multitask Language Understanding (MMLU) established a rigorous exam-style, multiple-choice protocol for assessing broad knowledge and reasoning across many subjects, setting the template for competency-oriented evaluation rather than narrow task performance. TyDi QA argued for native-language data collection across typologically diverse languages to avoid translation artifacts, demonstrating that linguistic authenticity changes task difficulty and model outcomes. MKQA operationalized a multilingual QA setup where queries and answers are authored in their respective languages, showing that natively created data can scale across languages while preserving cross-lingual comparability. In contrast, MLQA exemplified translation-based multilingual evaluation, highlighting how reliance on English-origin content limits cultural specificity and may distort difficulty. AGIEval demonstrated that standardized exams are a strong proxy for real-world knowledge and reasoning, while CEval showed that sourcing questions from local curricular exams captures domain breadth and cultural context within Chinese.
Together these works reveal a gap: multilingual LLM evaluation has either centered on English-origin content translated across languages or been monolingual in its use of authentic, curriculum-grounded exams. The natural next step is to fuse the exam-style, knowledge-and-reasoning rigor popularized by MMLU and AGIEval/CEval with the native-language, authenticity-preserving data practices advocated by TyDi QA and MKQA. This synthesis motivates constructing a large-scale suite of locally sourced exam questions across many languages to evaluate models in the language environments and regional knowledge contexts where they are actually used.

---

*Analysis generated on: 2026-01-06T07:45:32.179520*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
