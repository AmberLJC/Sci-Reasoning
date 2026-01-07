# Prior Work Analysis Report

## Target Paper

**Title:** Coeditor: Leveraging Repo-level Diffs for Code Auto-editing

**Conference:** ICLR 2024 (spotlight)

**Authors:** Jiayi Wei, Greg Durrett, Isil Dillig

**Keywords:** language model for code, editing, refactoring

**Abstract:** 
> Developers often dedicate significant time to maintaining and refactoring existing code. However, most prior work on generative models for code focuses solely on creating new code, overlooking the distinctive needs of editing existing code. In this work, we explore a multi-round code auto-editing setting, aiming to predict edits to a code region based on recent changes within the same codebase. Our model, Coeditor, is a fine-tuned language model specifically designed for code editing tasks. We r...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding and Generation** (2021)
- *Authors:* Shuai Lu et al.
- *Direct Connection:* CodeXGLUE’s code refinement formulation (buggy-to-fixed translation) crystallized the edit-as-generation task that Coeditor adopts but extends to real commit-derived edits and multi-round settings with repository-level information.

**CODIT: Code Editing with Tree-based Neural Networks** (2019)
- *Authors:* Matei Tufano et al.
- *Direct Connection:* CODIT framed learning code edits from historical commits, directly informing Coeditor’s commit-history-derived training data and focus on learning to apply edits rather than synthesize entire files.

### 💡 Inspiration

**Learning to Represent Edits** (2019)
- *Authors:* Pengcheng Yin et al.
- *Direct Connection:* This work introduced modeling edits as first-class objects rather than regenerating code from scratch, a key insight Coeditor leverages by representing recent code changes explicitly via line diffs to guide subsequent edits.

**Self-Refine: Iterative Refinement with Self-Feedback** (2023)
- *Authors:* Aman Madaan et al.
- *Direct Connection:* Self-Refine showed that multi-round iterative improvement markedly boosts LLM performance, motivating Coeditor’s multi-round auto-editing formulation where each round conditions on prior diffs within the same repository.

### 📊 Baseline

**InCoder: A Generative Model for Code Infilling** (2022)
- *Authors:* Daniel Fried et al.
- *Direct Connection:* InCoder established infilling/FIM as the dominant code-editing baseline but operates with local, file-level context, whose limitations in leveraging repository-wide recent changes Coeditor explicitly overcomes by conditioning on repo-level diffs and static-analysis-built contexts.

### 🔗 Related Problem

**RepoCoder: Repository-Level Code Generation with Retrieval-Augmented LLMs** (2023)
- *Authors:* Zhu et al.
- *Direct Connection:* RepoCoder demonstrated the necessity of repository-level context and retrieval/static-analysis signals for code generation, which Coeditor adapts to the editing setting by constructing large, customized contexts for predicting localized edits.

---

## Synthesis: How Prior Work Led to This Paper

InCoder introduced code infilling as an effective editing primitive but largely limited context to a single file, making it difficult to exploit cross-file changes in large repositories. CodeXGLUE standardized code refinement as translating buggy code to fixed code, sharpening the notion of code editing as a prediction problem, though typically scoped to local contexts and curated benchmarks rather than real-world commit streams. Learning to Represent Edits provided the crucial insight that edits themselves can be modeled explicitly, enabling systems to leverage edit signals rather than regenerate entire artifacts. CODIT operationalized this idea in software engineering by learning code edits from commit histories, showing that past changes contain rich supervision for applying multi-line, structured edits. RepoCoder established that repository-level tasks benefit from retrieval and static analysis to assemble the right cross-file context, suggesting that code generation—and by extension code editing—should be conditioned on project-wide information. Finally, Self-Refine demonstrated that iterative, multi-round refinement can systematically improve model outputs when each round conditions on prior outcomes.
Together, these works reveal a gap: dominant code-editing methods either ignore repository-wide recent changes or do not iterate with explicit edit history. Coeditor naturally synthesizes these insights by training on real commits, representing recent changes as line diffs, and using static analysis to build repo-level contexts, then iterating edits round-by-round while conditioning on prior diffs—thereby addressing both context and iteration shortcomings of prior approaches.

---

*Analysis generated on: 2026-01-06T13:25:11.529602*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
