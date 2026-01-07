# Prior Work Analysis Report

## Target Paper

**Title:** Tensor Trust: Interpretable Prompt Injection Attacks from an Online Game

**Conference:** ICLR 2024 (spotlight)

**Authors:** Sam Toyer, Olivia Watkins, Ethan Adrian Mendes, Justin Svegliato, Luke Bailey, Tiffany Wang, Isaac Ong, Karim Elmaaroufi, Pieter Abbeel, Trevor Darrell, Alan Ritter, Stuart Russell

**Keywords:** large language models, LLMs, security, adversarial examples, prompt extraction, prompt injection, prompt hijacking, prompt engineering

**Abstract:** 
> While Large Language Models (LLMs) are increasingly being used in real-world applications, they remain vulnerable to *prompt injection attacks*: malicious third party prompts that subvert the intent of the system designer. To help researchers study this problem, we present a dataset of over 563,000 prompt injection attacks and 118,000 prompt-based "defenses" against prompt injection, all created by players of an online game called Tensor Trust. To the best of our knowledge, this is the first dat...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**More Than You’ve Asked For: A Comprehensive Analysis of Novel Prompt Injection Threats to Application-Integrated Large Language Models** (2023)
- *Authors:* Greshake et al.
- *Direct Connection:* This work formalized the prompt injection threat model (including data exfiltration and instruction override) that directly underpins the paper’s extraction vs. hijacking taxonomy and benchmarking focus.

**PromptBench: Towards Evaluating the Robustness of Large Language Models to Adversarial Instructions** (2023)
- *Authors:* Liu et al.
- *Direct Connection:* By framing robustness evaluation with adversarial instructions, this work provided the evaluation lens that the paper extends into a large-scale, human-generated benchmark with explicit extraction/hijacking tasks and defenses.

### 💡 Inspiration

**Red Teaming Language Models** (2022)
- *Authors:* Perez et al.
- *Direct Connection:* By showing that human adversaries surface qualitatively rich failure modes at scale, this paper directly inspired the paper’s human-in-the-loop, gamified data collection of attacks and defenses.

### 🔍 Gap Identification

**Universal and Transferable Adversarial Attacks on Aligned Language Models** (2023)
- *Authors:* Zou et al.
- *Direct Connection:* This work’s powerful but opaque adversarial-suffix jailbreaks highlighted the need for interpretable attack strategies, motivating the paper’s focus on human-generated, structured prompts.

**WildJailbreak: In-the-Wild Jailbreaking Prompts on Large Language Models** (2023)
- *Authors:* Wang et al.
- *Direct Connection:* This in-the-wild jailbreak corpus exposed real vulnerabilities but lacked structured taxonomy and paired defenses, a gap the paper fills with interpretable attacks and human-written counter-prompts.

### 🔗 Related Problem

**Universal Adversarial Triggers for Attacking and Analyzing NLP** (2019)
- *Authors:* Wallace et al.
- *Direct Connection:* The demonstration that universal triggers can reliably subvert NLP models, while being unnatural, directly motivated collecting human-readable adversarial patterns the paper analyzes and benchmarks.

---

## Synthesis: How Prior Work Led to This Paper

Prompt injection was first crisply framed for application-integrated LLMs by Greshake et al., who described how untrusted content can drive data exfiltration and instruction override, articulating a concrete threat model that distinguishes between extracting hidden information and hijacking behavior. Perez et al. demonstrated that human red teamers uncover qualitatively novel and diverse failure modes, grounding the value of large-scale, human-generated adversarial data over purely automated attacks. Zou et al. introduced universal, transferable jailbreak suffixes that reliably defeat alignment but are opaque and uninterpretable, revealing a mismatch between attack effectiveness and explainability. Wallace et al. earlier showed universal adversarial triggers can broadly fool NLP models while being unnatural, reinforcing the need for human-comprehensible artifacts to study mechanisms and defenses. WildJailbreak compiled real-world jailbreak prompts, validating practical risk but lacking a structured taxonomy and paired defensive strategies. Complementing these, PromptBench formalized robustness evaluation against adversarial instructions, but primarily at smaller scale and without human-authored defense prompts.
Together, these works surfaced a clear opportunity: marry the formal threat model and evaluation framing with scalable, human-in-the-loop collection to obtain interpretable attack strategies and their corresponding defenses, organized around extraction versus hijacking. The paper synthesizes these threads by turning adversarial prompting into an online game that yields large, human-generated, structured attacks and defense prompts, enabling a benchmark that directly probes the two core injection modes while providing interpretable artifacts to analyze vulnerabilities and to study how defenses succeed or fail.

---

*Analysis generated on: 2026-01-07T00:16:11.858593*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
