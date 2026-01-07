# Prior Work Analysis Report

## Target Paper
**Title:** 8rKSfL3GsK
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Learning to Recognize Daily Actions using Gaze** (2012)
- *Authors:* Fathi et al.
- *Connection:* Established egocentric gaze as a direct signal of intention in first-person activities, providing the foundational link our paper leverages when forecasting the next locus of visual perception.

**Ego4D: Around the World in 3,000 Hours of Egocentric Video** (2022)
- *Authors:* Grauman et al.
- *Connection:* Defined large-scale egocentric forecasting tasks and provided head/gaze signals; our work targets the same predictive setting but grounds forecasts in reconstructed 3D environments.

### 💡 Inspiration

**A Simple Yet Effective Baseline for 3D Human Pose Estimation** (2017)
- *Authors:* Martinez et al.
- *Connection:* Popularized learning a 2D-to-3D ‘lifting’ function; EgoSpanLift adapts this lifting paradigm from 2D image-plane attention cues to 3D volumetric visual span forecasting.

### 🔍 Gap Identification

**EGTEA Gaze+: A Large-Scale Dataset for Gaze Tracking in Egocentric Video** (2018)
- *Authors:* Li et al.
- *Connection:* Standardized 2D, image-plane gaze prediction for egocentric video, whose lack of 3D scene grounding directly motivates our shift to forecasting gaze as volumetric regions in 3D.

### 📊 Baseline

**Predicting Gaze in Egocentric Video by Learning Task-Dependent Attention Transition** (2018)
- *Authors:* Huang et al.
- *Connection:* Introduced temporal modeling of gaze transitions in egocentric videos; we adopt this forecasting formulation but replace 2D heatmaps with 3D visual span volumes fused by a unidirectional transformer.

### 🔧 Extension

**ORB-SLAM2: An Open-Source SLAM System for Monocular, Stereo and RGB-D Cameras** (2017)
- *Authors:* Mur-Artal et al.
- *Connection:* Provides the SLAM keypoints and map points that our method explicitly converts into gaze-compatible 3D geometry, enabling extraction of volumetric visual span regions.

### 🔗 Related Problem

**Gaze360: Physically Unconstrained Gaze Estimation in the Wild** (2019)
- *Authors:* Kellnhofer et al.
- *Connection:* Framed gaze as 3D rays in world coordinates; we adopt this 3D geometric perspective but advance it to forecast future volumetric spans anchored in reconstructed scenes rather than static 3D gaze estimation.

---

## Synthesis

EgoSpanLift’s core innovation—forecasting egocentric visual span as volumetric regions grounded in a reconstructed 3D scene—rests on a clear lineage. Foundationally, Fathi et al. demonstrated that egocentric gaze is tightly coupled with intention, motivating prediction of where attention will move next. Large-scale egocentric benchmarks such as EGTEA Gaze+ and Ego4D then codified 2D gaze prediction/forecasting protocols and data, but their inherently image-plane formulations exposed a key gap: forecasts lack 3D scene grounding. On the temporal modeling side, Huang et al. established a now-standard baseline for egocentric gaze forecasting via attention transition in 2D, which our method retains conceptually while lifting the target to 3D and fusing spatio-temporal context with a unidirectional transformer. Enabling this lift, ORB-SLAM2 supplies the geometric substrate—sparse keypoints and map points—that EgoSpanLift explicitly converts into gaze-compatible 3D primitives, from which we extract volumetric visual span regions. Two additional threads directly inspire our design choices: the 2D-to-3D ‘lifting’ paradigm of Martinez et al. provides the methodological blueprint for mapping image-plane signals into structured 3D representations, while Gaze360’s 3D gaze ray formulation anchors our representation of gaze in world coordinates. Together, these works define the problem, expose the 2D limitation our paper addresses, and provide the geometric and methodological tools that make 3D visual span forecasting feasible.

---
*Generated: 2026-01-06T23:08:23.949829*
