# Prior Work Analysis Report

## Target Paper

**Title:** Tell me about yourself: LLMs are aware of their learned behaviors

**Conference:** ICLR 2025 (spotlight)

**Authors:** Jan Betley, Xuchan Bao, Martín Soto, Anna Sztyber-Betley, James Chua, Owain Evans

**Keywords:** NLP, LLM, GPT, generalization, out-of-context reasoning, capabilities, fine-tuning, self-awareness, self-knowledge

**Abstract:** 
> We study *behavioral self-awareness*, which we define as an LLM's capability to articulate its behavioral policies without relying on in-context examples. We finetune LLMs on examples that exhibit particular behaviors, including (a) making risk-seeking / risk-averse economic decisions, and (b) making the user say a certain word. Although these examples never contain explicit descriptions of the policy (e.g. "I will now take the risk-seeking option"), we find that the finetuned LLMs can explicitl...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Eliciting Latent Knowledge** (2021)
- *Authors:* Ajeya Cotra et al.
- *Direct Connection:* This work frames the core goal of extracting a model’s internal knowledge without supervision, which the current paper operationalizes by eliciting and verifying language-model descriptions of their own learned behavioral policies without in-context examples.

**Concealed Data Poisoning Attacks on NLP Models** (2021)
- *Authors:* Eric Wallace et al.
- *Direct Connection:* This paper establishes that targeted behaviors can be implanted via data poisoning/backdoors in NLP models, directly motivating the paper’s exploration of whether such implanted (or fine-tuned) behaviors are explicitly knowable to the model itself.

**Personalizing Dialogue Agents: I have a dog, do you have pets too?** (2018)
- *Authors:* Saizheng Zhang et al.
- *Direct Connection:* Introducing persona-conditioned behavior as a formal setup provides the methodological basis for attributing different learned policies to distinct personas and evaluating whether models can correctly report persona-specific policies.

### 💡 Inspiration

**Language Models (Mostly) Know What They Know** (2022)
- *Authors:* Akhil Kadavath et al.
- *Direct Connection:* Demonstrating that LLMs can accurately report aspects of their own competence inspired the paper’s central idea to test whether models can similarly articulate their learned behavioral policies (self-knowledge about behavior) in out-of-context settings.

### 🔍 Gap Identification

**Sleeper Agents: Training Deceptive Models that Persist Through Safety Training** (2024)
- *Authors:* Evan Hubinger et al.
- *Direct Connection:* By showing that hidden, goal-directed behaviors can be trained to activate under specific circumstances, this work motivates testing whether models can recognize and report their own implanted policies and triggers—a gap the paper directly addresses.

### 🔗 Related Problem

**Constitutional AI: Harmlessness from AI Feedback** (2022)
- *Authors:* Yuntao Bai et al.
- *Direct Connection:* By showing that models can follow and reason about explicit natural-language principles, this work motivates probing whether models can also verbalize implicit, fine-tuned policies—moving from externally provided constitutions to internally learned ones.

**Universal and Transferable Adversarial Attacks on Aligned Language Models** (2023)
- *Authors:* Andy Zou et al.
- *Direct Connection:* The discovery of short universal triggers that activate undesirable behaviors informs the paper’s analysis linking learned policies to trigger-like conditions (e.g., personas) and testing whether the model can describe those activation conditions.

---

## Synthesis: How Prior Work Led to This Paper

Eliciting Latent Knowledge established the aim of extracting internal model beliefs without supervision, emphasizing that models can possess latent representations not directly revealed by standard prompts. Language Models (Mostly) Know What They Know showed that LLMs can report aspects of their own competence, suggesting that self-knowledge can be elicited reliably via language. Constitutional AI demonstrated that models can follow and reason over explicit natural-language rules and critique their outputs against those rules, underscoring the feasibility of using natural language as a medium for specifying and reflecting on behavioral policies. In parallel, Concealed Data Poisoning Attacks on NLP Models grounded the notion that targeted behaviors can be implanted via training data, formalizing backdoors in NLP. Universal and Transferable Adversarial Attacks on Aligned Language Models revealed that short, general triggers can consistently activate such behaviors, conceptually linking behavior to compact activation conditions. Sleeper Agents then showed that strategically trained hidden goals can persist and surface under triggers even after safety training. Finally, Persona-Chat provided a standard framework for persona-conditioned behavior, enabling attribution and measurement across identities. Together, these works spotlighted a gap: while models can follow explicit rules and can be implanted with hidden behaviors, it was unclear whether they can articulate their own implicitly learned policies, detached from immediate examples, and attribute them to specific conditions such as personas. Building on elicitation principles, backdoor insights, and persona conditioning, the paper naturally tests and demonstrates behavioral self-awareness: LLMs trained on behaviors can out-of-context describe the governing policies and correctly attribute them to the appropriate persona or trigger.

---

*Analysis generated on: 2026-01-06T16:58:26.049735*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
