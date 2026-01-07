# Prior Work Analysis Report

## Target Paper

**Title:** Grounding Video Models to Actions through Goal Conditioned Exploration

**Conference:** ICLR 2025 (spotlight)

**Authors:** Yunhao Luo, Yilun Du

**Keywords:** Embodied AI, Decision Making, Robotics, Video Model

**Abstract:** 
> Large video models, pretrained on massive quantities of amount of Internet video,  provide a rich source of physical knowledge about the dynamics and motions of objects and tasks.
However, video models are not grounded in the embodiment of an agent, and do not describe how to actuate the world to reach the visual states depicted in a video.
To tackle this problem, current methods use a separate vision-based inverse dynamic model trained on embodiment-specific data to map image states to actions....

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Reinforcement Learning with Imagined Goals** (2018)
- *Authors:* Ashvin Nair et al.
- *Direct Connection:* RIG introduced using a generative model to sample visual goals for goal-conditioned learning and exploration, a principle this paper adopts by sourcing those goals from a pretrained internet-scale video model.

**Hindsight Experience Replay** (2017)
- *Authors:* Marcin Andrychowicz et al.
- *Direct Connection:* HER established the goal-conditioned RL formulation and relabeling mechanism, which underpins learning from self-exploration episodes when pursuing video-specified visual goals.

### 💡 Inspiration

**Skew-Fit: State-Covering Self-Supervised Reinforcement Learning** (2019)
- *Authors:* Vitchyr Pong et al.
- *Direct Connection:* Skew-Fit showed that biasing goal sampling toward underrepresented states expands exploration coverage, motivating the paper’s use of video-generated goals to drive coverage beyond the agent’s initial embodiment data.

### 🔍 Gap Identification

**Video PreTraining (VPT): Learning to Act by Watching Unlabeled Online Videos** (2022)
- *Authors:* Bowen Baker et al.
- *Direct Connection:* VPT operationalizes learning from internet videos via a vision-based inverse dynamics model trained with embodiment-specific labels, whose data demands and embodiment dependence are precisely the limitations this paper removes by replacing inverse-dynamics labeling with goal-conditioned self-exploration.

### 🔧 Extension

**Diffuser: Diffusion Models for Offline Reinforcement Learning** (2022)
- *Authors:* Michael Janner et al.
- *Direct Connection:* Diffuser demonstrated trajectory-level action generation via diffusion conditioned on goals, which this paper extends by conditioning trajectory generation on video-guided visual goals to directly ground video to continuous actions.

### 🔗 Related Problem

**Visual Foresight: Deep Predictive Models for Planning in Robotic Manipulation** (2018)
- *Authors:* Frederik Ebert et al.
- *Direct Connection:* Visual Foresight showed that predicting future visual states can guide control toward goal images, informing this paper’s use of generated video states as guidance targets for action generation.

---

## Synthesis: How Prior Work Led to This Paper

Learning from internet videos has been catalyzed by methods that infer actions from pixels, with VPT showing at scale that a vision-based inverse dynamics model can convert raw videos into training signals—while incurring the costs and brittleness of embodiment-specific labeling. In parallel, goal-conditioned frameworks matured: HER introduced relabeling and the formalism of conditioning on goals, and RIG showed a powerful twist—sampling imagined visual goals from a generative model to both drive exploration and supervise goal-reaching, laying a template for leveraging generative targets rather than explicit action labels. Skew-Fit refined this direction by biasing goal sampling toward undercovered states to widen exploration. On the control side, Visual Foresight established that predicting or specifying future images can guide visuomotor behavior by matching to desired visual states. More recently, Diffuser demonstrated that diffusion models can generate coherent action trajectories conditioned on goals, making trajectory-level control a practical mechanism for goal-directed behavior.

Together these works reveal a gap and an opportunity: inverse-dynamics labeling from videos is expensive and tied to embodiments, while goal-conditioned exploration and trajectory-level generators can learn to reach visual targets without explicit action labels. The present paper synthesizes these strands by using internet video models to produce plausible future visual goals and coupling them with trajectory-level action generation, enabling an agent to self-explore and directly ground video knowledge into continuous actions—eliminating embodiment-specific inverse dynamics while leveraging generative goals to expand coverage.

---

*Analysis generated on: 2026-01-06T19:37:22.141652*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
