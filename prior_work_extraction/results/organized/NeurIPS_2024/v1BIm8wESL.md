# Prior Work Analysis Report

## Target Paper
**Title:** v1BIm8wESL
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

MeshRet’s core innovation—retargeting by directly perceiving and leveraging dense geometric interactions—emerges at the intersection of three lines of prior work. First, skeleton-centric motion retargeting, exemplified by Neural Kinematic Networks (Villegas et al., 2018), demonstrated that learning to map kinematics across bodies is feasible but often suffers from foot-skate, interpenetration, and contact mismatch because geometry is treated post hoc. Second, classical and learning-based motion generation with built-in contact reasoning, notably Contact-Invariant Optimization (Mordatch et al., 2012), argued that contact must be modeled jointly with motion; this principle directly motivates MeshRet’s end-to-end formulation where geometry interaction is not a correction but a driver of retargeting. Third, dense, per-vertex interaction representations such as POSA (2020) showed that contacts and near-contacts can be encoded on meshes, suggesting that a spatio-temporal field over mesh points can capture rich interaction cues; MeshRet’s Dense Mesh Interaction (DMI) field generalizes this idea to capture both contact and non-contact interactions over time for retargeting.
To make dense interaction reasoning transferable across varied character topologies, MeshRet builds on cross-shape correspondence advances: deep template-based matching from 3D-CODED (2018) and the topology-agnostic principles of Functional Maps (2012) inform its Semantically Consistent Sensors (SCS) that anchor comparable surface locations across meshes. Finally, SMPL (2015) underpins the notion of skinned, semantically indexed meshes, providing a practical canvas for per-vertex signals. Together, these works directly inform MeshRet’s key contribution: a retargeting framework that aligns meshes via SCS and optimizes motion using a DMI field to maintain faithful, contact-consistent geometry interactions.

---
*Generated: 2026-01-07T00:02:04.756740*
