# Prior Work Analysis Report

## Target Paper

**Title:** Vision Language Models are In-Context Value Learners

**Conference:** ICLR 2025 (spotlight)

**Authors:** Yecheng Jason Ma, Joey Hejna, Chuyuan Fu, Dhruv Shah, Jacky Liang, Zhuo Xu, Sean Kirmani, Peng Xu, Danny Driess, Ted Xiao, Osbert Bastani, Dinesh Jayaraman, Wenhao Yu, Tingnan Zhang, Dorsa Sadigh, Fei Xia

**Keywords:** robot learning, vision-language model, value estimation, manipulation

**Abstract:** 
> Predicting temporal progress from visual trajectories is important for intelligent robots that can learn, adapt, and improve. However, learning such progress estimator, or temporal value function, across different tasks and domains requires both a large amount of diverse data and methods which can scale and generalize. To address these challenges, we present Generative Value Learning (GVL), a universal value function estimator that leverages the world knowledge embedded in vision-language models...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Universal Value Function Approximators** (2015)
- *Authors:* Tom Schaul et al.
- *Direct Connection:* GVL adopts the UVFA perspective of predicting a single value function across many tasks/goals and generalizes it by conditioning value estimates on open-vocabulary visual-linguistic context via a VLM.

**Deep Reinforcement Learning from Human Preferences** (2017)
- *Authors:* Paul F. Christiano et al.
- *Direct Connection:* GVL replaces the human preference annotator with a VLM that orders shuffled frames to produce pairwise progress preferences, turning those judgments into a scalar value signal without manual labels.

### 💡 Inspiration

**Shuffle and Learn: Unsupervised Learning using Temporal Order Verification** (2016)
- *Authors:* Ishan Misra et al.
- *Direct Connection:* GVL borrows the key insight that predicting temporal order over shuffled frames induces temporal reasoning, adapting this idea to prompt a VLM to sort frames by perceived task progress and then map the inferred order to values.

### 🔍 Gap Identification

**Time-Contrastive Networks: Self-Supervised Learning from Video** (2018)
- *Authors:* Pierre Sermanet et al.
- *Direct Connection:* Progress-from-video methods like TCN learn phase/progress via temporal proximity but require large, domain-specific training; GVL targets the same progress signal while avoiding task-specific training by leveraging VLM world knowledge through in-context ordering.

### 🔧 Extension

**Extrapolating Beyond Suboptimal Demonstrations via Inverse Reinforcement Learning from Observations (T-REX)** (2019)
- *Authors:* Daniel S. Brown et al.
- *Direct Connection:* Like T-REX, GVL casts reward/value learning as trajectory ranking based on temporal order, but extends it by using a VLM to infer semantic progress orderings rather than relying only on within-trajectory timestamps and in-domain training.

### 🔗 Related Problem

**Do As I Can, Not As I Say: Grounding Language in Robotic Affordances (SayCan)** (2022)
- *Authors:* Michael Ahn et al.
- *Direct Connection:* SayCan showed foundation models can score feasibility to guide robots; GVL analogously uses a foundation model to score visual task progress, but at the trajectory level to produce a value function rather than action feasibility.

---

## Synthesis: How Prior Work Led to This Paper

Universal Value Function Approximators established that a single value function can generalize across goals by conditioning on context, motivating methods that estimate progress across diverse tasks. Preference-based reinforcement learning demonstrated a practical route to value signals via pairwise comparisons, showing that scalar rewards can be inferred from judgments over trajectory snippets rather than explicit numeric labels. Trajectory-ranked reward extrapolation (T-REX) pushed this further by converting the temporal order inherent in demonstrations into ranked comparisons to learn rewards that extrapolate, highlighting temporal ordering as a powerful supervisory signal. Complementing these ideas, Shuffle and Learn showed that verifying temporal order of shuffled frames forces models to capture temporal dynamics instead of exploiting short-range correlations. Time-Contrastive Networks learned phase/progress-like embeddings from video using temporal proximity, but required sizable, task-specific video collections to train robustly. Meanwhile, SayCan revealed that foundation models’ world knowledge can meaningfully score or prioritize options for robots, hinting that such models might also assess notions of task progress.
Together, these works suggested a gap: progress/value estimation benefits from temporal ordering and preferences, yet existing approaches either need human labels or large in-domain video training and struggle to generalize broadly. Leveraging the demonstrated evaluative power and world knowledge of foundation models, the current work synthesizes these insights by prompting a VLM to sort shuffled frames—sidestepping temporal shortcutting—then converting those rank-based judgments into a universal progress value. This unifies UVFA’s generality with preference/ranking supervision while eliminating domain-specific training, yielding a scalable, cross-task value estimator.

---

*Analysis generated on: 2026-01-06T07:50:25.407669*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
