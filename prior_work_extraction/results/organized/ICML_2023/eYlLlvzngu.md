# Prior Work Analysis Report

## Target Paper
**Title:** eYlLlvzngu
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Computing Machinery and Intelligence** (1950)
- *Authors:* Alan M. Turing
- *Connection:* Introduces the Turing Test as an evaluation of human-like behavior; this paper explicitly reframes that paradigm into a “Turing Experiment” to address the limitation of simulating a single arbitrary individual by instead requiring a representative sample.

**An experimental analysis of ultimatum bargaining** (1982)
- *Authors:* Werner Güth et al.
- *Connection:* Defines the Ultimatum Game and the canonical human behavioral regularities (e.g., rejection of unfair offers) that this paper uses as a Turing Experiment to test whether LLM-simulated samples reproduce known outcomes.

**Making and correcting errors during sentence comprehension: Eye movements in the analysis of structurally ambiguous sentences** (1982)
- *Authors:* Lyn Frazier et al.
- *Connection:* Establishes garden-path effects in human sentence processing; the present work uses these stimuli to assess whether LLM ‘participants’ collectively replicate human difficulty patterns.

**Behavioral Study of Obedience** (1963)
- *Authors:* Stanley Milgram
- *Connection:* Provides the classic human-subject framework on obedience to authority that the paper adapts into a Turing Experiment to test whether simulated samples recover the qualitative obedience effect.

**Vox Populi** (1907)
- *Authors:* Francis Galton
- *Connection:* Introduces the wisdom-of-crowds phenomenon that this paper operationalizes as a Turing Experiment, revealing the LLM-specific ‘hyper-accuracy’ distortion when aggregating simulated participants.

### 💡 Inspiration

**Out of One, Many: Using Language Models to Simulate Human Samples** (2023)
- *Authors:* Lisa P. Argyle et al.
- *Connection:* Demonstrates that LLMs can be prompted to approximate responses of demographic subgroups in survey research, directly inspiring this paper’s formalization and extension to simulating representative samples for classic behavioral experiments.

### 🔧 Extension

**Personalizing Dialogue Agents: I have a dog, do you have pets too?** (2018)
- *Authors:* Saizheng Zhang et al.
- *Connection:* Introduces persona-conditioned generation; the current work extends this idea by conditioning LLMs on demographic/persona profiles to instantiate multiple distinct ‘participants’ in Turing Experiments.

---

## Synthesis

The paper’s core innovation—the Turing Experiment (TE)—sits at the intersection of classic evaluation of human-likeness and recent demonstrations that language models can emulate population-level patterns. Turing’s foundational proposal of the Turing Test provided the conceptual bedrock for evaluating human-like behavior; the present work directly addresses its limitation (a single arbitrary interlocutor) by elevating evaluation to representative samples via TEs. Argyle et al. showed that LLMs can simulate demographic subgroups for surveys, motivating the authors to formalize a principled methodology for sampling and evaluating simulated ‘participants’ beyond opinion surveys and into controlled behavioral paradigms. Persona-Chat’s persona conditioning is operationally extended here to instantiate many distinct participant profiles, enabling the multi-human simulation central to TEs. To ground and validate the TE methodology, the paper leverages seminal human-subjects paradigms: the Ultimatum Game (Güth et al.) for economic bargaining norms, garden-path sentence processing (Frazier & Rayner) for psycholinguistic processing difficulty, Milgram’s obedience study for social psychology, and Galton’s wisdom-of-crowds for aggregation effects. These canonical studies supply the precise behavioral regularities the TE aims to replicate, while also exposing LLM-specific distortions (e.g., hyper-accuracy in aggregation). Together, these works directly shaped the paper’s problem formulation, methodological design for multi-persona sampling, and the choice of benchmark phenomena that demonstrate both successes and systematic deviations in LLM-based human simulation.

---
*Generated: 2026-01-06T23:09:26.514777*
