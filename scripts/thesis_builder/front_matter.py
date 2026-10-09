"""Front Matter Module for Honours Thesis.
Conforms strictly to NSBM Faculty of Computing Guidelines (Appendices I - VII).
"""

CONTENT = """<div align="center">

# [Appendix – I: Cover page]

# AN INTELLIGENT FINANCIAL STRESS DETECTION SYSTEM USING USER SPENDING BEHAVIOR

<br/>
<br/>
<br/>

### GAMAGE SASINI UDESHIKA

<br/>

### Bachelor of Science (Honours) in Software Engineering

<br/>
<br/>
<br/>
<br/>

### Department of Software Engineering
### Faculty of Computing
### NSBM Green University Town
### Sri Lanka

<br/>

### September 2026

</div>

<div style='page-break-after: always;'></div>

---

<div align="center">

# [Appendix – II: Inner Title Page]

# AN INTELLIGENT FINANCIAL STRESS DETECTION SYSTEM USING USER SPENDING BEHAVIOR

<br/>

### A thesis submitted to NSBM Green University for the degree of
### Bachelor of Science (Honours) in Software Engineering

<br/>
<br/>

### By

<br/>

### GAMAGE SASINI UDESHIKA
### Student ID: 29108

<br/>
<br/>
<br/>

### Department of Software Engineering
### Faculty of Computing
### NSBM Green University Town
### Sri Lanka

<br/>

### September 2026

</div>

<div style='page-break-after: always;'></div>

---

# [Appendix – III: Declaration]

## DECLARATION

I declare that the content of this undergraduate thesis titled **"An Intelligent Financial Stress Detection System Using User Spending Behavior"** is my own work and this dissertation does not incorporate without acknowledgement any material previously submitted for any other degree in any university or institution of higher learning.

<br/>
<br/>

Signature: ...............................................................  
**Gamage Sasini Udeshika**  
Date: 15th November 2026  

<br/>
<br/>

Signature of the Supervisors:  
...............................................................  
**Mr. Gayan Perera**  
Principal Supervisor  
Senior Lecturer  
Department of Software Engineering  
Faculty of Computing  
NSBM Green University Town  
Date: 10th September 2026  

<div style='page-break-after: always;'></div>

---

## SUPERVISOR CERTIFICATION

I certify that **Gamage Sasini Udeshika** has carried out this research dissertation under my direct supervision and guidance in the Faculty of Computing, NSBM Green University Town. The work submitted satisfies the required standards for the degree of Bachelor of Science (Honours) in Software Engineering and is recommended for academic examination.

<br/>
<br/>

...............................................................  
**Mr. Gayan Perera**  
Senior Lecturer / Research Supervisor  
Faculty of Computing, NSBM Green University Town  
Date: 10th September 2026  

<div style='page-break-after: always;'></div>

---

## DEDICATION

*To my beloved parents and family, whose unconditional love, endless sacrifices, and unwavering faith have been my greatest pillars of strength.*

*To all individuals striving quietly against economic hardships, seeking clarity, peace of mind, and financial dignity in an increasingly complex world.*

<div style='page-break-after: always;'></div>

---

## ACKNOWLEDGEMENTS

I wish to express my deepest and most sincere gratitude to my supervisor, **Mr. Gayan Perera**, Senior Lecturer in the Faculty of Computing, NSBM Green University Town. His invaluable academic guidance, constructive critique, and patient mentorship throughout every phase of this research provided the intellectual rigor necessary to bring this project to fruition.

I extend my heartfelt appreciation to **Ms. Dulanjali Wijesekara**, Lecturer and Academic Coordinator, whose detailed thesis syllabus breakdown and comprehensive guidelines served as the architectural blueprint for the structuring and execution of this dissertation.

I would also like to thank the distinguished academic and administrative staff of the Faculty of Computing at NSBM Green University Town and our partner institution, the University of Plymouth, UK, for equipping me with the theoretical foundation, analytical capabilities, and software engineering competencies required to tackle real-world technological challenges.

My profound thanks go to my fellow undergraduate peers, colleagues, and friends for their camaraderie, continuous encouragement, and insightful discussions during collaborative development sessions.

Finally, I owe everything to my family. Their quiet patience, constant prayers, and unending support have made this academic journey possible.

<div style='page-break-after: always;'></div>

---

## ABSTRACT

Personal financial distress represents a pervasive socioeconomic vulnerability that exerts profound psychological, social, and physical strain on individuals, families, and communities. Contemporary personal finance management (PFM) applications and digital banking dashboards operate almost universally under a reactive, descriptive paradigm: they capture transactions, categorize historical outlays, and alert users only after overdraft fees have been levied or monthly budgets have been breached. Furthermore, conventional heuristic rules—such as presuming that solvency is preserved as long as total expenditure remains strictly below total monthly income ($E < I$)—fail to detect latent, compounding financial fragility driven by debt servicing burdens, collapsing savings cushions, acute discretionary creep, and volatile transaction frequency.

To bridge this critical operational and academic gap, this dissertation presents "Financial Weather", an intelligent, explainable, and privacy-preserving financial stress detection software system that diagnoses individual financial strain directly from granular spending behavior. Rooted within the Peffers et al. Design Science Research Methodology (DSRM) and framed under an empirical-pragmatist paradigm, the research develops an automated machine learning and behavioral feature engineering pipeline. The system constructs a comprehensive 35-variable behavioral feature space—including seven newly engineered behavioral ratios: spending-to-income ratio, savings ratio, debt-to-income ratio, discretionary spending ratio, essential spending ratio, subscription burden, and spending volatility ratio.

A benchmark dataset of 2,500 user profiles was synthesized via a latent factor model incorporating a Beta(2,3) distribution calibrated to established behavioral finance literature. Target stress classes (Low, Moderate, High) were mapped using sample-independent psychometric thresholds derived from the Consumer Financial Protection Bureau (CFPB) Financial Well-Being Scale (≥70 Low, 40–69 Moderate, <40 High). Five supervised classification algorithms—Logistic Regression, Support Vector Machine (SVM with RBF kernel), Random Forest, Extreme Gradient Boosting (XGBoost), and Decision Tree—were trained and evaluated on a held-out test split under 5-fold cross-validation. While SVM achieved the highest raw F1-macro score (0.776), Multinomial Logistic Regression was selected as the optimal production engine, attaining an F1-macro of 0.765, high-stress recall of 0.690, and the highest One-vs-Rest macro ROC-AUC (0.915) across all candidates, while providing a 60-fold inference speed advantage (~1.4 ms vs. ~84.0 ms) and native mathematical compatibility with linear Shapley Additive Explanations (SHAP).

The machine learning core was embedded into a production-grade asynchronous FastAPI backend and coupled with a client-side user interface featuring an innovative, non-stigmatizing "Financial Weather" metaphor (Clear, Changeable, Stormy). Every classification is paired with a local SHAP explanation identifying the top three influential behavioral drivers and non-prescriptive, gentle awareness nudges. The complete software artifact was verified through a rigorous 66-test automated pytest suite spanning unit mathematics, Pydantic validation, and end-to-end integration, accompanied by strict stateless privacy guarantees where zero user financial data is persisted. The resulting system demonstrates that multi-factor behavioral spending patterns provide decisive predictive signals for proactive financial stress detection, charting a viable path forward for human-centered FinTech decision support.

**Keywords**: Machine Learning, Personal Finance Management, Financial Stress Detection, Behavioral Economics, Feature Engineering, Explainable AI (SHAP), FastAPI, Software Engineering.

<div style='page-break-after: always;'></div>

---

# [Appendix – IV: Table of Contents]

## TABLE OF CONTENTS

- **Cover Page**
- **Inner Title Page**
- **Declaration**
- **Supervisor Certification**
- **Dedication**
- **Acknowledgements**
- **Abstract**
- **Table of Contents**
- **List of Figures**
- **List of Tables**
- **List of Abbreviations**

### **1 INTRODUCTION**
- 1.1 Chapter Overview
- 1.2 Background: The Socioeconomic Landscape of Financial Fragility and Cashless Digital Spending
- 1.3 Problem Statement
  - 1.3.1 General Problem Implication
  - 1.3.2 Specific Problem & Domain-Specific Shortcomings
- 1.4 Research Gap
- 1.5 Research Question or Hypotheses
  - 1.5.1 Primary Research Question
  - 1.5.2 Sub-Questions
  - 1.5.3 Operational Hypotheses
- 1.6 Research Motivation and Significance
  - 1.6.1 Personal Observation and Societal Need
  - 1.6.2 Software Engineering and Applied Machine Learning Challenge
  - 1.6.3 Ethical AI and Non-Stigmatizing Design
- 1.7 Scope
  - 1.7.1 Scope Boundary Matrix (In-Scope vs. Out-of-Scope Capabilities)
  - 1.7.2 In-Scope Capability Elaboration
  - 1.7.3 Deliberate Technical Exclusions
- 1.8 Overview of the Proposed Solution
  - 1.8.1 The "Financial Weather" Metaphor
  - 1.8.2 High-Level Solution Workflow and Rich Picture
- 1.9 Chapter Summary

### **2 OBJECTIVES**
- 2.1 General Objective or Aim
- 2.2 Specific Objectives
  - 2.2.1 Objective 1: Identify Spending Behavior Characteristics Associated with Financial Stress
  - 2.2.2 Objective 2: Collect and Construct a Standardized Behavioral Dataset
  - 2.2.3 Objective 3: Preprocess Data and Engineer Robust Behavioral Ratios
  - 2.2.4 Objective 4: Develop, Evaluate, and Compare Multi-Class Machine Learning Models
  - 2.2.5 Objective 5: Implement Explainable AI (XAI) for Transparent Inference
  - 2.2.6 Objective 6: Design and Deploy a Stateless, Non-Stigmatizing Software Prototype
  - 2.2.7 Objective 7: Empirically Validate System Usability, Performance, and Security
  - 2.2.8 Objectives Triangulation Framework
- 2.3 Chapter Summary

### **3 LITERATURE REVIEW**
- 3.1 Chapter Overview
- 3.2 Domain Concepts and Theories
  - 3.2.1 Conceptual Map of the Literature and Theoretical Pillars
  - 3.2.2 Behavioral Economics and Bounded Rationality
  - 3.2.3 Mental Accounting and Payment Decoupling
  - 3.2.4 Psychometric Formulations of Financial Well-Being (CFPB and APR Scales)
- 3.3 Existing Studies, Systems or Frameworks
  - 3.3.1 Study 1: CFPB Financial Well-Being Scale and Continuous Construct Modeling
  - 3.3.2 Study 2: APR Financial Stress Scale (Heo, Cho, & Lee)
  - 3.3.3 Study 3: The WONGA Intelligent Personal Finance Management System
  - 3.3.4 Study 4: Smart Spend Predictive Budgeting and Anomaly Detection
  - 3.3.5 Study 5: Impulsive and Compulsive Spending Patterns in Consumer Well-Being
  - 3.3.6 Study 6: Cashless E-Wallet Dynamics, Financial Literacy, and Youth Stress
  - 3.3.7 Study 7: Multimodal Behavioral Modeling for Personal Financial Distress
  - 3.3.8 Critical Synthesis Matrix and Personal Reflection
- 3.4 Technical Approaches
  - 3.4.1 Algorithmic Paradigms for Tabular Financial Classification
  - 3.4.2 Architectural Design Patterns
  - 3.4.3 Data Pipeline and Explainability Workflows
- 3.5 Research Gap and Implications for Your Work
  - 3.5.1 Synthesis of the Six Compounding Research Gaps
  - 3.5.2 Implications for Software Architecture and Machine Learning Design
  - 3.5.3 Consolidated Research Gap Statement
- 3.6 Chapter Summary

### **4 METHODOLOGY**
- 4.1 Research Design
  - 4.1.1 Research Paradigm Justification: Pragmatism and Positivism
  - 4.1.2 Deductive Reasoning and Quantitative Investigation
  - 4.1.3 Design Science Research (DSR) Strategy and the Four Artifact Dimensions
  - 4.1.4 Peffers DSRM Execution Workflow Across the Six Stages
- 4.2 Data, Participants or Stakeholders
  - 4.2.1 Stakeholder Analysis and Value Matrix
  - 4.2.2 Primary Data Collection Instrument Design (Questionnaire Schema)
  - 4.2.3 Justification for Synthetic Benchmark Dataset Generation
  - 4.2.4 Latent Factor Model Formulation: Beta(2,3) Distribution and Log-Normal Income
  - 4.2.5 Calibrated Stochastic Feature Generation and Noise Injection
  - 4.2.6 Establishing Ground-Truth Target Labels Using CFPB Psychometric Bands
  - 4.2.7 Data Transparency and Rigor
- 4.3 Requirements and Analysis
  - 4.3.1 Operationalization Process: Mapping Behavioral Inputs to Research Variables
  - 4.3.2 Requirements Engineering and Validation Process
  - 4.3.3 Formal Functional Requirements Specification (FR-01 to FR-08)
  - 4.3.4 Formal Non-Functional Requirements Specification (NFR-01 to NFR-05)
- 4.4 Proposed Design
  - 4.4.1 Dual-Pipeline System Architecture (Offline Training vs. Live Inference)
  - 4.4.2 UML Use Case Modeling and Formal Specifications (UC-01 to UC-08, Detailed UC-04)
  - 4.4.3 UML Structural Class Diagram
  - 4.4.4 UML Dynamic Activity Diagram
  - 4.4.5 UML Sequence Modeling
  - 4.4.6 UML Physical Deployment Diagram
- 4.5 Development or Implementation Procedure (My Step-by-Step Engineering Journey)
  - 4.5.1 Data Cleaning, Validation, and Outlier Handling: Deciding to Flag Rather than Discard
  - 4.5.2 Behavioral Feature Engineering: Deriving the 7 Core Financial Ratios and Handling Division-by-Zero Exceptions
  - 4.5.3 Preventing Catastrophic Data Leakage and Scaling Continuous Features
  - 4.5.4 Machine Learning Model Experiments, Training Pipeline, and Failed Attempts
    - 4.5.4.1 Attempt 1: Unregularized Decision Tree (CART) and Why It Failed
    - 4.5.4.2 Attempt 2: Support Vector Machine (RBF Kernel) and Why It Was Rejected for Live Deployment
    - 4.5.4.3 Attempt 3: Random Forest Ensemble
    - 4.5.4.4 Attempt 4: Extreme Gradient Boosting (XGBoost)
    - 4.5.4.5 Attempt 5: Multinomial Logistic Regression (L2 Regularized) and Why It Succeeded
  - 4.5.5 Production Model Selection Rationale and Engineering Trade-Offs
  - 4.5.6 Real-Time Explainable AI Implementation: Developing the Linear SHAP Engine
  - 4.5.7 Engineering the Contextual Gentle Awareness Suggestion Rule Engine
  - 4.5.8 Developing the Full-Stack Web Application: FastAPI Backend, Pydantic v2 Schema Guarding, Vanilla JS, Three.js Atmospheres, and Accessible Static SVG Fallback
- 4.6 Evaluation Plan
  - 4.6.1 Master Test Strategy and Verification Framework
  - 4.6.2 Formal Functional and Non-Functional Test Cases (TC-01 to TC-10)
  - 4.6.3 5-Fold Stratified Cross-Validation Protocol
  - 4.6.4 Held-Out Test Set Partitioning (80/20 Stratified Split)
  - 4.6.5 Selection and Mathematical Definition of Evaluation Metrics
- 4.7 Ethics and Project Management
  - 4.7.1 Project Management Framework: Agile Scrum Methodology
  - 4.7.2 Sprint Timeline, Task Decomposition, and Gantt Chart Analysis
  - 4.7.3 Ethical Guardrails: GDPR Compliance, Absolute Statelessness, and Responsible Non-Diagnostic Framing
- 4.8 Chapter Summary

### **5 RESULTS**
- 5.1 Chapter Overview
- 5.2 Final Data or Evaluation Setting
  - 5.2.1 Benchmark Dataset Profile, Feature Count, and Class Distributions
  - 5.2.2 Experimental Computing Environment and Software Toolchain
- 5.3 Developed Artefact or Analytical Outputs
  - 5.3.1 Grouped Web Input Form Interface
  - 5.3.2 Classification Visual States: Stormy, Changeable, and Clear
  - 5.3.3 Accessibility Mode and Static SVG Iconography
  - 5.3.4 Serialized Model Artifacts and Verification Metadata
- 5.4 Functional and Nonfunctional Test Results
  - 5.4.1 Comprehensive 66-Test Automated Pytest Execution Results
  - 5.4.2 Pydantic Schema Validation and Input Boundary Fuzzing Outcomes
  - 5.4.3 Sub-2 Millisecond Latency Benchmarking Results
- 5.5 Evaluation and Comparison (Empirical Machine Learning Benchmark)
  - 5.5.1 Master Model Benchmark Table on Held-Out Test Set
  - 5.5.2 Granular Per-Class Performance Comparison Across Candidate Models
  - 5.5.3 5-Fold Stratified Cross-Validation Consistency Benchmark
  - 5.5.4 Multi-Model Confusion Matrix Heatmap Analysis and Spillover Inspection
  - 5.5.5 One-vs-Rest Macro ROC Curves and Discriminative Sensitivity
  - 5.5.6 Global Standardized Feature Importance Rankings (Top 20 Predictors)
  - 5.5.7 Local Feature Attribution Analysis via SHAP Summary Beeswarm Plot
- 5.6 Results by Objective
  - 5.6.1 Objective 1: Spending Behavior Characteristics Associated with Stress
  - 5.6.2 Objective 2: Standardized Behavioral Dataset Construction
  - 5.6.3 Objective 3: Data Preprocessing and Feature Engineering
  - 5.6.4 Objective 4: Machine Learning Model Development and Benchmarking
  - 5.6.5 Objective 5: Explainable AI (XAI) Implementation
  - 5.6.6 Objective 6: Stateless, Non-Stigmatizing Software Prototype
  - 5.6.7 Objective 7: Empirical Usability, Performance, and Security Validation
- 5.7 Chapter Summary

### **6 DISCUSSION AND CONCLUSIONS**
- 6.1 Discussion of Key Findings
  - 6.1.1 The Dominance of Behavioral Ratios over Absolute Income
  - 6.1.2 The Primacy of Regular Savings Efficacy and Debt Burden
  - 6.1.3 The Surprising Efficacy of Regularized Linear Models on Tabular Ratio Spaces
  - 6.1.4 Critical Analysis of Algorithmic Failures: Decision Tree Overfitting and SVM Latency Penalties
  - 6.1.5 Reconciling High-Stress Recall with False Alarm Moderation
- 6.2 Comparison with Literature
  - 6.2.1 Convergence with Empirical Findings (CFPB, Heo et al., Hasin & Zainol, Kee et al.)
  - 6.2.2 Divergence from Traditional Personal Finance Tooling (WONGA, Smart Spend)
  - 6.2.3 Systematic Resolution of the Six Identified Research Gaps
- 6.3 Contribution and Practical Implications
  - 6.3.1 Academic and Theoretical Contributions
  - 6.3.2 Methodological and Technical Contributions
  - 6.3.3 Software Engineering and Architectural Contributions
  - 6.3.4 Practical and Societal Implications
  - 6.3.5 Commercial Viability and Industry Application Avenues
- 6.4 Limitations
  - 6.4.1 Reliance on Synthetic Latent Factor Benchmark Data
  - 6.4.2 Cross-Sectional Snapshot vs. Longitudinal Time-Series Dynamics
  - 6.4.3 Self-Reporting Biases and Questionnaire Fatigue
  - 6.4.4 Static Psychometric Thresholding Assumptions
  - 6.4.5 Absence of Long-Term Clinical Validation
- 6.5 Conclusions
  - 6.5.1 Direct Evidence-Based Resolution of the Primary Research Question
  - 6.5.2 Synthesis of Sub-Question Findings
  - 6.5.3 Final Dissertation Synthesis
- 6.6 Future Work
  - 6.6.1 Live Open Banking API Integration and Longitudinal Streaming
  - 6.6.2 Privacy-Preserving On-Device Federated Learning
  - 6.6.3 Longitudinal Randomized Controlled Trials (RCT) for Behavioral Interventions
  - 6.6.4 Dynamic Reinforcement Learning for Adaptive Financial Nudges

### **REFERENCES**

### **APPENDICES**
- Appendix A: Psychometric Mapping and Questionnaire Schema
- Appendix B: Synthetic Dataset Data Dictionary and Generation Parameters
- Appendix C: Comprehensive 66-Test Pytest Execution Log

<div style='page-break-after: always;'></div>

---

# [Appendix – V: List of Figures]

## LIST OF FIGURES

- Figure 1.1: Rich Picture of Personal Financial Stress Ecosystem and Solution Workflows
- Figure 3.1: Conceptual Map of Literature and Theoretical Pillars
- Figure 4.1: Peffers et al. Design Science Research Methodology (DSRM) Framework
- Figure 4.2: UML Use Case Diagram for Intelligent Financial Stress Detection
- Figure 4.3: UML Structural Class Diagram
- Figure 4.4: UML Dynamic Activity Diagram for Financial Stress Assessment Workflow
- Figure 4.5: Sequence Diagram 1 — End-to-End Prediction and UI Rendering Workflow
- Figure 4.6: Sequence Diagram 2 — Dynamic Feature Transformation Pipeline
- Figure 4.7: Sequence Diagram 3 — SHAP Linear Attribution and Guidance Synthesis
- Figure 4.8: UML Physical Deployment Diagram
- Figure 4.9: Dual-Pipeline System Architecture (Offline Training and Live Inference)
- Figure 4.10: Project Milestone Schedule and Execution Timeline (Gantt Chart)
- Figure 5.1: Web Interface Input Form Grouped Layout
- Figure 5.2: Stormy (High Stress) Classification State with Confidence Breakdown
- Figure 5.3: Changeable (Moderate Stress) Classification State
- Figure 5.4: Clear (Low Stress) Classification State
- Figure 5.5: Accessibility Floor and Static SVG Fallback for Reduced Motion
- Figure 5.6: Multi-Model Confusion Matrix Heatmaps on 500-Instance Held-Out Test Set
- Figure 5.7: One-vs-Rest Macro ROC Curves Across 5 Evaluated Models
- Figure 5.8: Logistic Regression Standardized Feature Importance (Top 20 Predictors)
- Figure 5.9: SHAP Summary Beeswarm Plot for High-Stress Class

<div style='page-break-after: always;'></div>

---

# [Appendix – VI: List of Tables]

## LIST OF TABLES

- Table 1.1: System Scope Boundary Matrix (In-Scope vs. Out-of-Scope Capabilities)
- Table 1.2: Hardware Resources and Operational Specifications
- Table 1.3: Software Frameworks and Toolchain Configuration
- Table 2.1: Specific Research Objectives Mapped to Methodology and Anticipated Results
- Table 3.1: Comparative Evaluation Matrix of Existing Financial Management and Stress Models
- Table 4.1: DSRM Research Execution Matrix Mapped to Project Milestones
- Table 4.2: Stakeholder Analysis and Value Realization Matrix
- Table 4.3: Operationalization Mapping of Behavioral Inputs to Research Variables
- Table 4.4: Functional Requirements Specification Matrix
- Table 4.5: Non-Functional Requirements Specification Matrix
- Table 4.6: Formal Use Case Specifications for Core System Interactions
- Table 4.7: Engineered Behavioral Ratios and Mathematical Formulations
- Table 4.8: Technology Stack Comparative Justification Matrix
- Table 4.9: Contextual Gentle Awareness Suggestion Mapping Rules
- Table 4.10: Master Test Plan and Formal Test Case Specifications
- Table 4.11: Agile Scrum Sprint Decomposition and Deliverables
- Table 5.1: Benchmark Dataset Class Distribution and Partitioning Breakdown
- Table 5.2: Master Model Evaluation Benchmark on Held-Out Test Set (N=500)
- Table 5.3: Granular Per-Class Performance Breakdown Across Candidate Models
- Table 5.4: 5-Fold Stratified Cross-Validation Consistency Benchmark
- Table 5.5: Real-Time Inference and Explanation Latency Benchmark
- Table 5.6: Empirical Triangulation Matrix Mapped to Research Objectives
- Table 6.1: Synthesis of Research Findings Against Existing Literature

<div style='page-break-after: always;'></div>

---

# [Appendix – VII: List of Abbreviations]

## LIST OF ABBREVIATIONS

| Abbreviation | Full Name / Description |
|---|---|
| **API** | Application Programming Interface |
| **ASGI** | Asynchronous Server Gateway Interface |
| **BNPL** | Buy-Now-Pay-Later |
| **CART** | Classification and Regression Trees |
| **CFPB** | Consumer Financial Protection Bureau |
| **CPU** | Central Processing Unit |
| **CSV** | Comma-Separated Values |
| **DSR** | Design Science Research |
| **DSRM** | Design Science Research Methodology |
| **DTO** | Data Transfer Object |
| **F1** | Harmonic Mean of Precision and Recall |
| **FR** | Functional Requirement |
| **GDPR** | General Data Protection Regulation |
| **GPU** | Graphics Processing Unit |
| **HCI** | Human-Computer Interaction |
| **HTML** | HyperText Markup Language |
| **HTTP** | Hypertext Transfer Protocol |
| **IQR** | Interquartile Range |
| **IRT** | Item Response Theory |
| **JSON** | JavaScript Object Notation |
| **LKR** | Sri Lankan Rupee |
| **LLM** | Large Language Model |
| **ML** | Machine Learning |
| **NFC** | Near-Field Communication |
| **NFR** | Non-Functional Requirement |
| **NLP** | Natural Language Processing |
| **NVMe** | Non-Volatile Memory Express |
| **OCR** | Optical Character Recognition |
| **PFM** | Personal Finance Management |
| **PII** | Personally Identifiable Information |
| **RAM** | Random Access Memory |
| **RBF** | Radial Basis Function |
| **REST** | Representational State Transfer |
| **ROC-AUC** | Receiver Operating Characteristic - Area Under the Curve |
| **RQ** | Research Question |
| **SHAP** | Shapley Additive Explanations |
| **SRS** | System Requirement Specification |
| **SSD** | Solid State Drive |
| **SVG** | Scalable Vector Graphics |
| **SVM** | Support Vector Machine |
| **TDD** | Test-Driven Development |
| **UI** | User Interface |
| **UML** | Unified Modeling Language |
| **WCAG** | Web Content Accessibility Guidelines |
| **WHO** | World Health Organization |
| **XAI** | Explainable Artificial Intelligence |
| **XGBoost** | Extreme Gradient Boosting |
"""
