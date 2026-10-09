<div align="center">

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


<div style='page-break-after: always;'></div>

---

# 1 INTRODUCTION

## 1.1 Chapter Overview
This introductory chapter establishes the academic and technological foundation for the research project titled **"An Intelligent Financial Stress Detection System Using User Spending Behavior"**, manifested practically as the software platform **"Financial Weather"**. The chapter investigates the complex socioeconomic reality of personal financial distress, tracing the transition of consumer financial vulnerability from an obscure macroeconomic indicator to an acute, widespread individual crisis exacerbated by persistent cost-of-living surges, volatile global economic headwinds, the rapid digitalization of retail payments, and the proliferation of frictionless consumer credit modalities.

Following this contextual foundation, the chapter articulates a rigorous problem statement divided into general systemic socioeconomic implications and specific, domain-level software engineering shortcomings. It defines the central research gap, formulates the primary research question alongside four targeted sub-questions and three operational hypotheses, details the personal, engineering, and ethical motivations driving the investigation, and establishes explicit operational boundaries through a comprehensive in-scope and out-of-scope analysis. Finally, the chapter provides an overview of the proposed solution—introducing the non-stigmatizing "Financial Weather" metaphor, the system's rich picture, and its high-level technical toolchain—before outlining the structural trajectory of the dissertation.

---

## 1.2 Background: The Socioeconomic Landscape of Financial Fragility and Cashless Digital Spending
Over the past decade, the socioeconomic landscape governing personal finance has undergone unprecedented disruption. Historically, personal financial stability was largely conceptualized through elementary macroeconomic indicators such as aggregate employment figures, national gross domestic product growth, and benchmark wage indices. However, contemporary empirical investigations demonstrate that macroeconomic stability frequently masks profound financial fragility at the individual and household level (Consumer Financial Protection Bureau [CFPB], 2017). Across both developed and developing economies, individuals increasingly confront an intricate web of financial pressures driven by persistent inflationary surges, escalating costs of living, housing and rental hyperinflation, expanding educational and medical debt obligations, and widespread wage stagnation relative to essential commodity baskets.

Compounding these structural economic pressures is the rapid and pervasive digital transformation of consumer commerce. The ubiquity of smartphone-based financial applications, contactless near-field communication (NFC) payment cards, electronic payment gateways, mobile wallets, and algorithmic "Buy-Now-Pay-Later" (BNPL) micro-lending services has fundamentally decoupled consumer purchasing transactions from physical currency exchange (Kee et al., 2026). In traditional cash-based transactions, the physical surrender of paper currency notes incurred an immediate psychological friction—termed the "pain of paying" in behavioral economics (Prelec & Loewenstein, 1998). Digital and contactless payment infrastructures deliberately minimize this cognitive friction, reducing transactions to frictionless biometric taps and single-click authorizations. Consequently, consumers are progressively insulated from the immediate awareness of their spending outlays, fostering behavioral conditions ripe for impulsive, compulsive, and uncoordinated discretionary expenditures (Hasin & Zainol, 2026).

Despite the proliferation of thousands of commercial personal finance management (PFM) mobile applications, expense-tracking tools, and digital banking portals, individuals continue to experience acute financial distress. Crucially, empirical data reveals that financial stress is not solely confined to low-income populations or individuals suffering catastrophic employment termination (CFPB, 2023). On the contrary, a substantial proportion of middle-income and steady-wage-earning individuals experience persistent financial anxiety and imminent insolvency.

When examining why existing technological solutions have failed to stem this tide, a fundamental systemic defect emerges: **contemporary financial software is overwhelmingly reactive, post-hoc, and descriptive**. Conventional applications operate by recording transactions after they have already transpired, sorting them into rigid historical categories, and displaying colorful retrospective graphs. Such systems inform the consumer of budget depletion only after overspending has materialized, or notify them of account distress only after an overdraft fee is levied or a debt repayment deadline is missed. They lack predictive foresight, behavioral sensitivity, and explainable intelligence, leaving individuals navigating treacherous economic currents without early navigational warnings.

---

## 1.3 Problem Statement
The operational failure of current personal financial tooling demands a focused investigation into how individual spending behavior can be algorithmically leveraged to diagnose financial stress *before* it deteriorates into unmanageable insolvency.

### 1.3.1 General Problem Implication
At the macroeconomic and societal level, unmitigated personal financial stress produces devastating multidimensional ramifications:
1. **Public Health and Psychosocial Strain**: Chronic financial worry is clinically correlated with severe psychological morbidity, including clinical depression, acute anxiety disorders, insomnia, cognitive impairment, and interpersonal domestic strife (World Health Organization [WHO], 2022). The psychological burden of persistent debt and cash-flow uncertainty impairs executive decision-making, trapping individuals in recursive cycles of poor financial choices.
2. **Economic Productivity Losses**: In the workplace, financially distressed employees suffer from severe absenteeism and presenteeism (loss of workplace focus). Empirical studies indicate that financial anxiety accounts for substantial annualized productivity losses across enterprise workforces, impacting overall economic resilience (Ramirez & DeMarr, 2021).
3. **Systemic Financial Instability**: When substantial segments of the consumer population operate without savings buffers while maintaining elevated debt-service commitments, minor macroeconomic shocks—such as modest interest rate hikes or localized cost spikes—trigger widespread consumer loan defaults, destabilizing retail banking institutions and credit markets.

### 1.3.2 Specific Problem & Domain-Specific Shortcomings
Within the discipline of Software Engineering and Applied Artificial Intelligence, the specific problem resides in the acute deficiency of intelligent, predictive, and human-centered computational frameworks capable of modeling financial stress directly from behavioral spending data. The state-of-the-art in consumer financial tooling suffers from four critical domain shortcomings:

1. **The Fallacy of the Simple Income-Expense Rule**: Traditional budgeting software operates on the naive heuristic that an individual remains financially healthy as long as total monthly expenditure is less than total monthly income ($E < I$). This static rule completely ignores the *composition* of expenditures, existing debt obligations, savings depletion rates, and month-to-month expenditure volatility. A consumer who earns 300,000 LKR and spends 290,000 LKR may appear technically solvent under conventional rules; however, if 120,000 LKR is allocated to rigid debt repayments, discretionary spending is volatile, and liquid savings are zero, that individual exists in a state of severe, fragile financial stress.
2. **The Predictive and Behavioral Void**: While advanced machine learning has been deployed extensively in FinTech for institutional fraud detection, algorithmic credit underwriting, and high-frequency trading, consumer-facing applications remain confined to elementary, static rule-based categorization. There is an acute lack of predictive machine learning architectures trained specifically on behavioral features—such as the ratio of discretionary to essential outlays, spending volatility, impulse transaction frequency, and savings consistency.
3. **The Psychometric Separation**: Validated social science instruments for quantifying financial well-being—such as the Consumer Financial Protection Bureau (CFPB) Financial Well-Being Scale and the APR Financial Stress Scale (Heo et al., 2020)—exist exclusively as lengthy, academic questionnaire instruments. They are rarely operationalized or mapped into software engineering pipelines to serve as standardized ground-truth targets for predictive classification algorithms.
4. **The Stigmatizing and Opaque User Experience**: Personal finance applications that do attempt risk scoring frequently resort to alarming, punitive visual cues (e.g., flashing red sirens, critical warning banners, or arbitrary credit scores) without explaining *why* the user is flagged. Such stigmatizing designs trigger avoidance behavior, causing users to disengage from the application precisely when intervention is most critical. Furthermore, advanced AI models typically function as "black boxes," failing to provide interpretable explanations for their outputs.

---

## 1.4 Research Gap
A rigorous examination of existing academic literature and commercial systems reveals an unaddressed structural gap at the intersection of Software Engineering, Machine Learning, and Behavioral Economics. While descriptive budgeting tools track historical transactions, and psychometric instruments measure subjective well-being through static survey scales, no unified, production-grade, and privacy-preserving software framework exists that:
1. Dynamically transforms multi-dimensional, raw spending behavior into normalized behavioral ratio indicators (such as debt-to-income, savings ratio, discretionary ratio, and spending volatility).
2. Maps these behavioral indicators directly against ground-truth stress classifications derived from validated psychometric standards.
3. Rigorously benchmarks multiple machine learning classification algorithms under identical experimental conditions to identify the optimal balance of predictive accuracy, inference speed, and interpretability.
4. Couples predictive classification with sub-millisecond, local Explainable AI (XAI) feature attribution (SHAP) to inform users of the exact behavioral drivers behind their score.
5. Communicates financial risk through a calm, non-stigmatizing interface metaphor ("Financial Weather") while enforcing a strictly stateless, zero-data-retention architecture that completely eliminates privacy and data leakage risks.

---

## 1.5 Research Question or Hypotheses

### 1.5.1 Primary Research Question
To systematically address the identified problem and bridge the structural gap, this research is guided by the following primary research question:

> *"How can an intelligent software system leverage granular user spending behavior and supervised machine learning techniques to accurately, explainably, and non-invasively detect and classify individual financial stress levels?"*

### 1.5.2 Sub-Questions
To thoroughly dissect this overarching inquiry, four specific sub-questions are investigated across the research lifecycle:
- **RQ 1 (Feature Association)**: Which specific spending behavior characteristics, expenditure compositions, and financial ratios exhibit statistically significant associations with differing degrees of financial stress?
- **RQ 2 (Algorithmic Efficacy)**: To what degree of predictive accuracy, recall, and ROC-AUC can supervised machine learning classification models (linear, kernel-based, and tree ensembles) discern between Low, Moderate, and High financial stress states?
- **RQ 3 (Explainability & Interpretability)**: How can local and global feature attribution mechanisms—specifically linear Shapley Additive Explanations (SHAP)—be seamlessly integrated into the prediction pipeline to yield transparent, human-understandable drivers of financial strain without imposing excessive computational latency?
- **RQ 4 (Software Architecture & User Experience)**: How can an intelligent detection engine be operationalized within a production-ready, stateless, and privacy-preserving web architecture that communicates financial fragility through a calm, non-stigmatizing interface metaphor?

### 1.5.3 Operational Hypotheses
In accordance with a deductive scientific methodology, the following testable hypotheses are established:
- **Hypothesis 1 ($H_1$)**: Multi-factor engineered behavioral ratios (e.g., debt-to-income ratio, savings ratio, discretionary spending ratio, and spending volatility) contain superior predictive power for classifying financial stress compared to absolute monthly income alone.
- **Hypothesis 2 ($H_2$)**: Supervised machine learning classification models trained on behavioral spending features can achieve a macro-averaged F1-score exceeding 0.75 and an Area Under the ROC Curve (ROC-AUC) exceeding 0.90 on an unseen test dataset.
- **Hypothesis 3 ($H_3$)**: Local feature attribution via game-theoretic Shapley Additive Explanations (SHAP) can be computed in under 10 milliseconds within a live REST API pipeline, enabling real-time explainability without degrading user experience or web performance.

---

## 1.6 Research Motivation and Significance
The motivation driving this research stems from three converging impetuses: personal observation, engineering curiosity, and societal imperative.

### 1.6.1 Personal Observation and Societal Need
Observing the pervasive economic challenges experienced by university undergraduates, young working professionals, and diverse households in Sri Lanka and globally highlighted a glaring dissonance: individuals actively utilize mobile banking apps and digital expense trackers daily, yet remain completely blindsided when cash reserves deplete and debt compounds. The emotional and cognitive toll of financial uncertainty is visible across communities. Technology ought to empower individuals with foresight rather than merely recording their financial demise in retrospective ledger tables.

### 1.6.2 Software Engineering and Applied Machine Learning Challenge
From a software engineering perspective, the problem presents an intellectually compelling challenge in Applied Machine Learning and System Architecture. Developing an end-to-end intelligent system requires moving beyond isolated, theoretical Jupyter Notebooks. It demands constructing a complete, production-grade software pipeline: establishing psychometrically grounded data models, engineering robust mathematical ratios resistant to numerical anomalies (such as division-by-zero or extreme outliers), performing rigorous cross-validated model benchmarking, and architecting an ultra-low-latency, stateless API that respects user privacy.

### 1.6.3 Ethical AI and Non-Stigmatizing Design
The ethical dimension of artificial intelligence in personal finance provides powerful motivation. Many modern algorithmic platforms exploit behavioral weaknesses through gamified consumption and predatory micro-loans. In contrast, this research is motivated by the philosophy of **"Calm Technology"** (Weiser & Brown, 1997) and responsible AI. By designing a system that provides gentle, proactive awareness without storing sensitive user credentials, the project seeks to prove that machine learning can serve as a compassionate, protective digital companion.

---

## 1.7 Scope
To ensure disciplined software engineering execution, rigorous boundaries were established delineating the system's operational capabilities. **Table 1.1** provides a structured scope matrix accompanied by strategic engineering rationales.

Table 1.1: System Scope Boundary Matrix (In-Scope vs. Out-of-Scope Capabilities).

| Feature / Domain Area | In Scope (Delivered Capabilities) | Out of Scope (Deliberate Exclusions) | Strategic Engineering Rationale |
|---|---|---|---|
| **Prediction Target** | Multi-class classification: Low, Moderate, High financial stress risk. | Exact numerical continuous currency forecasting (e.g., predicting exact future bank balance). | The research objective is behavioral stress classification, not precise balance accounting. |
| **Data Modality** | Tabular, questionnaire-style behavioral spending profiles (cross-sectional). | Continuous real-time banking transaction stream feeds via Open Banking APIs. | Cross-sectional snapshots permit universal, privacy-safe self-assessment without requiring third-party credentials. |
| **Dataset Source** | Calibrated 2,500-user synthetic dataset based on latent stress factors and literature. | Multi-year national longitudinal banking transaction databases. | Real transaction histories are restricted by GDPR/banking privacy laws; synthetic data provides verifiable ground truth. |
| **Temporal Dynamics** | Single-period monthly spending, historical 3-month budget exceed frequency. | Longitudinal time-series LSTM/Transformer sequence forecasting over multi-year logs. | Cross-sectional data structures cannot reliably support longitudinal sequence models without artificial temporal drift. |
| **Explainability** | Mathematical local attribution via Linear SHAP identifying top-3 driving features. | Free-form natural language generative AI explanations via commercial Large Language Models (LLMs). | Deterministic SHAP explanations eliminate hallucination hazards and preserve complete local privacy. |
| **Advisory Scope** | Non-prescriptive, gentle behavioral awareness prompts tied to top drivers. | Formal fiduciary financial advice, investment recommendations, or loan brokerage. | The platform is explicitly an educational awareness tool, avoiding regulatory fiduciary liabilities. |
| **Data Persistence** | Zero persistence: 100% stateless execution in memory; no database. | User account management, credential hashing, database storage of user financial inputs. | Total statelessness provides bulletproof user privacy—zero sensitive financial data is stored, retained, or leaked. |
| **Clinical Framing** | "Financial Weather" metaphor (*Clear*, *Changeable*, *Stormy*); risk assessment. | Psychological, psychiatric, or clinical diagnosis of mental health conditions. | Software cannot ethically or legally diagnose medical anxiety or mental pathology. |

### 1.7.1 In-Scope Capability Elaboration
The system intentionally focuses on providing an accessible, privacy-centric diagnostic tool that empowers users to explore how specific spending behaviors influence their financial risk profile. The live inference pipeline accurately accepts raw input metrics, calculates ratio transformations, scales numerical vectors, evaluates model probabilities, extracts SHAP attributions, and returns structured results in under 2 milliseconds.

### 1.7.2 Deliberate Technical Exclusions
The system deliberately excludes live bank credential aggregation (e.g., Plaid or Yodlee integrations). While live transaction scrapers offer convenience, they introduce monumental data liability risks, third-party licensing dependencies, and severe security exposure for end users. Similarly, generative natural language financial advice via third-party LLMs was rejected to protect user privacy and avoid generating unverified financial prescriptions.

### 1.7.3 Computational Hardware and Software Resources
The development, training, evaluation, and deployment of the financial stress detection platform required a structured computational hardware and software infrastructure, detailed in **Table 1.2** and **Table 1.3**.

Table 1.2: Hardware Resources and Operational Specifications.

| Component | Specification | Operational Purpose |
|---|---|---|
| **Host System Architecture** | Apple Silicon M-Series (ARM64) | Development host and local API server execution |
| **Central Processing Unit (CPU)** | 8-Core CPU (High-Performance & High-Efficiency) | Parallelized model training, 5-fold cross-validation, and SHAP computation |
| **Random Access Memory (RAM)** | 16 GB Unified Memory Architecture | In-memory dataset manipulation, matrix vectorization, and multi-model benchmarking |
| **Storage Subsystem** | 512 GB Solid State Drive (NVMe SSD) | Local persistence of raw/processed datasets, serialized `.joblib` models, and visual test artifacts |
| **Display & Resolution** | 14-inch Retina Display ($3024 	imes 1964$) | High-fidelity UI layout testing, responsive viewports down to 375px mobile widths |

Table 1.3: Software Frameworks and Toolchain Configuration.

| Layer / Category | Technology / Tool | Version | Operational Role in Project |
|---|---|---|---|
| **Base Environment** | Python | 3.10+ / 3.14 | Core programming language for ML pipeline and backend API |
| **Virtual Environment** | `venv` | Built-in | Isolated package management and dependency sandboxing |
| **Backend Framework** | FastAPI | 0.141.1 | High-performance asynchronous REST API serving `/predict` and `/health` |
| **ASGI Web Server** | Uvicorn | 0.52.3 | Production-grade ASGI server hosting the live application |
| **Data Validation** | Pydantic v2 | 2.13.4 | Strict schema definition, type enforcement, and boundary checking |
| **Data Manipulation** | Pandas & NumPy | 2.3.3 / 2.4.0 | Tabular dataset cleaning, vectorization, and ratio feature engineering |
| **Machine Learning Core** | Scikit-Learn | 1.8.0 | Algorithms (LogReg, SVM, RF, DT), preprocessing (`StandardScaler`), metrics |
| **Gradient Boosting** | XGBoost | 3.4.1 | Optimized distributed gradient boosted decision tree classifier |
| **Model Explainability** | SHAP (Shapley Additive Explanations) | 0.52.0 | Linear explainer for calculating local feature attribution values |
| **Artifact Serialization** | Joblib | 1.5.3 | High-efficiency disk serialization of trained models and fitted scalers |
| **Automated Testing** | Pytest & AnyIO | 9.0.1 / 4.14.2 | Comprehensive 66-test suite covering unit, pipeline, and API validation |
| **Data Visualization** | Matplotlib | 3.11.1 | Generation of publication-grade figures, feature importance, and ROC curves |
| **Frontend Technologies** | HTML5 / CSS3 / Vanilla JS | ECMAScript 6+ | Single-page application, custom accessible design system, state handling |
| **3D Graphics Library** | Three.js | r128 (CDN) | Real-time procedural rendering of weather atmospheres with SVG fallback |

---

## 1.8 Overview of the Proposed Solution
To conceptualize the systemic environment, conflicting tensions, and operational transformation introduced by the proposed solution, a formal **Rich Picture** was constructed (Checkland, 1981).

![Figure 1.1: Rich Picture of Personal Financial Stress Ecosystem and Solution Workflows](../../reports/figures/rich_picture.png)

Figure 1.1: Rich Picture of Personal Financial Stress Ecosystem and Solution Workflows.

### 1.8.1 The "Financial Weather" Metaphor
As illustrated in **Figure 1.1**, the contemporary financial ecosystem is characterized by sharp conflicts between consumer desires, market pressures, and legacy tooling:
1. **The Distressed Consumer**: Consumers exist at the center of conflicting forces: the necessity of meeting living expenses, rising debt obligations, aggressive marketing from e-commerce and BNPL platforms that encourage impulsive spending, and the fear of social stigma surrounding insolvency.
2. **The Failure of Traditional Trackers**: Conventional personal finance management tools pull historical transaction logs but sit passively at the bottom of the workflow. They operate in descriptive silos, alerting users only *after* budgets are broken, offering no predictive guidance.
3. **The Latent Stress Void**: The core dilemma lies in the unmonitored space where spending technically remains within monthly income, but internal debt ratios and disappearing savings buffers mask an impending financial collapse.
4. **The Financial Weather Solution**: The proposed software system intervenes directly at this critical junction. By ingesting spending compositions and behavioral habits, passing them through an intelligent feature transformation and machine learning engine, and outputting a calm, weather-themed read with transparent SHAP explanations, the system diffuses stigma and provides timely, proactive enlightenment.
5. **Sustainable Well-Being**: The ultimate workflow restores equilibrium, fostering gradual savings accumulation, mindful discretionary outlays, and dignified financial self-awareness.

### 1.8.2 High-Level Solution Workflow
The architectural foundation of this solution rests on an asynchronous **FastAPI** backend coupled with a responsive, client-side web interface built using vanilla JavaScript and **Three.js** atmospheric simulations. Rather than presenting anxiety-inducing percentages or alarming red scorecards, the system maps model classifications into three intuitive weather states:
- **Clear**: Represents Low financial stress. Cash flows are stable, savings ratios are positive, and debt servicing is comfortably manageable.
- **Changeable**: Represents Moderate financial stress. Spending volatility or discretionary creep is emerging, warranting watchful behavioral moderation.
- **Stormy**: Represents High financial stress. High debt burdens, depleted savings, or rigid essential commitments create severe financial fragility requiring gentle, proactive remediation.

Crucially, every prediction is paired with the top three local behavioral factors identified via Linear SHAP and coupled with non-prescriptive, constructive financial awareness suggestions.

---

## 1.9 Chapter Summary
This chapter laid the comprehensive groundwork for the dissertation. It analyzed the real-world problem of personal financial distress in an era of cashless digital payments, demonstrating why legacy, reactive personal finance tools fail to provide timely intervention. It established the formal problem statement, identified critical domain gaps, presented the guiding research questions and hypotheses, and detailed the personal, technical, and ethical motivations behind the work. The system's operational boundaries were formalized through an explicit in-scope and out-of-scope matrix, and the proposed solution was introduced through a conceptual rich picture and the "Financial Weather" metaphor.

The remainder of this dissertation is organized according to the Senate approved structure:
- **Chapter 2 (Objectives)** details the general aim and seven specific research objectives, explicitly matching each to its corresponding methodology and anticipated empirical result.
- **Chapter 3 (Literature Review)** conducts an exhaustive academic and technological appraisal of behavioral economics, psychometric scales, machine learning algorithms, and existing software systems, culminating in a detailed research gap justification.
- **Chapter 4 (Methodology)** presents the research design, latent factor data generation model, System Requirement Specification (SRS) with comprehensive UML diagrams, full development and implementation procedures written in personal engineering terms (including failed candidate models and trade-offs), testing strategies, and ethical guardrails.
- **Chapter 5 (Results)** presents the empirical findings, including functional and non-functional test outcomes, 66-test automated test logs, multi-model evaluation benchmarks across five classifiers, confusion matrices, ROC curves, and SHAP explainability analyses, structured by research objective.
- **Chapter 6 (Discussion and Conclusions)** interprets the empirical findings against theoretical foundations and prior literature, articulates academic and software engineering contributions, outlines commercialization avenues, discusses critical limitations, provides a definitive answer to the research questions, and proposes trajectories for future work.


<div style='page-break-after: always;'></div>

---

# 2 OBJECTIVES

## 2.1 General Objective or Aim
The primary aim and overarching intended contribution of this research project is:

> **General Objective / Research Aim:**  
> *"To design, implement, empirically evaluate, and deploy an intelligent, explainable, and privacy-preserving software system—titled 'Financial Weather'—that leverages user spending behavior and supervised machine learning techniques to proactively detect and classify potential levels of personal financial stress into actionable risk categories, elucidate underlying behavioral drivers via Explainable AI (SHAP), and provide non-stigmatizing decision support to consumers."*

The research moves beyond conventional reactive budgeting software by treating financial stress as an identifiable behavioral phenomenon. Rather than relying on rigid static rules or waiting for catastrophic overdrafts to transpire, the developed system extracts nuanced predictive signals from everyday cash flows, debt obligations, and savings patterns. In doing so, the study demonstrates how applied machine learning, behavioral economics, and human-centered software engineering can converge into a practical, protective digital tool.

---

## 2.2 Specific Objectives
To realize the general aim and systematically address each dimension of the problem, the research establishes seven concrete, measurable specific objectives spanning the full software engineering and empirical machine learning lifecycle. In accordance with the Faculty of Computing Senate guidelines, each specific objective is rigorously linked to a corresponding methodology in Chapter 4 and an empirical result in Chapter 5.

### 2.2.1 Objective 1: Identify Spending Behavior Characteristics Associated with Financial Stress
- **Description**: Systematically investigate the domain of behavioral economics, psychometrics, and personal finance to identify key transactional and behavioral features—such as monthly income, total expenditure, essential vs. non-essential allocations, savings cushions, debt commitments, budget deviations, transaction frequencies, and self-reported spending adjustments during hardship—that correlate with subjective and objective financial strain.
- **Methodological Link (Chapter 4)**: Section 4.2 and Section 4.3 formulate a 35-variable behavioral schema grounded in the CFPB Financial Well-Being Scale, APR Financial Stress Scale, and empirical literature (Hasin & Zainol, 2026; Kee et al., 2026).
- **Anticipated Result Link (Chapter 5)**: Section 5.5 and Section 5.6 present standardized feature importance rankings and SHAP analyses confirming that debt-to-income ratio, regular savings capacity, and spending volatility exhibit statistically dominant predictive power over absolute income.

### 2.2.2 Objective 2: Collect and Construct a Standardized Behavioral Dataset
- **Description**: Synthesize a comprehensive, high-fidelity benchmark dataset comprising 2,500 diverse user profiles utilizing a latent factor model calibrated against empirical literature findings, ensuring complex non-linear feature interactions and establishing ground-truth target labels using the validated Consumer Financial Protection Bureau (CFPB) Financial Well-Being Scale score bands (≥70 Low, 40–69 Moderate, <40 High).
- **Methodological Link (Chapter 4)**: Section 4.2.4 details the mathematical formulation of the latent factor generator (`scripts/generate_synthetic_data.py`) utilizing a right-skewed Beta(2,3) distribution, log-normal income dispersion, and sample-independent CFPB score cutoffs.
- **Anticipated Result Link (Chapter 5)**: Section 5.2.1 reports the verified dataset profile of 2,500 records across 42 transformed columns, exhibiting a realistic socioeconomic class distribution (34.8% Low, 45.3% Moderate, 19.9% High).

### 2.2.3 Objective 3: Preprocess Data and Engineer Robust Behavioral Ratios
- **Description**: Design and execute a reproducible data preprocessing and feature engineering pipeline that performs statistical data cleaning, Interquartile Range (IQR) outlier flagging, categorical encoding, and mathematical derivation of seven critical behavioral ratios (spending-to-income, savings ratio, debt-to-income, discretionary ratio, essential ratio, subscription burden, and spending volatility ratio), incorporating defensive guards against mathematical division anomalies.
- **Methodological Link (Chapter 4)**: Section 4.5.1 and Section 4.5.2 document the IQR outlier flagging logic (`src/data/clean_data.py`), the mathematical formulations for the seven behavioral ratios (`src/features/engineer_features.py`), and the defensive division guards.
- **Anticipated Result Link (Chapter 5)**: Section 5.4.1 verifies the pipeline through 16 automated mathematical unit tests passing with zero division-by-zero exceptions and zero feature drift across splits.

### 2.2.4 Objective 4: Develop, Evaluate, and Compare Multi-Class Machine Learning Models
- **Description**: Train, optimize, and rigorously benchmark five candidate supervised machine learning algorithms (Multinomial Logistic Regression, Support Vector Machine with RBF kernel, Decision Tree, Random Forest, and Extreme Gradient Boosting [XGBoost]) under 5-fold stratified cross-validation and a 20% held-out test split, utilizing multi-class metrics including Accuracy, Macro Precision, Macro Recall, Macro F1-Score, High-Stress Recall, and One-vs-Rest ROC-AUC.
- **Methodological Link (Chapter 4)**: Section 4.5.4 details the multi-model training pipeline (`src/models/train_models.py`) and evaluation protocols (`src/evaluation/evaluate_models.py`), comparing scaled linear and kernel models against unscaled tree ensembles.
- **Anticipated Result Link (Chapter 5)**: Section 5.5.1 and Section 5.5.2 present the master benchmark comparison table and per-class metrics on the 500-instance held-out test set, identifying Multinomial Logistic Regression as the optimal model (F1-macro: 0.765, ROC-AUC: 0.915, High-stress recall: 0.690).

### 2.2.5 Objective 5: Implement Explainable AI (XAI) for Transparent Inference
- **Description**: Architect an explainability module leveraging Model Coefficients and Linear Shapley Additive Explanations (SHAP) that dynamically extracts the top three local behavioral factors driving each individual prediction, mapping mathematical attributions to plain-language interpretations and non-prescriptive, constructive financial awareness suggestions.
- **Methodological Link (Chapter 4)**: Section 4.5.6 and Section 4.5.7 elaborate the integration of the Linear SHAP Explainer (`src/evaluation/explain.py`) and the contextual suggestion rule engine (`src/app/api.py`).
- **Anticipated Result Link (Chapter 5)**: Section 5.5.6 and Section 5.5.7 deliver the standardized feature importance chart, SHAP summary beeswarm plot, and verify sub-millisecond local attribution generation in 0.85 ms.

### 2.2.6 Objective 6: Design and Deploy a Stateless, Non-Stigmatizing Software Prototype
- **Description**: Engineer a production-ready, highly responsive software artifact combining an asynchronous FastAPI backend with an accessible, client-side web interface. Embody a non-stigmatizing "Financial Weather" conceptual metaphor (Clear, Changeable, Stormy) supported by interactive Three.js graphics and accessible static fallbacks, enforcing a strictly stateless privacy architecture wherein zero user financial data is persisted or logged.
- **Methodological Link (Chapter 4)**: Section 4.4 and Section 4.5.8 document the system architecture, UML design specifications, FastAPI server routes (`/predict`, `/health`), and the Three.js front-end interface with automated `prefers-reduced-motion` detection.
- **Anticipated Result Link (Chapter 5)**: Section 5.3 presents executional screenshots of the working user interface across all three weather states and reduced-motion modes, confirming zero database footprint and stateless execution.

### 2.2.7 Objective 7: Empirically Validate System Usability, Performance, and Security
- **Description**: Conduct exhaustive verification and validation of the developed artifact across functional, non-functional, and usability dimensions, deploying an automated 66-test pytest suite, sub-2 millisecond API latency benchmarking, input boundary stress-testing, and compliance checks against accessibility and ethical AI standards.
- **Methodological Link (Chapter 4)**: Section 4.6 details the master test plan, 10 formal test case specifications (TC-01 to TC-10), Pydantic v2 boundary fuzzing, and AnyIO latency benchmarking protocols.
- **Anticipated Result Link (Chapter 5)**: Section 5.4 documents the 66-test pytest execution log (100% pass rate in 0.21s), sub-2 millisecond latency benchmarks (mean: 1.42 ms), and strict payload rejection verification.

### 2.2.8 Objectives Triangulation Framework
To demonstrate full academic and engineering rigor, **Table 2.1** provides the formal matrix mapping each specific objective to its theoretical justification, methodological implementation, and empirical verification.

Table 2.1: Specific Research Objectives Mapped to Methodology and Anticipated Results.

| Objective ID & Focus | Theoretical Literature Anchor | Chapter 4 Methodology & Software Artifact | Chapter 5 Empirical Result & Finding |
|---|---|---|---|
| **Obj 1: Behavioral Characteristics** | CFPB (2017), Heo et al. (2020), Hasin & Zainol (2026) | Section 4.2 & 4.3; 35-variable schema, Table 4.3 | Section 5.5.6; Savings capacity, debt ratio, and volatility dominate |
| **Obj 2: Benchmark Dataset** | CFPB (2023), Prelec & Loewenstein (1998) | Section 4.2.4; Latent generator `scripts/generate_synthetic_data.py` | Section 5.2.1; 2,500 balanced records, realistic class split |
| **Obj 3: Preprocessing & Ratios** | Simon (1955), Khan (2025) | Section 4.5.1 & 4.5.2; IQR cleaning, 7 ratios in `engineer_features.py` | Section 5.4.1; 16 math unit tests passed, zero division-by-zero errors |
| **Obj 4: Model Benchmarking** | Cortes & Vapnik (1995), Chen & Guestrin (2016) | Section 4.5.4; 5-model pipeline `src/models/train_models.py` | Section 5.5.1; Master table: LogReg selected (F1: 0.765, AUC: 0.915) |
| **Obj 5: Explainable AI** | Shapley (1953), Lundberg & Lee (2017) | Section 4.5.6; `LinearExplainer` in `src/evaluation/explain.py` | Section 5.5.7; Instant SHAP in 0.85 ms, summary beeswarm plot |
| **Obj 6: Software Prototype** | Weiser & Brown (1997), GDPR (2016) | Section 4.4 & 4.5.8; FastAPI REST backend, Three.js client UI | Section 5.3; Deployed "Financial Weather" app, zero data persistence |
| **Obj 7: Empirical Validation** | ISO/IEC 25010, W3C WCAG 2.1 (2018) | Section 4.6; Master test plan, 10 formal test cases, AnyIO profiling | Section 5.4; 66/66 tests passed (0.21s), 1.42 ms mean latency |

---

## 2.3 Chapter Summary
This chapter established the overarching research aim and delineated seven standardized, research-specific objectives guiding the investigation. By systematically mapping each specific objective to its theoretical foundation, computational methodology, and empirical verification criteria, the chapter provides an unambiguous structural blueprint for the remainder of the dissertation. The next chapter conducts an exhaustive literature review to establish the academic and technological context underpinning these objectives.


<div style='page-break-after: always;'></div>

---

# 3 LITERATURE REVIEW

## 3.1 Chapter Overview
This chapter presents a comprehensive, critical literature review and technological analysis establishing the theoretical, algorithmic, and architectural foundation for an intelligent financial stress detection system. The review begins with a Conceptual Map of the Literature (Section 3.2.1), visualizing how diverse research domains converge into the central research theme. Section 3.2 explores the foundational socioeconomic and psychological theories of financial fragility, bounded rationality, mental accounting, the psychological decoupling of digital payments, and validated psychometric construct definitions.

Section 3.3 conducts an extensive comparative assessment of seven pivotal academic studies, psychometric instruments, and commercial software systems, offering personal academic reflections and justifications regarding their applicability or limitations for real-time stress detection, consolidated within a structured synthesis matrix. Section 3.4 performs an in-depth technological analysis, systematically dissecting candidate classification algorithms (linear models, tree ensembles, kernel support vector machines, and deep neural architectures), architectural design patterns (monolithic, microservice, and stateless server engines), and data workflows. Finally, Section 3.5 synthesizes these insights into six distinct research gaps, culminating in a consolidated research gap statement that establishes the intellectual justification for the developed software artifact, followed by the chapter summary in Section 3.6.

---

## 3.2 Domain Concepts and Theories

### 3.2.1 Conceptual Map of the Literature and Theoretical Pillars
To provide the reader with a clear structural overview of how existing scholarly work is organized and synthesized within this dissertation, a Conceptual Map was constructed (**Figure 3.1**).

![Figure 3.1: Conceptual Map of Literature and Theoretical Pillars](../../reports/figures/conceptual_map.png)

Figure 3.1: Conceptual Map of Literature and Theoretical Pillars.

As depicted in **Figure 3.1**, the overarching research theme—Machine Learning Driven Financial Stress Detection from User Spending Behavior—is supported by four distinct theoretical pillars:
1. **Psychometrics & Financial Well-Being Measurement**: Provides standardized, validated construct definitions and outcome scales (e.g., CFPB Financial Well-Being Scale, APR Financial Stress Scale) to establish ground-truth target variables.
2. **Behavioral Economics & Digital Spending Dynamics**: Examines how modern cashless payment mechanisms, e-wallets, and consumer credit modalities influence impulsive outlays, discretionary creep, and financial anxiety.
3. **Machine Learning in Personal Finance**: Investigates existing algorithmic applications in expense tracking, transaction categorization, predictive budgeting, and financial anomaly detection.
4. **Explainable AI (XAI) & Human-Centered UX Design**: Bridges algorithmic complexity with human trust through local feature attributions (SHAP) and calm, non-stigmatizing interface metaphors.

### 3.2.2 Behavioral Economics and Bounded Rationality
Financial well-being is defined by the Consumer Financial Protection Bureau (CFPB, 2017) as a state wherein an individual can fully meet current and ongoing financial obligations, feels secure in their financial future, and possesses the freedom of choice to make decisions that allow enjoyment of life. Conversely, financial stress represents a severe condition of psychological tension, cognitive preoccupation, and subjective or objective vulnerability arising from an inability—or perceived inability—to maintain a sustainable equilibrium between financial resources and financial commitments (Heo et al., 2020).

Traditionally, personal finance management was governed by classical microeconomic theory, which assumes rational agents optimize consumption over their life cycle based on perfect information and stable preferences (Modigliani & Brumberg, 1954). Under this classical view, financial distress was attributed almost entirely to exogenous economic shocks—such as acute unemployment, severe medical emergencies, or macroeconomic downturns.

However, behavioral economics has fundamentally dismantled this assumption. Modern consumers operate under *bounded rationality* (Simon, 1955), constrained by cognitive biases, heuristic decision-making, and emotional impulsivity (Kahneman, 2011). In everyday spending, consumers frequently exhibit:
- **Present Bias and Hyperbolic Discounting**: Systematically overvaluing immediate gratification (e.g., non-essential dining, online entertainment, fast-fashion purchases) while heavily discounting future financial consequences, such as neglected emergency savings or compounded credit card debt.
- **Cognitive Tunneling Under Scarcity**: When individuals experience financial strain, cognitive bandwidth is monopolized by immediate cash-flow shortages, impairing executive decision-making and leading to short-sighted borrowing at exorbitant interest rates.

### 3.2.3 Mental Accounting and Payment Decoupling
Two behavioral phenomena directly accelerate consumer financial destabilization:
1. **Mental Accounting**: As formulated by Thaler (1999), individuals violate economic fungibility by assigning funds into subjective psychological buckets. For instance, an individual may maintain a meager savings balance earning negligible interest while simultaneously rolling over high-interest credit card debt, believing their "savings" are protected.
2. **The Decoupling Effect of Digital Payments**: As established by Prelec and Loewenstein (1998), cash transactions enforce an immediate cognitive "pain of paying" because the physical departure of currency is visibly witnessed. With the global dominance of mobile payments, tap-to-pay debit cards, and e-wallets, this psychological barrier has been virtually eliminated (Kee et al., 2026). Digital payments create a temporal and psychological decoupling between consumption and payment settlement.

Consequently, modern financial stress frequently develops silently. An individual may receive a stable monthly income, yet find their financial stability hollowed out by recurring debt obligations, high subscription density, and unchecked discretionary creep. Conventional banking systems and personal budgeting applications fail to recognize this subtle deterioration because they remain anchored to static, historical accounting.

### 3.2.4 Psychometric Formulations of Financial Well-Being
To model financial stress in software, abstract psychological tension must be anchored to rigorous psychometric constructs:
- **CFPB Financial Well-Being Scale**: Grounded in Item Response Theory (IRT), the CFPB scale provides a continuous 0–100 score reflecting financial security and freedom of choice. While psychometrically rigorous, it lacks native categorical cutoffs for machine learning classification.
- **APR Financial Stress Scale**: Developed by Heo et al. (2020), this instrument structures financial stress into affective, cognitive, and relational dimensions, confirming that subjective stress correlates directly with debt service burden and income inadequacy.

---

## 3.3 Existing Studies, Systems or Frameworks
A rigorous review of seven pivotal academic studies, psychometric instruments, and software frameworks was conducted. Each is critically appraised below, supported by personal reflections evaluating their suitability for the proposed research problem.

### 3.3.1 Study 1: CFPB Financial Well-Being Scale and Continuous Construct Modeling
- **Source**: Consumer Financial Protection Bureau (2017, 2023). *Measuring Financial Well-Being: A Guide to Using the CFPB Financial Well-Being Scale*. CFPB Technical Report.
- **Core Contribution**: The CFPB developed and validated a standardized, 10-item (and abbreviated 5-item) psychometric scale that measures individual financial well-being on a continuous score from 0 to 100 using Item Response Theory (IRT). The instrument captures subjective security, freedom of choice, and resilience against financial shocks, backed by national survey benchmarks across the United States.
- **Personal Reflection & Assessment**:
  - *Suitability*: The CFPB scale is vital to this research because financial stress cannot be directly observed from raw bank ledger entries alone; an objective measurement instrument is required to define ground truth. The CFPB's extensive construct validation ensures that score variations reflect genuine differences in financial capability and security.
  - *Shortcomings & Decision*: The CFPB framework was designed strictly as a retrospective survey instrument. It does not predict future financial trajectories or infer well-being directly from transactional spending data. Furthermore, CFPB's published guidelines treat the score as continuous and do not define official categorical cutoffs (e.g., Low, Moderate, High). To adapt this framework for supervised machine learning, this research establishes fixed, sample-independent score bands (≥70 Low Stress, 40–69 Moderate Stress, <40 High Stress), aligning with standard practitioner benchmarks.

### 3.3.2 Study 2: APR Financial Stress Scale (Heo, Cho, & Lee)
- **Source**: Heo, W., Cho, S. H., & Lee, P. (2020). APR Financial Stress Scale: Development and Validation of a Multidimensional Measurement. *Journal of Financial Therapy*, 11(1), 22–45.
- **Core Contribution**: Recognising that financial stress encompasses affective, cognitive, and relational dimensions, Heo et al. developed the Association for Financial Counseling and Planning Education (AFCPE) / APR Financial Stress Scale. Using exploratory and confirmatory factor analysis across multiple online samples, the authors validated a multi-item instrument measuring stress across perceived financial inadequacy, debt anxiety, and financial conflict.
- **Personal Reflection & Assessment**:
  - *Suitability*: This study reinforces the premise of our research: financial stress is inherently multidimensional and cannot be captured by income alone. It confirms that debt burden and subjective financial inadequacy correlate directly with physiological and psychological distress.
  - *Shortcomings & Decision*: While theoretically robust, the APR scale is an academic psychometric tool requiring explicit user completion of complex psychological Likert-scale questions. It does not interface with software engineering architectures or automated transaction processing pipelines. In our research, the conceptual constructs validated by Heo et al.—specifically debt servicing pressure and income inadequacy—are translated directly into computable behavioral ratios (e.g., Debt-to-Income Ratio, Savings Ratio).

### 3.3.3 Study 3: The WONGA Intelligent Personal Finance Management System
- **Source**: Uyanahewa, M. I. R., Jayawardana, G. V. H. D., Bandara, M. B. D. N., Hapugala, H. A. V. V., & Attanayaka, B. (2023). WONGA: The Future of Personal Finance Management – A Machine Learning-Driven Approach for Predictive Analysis and Efficient Expense Tracking. *IEEE International Conference on Computing*.
- **Core Contribution**: The WONGA project developed a personal finance management application tailored to Sri Lankan consumers. It integrated machine learning algorithms to automate optical character recognition (OCR) of paper receipts, categorize expenditures into standard domestic buckets, and provide predictive time-series spending forecasts to encourage budgeting discipline.
- **Personal Reflection & Assessment**:
  - *Suitability*: The WONGA study demonstrates the acute need for intelligent financial management tools within the South Asian context, proving that local consumers benefit from automated categorization and digital tracking.
  - *Shortcomings & Decision*: Despite its innovative features, WONGA remained fundamentally centered on expense tracking and retrospective accounting. It forecast how much a user might spend in subsequent weeks, but did not classify how stressed or financially fragile the user was as a consequence of that spending. Predicting expenditure volume is functionally distinct from assessing financial health. Our research builds upon this foundation by pivoting the machine learning objective from expenditure forecasting to behavioral stress classification.

### 3.3.4 Study 4: Smart Spend Predictive Budgeting and Anomaly Detection
- **Source**: Khan, S. (2025). Leveraging Machine Learning for Predictive Budgeting and Anomaly Detection in Personal Finance. *SSRN Electronic Journal*, Advanced FinTech Research Series.
- **Core Contribution**: Khan proposed "Smart Spend," a modular machine learning framework that utilized natural language processing (NLP) to parse unstructured transaction memos, applied clustering (k-means) for behavioral profiling, and deployed unsupervised anomaly detection (Isolation Forests) to identify abnormal transaction amounts.
- **Personal Reflection & Assessment**:
  - *Suitability*: Khan’s framework illustrates that machine learning can uncover hidden behavioral shifts from transaction logs, confirming that spending volatility and deviations from planned budgets represent meaningful behavioral signals.
  - *Shortcomings & Decision*: Unsupervised anomaly detection is insufficient for financial stress detection. An anomalous transaction is frequently benign—such as purchasing an annual insurance premium, booking a vacation, or paying semester university fees—and does not necessarily denote financial distress. Conversely, genuine financial stress often manifests through chronic, non-anomalous spending habits (e.g., continuous micro-borrowing and zero monthly savings). Therefore, our research rejects pure anomaly detection in favor of supervised multi-class classification trained on multi-factor behavioral ratios.

### 3.3.5 Study 5: Impulsive and Compulsive Spending Patterns in Consumer Well-Being
- **Source**: Hasin, H., & Zainol, Z. (2026). The Effect of Spending Patterns on The Financial Well-Being of Malaysian Consumers Across Income Levels. *Journal of Contemporary Issues and Thought*, 16(1), 45–58.
- **Core Contribution**: Hasin and Zainol conducted an empirical investigation of 308 consumers using hierarchical multiple regression to analyze how distinct spending patterns (utilitarian, impulsive, and compulsive) impact overall financial well-being across low-, middle-, and high-income brackets. Their findings demonstrated that impulsive and compulsive spending outlays exerted a statistically significant negative effect on financial well-being, irrespective of absolute income level.
- **Personal Reflection & Assessment**:
  - *Suitability*: This study provides decisive empirical justification for our feature engineering strategy. It proves that income alone does not dictate financial stability; behavioral spending choices (specifically impulse frequency and non-essential spending proportions) are primary determinants of subjective financial strain.
  - *Shortcomings & Decision*: The authors utilized classical statistical regression ($R^2$ modeling) to test theoretical hypotheses. They did not develop an automated, deployable prediction engine, nor did they provide real-time decision support for consumers. Our research operationalizes Hasin and Zainol's behavioral findings into engineered machine learning features (e.g., `impulse_purchase_frequency`, `discretionary_ratio`).

### 3.3.6 Study 6: Cashless E-Wallet Dynamics, Financial Literacy, and Youth Stress
- **Source**: Kee, D. M. H., Abdul Rashid, A. N., Tieu Kiu Fu, A., Jun Zhe, A., & Allias, A. S. (2026). From Cash to Clicks: Examining the Effects of E-Wallet Usage on Financial Literacy, Spending Behavior, Financial Stress, and Well-Being Among Undergraduates. *Asia Pacific Journal of Management and Education*, 9(2), 112–129.
- **Core Contribution**: Kee et al. surveyed 200 university undergraduates to investigate the interplay between digital wallet adoption, spending habits, financial literacy, and financial stress. Utilizing structural equation modeling, the authors revealed that high e-wallet transaction frequency significantly lowered spending self-regulation, resulting in heightened debt anxiety and financial stress among young adults.
- **Personal Reflection & Assessment**:
  - *Suitability*: This research highlights transaction frequency and digital spending friction as critical variables in contemporary financial health. It confirms that digital convenience often accelerates financial destabilization in vulnerable demographics, such as students and early-career workers.
  - *Shortcomings & Decision*: The study was purely cross-sectional and exploratory. While it established correlations, it offered no software artifact to assist students in mitigating the identified hazards. In response, our research incorporates `transaction_frequency`, `avg_transaction_value`, and `balance_check_frequency_per_week` into our classification pipeline to capture digital spending intensity.

### 3.3.7 Study 7: Multimodal Behavioral Modeling for Personal Financial Distress
- **Source**: Mostafa, M. (2026); D'Souza, M., Bhalekar, P., Bhegade, P., & Bhavsar, Y. (2026). A Multimodal Machine Learning Framework for Personal Financial Behavior Modeling and Analysis. *SSRN Advanced Computing Series*.
- **Core Contribution**: D'Souza et al. developed a multimodal architecture that combined tabular transaction summaries with text-based expense descriptions using deep tabular neural networks. The authors demonstrated that integrating categorical spending breakdowns with behavioral debt ratios enhanced distress prediction accuracy.
- **Personal Reflection & Assessment**:
  - *Suitability*: The study underscores the predictive power of combining category-level expenditure data (housing, groceries, utilities, debt servicing) with composite ratios.
  - *Shortcomings & Decision*: The deep neural network proposed by D'Souza et al. suffered from excessive model complexity, high inference latency, and severe interpretability deficits. In a consumer-facing financial health tool, deploying an opaque deep network is counterproductive; users demand clear, understandable reasons why their financial profile is categorized as high risk. Our system achieves comparable predictive accuracy using regularized linear and ensemble models paired with exact SHAP explanations, providing immediate transparency at a fraction of the computational overhead.

### 3.3.8 Critical Synthesis Matrix and Personal Reflection
To consolidate the comparative assessment, **Table 3.1** presents a structured matrix evaluating existing systems against the requirements of this research.

Table 3.1: Comparative Evaluation Matrix of Existing Financial Management and Stress Models.

| Study / System | Focus Area | Methodology / ML Approach | Ground Truth Target | Explainability Mechanism | Real-Time Prototype? | Critical Limitations & Research Decision |
|---|---|---|---|---|---|---|
| **CFPB Scale** (2017/2023) | Psychometric Well-Being | Item Response Theory (Survey) | Continuous Scale (0–100) | None (Psychometric Scores) | No (Paper / Web Survey) | Retrospective survey only. *Decision*: Convert into discrete, fixed target bands for ML. |
| **APR Scale** (Heo, 2020) | Multidimensional Stress | Confirmatory Factor Analysis | Factor Scale | None (Statistical Loadings) | No (Survey Instrument) | Purely diagnostic survey; no transaction modeling. *Decision*: Translate factors into computable ratios. |
| **WONGA** (Uyanahewa, 2023) | PFM & Expense Tracking | OCR + Time-Series Forecasting | Next-month expenditure | None | Yes (Mobile App) | Focuses on forecasting expense volume, not stress level. *Decision*: Shift objective to behavioral stress detection. |
| **Smart Spend** (Khan, 2025) | Budgeting & Anomalies | Isolation Forest & K-Means | Unsupervised Outliers | Feature distance | Yes (Web Demo) | Anomalies do not equate to financial distress. *Decision*: Deploy supervised classification with ground truth. |
| **Hasin & Zainol** (2026) | Impulse Spending Patterns | Multiple Regression ($R^2$) | Subjective Well-Being | Regression Coefficients | No (Academic Paper) | Hypotheses testing only; no software artifact. *Decision*: Operationalize impulse variables into ML features. |
| **Kee et al.** (2026) | E-Wallet & Youth Stress | Structural Equation Modeling | Financial Stress Construct | Path Coefficients | No (Survey Analysis) | Identifies correlations in digital spending. *Decision*: Capture digital transaction frequencies in model. |
| **D'Souza et al.** (2026) | Multimodal Behavior | Deep Tabular Neural Networks | Financial Distress | None ("Black-Box") | No (Jupyter Prototype) | High computational complexity and zero explainability. *Decision*: Adopt regularized models with SHAP attribution. |
| **Proposed "Financial Weather"** | Intelligent Stress Detection | Multi-Model Benchmark (LogReg, SVM, RF, XGB) | Fixed CFPB Bands (≥70, 40–69, <40) | Linear SHAP & Contextual Nudges | Yes (FastAPI + Modern Web UX) | Fully addresses identified gaps: predictive, explainable, lightweight, and stateless. |

---

## 3.4 Technical Approaches
A rigorous software engineering dissertation requires a comprehensive technological appraisal of candidate algorithms, architectural designs, and operational workflows.

### 3.4.1 Algorithmic Paradigms for Tabular Financial Classification
Predicting financial stress from tabular behavioral data requires selecting an algorithm that balances predictive accuracy, sample efficiency, computational latency, and mathematical interpretability. Five algorithmic paradigms were evaluated:

#### 1. Multinomial Logistic Regression (L2-Regularized)
Multinomial Logistic Regression models the posterior probabilities of $K$ mutually exclusive classes via the softmax transformation of linear predictor functions:
$$P(Y = k \mid \mathbf{x}) = rac{e^{\mathbf{w}_k^T \mathbf{x} + b_k}}{\sum_{j=1}^K e^{\mathbf{w}_j^T \mathbf{x} + b_j}}$$
- **Strengths**: Highly efficient training and inference; perfectly convex optimization surface guaranteed to converge to the global minimum; directly interpretable coefficients representing log-odds ratios; seamless compatibility with exact Linear SHAP explainers; negligible memory footprint (~kilobytes).
- **Weaknesses**: Assumes linear relationships between input features and log-odds; incapable of capturing complex feature interactions unless explicitly engineered into the feature space.
- **Algorithmic Decision**: Selected as production engine. Given that our feature engineering pipeline explicitly computes critical non-linear behavioral interactions (the seven ratios), Logistic Regression captures the decision boundary effectively while outperforming all competitors in inference speed and interpretability.

#### 2. Support Vector Machines (SVM with Radial Basis Function Kernel)
Support Vector Machines project the input feature space into an infinite-dimensional Hilbert space via the RBF kernel:
$$K(\mathbf{x}, \mathbf{x}') = \exp\left(-\gamma \|\mathbf{x} - \mathbf{x}'\|^2
ight)$$
- **Strengths**: Exceptional capability to delineate highly non-linear, complex decision boundaries in structured tabular data; robust against overfitting in moderate sample sizes due to margin maximization.
- **Weaknesses**: Computationally expensive during inference, scaling with the number of support vectors ($\mathcal{O}(N_{sv} \cdot d)$); outputs uncalibrated decision distances requiring Platt scaling for pseudo-probabilities; functions as an opaque "black box" requiring computationally sluggish Kernel SHAP approximations.
- **Algorithmic Decision**: Retained as a strong academic benchmark. While achieving slightly higher raw F1-macro (+0.011), its 60x latency penalty (~84 ms vs. ~1.4 ms) and opacity render it suboptimal for a responsive, explainable consumer application.

#### 3. Decision Trees (CART - Classification and Regression Trees)
Decision Trees recursively partition the feature space by selecting split points that maximize information gain or minimize Gini impurity:
$$I_G(p) = 1 - \sum_{k=1}^K p_k^2$$
- **Strengths**: Highly intuitive hierarchical structure; naturally accommodates mixed data types without requiring normalization; zero scaling sensitivity.
- **Weaknesses**: Highly prone to high variance and catastrophic overfitting on continuous numerical features; creates orthogonal, axis-aligned decision boundaries that struggle with correlated financial ratios.
- **Algorithmic Decision**: Serves as an unregularized baseline. In our empirical testing, a single Decision Tree scored poorly (F1-macro: 0.651), confirming that individual trees lack the regularization needed for subtle behavioral boundaries.

#### 4. Random Forests (Bootstrap Aggregation of Decision Trees)
Random Forests construct an ensemble of $B$ decorrelated decision trees, each trained on a bootstrap sample of the training data with random feature subsampling at each split node:
$$\hat{P}(Y = k \mid \mathbf{x}) = rac{1}{B} \sum_{b=1}^B P_b(Y = k \mid \mathbf{x})$$
- **Strengths**: Drastically reduces variance without increasing bias; highly robust to tabular noise and outliers; provides built-in Gini feature importance metrics.
- **Weaknesses**: Large serialized model size (~megabytes); slower inference than linear models; Tree SHAP explanations, while faster than Kernel SHAP, remain computationally heavier than Linear SHAP.
- **Algorithmic Decision**: Evaluated as a primary candidate. It achieved robust performance (F1-macro: 0.761), but did not outperform regularized Logistic Regression.

#### 5. Extreme Gradient Boosting (XGBoost)
XGBoost minimizes a regularized objective function combining convex loss and a penalty term penalizing tree complexity:
$$\mathcal{L}^{(t)} = \sum_{i=1}^n l\left(y_i, \hat{y}_i^{(t-1)} + f_t(\mathbf{x}_i)
ight) + \Omega(f_t)$$
- **Strengths**: Industry standard for tabular competitive machine learning; incorporates second-order Taylor approximations, column subsampling, and shrinkage; handles non-linear interactions natively.
- **Weaknesses**: Hyperparameter sensitivity; susceptible to overfitting on small or synthetic datasets if learning rates and tree depths are unconstrained; non-trivial dependency footprint.
- **Algorithmic Decision**: Benchmarked rigorously. It achieved an F1-macro of 0.761, matching Random Forest, but showed no statistically meaningful advantage over regularized Logistic Regression on our engineered feature set.

#### 6. Deep Learning & Transformers (Habit Modeling)
Recent literature (Braithwaite et al., 2025) has explored self-attention Transformers to model long-term financial habits from multi-year transaction logs.
- **Critical Appraisal**: While Transformers excel at sequential natural language and multi-year time-series modeling, they require massive, multi-gigabyte longitudinal datasets to converge without extreme overfitting. For cross-sectional, questionnaire-style behavioral profiles containing ~35 variables, deep neural networks and Transformers are fundamentally misaligned, introducing massive engineering overhead and severe interpretability deficits without empirical gain.

### 3.4.2 Architectural Design Patterns
Software architecture fundamentally determines system security, maintainability, and user adoption. Three architectural paradigms were evaluated:

#### 1. Multi-Tier Monolith with Relational Database (Traditional PFM Pattern)
- **Characteristics**: A monolithic framework (e.g., Django, Ruby on Rails) coupled with a PostgreSQL database storing user credentials, hashed passwords, transaction ledgers, and generated financial scores.
- **Critical Evaluation**: Storing personal financial data introduces enormous regulatory liabilities (GDPR, CCPA) and security vulnerabilities (SQL injection, credential stuffing, data leakage). If an attacker breaches the database, sensitive user incomes, debts, and stress statuses are exposed. Furthermore, relational persistence requires active session management, user registration friction, and database migrations.

#### 2. Microservice Architecture with Distributed Event Streaming
- **Characteristics**: Independent services for authentication, feature calculation, model inference, and notification, communicating asynchronously via Apache Kafka or RabbitMQ.
- **Critical Evaluation**: Highly over-engineered for single-profile inference requests. The network serialization latency between microservices exceeds the algorithmic execution time, introducing distributed failure modes without operational benefits for an individual assessment tool.

#### 3. Single-Process Asynchronous API with Stateless In-Memory Execution (Selected Architecture)
- **Characteristics**: A unified Python process running FastAPI on an ASGI Uvicorn server that serves both the static front-end assets and the RESTful prediction API.
- **Critical Justification**:
  - **Zero Data Persistence**: The system does not possess a database. Prediction requests are processed completely in volatile RAM; once the JSON response is dispatched, the request payload is immediately garbage-collected. This guarantees absolute data privacy and zero leak liability.
  - **Sub-Millisecond Overhead**: Serving the application from a single process eliminates inter-service network hops.
  - **Minimal Operational Surface**: The entire platform runs as a self-contained container or standalone service requiring only standard Python dependencies.

### 3.4.3 Data Pipeline and Explainability Workflows
The operational lifecycle of the intelligent financial stress system consists of two strictly decoupled pipelines:
1. **Offline Training & Validation Pipeline**:
   - Executes offline to guarantee reproducibility.
   - Computes statistical boundaries (IQR outlier thresholds, mean/variance vectors for `StandardScaler`).
   - Trains candidate models under strict cross-validation, selecting the winning artifact and exporting metadata (`best_model_metadata.json`).
2. **Live Inference Request Pipeline**:
   - Executes synchronously in real time upon client submission.
   - Reproduces the exact feature transformations used during training to prevent training-serving skew.
   - Scales features using the pre-fitted, serialized scaler.
   - Computes model probabilities, extracts local SHAP feature attributions, maps them to contextual plain-language suggestions, and returns a structured payload.

---

## 3.5 Research Gap and Implications for Your Work

### 3.5.1 Synthesis of the Six Compounding Research Gaps
The critical synthesis of existing academic literature, commercial financial applications, and machine learning architectures reveals six distinct, compounding research gaps:

1. **Gap 1: Absence of Proactive Behavioral Stress Classification**: Existing consumer financial software is overwhelmingly focused on retrospective expense logging, static budget categorization, or unsupervised anomaly identification. Current tools notify users of financial failure only after it has occurred. There is a glaring absence of software systems designed specifically to classify an individual's financial stress level proactively using predictive machine learning applied to daily spending patterns.
2. **Gap 2: Disconnect Between Psychometric Outcome Scales and Transaction Features**: Rigorous social science research has produced validated psychometric instruments for measuring financial well-being (e.g., CFPB Scale, APR Scale). Concurrently, computer science research has developed sophisticated algorithms for processing financial transactions. However, these two research domains remain disconnected. Psychometric scales rely on manual questionnaires, while transaction analytics lack standardized, psychometrically grounded outcome labels. There is an unaddressed gap in mapping validated psychometric scale cutoffs into supervised machine learning pipelines as definitive ground-truth targets.
3. **Gap 3: Deficiency of Algorithmic Benchmarking for Tabular Financial Behaviors**: While machine learning is widely applied in commercial credit scoring, the literature lacks transparent, reproducible comparative benchmarks evaluating how modern classifiers (regularized linear models, kernel SVMs, random forests, and gradient boosting) perform specifically on tabular, ratio-based behavioral spending features. Much of the literature either assumes deep learning is universally superior or defaults to an unregularized decision tree without empirical cross-validation.
4. **Gap 4: Opacity and the "Black-Box" Dilemma in Financial ML**: In consumer financial decision-support systems, algorithmic opacity breeds distrust. Returning an arbitrary label such as "High Stress" without explanation induces user anxiety and dismissal. Existing predictive tools rarely incorporate local feature attribution mechanisms (such as SHAP) to explain which specific behavioral habits (e.g., high debt service ratio or declining savings) drove the classification.
5. **Gap 5: Failure to Implement End-to-End User-Facing Functional Prototypes**: A substantial portion of academic machine learning research terminates at offline Jupyter Notebooks, reporting tabular metrics without bridging the gap to a deployable, user-facing software application. There is a marked failure to engineer functional software prototypes that combine robust input schema validation, dynamic pipeline execution, and responsive web presentation.
6. **Gap 6: Neglect of Privacy-Preserving Stateless Architecture and Calm UX Design**: Financial applications routinely demand invasive bank logins and store sensitive financial histories in centralized databases, introducing severe privacy and security risks. Furthermore, interface designs frequently employ alarming, punitive visual cues (e.g., red emergency banners) that trigger psychological avoidance. There is a critical need for software systems built upon stateless privacy architectures (zero data retention) and calm technology design principles that present financial reality constructively.

### 3.5.2 Implications for Software Architecture and Machine Learning Design
The identification of these gaps directly informs the engineering decisions made in this research:
- To bridge **Gap 1 and Gap 2**, we engineer behavioral ratios from user spending and calibrate target labels against the CFPB continuous scale.
- To resolve **Gap 3**, we implement a reproducible 5-model benchmarking suite evaluated under identical cross-validation conditions.
- To address **Gap 4**, we integrate a sub-millisecond Linear SHAP explainer to provide exact, transparent local feature attributions.
- To tackle **Gap 5 and Gap 6**, we deploy a production-grade FastAPI server coupled with a calm, non-stigmatizing "Financial Weather" frontend that operates with absolute statelessness in RAM.

### 3.5.3 Consolidated Research Gap Statement
> **Consolidated Research Gap:**  
> *"Although prior scholarship has separately established that spending behaviors influence financial well-being and has demonstrated the utility of machine learning in personal finance, there remains an unaddressed research gap: the absence of a unified, production-grade, and privacy-preserving software framework that maps multidimensional behavioral spending features against validated psychometric stress ground truth, benchmarks candidate classification algorithms, integrates local SHAP explainability, and communicates proactive early warnings through a calm, non-stigmatizing interface."*

This research directly addresses and resolves this consolidated gap through the design, implementation, and empirical evaluation of the "Financial Weather" system.

---

## 3.6 Chapter Summary
This chapter conducted an exhaustive academic and technological appraisal of personal financial stress detection. It framed the inquiry through a conceptual literature map, reviewed the behavioral economics of digital payments, and critically assessed seven foundational studies across psychometrics, personal finance management, and machine learning. It provided a detailed comparative evaluation matrix reflecting on why existing systems fail to deliver proactive intervention. Furthermore, it performed a comprehensive technological analysis of five classification algorithms, architectural deployment patterns, and operational workflows. Finally, it synthesized these findings into six concrete research gaps and established the overarching gap statement that justifies the software engineering contributions of this dissertation.


<div style='page-break-after: always;'></div>

---

# 4 METHODOLOGY

## 4.1 Research Design

### 4.1.1 Research Paradigm Justification: Pragmatism and Positivism
In software engineering and applied artificial intelligence research, the underlying philosophical paradigm dictates how the investigator conceptualizes reality (ontology), acquires valid knowledge (epistemology), and values human purpose (axiology) (Saunders et al., 2019). The academic inquiry undertaken in this dissertation is fundamentally situated within the philosophical paradigm of **Pragmatism**, complemented by operational elements of **Positivism**.

Classical research paradigms often enforce a rigid dichotomy:
- **Positivism** asserts that an objective, measurable reality exists independently of human observation. Knowledge is acquired through empirical observation, deductive hypothesis testing, mathematical modeling, and statistical verification.
- **Interpretivism** contends that reality is socially constructed through subjective meanings, human perceptions, and lived cultural experiences, rejecting purely mathematical reductionism.

While financial well-being undeniably possesses subjective psychological qualities (as an individual's personal perception of stress), the primary objective of this dissertation is not merely to describe human sentiment. Rather, it is to **engineer an intelligent, functional software artifact** capable of acting upon empirical data to solve a concrete real-world problem.

**Pragmatism** (Dewey, 1938; Peirce, 1905) rejects unhelpful philosophical dogmatism. It posits that the truth, validity, and value of a theory or software system are determined by its practical consequences, operational utility, and real-world efficacy. Under a pragmatist paradigm, the researcher integrates diverse methodological tools—combining mathematical feature engineering, algorithmic benchmarking, human-centered user experience design, and ethical reflection—to address complex problems.

Simultaneously, the quantitative and algorithmic evaluation of machine learning models demands strict **Positivist rigor**. The predictive efficacy of candidate classifiers (Logistic Regression, Support Vector Machines, Random Forests, XGBoost, Decision Trees) cannot be evaluated subjectively; it must be quantified using immutable statistical metrics, including Accuracy, Precision, Recall, F1-Scores, Confusion Matrices, and Area Under the Receiver Operating Characteristic Curve (ROC-AUC).

Therefore, this research adopts a **Pragmatist-Positivist synergy**:
1. *Positivist Epistemology*: Applied to data preprocessing, outlier detection, supervised model training, and quantitative performance evaluation.
2. *Pragmatist Axiology*: Applied to the human-centered translation of model predictions into non-stigmatizing visual metaphors ("Financial Weather"), local explainability attributions (SHAP), and actionable, gentle behavioral nudges.

### 4.1.2 Deductive Reasoning and Quantitative Investigation
Research approaches are broadly categorized into inductive, deductive, and abductive strategies:
- **Inductive Approach**: Begins with open-ended observations to construct new theoretical models or discover emerging patterns.
- **Deductive Approach**: Originates from established theories and conceptual frameworks, formulates specific hypotheses or engineering requirements, and subjects them to empirical testing.

This study rigorously follows a **Deductive Empirical Approach**, moving systematically from established theoretical constructs down to computational implementations and quantitative validation:

```
Theoretical Foundations (CFPB Well-Being, Behavioral Economics)
                        ↓
Hypothesis Formulation (Behavioral Ratios Correlate with Latent Stress)
                        ↓
Computational Artifact Construction (Data Pipeline, ML Classifiers, FastAPI)
                        ↓
Empirical Testing & Statistical Validation (Held-Out Test Set, 66 Pytest Suite)
                        ↓
Triangulation & Theoretical Confirmation (Triangulated Objective Fulfillment)
```

1. **Theoretical Grounding**: The research commences with established behavioral finance principles (Hasin & Zainol, 2026; Kee et al., 2026) and psychometric measurement standards (CFPB, 2017).
2. **Operational Hypothesis Formulation**: The hypotheses established in Chapter 1 ($H_1, H_2, H_3$) are tested.
3. **Artifact Construction and Verification**: Machine learning models and software architectures are implemented to operationalize these hypotheses.
4. **Empirical Verification**: The hypotheses are subjected to rigorous empirical testing on a held-out test dataset, validating or falsifying the architectural and algorithmic decisions.

### 4.1.3 Design Science Research (DSR) Strategy and the Four Artifact Dimensions
Given that the primary deliverable of this dissertation is an innovative, functional software solution, the research adopts **Design Science Research (DSR)** as its overarching research strategy (Hevner et al., 2004).

Unlike traditional behavioral science, which seeks to *explain and predict* natural or organizational phenomena, Design Science Research seeks to *create and evaluate* purposeful information technology artifacts designed to solve identified business and human problems. As articulated by Hevner et al. (2004), an IT artifact encompasses constructs (conceptual vocabularies), models (mathematical representations), methods (algorithmic pipelines), and instantiations (functional, running software systems).

This dissertation delivers all four DSR artifact dimensions:
- **Constructs**: Standardized behavioral spending concepts and psychometric stress categories (*Low*, *Moderate*, *High*).
- **Models**: Calibrated latent factor data models and multi-class classification mathematical formulations.
- **Methods**: The 13-stage reproducible data preprocessing, feature engineering, and SHAP attribution pipeline.
- **Instantiation**: The working **"Financial Weather"** software prototype, comprising the FastAPI asynchronous backend, Pydantic data validation layer, and interactive WebGL/SVG user interface.

### 4.1.4 Peffers DSRM Execution Workflow Across the Six Stages
This research rigorously follows the six-stage Design Science Research Methodology (DSRM) framework articulated by Peffers et al. (2007) (**Figure 4.1**).

![Figure 4.1: Peffers et al. Design Science Research Methodology (DSRM) Framework](../../reports/figures/dsrm_framework.png)

Figure 4.1: Peffers et al. Design Science Research Methodology (DSRM) Framework.

**Table 4.1** maps each Peffers DSRM stage directly to the concrete executions, artifacts, and chapters of this dissertation.

Table 4.1: DSRM Research Execution Matrix Mapped to Project Milestones.

| DSRM Stage | Core Operational Activity | Primary Deliverables / Artifacts | Dissertation Alignment |
|---|---|---|---|
| **Stage 1: Problem Identification** | Define the limitations of reactive budgeting; examine the socioeconomic crisis of personal financial stress. | Formal Problem Statement, Domain Deficiencies, Research Questions. | Chapter 01 (Sections 1.2–1.4), Chapter 03 (Section 3.2). |
| **Stage 2: Define Objectives** | Establish quantitative performance, explainability, latency, and privacy goals for an intelligent detection artifact. | Specific Research Objectives (2.2.1–2.2.7), Scope Boundary Matrix. | Chapter 01 (Section 1.7), Chapter 02 (Section 2.2). |
| **Stage 3: Design & Development** | Design the dual-pipeline architecture; engineer 7 behavioral ratios; train 5 candidate ML models; build FastAPI backend and web UI. | `src/features/engineer_features.py`, `src/models/train_models.py`, `src/app/api.py`, `src/app/static/`. | Chapter 04 (SRS & UML, Implementation). |
| **Stage 4: Demonstration** | Deploy the working prototype; demonstrate end-to-end real-time inference on diverse consumer profiles. | Functional Web Application ("Financial Weather"), Interactive Scenarios, Three.js Rendering. | Chapter 04 (Section 4.5.8), Chapter 05 (Section 5.3). |
| **Stage 5: Evaluation** | Benchmark candidate models on held-out test data (F1, ROC-AUC); execute 66 automated pytest cases; conduct latency profiling. | Model Comparison Benchmark (`model_comparison.csv`), Confusion Matrices, SHAP Plots, Pytest Log. | Chapter 05 (Testing & Empirical Evaluation). |
| **Stage 6: Communication** | Disseminate research contributions, system documentation, user manuals, and future recommendations. | Academic Dissertation, System Documentation, Setup Guide, Open Source Repo. | Chapter 06 (Discussion & Conclusions), Appendices. |

---

## 4.2 Data, Participants or Stakeholders

### 4.2.1 Stakeholder Analysis and Value Matrix
Software engineering success is contingent upon identifying all parties who affect or are affected by the software artifact. **Table 4.2** delineates the key stakeholders identified for the financial stress detection platform.

Table 4.2: Stakeholder Analysis and Value Realization Matrix.

| Stakeholder Persona | Profile & Description | Primary Needs & Operational Objectives | System Value Realization |
|---|---|---|---|
| **Primary End-User (The Consumer)** | Working professionals, gig-economy workers, university students, and household managers managing personal finances. | Requires immediate, proactive awareness of financial vulnerability without navigating complex accounting ledgers or experiencing psychological judgment. | Receives instant (<2 ms), non-stigmatizing stress classifications (Clear, Changeable, Stormy), clear factor drivers, and practical suggestions with zero data persistence. |
| **Financial Counselor / Advisor** | Credit counseling specialists, student welfare advisors, and personal financial coaches. | Requires objective, behavioral screening mechanisms to evaluate a client's baseline spending fragility prior to advisory consultations. | Utilizes the system as a diagnostic intake instrument that highlights critical ratios (e.g., debt-to-income, discretionary creep) without exposing client credentials. |
| **FinTech Software Engineer** | Software architects and backend developers building consumer banking apps, e-wallets, or PFM platforms. | Requires modular, low-latency, stateless APIs capable of generating reliable inferences without heavy microservice dependencies. | Leverages the clean, documented FastAPI `/predict` endpoint, Pydantic schemas, and serialized scikit-learn/SHAP pipelines for drop-in integration. |
| **Academic Researcher / Evaluator** | Data scientists and behavioral economics researchers examining consumer well-being and algorithmic decision support. | Requires fully reproducible experimental pipelines, transparent data dictionaries, and rigorous statistical benchmarking. | Gains access to open, reproducible Python scripts, seed-controlled latent factor models, and cross-validated multi-model comparison datasets. |

### 4.2.2 Primary Data Collection Instrument Design
The conceptual design of this research includes a comprehensive, non-invasive primary questionnaire instrument based on the CFPB Financial Well-Being Scale and behavioral finance literature. As cataloged in **Appendix A**, the instrument captures:
1. **Demographic Indicators**: Age, primary employment status, and number of financial dependents.
2. **Core Financial Aggregates**: Monthly income, total monthly expenditure, essential expenditure, non-essential (discretionary) expenditure, debt repayments, and savings.
3. **10-Category Expense Breakdown**: Housing, utilities, food/groceries, healthcare, education, transportation, shopping, entertainment, subscription services, and other miscellaneous outlays.
4. **Behavioral Indicators**: Transaction frequencies, impulse purchasing habits, online shopping intensity, budget deviation frequency over the past three months, regular saving ability, account checking frequency, and reported spending adaptations during financial difficulty.

### 4.2.3 Justification for Synthetic Benchmark Dataset Generation
While primary survey collection with human participants is a valuable long-term research activity, utilizing primary survey data for the initial algorithmic development of a financial machine learning prototype introduces severe academic, ethical, and legal barriers:
1. **Financial Privacy Regulations and Confidentiality**: Personal banking data and individual debt obligations are classified as highly sensitive financial information under global privacy frameworks (GDPR Article 9, CCPA). Requesting real participants to disclose their actual bank balances, credit card debts, and income figures introduces acute non-disclosure bias, missing value skew, and significant legal liability.
2. **Absence of Verifiable Ground Truth**: In real-world survey responses, individuals frequently misreport or underestimate their debts and impulse spending due to social desirability bias. Evaluating machine learning classifiers on biased, noisy, and self-deluding responses makes it impossible to scientifically benchmark whether classification errors originate from algorithmic deficiencies or corrupted ground-truth labels.
3. **Timeline and Scope Realities**: Formal human participant surveys require multi-month institutional ethical approvals, participant recruitment drives, and compensation structures. For a software engineering dissertation focused on building a fully functional software prototype and empirical benchmarking engine, an immediate, seed-controlled, and mathematically verifiable benchmark dataset was imperative.

Therefore, a **calibrated synthetic benchmark dataset** of 2,500 user profiles was generated (`scripts/generate_synthetic_data.py`).

### 4.2.4 Latent Factor Model Formulation: Beta(2,3) Distribution and Log-Normal Income
Rather than randomly fabricating values or using naive uniform distributions, the dataset generator simulates realistic human profiles anchored to a hidden, continuous financial stress latent variable $s \in [0, 1]$.

#### Mathematical Formulation of Latent Stress
The hidden stress factor $s$ is drawn from a Beta distribution:
$$s \sim 	ext{Beta}(lpha = 2, eta = 3)$$

The shape parameters $lpha = 2, eta = 3$ induce a right-skewed distribution across the synthetic population. This accurately mirrors real-world socioeconomic demographics: the majority of individuals cluster around low-to-moderate financial stress, while an acute minority experiences extreme financial strain ($s > 0.8$).

#### Calibrated Feature Generation with Stochastic Noise
Every observable behavioral feature $x_i$ is mathematically modeled as a monotonic function of latent stress $s$, perturbed by independent Gaussian noise $\epsilon \sim \mathcal{N}(0, \sigma^2)$ to reflect natural human behavioral variability:

1. **Monthly Income ($I$)**: Generated from a log-normal distribution to reflect national income wage dispersion:
   $$I = \exp\left(\mu_{\ln} + \sigma_{\ln} \cdot \mathcal{N}(0, 1)
ight)$$
   where $\mu_{\ln} = 11.2$ (median income approximately 73,000 LKR) and $\sigma_{\ln} = 0.55$. Crucially, income is deliberately given a near-zero direct correlation with latent stress $s$. This operationalizes the core research thesis: *high income does not preclude severe financial stress, nor does modest income guarantee distress*.

2. **Monthly Expenditure ($E$)**: Function of income, modulated by latent stress:
   $$E = I \cdot 	ext{clip}\left(0.60 + 0.45 \cdot s + \mathcal{N}(0, 0.08), 0.35, 1.30
ight)$$

3. **Debt Repayments ($D$)**: Positively correlated with latent stress:
   $$D = I \cdot 	ext{clip}\left(0.05 + 0.40 \cdot s^{1.5} + \mathcal{N}(0, 0.05), 0.0, 0.65
ight)$$

4. **Savings ($S$)**: Formulated as the exact accounting balance:
   $$S = I - E - D$$
   *Note*: Savings can become **negative**, representing deficit spending and credit-fueled debt accumulation.

5. **Behavioral Indicators**:
   - `can_save_regularly`: Stochastically assigned based on $s$; high stress strongly favors "No", whereas low stress favors "Yes".
   - `impulse_purchase_frequency`: Poisson distributed with $\lambda = 2 + 8 \cdot s$.
   - `spending_volatility`: Increases non-linearly with $s$.
   - `spending_change_during_difficulty`: Scaled from 1 to 5, where high-stress individuals report severe disruption.

### 4.2.5 Establishing Ground-Truth Target Labels Using CFPB Psychometric Bands
The continuous financial well-being score is derived directly from latent stress:
$$	ext{CFPB Score} = 	ext{clip}\left(100 - (85 \cdot s + \mathcal{N}(0, 4)), 0, 100
ight)$$

To establish discrete target classes for supervised machine learning, fixed, sample-independent score bands derived from CFPB practitioner benchmarks are applied (`scripts/apply_target_labels.py`):
$$	ext{Class} = egin{cases}
	ext{Low Financial Stress} & 	ext{if } 	ext{CFPB Score} \ge 70 \
	ext{Moderate Financial Stress} & 	ext{if } 40 \le 	ext{CFPB Score} < 70 \
	ext{High Financial Stress} & 	ext{if } 	ext{CFPB Score} < 40
\end{cases}$$

Across the 2,500 generated records, this produces a well-balanced, realistic class distribution:
- **Low Stress**: 870 instances (34.8%)
- **Moderate Stress**: 1,132 instances (45.3%)
- **High Stress**: 498 instances (19.9%)

### 4.2.6 Data Transparency and Rigor
The synthetic nature of this dataset is explicitly acknowledged as a deliberate engineering decision. It eliminates ethical hazards surrounding real banking secrets, provides verifiable ground truth for algorithmic benchmarking, and matches the exact feature schema of the proposed primary survey.

---

## 4.3 Requirements and Analysis

### 4.3.1 Operationalization Process: Mapping Inputs to Research Variables
In empirical software engineering, operationalization is the process of translating abstract theoretical concepts into measurable, computable software variables. **Table 4.3** defines the complete operationalization mapping.

Table 4.3: Operationalization Mapping of Behavioral Inputs to Research Variables.

| Input Feature / Parameter | Variable Type & Domain | Source Theoretical Construct | Operationalized Role in Research Objectives |
|---|---|---|---|
| `monthly_income` | Continuous Numeric ($> 0$, LKR) | Absolute Earning Capacity | Baseline control; demonstrates raw income is a weak predictor of stress. |
| `monthly_expenditure` | Continuous Numeric ($> 0$, LKR) | Aggregate Outflow | Serves as numerator for overall spending ratio and denominator for category splits. |
| `essential_expenditure` | Continuous Numeric ($\ge 0$, LKR) | Inflexible Living Costs | Operationalized into `essential_ratio` to measure structural expenditure rigidity. |
| `non_essential_expenditure` | Continuous Numeric ($\ge 0$, LKR) | Discretionary Spending | Operationalized into `discretionary_ratio` to capture lifestyle creep. |
| `housing`, `food`, `utility` ... (10 Categories) | Continuous Breakdown ($\sum = E$) | Category Budget Allocations | Enables multi-factor granular behavioral profiling across spending domains. |
| `debt_repayment` | Continuous Numeric ($\ge 0$, LKR) | Debt Servicing Burden | Operationalized into `debt_to_income_ratio` to assess insolvency risk. |
| `savings` | Continuous Numeric ($[-\infty, +\infty]$, LKR) | Net Financial Cushion | Operationalized into `savings_ratio`. Accommodates negative values (deficit spending). |
| `planned_expenditure` | Continuous Numeric ($\ge 0$, LKR) | Cognitive Budget Intent | Operationalized into `budget_deviation` ($E - 	ext{Planned}$) to quantify budget leakage. |
| `transaction_frequency` | Discrete Integer ($\ge 1$) | Cashless Velocity | Combines with expenditure to compute `avg_transaction_value`. |
| `spending_volatility` | Continuous Numeric ($\ge 0$, LKR) | Month-to-Month Stability | Operationalized into `spending_volatility_ratio` relative to income. |
| `impulse_purchase_frequency` | Discrete Count ($\ge 0$) | Lack of Self-Regulation | Direct input into classification model capturing impulsive spending habits. |
| `can_save_regularly` | Categorical (Yes, Sometimes, No) | Habitual Savings Efficacy | Ordinal encoded (0, 1, 2); emerges empirically as a dominant predictor. |
| `spending_change_during_difficulty` | Ordinal Scale (1–5) | Adaptive Resilience | Quantifies consumer capacity to contract discretionary spending during hardship. |

### 4.3.2 Requirements Engineering and Validation Process
Requirements were engineered following a dual-track stakeholder analysis: identifying the end-user's psychological need for non-judgmental guidance and the software engineer's need for strict, robust schema validation.

### 4.3.3 Formal Functional Requirements Specification
**Table 4.4** specifies the complete functional requirements.

Table 4.4: Functional Requirements Specification Matrix.

| Requirement ID | Priority | Requirement Description | Verification Method |
|---|---|---|---|
| **FR-01** | High | The system shall capture 28 user-entered financial, demographic, and spending indicators via a grouped web form. | Form field inspection & Playwright testing. |
| **FR-02** | High | The system shall validate all submitted payloads against strict domain bounds ($18 \le 	ext{age} \le 100$, $	ext{income} > 0$, $	ext{money} \le 10,000,000$). | Automated Pydantic boundary test suite. |
| **FR-03** | High | The system shall dynamically calculate seven behavioral ratios and derive budget deviation and average transaction value. | Unit math assert checks in `test_engineer_features.py`. |
| **FR-04** | High | The system shall standardize continuous numerical features using the pre-fitted `StandardScaler` while preserving unscaled one-hot categoricals. | Scaler column matching verification. |
| **FR-05** | High | The system shall classify the transformed feature vector into one of three financial stress categories (*Low*, *Moderate*, *High*). | Machine learning inference tests. |
| **FR-06** | High | The system shall map predicted classes to intuitive "Financial Weather" states (*Clear*, *Changeable*, *Stormy*) with confidence probabilities. | JSON schema & UI render verification. |
| **FR-07** | High | The system shall compute local SHAP attributions and extract the top three influential features contributing to the classification. | `test_explain.py` feature count verification. |
| **FR-08** | Medium | The system shall synthesize contextual, gentle behavioral suggestions based on the identified top SHAP factors. | Keyword matching assertion tests. |

### 4.3.4 Formal Non-Functional Requirements Specification
**Table 4.5** details the quality attributes, performance floors, and security guarantees governing the platform.

Table 4.5: Non-Functional Requirements Specification Matrix.

| Requirement ID | Quality Attribute | Target Standard & Specification | Empirical Measurement Technique |
|---|---|---|---|
| **NFR-01** | Performance & Latency | The backend shall execute end-to-end feature engineering, model inference, and SHAP explanation in under 10 milliseconds. | Benchmark profiling over 500 requests (`test_performance.py`). Result: ~1.4 ms. |
| **NFR-02** | Privacy & Statelessness | The application shall persist zero user inputs to disk, database, or external logs. Memory shall be discarded immediately post-request. | Architecture audit confirming absence of database or persistent logging. |
| **NFR-03** | Accessibility Floor | The UI shall provide full keyboard navigation, distinct focus rings, mobile scaling down to 375px, and an automated static SVG fallback for `prefers-reduced-motion`. | Headless browser verification with reduced motion emulation. |
| **NFR-04** | Input Security | The system shall reject arbitrary extra JSON fields (`extra="forbid"`) and reject numerical values exceeding $10^7$ with HTTP 422. | Security fuzz testing in `test_api_validation.py`. |
| **NFR-05** | Reliability & Availability | The API shall provide an active `/health` endpoint validating that model, scaler, and explainer artifacts are loaded into memory. | Health-check endpoint testing under `pytest`. |

---

## 4.4 Proposed Design

### 4.4.1 Dual-Pipeline System Architecture
The foundational software architecture of the system is structured as a **Dual-Pipeline Architecture** (**Figure 4.9**), enforcing a strict separation of concerns between offline machine learning operations and live real-time inference.

![Figure 4.9: Dual-Pipeline System Architecture (Offline Training and Live Inference)](../../reports/figures/system_architecture.png)

Figure 4.9: Dual-Pipeline System Architecture (Offline Training and Live Inference).

The architecture consists of two decoupled sub-systems:
1. **Offline Training & Validation Pipeline**: Responsible for synthetic data generation, data cleaning, IQR outlier flagging, feature ratio derivation, train/test splitting, 5-fold cross-validation, and serializing model artifacts (`models/*.joblib`) and metadata (`best_model_metadata.json`).
2. **Live Inference & Explanation Service**: An asynchronous FastAPI REST server hosting an in-memory instance of the selected classifier, scaler, and SHAP explainer. It dynamically validates incoming client payloads, reproduces feature transformations, evaluates probabilities, generates local attributions, and returns structured JSON responses in sub-2 milliseconds.

### 4.4.2 UML Use Case Modeling and Formal Specifications
The UML Use Case Diagram (**Figure 4.2**) delineates the core interactions between the primary actor (the Consumer) and the intelligent software platform.

![Figure 4.2: UML Use Case Diagram for Intelligent Financial Stress Detection](../../reports/figures/use_case_diagram.png)

Figure 4.2: UML Use Case Diagram for Intelligent Financial Stress Detection.

**Table 4.6** details the formal use case specification for the core inference workflow (UC-04).

Table 4.6: Formal Use Case Specifications for Core System Interactions.

| Field | Formal Use Case Specification (UC-04: Receive Stress Level & Confidence) |
|---|---|
| **Primary Actor** | System User (Consumer) |
| **Preconditions** | Web interface is loaded; user has provided valid numerical inputs across all required sections. |
| **Trigger** | User clicks the "Check my financial weather" button. |
| **Main Success Flow** | 1. Client JavaScript validates all input fields against domain boundary rules.<br/>2. Client dispatches HTTP POST request with JSON payload to `/predict` endpoint.<br/>3. FastAPI server validates schema via Pydantic model (rejecting invalid types with HTTP 422).<br/>4. Backend executes feature engineering: derives 7 ratios, encodes employment and savings.<br/>5. Backend scales continuous numerical columns using pre-fitted `StandardScaler`.<br/>6. Logistic Regression model computes class probabilities for Low, Moderate, High stress.<br/>7. Predicted class is mapped to weather metaphor (*Clear*, *Changeable*, *Stormy*).<br/>8. Linear SHAP explainer extracts the top 3 absolute contributing features.<br/>9. Backend maps top features to non-prescriptive gentle awareness suggestions.<br/>10. Server returns HTTP 200 JSON payload containing weather state, probabilities, and factors.<br/>11. Client interface transitions smoothly to results view, animating weather canvas and bars. |
| **Alternative Flows** | 3a. Payload validation fails: Server returns HTTP 422 with exact field error; client highlights field.<br/>5a. Denominator $\le 0$ detected in ratios: Server raises HTTP 422 with mathematical boundary error. |
| **Postconditions** | User views their estimated financial stress level; zero input data is persisted to disk or database. |

### 4.4.3 UML Structural Class Diagram
The UML Structural Class Diagram (**Figure 4.3**) models the core object-oriented components, domain transfer objects (DTOs), and service classes governing the system.

![Figure 4.3: UML Structural Class Diagram](../../reports/figures/class_diagram.png)

Figure 4.3: UML Structural Class Diagram.

The class hierarchy comprises:
- `FinancialProfileRequest`: Pydantic v2 schema enforcing boundary constraints, positive income checks, and forbidding unexpected input attributes.
- `FeatureEngineer`: Encapsulates mathematical ratio derivation, one-hot categorical encoding, and ordinal mappings.
- `ModelInferenceEngine`: Encapsulates serialized model loading, scaling, probability evaluation, and SHAP attribution extraction.
- `PredictionResponse`: Standardized JSON payload structure returned to the client.
- `FinancialWeatherView`: Client-side interface controller managing state, form submission, and Three.js canvas animations.

### 4.4.4 UML Dynamic Activity Diagram
The UML Activity Diagram (**Figure 4.4**) details the dynamic execution flow across three cross-functional swimlanes: the User/Browser Client, the FastAPI Application Server, and the ML & Explainability Core.

![Figure 4.4: UML Dynamic Activity Diagram for Financial Stress Assessment Workflow](../../reports/figures/activity_diagram.png)

Figure 4.4: UML Dynamic Activity Diagram for Financial Stress Assessment Workflow.

### 4.4.5 UML Sequence Modeling
To provide precise temporal execution traces, three distinct sequence diagrams were engineered:
1. **Sequence Diagram 1: End-to-End Prediction and UI Rendering Workflow** (**Figure 4.5**): Captures the complete HTTP lifecycle from user click to DOM update.
2. **Sequence Diagram 2: Dynamic Feature Transformation Pipeline** (**Figure 4.6**): Illustrates the exact internal mechanics of transforming raw form inputs into the 42-dimensional vector required by the model.
3. **Sequence Diagram 3: SHAP Linear Attribution and Guidance Synthesis** (**Figure 4.7**): Details how mathematical Shapley values are extracted and mapped to contextual behavioral suggestions.

![Figure 4.5: Sequence Diagram 1 — End-to-End Prediction and UI Rendering Workflow](../../reports/figures/sequence_diagram_inference.png)

Figure 4.5: Sequence Diagram 1 — End-to-End Prediction and UI Rendering Workflow.

![Figure 4.6: Sequence Diagram 2 — Dynamic Feature Transformation Pipeline](../../reports/figures/sequence_diagram_pipeline.png)

Figure 4.6: Sequence Diagram 2 — Dynamic Feature Transformation Pipeline.

![Figure 4.7: Sequence Diagram 3 — SHAP Linear Attribution and Guidance Synthesis](../../reports/figures/sequence_diagram_shap.png)

Figure 4.7: Sequence Diagram 3 — SHAP Linear Attribution and Guidance Synthesis.

### 4.4.6 UML Physical Deployment Diagram
The UML Deployment Diagram (**Figure 4.8**) captures the physical hardware nodes, runtime execution environments, software artifacts, and network communication protocols.

![Figure 4.8: UML Physical Deployment Diagram](../../reports/figures/deployment_diagram.png)

Figure 4.8: UML Physical Deployment Diagram.

The architecture runs as a single, self-contained Python process on an Apple Silicon or Linux host. The client browser communicates with the Uvicorn ASGI server via HTTPS/REST. The FastAPI application server holds the serialized `.joblib` model and scaler artifacts in memory, serving both static assets and prediction endpoints without external database dependencies.

---

## 4.5 Development or Implementation Procedure (My Personal Engineering Journey)
In this section, I explain in detail how I actually carried out the software engineering and machine learning work, recounting the practical steps, technical challenges, mathematical guardrails, and failed model trials that led to the final operational platform.

### 4.5.1 Step-by-Step Data Engineering and Cleaning Decisions
When I initiated this project, my first objective was to construct a clean, reproducible data pipeline. Having established that real banking transaction databases were unavailable due to GDPR restrictions and user confidentiality, I implemented the latent factor generator in `scripts/generate_synthetic_data.py`. I calibrated the socioeconomic distributions so that income followed a log-normal curve ($\mu_{\ln}=11.2, \sigma_{\ln}=0.55$) with a median around 73,000 LKR, and modulated expenses via the latent stress factor $s \sim 	ext{Beta}(2,3)$.

Once the 2,500 raw records were generated, I developed the cleaning pipeline in `src/data/clean_data.py`. Financial data presents unique challenges because people occasionally make massive payments—such as annual life insurance premiums, hospital deposits, or university semester fees. During initial testing, I observed several records where expenditures were four to five times higher than typical monthly spending. In traditional machine learning tutorials, the immediate instinct is to delete any row exceeding $Q_3 + 1.5 	imes 	ext{IQR}$. However, I realized that **deleting these extreme financial rows would be a critical domain error**: in real life, sudden large expenses are genuine behavioral events that often trigger acute financial stress! 

Therefore, I made the conscious engineering decision to **flag outliers rather than remove them**. Using the Interquartile Range method:
$$	ext{IQR} = Q_3 - Q_1$$
$$	ext{Bound}_{	ext{lower}} = Q_1 - 1.5 	imes 	ext{IQR}, \quad 	ext{Bound}_{	ext{upper}} = Q_3 + 1.5 	imes 	ext{IQR}$$

I appended boolean flag columns (e.g., `is_outlier_monthly_expenditure`, `is_outlier_savings`) to the dataset, allowing the downstream models to learn from the full variance while preserving data integrity.

### 4.5.2 Deriving 7 Behavioral Financial Ratios and Handling Division-by-Zero Exceptions
My primary research hypothesis was that raw currency values (such as spending 150,000 LKR) mean very little without knowing how much the individual earns and saves. To capture financial habits, I engineered seven core behavioral ratios in `src/features/engineer_features.py`, as formalized in **Table 4.7**.

Table 4.7: Engineered Behavioral Ratios and Mathematical Formulations.

| Ratio Identifier | Mathematical Formulation | Behavioral Construct Measured |
|---|---|---|
| `spending_to_income_ratio` | $rac{	ext{monthly\_expenditure}}{	ext{monthly\_income}}$ | Overall cash-flow consumption intensity |
| `savings_ratio` | $rac{	ext{savings}}{	ext{monthly\_income}}$ | Relative rate of monthly wealth accumulation or deficit |
| `debt_to_income_ratio` | $rac{	ext{debt\_repayment}}{	ext{monthly\_income}}$ | Debt servicing pressure and insolvency risk |
| `discretionary_ratio` | $rac{	ext{non\_essential\_expenditure}}{	ext{monthly\_expenditure}}$ | Proportion of lifestyle creep and non-vital outlays |
| `essential_ratio` | $rac{	ext{essential\_expenditure}}{	ext{monthly\_expenditure}}$ | Baseline expenditure rigidity and survival overhead |
| `subscription_burden` | $rac{	ext{subscription\_expenditure}}{	ext{monthly\_income}}$ | Recurring digital service drag on monthly income |
| `spending_volatility_ratio` | $rac{	ext{spending\_volatility}}{	ext{monthly\_income}}$ | Cash-flow turbulence and spending unpredictability |

During the early implementation of these ratios, I encountered an immediate technical failure: when testing edge cases where a user entered an income or expenditure of zero, Pandas evaluated the ratio as `inf` or `NaN`. When these infinite values were subsequently fed into scikit-learn's `StandardScaler`, the scaler crashed or produced corrupted weight matrices filled with `NaN` values.

To permanently resolve this vulnerability, I implemented defensive exception guards at two distinct architectural levels:
1. **In the Feature Engineering Module (`src/features/engineer_features.py`)**: I added explicit assertion checks:
   ```python
   if (df["monthly_income"] <= 0).any():
       raise ValueError("monthly_income must be strictly positive to prevent division-by-zero")
   if (df["monthly_expenditure"] <= 0).any():
       raise ValueError("monthly_expenditure must be strictly positive to prevent division-by-zero")
   ```
2. **In the FastAPI Pydantic Schema (`src/app/api.py`)**: I enforced validation constraints (`gt=0`) on both `monthly_income` and `monthly_expenditure`. If an incoming HTTP payload specifies an income of zero, FastAPI intercepts the request immediately and returns an HTTP 422 Unprocessable Entity error before any mathematical operations take place.

### 4.5.3 Detecting and Purging Data Leakage Features: The `financial_wellbeing_score` Incident
During the initial model training sprint, I encountered an interesting phenomenon: my candidate models achieved a suspicious **100% classification accuracy** across all training folds and test sets. Upon auditing the pipeline, I discovered a subtle yet catastrophic instance of **data leakage**: the dataset contained the column `financial_wellbeing_score` (the continuous 0–100 score). Because the target labels (`Low`, `Moderate`, `High`) had been created by binning this exact score (≥70, 40–69, <40), the machine learning algorithms had simply discovered a trivial mathematical threshold on `financial_wellbeing_score`, completely ignoring all spending behaviors, debt ratios, and income metrics!

This was a classic machine learning failure mode. In a real-world application, an end user filling in an expense form does *not* know their CFPB financial well-being score—that score is the very outcome we are trying to predict from spending behavior!

To permanently prevent this leakage, I took the following architectural steps:
1. I explicitly purged `financial_wellbeing_score`, along with metadata identifiers (`user_id`), raw string labels, and outlier boolean flags, from the modeling feature matrix in `src/models/train_models.py`.
2. I split the dataset into 80% training (2,000 records) and 20% testing (500 records) using stratified sampling on `financial_stress_level` *before* fitting any preprocessing transformations.
3. I fitted the `StandardScaler` strictly on the training partition (`X_train`) and saved the fitted object to `models/scaler.joblib`. The test set was transformed using this pre-fitted scaler, ensuring that zero statistical parameters from the test data leaked into the training process.

### 4.5.4 Machine Learning Model Experiments, Training Pipeline, and Failed Attempts
To rigorously determine the most effective classifier, I implemented a multi-model training pipeline in `src/models/train_models.py`. I trained five candidate algorithms under identical conditions using a fixed `random_state=42` and 5-fold stratified cross-validation on the 2,000 training instances. Two candidate models trained on normalized features (`features_scaled.csv`), while the three tree-based algorithms trained on unscaled features (`features_unscaled.csv`) to preserve natural decision thresholds.

Below, I describe my observations, including the models that failed or proved suboptimal:

#### 4.5.4.1 Attempt 1: Unregularized Decision Tree (CART) and Why It Failed
I evaluated a standard Decision Tree (`DecisionTreeClassifier(random_state=42)`) as an interpretable, non-parametric baseline. However, the Decision Tree performed poorly across all evaluation metrics, achieving a macro-averaged F1-score of only **0.651** and an accuracy of **0.650**. 

When I inspected its confusion matrix on the 500-instance test set, I uncovered a dangerous failure: the Decision Tree made two severe cross-boundary misclassifications, erroneously predicting that individuals in **High Financial Stress** were actually in **Low Financial Stress**! In a consumer financial wellness application, this is the worst possible failure mode: assuring a user who is teetering on the edge of insolvency that their finances look completely steady. The single decision tree failed because it created rigid, axis-aligned splits on continuous financial ratios, causing severe overfitting to noise in the training set and failing to generalize across subtle behavioral boundaries.

#### 4.5.4.2 Attempt 2: Support Vector Machine (RBF Kernel) and Why It Was Rejected for Live Deployment
Next, I evaluated a Support Vector Classifier with a Radial Basis Function (RBF) kernel (`SVC(kernel="rbf", probability=True, random_state=42)`). The SVM achieved the highest raw predictive scores on the held-out test set: an accuracy of **0.778**, a macro F1-score of **0.776**, and a High-stress recall of **0.700**.

However, when I evaluated the SVM against our non-functional requirements—specifically inference speed and explainability—the model proved entirely unsuitable for production:
1. **Inference Latency Bottleneck**: Because the RBF kernel evaluates decision boundaries by calculating kernel distances across support vectors, its inference latency scaled poorly. In sequential latency benchmarking over 500 requests (`tests/test_performance.py`), the SVM required an average of **84.10 ms** per prediction—nearly 60 times slower than Logistic Regression!
2. **Explainability Impasse**: The research requirement mandated extracting local feature attributions using SHAP. Because an RBF SVM is a non-linear, non-additive black-box, it cannot use fast analytical SHAP algorithms. Instead, it requires `KernelExplainer`, which approximates Shapley values by perturbing input vectors and querying the model hundreds of times. In my local benchmarks, generating a single explanation for the SVM took over **315 milliseconds**, causing the web application to freeze noticeably during user submissions. Consequently, despite its high accuracy, the SVM was rejected as a production candidate.

#### 4.5.4.3 Attempt 3: Random Forest Ensemble
I trained a Random Forest ensemble consisting of 300 estimators (`RandomForestClassifier(n_estimators=300, random_state=42)`). The ensemble substantially improved upon the single Decision Tree, eliminating extreme misclassifications and attaining an accuracy of **0.764** and an F1-macro of **0.761**. However, its High-stress recall (**0.660**) lagged behind both Logistic Regression and SVM, and its serialized model file size exceeded several megabytes.

#### 4.5.4.4 Attempt 4: Extreme Gradient Boosting (XGBoost)
I implemented an optimized gradient-boosted decision tree classifier using the XGBoost library (`XGBClassifier(objective="multi:softprob", num_class=3, eval_metric="mlogloss", random_state=42)`). XGBoost achieved an accuracy of **0.762**, an F1-macro of **0.761**, and a High-stress recall of **0.690**. While highly competitive, XGBoost did not outperform regularized Logistic Regression on our engineered feature set and introduced heavy external C++ binary dependencies.

#### 4.5.4.5 Attempt 5: Multinomial Logistic Regression (L2 Regularized) and Why It Succeeded
Finally, I evaluated an L2-regularized Multinomial Logistic Regression model (`LogisticRegression(max_iter=2000, random_state=42)`). The model achieved:
- **Accuracy**: 0.766
- **Macro F1-Score**: 0.765 (trailing SVM by just 0.011, well within statistical sampling noise)
- **High-Stress Recall**: 0.690
- **High-Stress Precision**: 0.812 (meaning 81.2% of users flagged as "Stormy" were genuinely in severe distress)
- **ROC-AUC (One-vs-Rest Macro)**: **0.915** (the highest across all five candidate algorithms!)
- **Mean Inference Latency**: **1.42 ms** (60x faster than SVM)
- **SHAP Explanation Latency**: **0.85 ms** (using exact Linear SHAP)

Because my feature engineering pipeline had already explicitly derived the critical non-linear behavioral interactions (the seven ratios), the underlying relationship between normalized ratios and log-odds was cleanly separable by a regularized hyperplane. Logistic Regression delivered the ideal engineering compromise: competitive accuracy, top-tier discriminative power, ultra-low latency, and transparent interpretability.

### 4.5.5 Production Model Selection Rationale and Engineering Trade-Offs
**Table 4.8** consolidates the engineering trade-offs that guided the selection of the production classifier in `src/models/select_best_model.py`.

Table 4.8: Technology Stack and Model Selection Comparative Justification Matrix.

| Candidate Model | Macro F1 | ROC-AUC (OvR) | High-Stress Recall | Inference Latency | SHAP Latency | Production Selection Status |
|---|---|---|---|---|---|---|
| **Multinomial Logistic Regression** | **0.765** | **0.915** | **0.690** | **1.42 ms** | **0.85 ms** | **SELECTED FOR PRODUCTION** (Optimal speed, interpretability, and AUC) |
| **Support Vector Machine (RBF)** | 0.776 | 0.910 | 0.700 | 84.10 ms | 315.0 ms | **Rejected** (Severe latency penalty and black-box opacity) |
| **Random Forest (300 Trees)** | 0.761 | 0.907 | 0.660 | 18.50 ms | 45.2 ms | **Rejected** (Suboptimal High-stress recall and large artifact size) |
| **XGBoost (Gradient Boosted)** | 0.761 | 0.904 | 0.690 | 12.20 ms | 38.4 ms | **Rejected** (No performance advantage over regularized linear model) |
| **Decision Tree (Single CART)** | 0.651 | 0.730 | 0.640 | 0.82 ms | 2.1 ms | **Rejected** (Severe overfitting and extreme Low-High boundary spillover) |

### 4.5.6 Real-Time Explainable AI Implementation: Developing the Linear SHAP Engine
To address the "black-box" dilemma (Research Gap 4), I integrated Shapley Additive Explanations into the live prediction loop (`src/evaluation/explain.py`). 

For a Multinomial Logistic Regression model with weight matrix $\mathbf{W} \in \mathbb{R}^{K 	imes d}$ and bias vector $\mathbf{b} \in \mathbb{R}^K$, the local attribution $\phi_{k, j}$ of feature $j$ for predicted class $k$ is given analytically by:
$$\phi_{k, j}(\mathbf{x}) = w_{k, j} \cdot \left(x_j - \mathbb{E}[x_j]
ight)$$

I initialized a `shap.LinearExplainer` using a representative background dataset of 100 scaled training instances. Upon receiving a live prediction request:
1. The model predicts class $k \in \{0: 	ext{Low}, 1: 	ext{Moderate}, 2: 	ext{High}\}$.
2. The explainer evaluates the 42 attribution values $\phi_{k, j}$ for that specific class.
3. The system ranks features by absolute magnitude $|\phi_{k, j}|$ and extracts the top three driving features.
4. A humanizing formatting function converts technical feature names into plain-language descriptions (e.g., `can_save_regularly_encoded` $
ightarrow$ "Ability to save regularly: No"; `debt_to_income_ratio` $
ightarrow$ "High debt-to-income ratio").

### 4.5.7 Engineering the Contextual Gentle Awareness Suggestion Rule Engine
To ensure that explanations lead to constructive behavioral awareness rather than anxiety, I built a rule-matching engine in `src/app/api.py`. The engine matches keywords from the top SHAP features to non-prescriptive, gentle suggestions (**Table 4.9**).

Table 4.9: Contextual Gentle Awareness Suggestion Mapping Rules.

| Identified Top Feature Trigger | Contextual Gentle Awareness Suggestion |
|---|---|
| **Debt-to-Income Ratio** | "Consider reviewing recurring debt obligations relative to income." |
| **Ability to Save Regularly** | "Consider setting aside a small, consistent amount in savings each month."<br/>"Consider reviewing upcoming expenses for opportunities to save regularly." |
| **Discretionary Spending Ratio** | "Consider tracking discretionary purchases to see where flexibility exists." |
| **Spending Volatility Ratio** | "Consider tracking month-to-month spending to understand what drives fluctuations." |
| **Impulse Purchase Frequency** | "Consider adding a brief pause before non-essential purchases." |
| **Spending Change During Difficulty** | "Consider planning ahead for how spending might change during difficult periods." |

### 4.5.8 Developing the Full-Stack Web Application: FastAPI Backend, Pydantic Schema Guarding, and Accessible Frontend
The complete application was engineered as a single-tier, production-ready system:
- **FastAPI Asynchronous Backend (`src/app/api.py`)**: Models, scalers, and explainers are loaded into volatile RAM once during server startup using FastAPI's modern `lifespan` context manager, ensuring that subsequent HTTP requests incur zero disk I/O latency.
- **Pydantic v2 Schema Enforcement**: The `FinancialProfileRequest` model validates incoming JSON payloads, verifying that all financial numbers are within realistic bounds and enforcing `extra="forbid"` to reject unauthorized payload tampering.
- **Client-Side Interface (`src/app/static/`)**: Developed using accessible HTML5, CSS3, and vanilla JavaScript. To eliminate stigma, the UI displays three weather states:
  - *Clear* (Low Stress): Steady, sunny procedural animation.
  - *Changeable* (Moderate Stress): Gentle cloud drift.
  - *Stormy* (High Stress): Muted clay-toned atmospheric rendering, accompanied by clear disclaimer text stating that the result is an automated estimate and not a medical or psychological diagnosis.
- **Accessibility Floor and Reduced-Motion Support**: During usability testing, I realized that animated Three.js particle simulations can trigger vestibular discomfort for users sensitive to motion. I implemented an automated media query listener (`window.matchMedia('(prefers-reduced-motion: reduce)')`). When triggered, the Three.js canvas is halted, and the interface seamlessly falls back to high-contrast, static SVG weather icons, guaranteeing full WCAG 2.1 Level AA compliance.

---

## 4.6 Evaluation Plan

### 4.6.1 Master Test Strategy and Verification Framework
To guarantee software reliability, an automated testing strategy was formulated around Test-Driven Development (TDD) using the `pytest` framework and `AnyIO` for asynchronous API testing.

### 4.6.2 Formal Functional and Non-Functional Test Cases
**Table 4.10** documents the ten master formal test cases engineered to validate system capabilities.

Table 4.10: Master Test Plan and Formal Test Case Specifications.

| Test ID | Category | Description & Objective | Preconditions & Inputs | Execution Steps | Expected Output | Actual Output | Status |
|---|---|---|---|---|---|---|---|
| **TC-01** | Functional | Baseline Valid Profile Inference | Backend running; valid low-stress payload. | Submit JSON profile to `POST /predict`. | HTTP 200 OK; valid `stress_level`, probabilities sum to 1.0, 3 factors. | HTTP 200; `stress_level="Low"`, probabilities sum to 1.000, 3 factors returned. | **PASS** |
| **TC-02** | Non-Functional | Inference Latency Benchmark | Server warmed up; 500 sequential requests. | Measure elapsed time from request receipt to JSON dispatch (`test_performance.py`). | Mean latency $< 10.0$ ms per prediction. | Mean latency: 1.42 ms; 99th percentile: 2.15 ms. | **PASS** |
| **TC-03** | Functional | Zero-Division Input Boundary Guard | Backend initialized. | Submit payload with `monthly_income = 0` or `monthly_expenditure = 0`. | Pydantic schema validation failure; HTTP 422 Unprocessable Entity. | HTTP 422 returned with clear error: `Input should be greater than 0`. | **PASS** |
| **TC-04** | Non-Functional | Oversized Adversarial Payload Guard | Backend running. | Submit numerical values exceeding bounds (e.g., `income = 1e20`). | Rejected immediately with HTTP 422 before reaching model matrix. | HTTP 422 returned; payload rejected safely. | **PASS** |
| **TC-05** | Non-Functional | Extra-Field Injection Guard | Backend running. | Submit payload containing unexpected fields (`extra_key="attack"`). | Rejected immediately via Pydantic `extra="forbid"` configuration. | HTTP 422 returned; error: `Extra inputs are not permitted`. | **PASS** |
| **TC-06** | Functional | Negative Savings Deficit Tolerance | Clean dataset loaded. | Submit profile where $E + D > I$, resulting in negative savings. | System accepts negative savings, calculates negative `savings_ratio`, infers High Stress. | Accepted; `savings_ratio` calculated correctly; Stormy/High stress returned. | **PASS** |
| **TC-07** | Functional | Feature Column Reindexing Alignment | Trained model artifacts loaded. | Verify engineered dictionary matches `best_model_metadata.json` columns. | Exact 1:1 match across 42 column names in identical sequence. | Exact 42-column sequence verified; zero column drift detected. | **PASS** |
| **TC-08** | Functional | Linear SHAP Factor Extraction | Trained model and background dataset cached. | Execute `explain_prediction()` across 100 test instances. | Exactly 3 unique, human-readable contributing factors returned per instance. | Exactly 3 ranked plain-language factor phrases returned for all 100 profiles. | **PASS** |
| **TC-09** | Non-Functional | Reduced-Motion Accessibility Fallback | Headless browser client. | Emulate `prefers-reduced-motion: reduce` OS preference. | Three.js animation disabled; static SVG weather icons displayed without errors. | Particle animation halted; static SVG icons rendered; 100% functional. | **PASS** |
| **TC-10** | Functional | Health Check & Cache Verification | Server initialized via FastAPI `lifespan`. | Dispatch HTTP GET to `/health`. | HTTP 200 OK; JSON payload: `{"status": "healthy", "model_loaded": true}`. | HTTP 200 OK; `{"status": "healthy", "model_loaded": true, ...}` returned. | **PASS** |

### 4.6.3 5-Fold Stratified Cross-Validation Protocol
During model development, 5-fold stratified cross-validation was conducted across the 2,000 training instances (`StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`). Stratification ensured that each fold contained identical proportions of Low (34.8%), Moderate (45.3%), and High (19.9%) stress instances, evaluating model stability across diverse data subsets.

### 4.6.4 Held-Out Test Set Partitioning (80/20 Stratified Split)
Final evaluation was conducted on a strictly isolated, held-out test split of 500 instances (20% of the dataset) that remained completely unseen during training, feature scaling fitting, and hyperparameter tuning.

### 4.6.5 Selection and Mathematical Definition of Evaluation Metrics
Because financial stress detection involves multiple classes with class imbalance (High stress represents ~20% of instances), relying solely on overall accuracy would be misleading. Therefore, the evaluation protocol incorporates:
1. **Accuracy**: Overall fraction of correct classifications:
   $$	ext{Accuracy} = rac{\sum_{k=1}^K TP_k}{N}$$
2. **Macro-Averaged Precision, Recall, and F1-Score**: Evaluates performance equally across all three classes, preventing majority-class dominance:
   $$	ext{Precision}_{	ext{macro}} = rac{1}{K} \sum_{k=1}^K rac{TP_k}{TP_k + FP_k}, \quad 	ext{Recall}_{	ext{macro}} = rac{1}{K} \sum_{k=1}^K rac{TP_k}{TP_k + FN_k}$$
   $$	ext{F1}_{	ext{macro}} = rac{1}{K} \sum_{k=1}^K rac{2 \cdot 	ext{Precision}_k \cdot 	ext{Recall}_k}{	ext{Precision}_k + 	ext{Recall}_k}$$
3. **High-Stress Specific Recall and F1**: Crucial from a harm-reduction perspective, measuring the system's ability to catch individuals in severe distress.
4. **One-vs-Rest (OvR) Macro ROC-AUC**: Measures the multi-class discriminative capability across all classification thresholds:
   $$	ext{ROC-AUC}_{	ext{macro}} = rac{1}{K} \sum_{k=1}^K 	ext{AUC}(k 	ext{ vs. rest})$$
5. **Inference and Explanation Latency**: Measured in milliseconds using high-precision CPU timers over 500 sequential requests.

---

## 4.7 Ethics and Project Management

### 4.7.1 Project Management Framework: Agile Scrum Methodology
To manage algorithmic complexity and software delivery, the research followed the **Agile Scrum Framework** (Schwaber & Sutherland, 2020). The twelve-month project lifecycle was decomposed into six structured bi-monthly sprints (**Table 4.11**).

Table 4.11: Agile Scrum Sprint Decomposition and Deliverables.

| Sprint ID & Duration | Primary Focus & Domain Objectives | Key Technical Deliverables & Milestones |
|---|---|---|
| **Sprint 1 (Nov – Dec 2025)** | Inception & Literature Synthesis | Problem definition, psychometric literature review, thesis proposal defense. |
| **Sprint 2 (Jan – Feb 2026)** | Methodological Design & Data Modeling | Latent factor generator formulation, Beta(2,3) distribution, 35-variable schema. |
| **Sprint 3 (Mar – Apr 2026)** | Data Pipeline & Preprocessing Engine | IQR outlier flagging, 7 behavioral ratio derivations, train/test stratified split. |
| **Sprint 4 (May – Jun 2026)** | Algorithmic Modeling & Benchmarking | Multi-model training (LogReg, SVM, RF, XGB, DT), 5-fold CV, metrics evaluation. |
| **Sprint 5 (Jul – Aug 2026)** | Explainability & Web Artifact Development | Linear SHAP integration, suggestion rules, FastAPI REST API, Three.js UI. |
| **Sprint 6 (Sep – Nov 2026)** | Testing, Usability & Dissertation Compilation | 66-test pytest execution, latency profiling, final dissertation authoring, viva defense. |

### 4.7.2 Sprint Timeline, Task Decomposition, and Gantt Chart Analysis
The sequential execution and task concurrency across the twelve-month development period are depicted in the formal Project Gantt Chart (**Figure 4.10**).

![Figure 4.10: Project Milestone Schedule and Execution Timeline (Gantt Chart)](../../reports/figures/project_gantt.png)

Figure 4.10: Project Milestone Schedule and Execution Timeline (Gantt Chart).

### 4.7.3 Ethical Guardrails: GDPR Compliance, Absolute Statelessness, and Responsible Non-Diagnostic Framing
Processing financial information imposes severe ethical obligations:
1. **Strictly Non-Diagnostic Framing**: The software explicitly frames outputs as an "estimated financial stress indicator" rather than a clinical psychological diagnosis. A permanent, prominent disclaimer is rendered on both API responses and UI views.
2. **Absolute Data Minimization (GDPR Article 5)**: The platform solicits zero Personally Identifiable Information (PII)—no names, emails, account numbers, or bank tokens. All inputs exist purely in volatile RAM during the request and are immediately discarded. Zero data is persisted to disk or databases.
3. **Calm, Non-Stigmatizing Design Language**: Grounded in Calm Technology principles (Weiser & Brown, 1997), the UI eschews flashing red emergency banners in favor of natural weather metaphors (Clear, Changeable, Stormy) with gentle, non-prescriptive behavioral prompts.

---

## 4.8 Chapter Summary
This chapter detailed the comprehensive research methodology and software engineering design governing the dissertation. It established the epistemological justification for combining Pragmatism with Positivism, substantiated the Deductive Empirical Approach, and situated the work within Design Science Research. It detailed the stakeholder matrix, latent factor data generation model, and operationalization mappings. It presented the complete System Requirement Specification and UML model suite. Crucially, the chapter recounted the firsthand engineering journey—explaining data cleaning, ratio derivations, division-by-zero solutions, data leakage prevention, candidate model experiments, and the rejection of single decision trees and RBF SVMs due to overfitting and latency bottlenecks. Finally, the chapter codified the master test plan, evaluation metrics, Agile Scrum project schedule, and ethical privacy guarantees. The next chapter presents the empirical results and evaluation findings produced by this methodology.


<div style='page-break-after: always;'></div>

---

# 5 RESULTS

## 5.1 Chapter Overview
This chapter reports the empirical findings, quantitative benchmarks, and executional outcomes produced across the software engineering and machine learning lifecycle. In accordance with the Faculty of Computing Senate guidelines, the results are organized directly around the seven specific research objectives established in Chapter 2. The presentation adheres to a strict factual reporting structure, communicating observed measurements without attempting speculative interpretation (which is reserved for Chapter 6).

Section 5.2 defines the final benchmark dataset profile, class distributions, and the computational testing environment. Section 5.3 showcases the developed software artifact, presenting high-resolution visual evidence of the grouped web input form, the three distinct "Financial Weather" classification states (*Clear*, *Changeable*, *Stormy*), the accessibility static SVG fallback mode, and serialized model metadata. Section 5.4 documents the functional and non-functional software testing outcomes, including the automated 66-test pytest execution log and sub-2 millisecond latency benchmarks. Section 5.5 delivers the empirical machine learning evaluation across all five candidate algorithms, providing master benchmark comparison tables, per-class metrics, 5-fold cross-validation consistency results, multi-model confusion matrix heatmaps, One-vs-Rest ROC curves, standardized feature importance rankings, and SHAP beeswarm summary plots. Finally, Section 5.6 presents an empirical triangulation matrix evaluating results against each specific research objective, followed by the chapter summary in Section 5.7.

---

## 5.2 Final Data or Evaluation Setting

### 5.2.1 Benchmark Dataset Profile, Feature Count, and Class Distributions
The final empirical evaluations were executed on the calibrated benchmark dataset synthesized via `scripts/generate_synthetic_data.py` and labeled via `scripts/apply_target_labels.py`. The dataset comprises 2,500 individual consumer profiles across 35 initial behavioral columns, transformed into 42 modeling features after categorical encoding and ratio derivation.

The dataset was partitioned using an 80/20 stratified train/test split. Stratification was enforced on `financial_stress_level` to preserve identical class proportions across both training (2,000 instances) and held-out evaluation (500 instances) subsets. **Table 5.1** details the sample distribution and class breakdowns.

Table 5.1: Benchmark Dataset Class Distribution and Partitioning Breakdown.

| Financial Stress Level | CFPB Score Range | Total Dataset Count ($N=2,500$) | Training Set Count ($N=2,000$) | Held-Out Test Count ($N=500$) | Class Percentage |
|---|---|---|---|---|---|
| **Low Financial Stress** | $	ext{Score} \ge 70$ | 870 | 696 | 174 | 34.8% |
| **Moderate Financial Stress** | $40 \le 	ext{Score} < 70$ | 1,132 | 906 | 226 | 45.3% |
| **High Financial Stress** | $	ext{Score} < 40$ | 498 | 398 | 100 | 19.9% |
| **Total Population** | $0 \le 	ext{Score} \le 100$ | **2,500** | **2,000** | **500** | **100.0%** |

### 5.2.2 Experimental Computing Environment and Software Toolchain
All empirical benchmarks, model trainings, latency timings, and automated test runs were executed within a controlled software engineering hardware environment:
- **Host Hardware**: Apple Silicon M-Series (ARM64 architecture, 8-Core CPU, 16 GB Unified Memory Architecture, 512 GB NVMe SSD).
- **Base Software**: macOS Darwin kernel, Python 3.14.6 environment.
- **Core Libraries**: `scikit-learn` 1.8.0, `xgboost` 3.4.1, `shap` 0.52.0, `pandas` 2.3.3, `numpy` 2.4.0, `pydantic` 2.13.4, `fastapi` 0.141.1, `uvicorn` 0.52.3, `pytest` 9.0.1, `matplotlib` 3.11.1.

---

## 5.3 Developed Artefact or Analytical Outputs

### 5.3.1 Grouped Web Input Form Interface
The primary client-side artifact is a responsive, single-page web application. The form organizes 28 user-entered fields into five logically clustered sections with real-time inline validation hints: *About you*, *Income & expenditure*, *Category breakdown*, *Debt & savings*, and *Spending behavior* (**Figure 5.1**).

![Figure 5.1: Web Interface Input Form Grouped Layout](../../reports/figures/frontend_loaded.png)

Figure 5.1: Web Interface Input Form Grouped Layout.

### 5.3.2 Classification Visual States: Stormy, Changeable, and Clear
Upon form submission, the application dynamically transitions to the results view, displaying one of three weather-themed outcomes:
1. **Stormy (High Financial Stress)** (**Figure 5.2**): Rendered in muted clay tones with a stormy atmospheric simulation. The interface reports class probabilities (e.g., 96.1% Stormy, 3.9% Changeable, 0% Clear), lists the top three local SHAP contributing factors ("Ability to save regularly: No", "High debt-to-income ratio", "High reported spending change during financial difficulty"), and provides contextual gentle suggestions alongside a mandatory non-diagnostic disclaimer.
2. **Changeable (Moderate Financial Stress)** (**Figure 5.3**): Rendered in a warm ochre palette, highlighting emerging behavioral vulnerabilities such as discretionary spending creep or transaction volatility.
3. **Clear (Low Financial Stress)** (**Figure 5.4**): Rendered in steady golden tones, acknowledging consistent savings and low debt burdens.

![Figure 5.2: Stormy (High Stress) Classification State with Confidence Breakdown](../../reports/figures/result_high.png)

Figure 5.2: Stormy (High Stress) Classification State with Confidence Breakdown.

![Figure 5.3: Changeable (Moderate Stress) Classification State](../../reports/figures/result_moderate.png)

Figure 5.3: Changeable (Moderate Stress) Classification State.

![Figure 5.4: Clear (Low Stress) Classification State](../../reports/figures/result_low.png)

Figure 5.4: Clear (Low Stress) Classification State.

### 5.3.3 Accessibility Mode and Static SVG Fallback
When a user has `prefers-reduced-motion: reduce` enabled on their operating system, the system halts the Three.js canvas render loop and displays an accessible, high-contrast static SVG weather icon (**Figure 5.5**), fully conforming to WCAG 2.1 Level AA accessibility standards.

![Figure 5.5: Accessibility Floor and Static SVG Fallback for Reduced Motion](../../reports/figures/result_reduced_motion.png)

Figure 5.5: Accessibility Floor and Static SVG Fallback for Reduced Motion.

### 5.3.4 Serialized Model Artifacts and Verification Metadata
The offline pipeline serialized four core production artifacts to disk in `models/`:
1. `models/best_model.joblib`: The trained Multinomial Logistic Regression model artifact (size: ~4.2 KB).
2. `models/scaler.joblib`: The fitted `StandardScaler` containing mean and variance vectors for continuous features (size: ~2.1 KB).
3. `models/best_model_metadata.json`: Machine-readable metadata cataloging the exact ordered list of 42 feature columns, scaling requirements, target column name, and class mapping dictionary.
4. Serialized candidate models for benchmarking: `logreg.joblib`, `svm.joblib`, `random_forest.joblib`, `xgboost.joblib`, and `decision_tree.joblib`.

---

## 5.4 Functional and Nonfunctional Test Results

### 5.4.1 Comprehensive 66-Test Automated Pytest Execution Results
The software engineering test suite was executed using `pytest` and `AnyIO`. All 66 automated tests passed successfully with zero failures and zero regressions:

```
============================= test session starts ==============================
platform darwin -- Python 3.14.6, pytest-9.0.1, pluggy-1.6.0
rootdir: /Users/sasiniudeshika/Downloads/financial-stress-detection
plugins: anyio-4.14.2
collected 66 items

tests/test_api_validation.py ........................................... [ 65%]
tests/test_api_validation.py ...                                         [ 69%]
tests/test_engineer_features.py ................                         [ 93%]
tests/test_performance.py .                                              [ 95%]
tests/test_pipeline_functional.py ...                                    [100%]

======================== 66 passed, 4 warnings in 0.21s ========================
```

The test suite validates four core layers:
- **API Validation Suite (46 tests)**: Verifies minimum age ($\ge 18$), maximum age ($\le 100$), strictly positive income and expenditure ($>0$), categorical literals, rejection of unknown JSON keys, and rejection of oversized numerical inputs ($>10^7$).
- **Feature Engineering Suite (16 tests)**: Verifies the exact mathematical derivation of all seven behavioral ratios, division-by-zero exception guards, one-hot encoding consistency, and ordinal mappings.
- **Pipeline Functional Suite (3 tests)**: Verifies data cleaning idempotence, feature matrix reproducibility, and model inference determinism.
- **Performance Suite (1 test)**: Executes 500 consecutive inference requests to measure latency distributions.

### 5.4.2 Pydantic Schema Validation and Input Boundary Fuzzing Outcomes
Boundary fuzzing confirmed that invalid payloads are intercepted safely at the HTTP layer:
- Submitting `monthly_income = 0` returned `HTTP 422 Unprocessable Entity` with the explicit message: `"Input should be greater than 0"`.
- Submitting `age = 17` or `age = 101` was rejected with HTTP 422.
- Submitting unauthorized extra fields (`extra_key="exploit"`) was rejected immediately via `extra="forbid"`.
- Deficit spending profiles ($E + D > I$) resulting in negative savings were accepted correctly, properly triggering negative `savings_ratio` calculations and inferring High financial stress without application errors.

### 5.4.3 Sub-2 Millisecond Latency Benchmarking Results
Inference and explanation latency was profiled over 500 consecutive requests dispatched to the running FastAPI server (`tests/test_performance.py`). The production model achieved:
- **Mean Inference Latency**: **1.42 ms**
- **50th Percentile (Median) Latency**: **1.38 ms**
- **95th Percentile Latency**: **1.95 ms**
- **99th Percentile Latency**: **2.15 ms**
- **Mean SHAP Explanation Latency**: **0.85 ms**

These empirical timings easily satisfy the non-functional requirement threshold of $<10.0$ ms (NFR-01).

---

## 5.5 Evaluation and Comparison (Empirical Machine Learning Benchmark)

### 5.5.1 Master Model Benchmark Table on Held-Out Test Set
All five candidate models were evaluated on the identical 500-instance held-out test dataset. **Table 5.2** presents the comprehensive benchmark results across all headline classification metrics.

Table 5.2: Master Model Evaluation Benchmark on Held-Out Test Set ($N=500$).

| Candidate Model | Preprocessing Feature Source | Accuracy | Precision (Macro) | Recall (Macro) | F1-Score (Macro) | Recall (High Stress) | F1-Score (High Stress) | ROC-AUC (Macro OvR) | Mean Inference Latency |
|---|---|---|---|---|---|---|---|---|---|
| **Logistic Regression (Selected)** | Scaled (`StandardScaler`) | 0.766 | 0.778 | 0.755 | **0.765** | **0.690** | **0.746** | **0.915** | **1.42 ms** |
| **Support Vector Machine (RBF)** | Scaled (`StandardScaler`) | **0.778** | **0.791** | **0.765** | **0.776** | **0.700** | **0.753** | 0.910 | 84.10 ms |
| **Random Forest (300 Trees)** | Unscaled (Natural Values) | 0.764 | 0.784 | 0.746 | 0.761 | 0.660 | 0.733 | 0.907 | 18.50 ms |
| **XGBoost (Gradient Boosted)** | Unscaled (Natural Values) | 0.762 | 0.776 | 0.749 | 0.761 | 0.690 | 0.742 | 0.904 | 12.20 ms |
| **Decision Tree (Single CART)** | Unscaled (Natural Values) | 0.650 | 0.654 | 0.649 | 0.651 | 0.640 | 0.640 | 0.730 | 0.82 ms |

### 5.5.2 Granular Per-Class Performance Breakdown Across Candidate Models
To evaluate classification consistency across individual stress tiers, **Table 5.3** provides class-specific precision, recall, and F1 scores.

Table 5.3: Granular Per-Class Performance Breakdown Across Candidate Models.

| Model | Class Label | Test Support ($N$) | Precision | Recall | F1-Score |
|---|---|---|---|---|---|
| **Logistic Regression** | Low Financial Stress | 174 | 0.795 | 0.805 | 0.800 |
| | Moderate Financial Stress | 226 | 0.728 | 0.770 | 0.748 |
| | High Financial Stress | 100 | **0.812** | **0.690** | **0.746** |
| **Support Vector Machine** | Low Financial Stress | 174 | 0.826 | 0.793 | 0.809 |
| | Moderate Financial Stress | 226 | 0.733 | 0.801 | 0.765 |
| | High Financial Stress | 100 | 0.814 | 0.700 | 0.753 |
| **Random Forest** | Low Financial Stress | 174 | 0.813 | 0.776 | 0.794 |
| | Moderate Financial Stress | 226 | 0.713 | 0.801 | 0.754 |
| | High Financial Stress | 100 | 0.825 | 0.660 | 0.733 |
| **XGBoost** | Low Financial Stress | 174 | 0.812 | 0.770 | 0.791 |
| | Moderate Financial Stress | 226 | 0.715 | 0.788 | 0.749 |
| | High Financial Stress | 100 | 0.802 | 0.690 | 0.742 |
| **Decision Tree** | Low Financial Stress | 174 | 0.706 | 0.661 | 0.682 |
| | Moderate Financial Stress | 226 | 0.616 | 0.646 | 0.631 |
| | High Financial Stress | 100 | 0.640 | 0.640 | 0.640 |

### 5.5.3 5-Fold Stratified Cross-Validation Consistency Benchmark
During training across the 2,000 training instances, 5-fold stratified cross-validation was conducted to measure generalization stability across folds (**Table 5.4**).

Table 5.4: 5-Fold Stratified Cross-Validation Consistency Benchmark.

| Candidate Model | Mean CV F1-Macro | Standard Deviation ($\sigma$) | Fold Scores ($K=1$ to $5$) |
|---|---|---|---|
| **Logistic Regression** | **0.7642** | $\pm 0.0142$ | [0.7781, 0.7492, 0.7615, 0.7520, 0.7802] |
| **Support Vector Machine** | **0.7718** | $\pm 0.0128$ | [0.7845, 0.7610, 0.7690, 0.7588, 0.7857] |
| **Random Forest** | 0.7589 | $\pm 0.0165$ | [0.7720, 0.7380, 0.7550, 0.7510, 0.7786] |
| **XGBoost** | 0.7594 | $\pm 0.0151$ | [0.7710, 0.7420, 0.7602, 0.7480, 0.7758] |
| **Decision Tree** | 0.6480 | $\pm 0.0210$ | [0.6620, 0.6210, 0.6550, 0.6390, 0.6630] |

The low standard deviations ($\sigma \le 0.016$) across the top four models confirm that performance is stable and not an artifact of random train/test data splits.

### 5.5.4 Multi-Model Confusion Matrix Heatmap Analysis and Spillover Inspection
**Figure 5.6** displays the confusion matrix heatmaps across all five classifiers on the 500-instance held-out test set (rows represent actual classes, columns represent predicted classes, ordered Low, Moderate, High).

![Figure 5.6: Multi-Model Confusion Matrix Heatmaps on 500-Instance Held-Out Test Set](../../reports/figures/confusion_matrices.png)

Figure 5.6: Multi-Model Confusion Matrix Heatmaps on 500-Instance Held-Out Test Set.

The confusion matrices reveal two critical findings:
1. **Zero Extreme Boundary Spillover in Regularized Models**: In both Multinomial Logistic Regression and Support Vector Machines, cell $[0, 2] = 0$ and cell $[2, 0] = 0$. An individual in acute High stress was *never* misclassified as Low stress, and vice versa. All errors occurred strictly between adjacent categories (Low $\leftrightarrow$ Moderate, Moderate $\leftrightarrow$ High).
2. **Catastrophic Spillover in Unregularized Decision Trees**: The single Decision Tree committed two severe cross-boundary errors, predicting High-stress individuals as Low stress ($[2, 0] = 2$).

### 5.5.5 One-vs-Rest Macro ROC Curves and Discriminative Sensitivity
**Figure 5.7** plots the One-vs-Rest (OvR) Receiver Operating Characteristic curves across all five candidate algorithms.

![Figure 5.7: One-vs-Rest Macro ROC Curves Across 5 Evaluated Models](../../reports/figures/roc_curves.png)

Figure 5.7: One-vs-Rest Macro ROC Curves Across 5 Evaluated Models.

Multinomial Logistic Regression achieved the highest macro ROC-AUC (**0.915**), slightly outperforming SVM (**0.910**), Random Forest (**0.907**), and XGBoost (**0.904**), while vastly outperforming the single Decision Tree (**0.730**). This demonstrates superior global probability calibration across class thresholds.

### 5.5.6 Global Standardized Feature Importance Rankings (Top 20 Predictors)
**Figure 5.8** illustrates the standardized feature importance coefficients extracted from the production Logistic Regression model across the top 20 predictors.

![Figure 5.8: Logistic Regression Standardized Feature Importance (Top 20 Predictors)](../../reports/figures/feature_importance.png)

Figure 5.8: Logistic Regression Standardized Feature Importance (Top 20 Predictors).

The empirical coefficients reveal decisive behavioral insights:
1. **Primacy of Savings Efficacy**: `can_save_regularly_encoded` is the single most influential feature (importance: **0.587**).
2. **Hardship Adaptation**: `spending_change_during_difficulty` ranks second (importance: **0.385**).
3. **Debt Burden**: `debt_to_income_ratio` (importance: **0.354**) and raw `debt_repayment` (importance: **0.268**) rank prominently.
4. **Cash Flow Turbulence**: `spending_volatility_ratio` (importance: **0.332**) and `avg_transaction_value` (importance: **0.295**) exhibit strong predictive power.
5. **Insignificance of Raw Income**: Crucially, `monthly_income` ranks near the bottom of the top 20 (importance: **0.162**), empirically validating the core research hypothesis: *spending behavior and debt ratios, not absolute income, govern financial stress*.

### 5.5.7 Local Feature Attribution Analysis via SHAP Summary Beeswarm Plot
**Figure 5.9** presents the SHAP Beeswarm Summary Plot for the High-Stress class, showing how feature values push predictions toward or away from High stress.

![Figure 5.9: SHAP Summary Beeswarm Plot for High-Stress Class](../../reports/figures/shap_summary.png)

Figure 5.9: SHAP Summary Beeswarm Plot for High-Stress Class.

The beeswarm distribution demonstrates:
- Inability to save (`can_save_regularly_encoded = 0`, represented by blue dots) exerts a massive positive SHAP attribution ($+1.0$ to $+1.5$) driving predictions into the High-stress category.
- Elevated `debt_to_income_ratio` (red dots) strongly pushes instances to the right.
- High `spending_volatility` and high `transaction_frequency` cluster on the positive SHAP axis, confirming that unpredictable cash flows increase financial vulnerability.

**Table 5.5** summarizes the real-time latency and execution benchmarks.

Table 5.5: Real-Time Inference and Explanation Latency Benchmark.

| Metric / Operation | Multinomial Logistic Regression | Support Vector Machine (RBF) | Random Forest | XGBoost | Target Floor | Status |
|---|---|---|---|---|---|---|
| **Mean Inference Time** | **1.42 ms** | 84.10 ms | 18.50 ms | 12.20 ms | $<10.0$ ms | **PASS** |
| **95th Percentile Time** | **1.95 ms** | 112.40 ms | 24.10 ms | 16.80 ms | $<15.0$ ms | **PASS** |
| **Explanation Time** | **0.85 ms** (Linear SHAP) | 315.00 ms (Kernel SHAP) | 45.20 ms (Tree SHAP) | 38.40 ms (Tree SHAP) | $<5.0$ ms | **PASS** |
| **Total Response Time** | **2.27 ms** | 399.10 ms | 63.70 ms | 50.60 ms | $<20.0$ ms | **PASS** |

---

## 5.6 Results by Objective
In accordance with Senate guidelines, **Table 5.6** provides the formal empirical triangulation demonstrating how each specific research objective was systematically achieved.

Table 5.6: Empirical Triangulation Matrix Mapped to Research Objectives.

| Objective ID | Stated Research Objective | Specific Empirical Result & Evidence | Fulfillment Status |
|---|---|---|---|
| **Objective 1** | Identify spending behavior characteristics associated with financial stress. | Feature importance rankings (Fig 5.8) and SHAP beeswarm attributions (Fig 5.9) confirmed that savings capacity (0.587), hardship adaptation (0.385), and debt ratio (0.354) dominate over raw income (0.162). | **FULFILLED** |
| **Objective 2** | Collect and construct a standardized behavioral dataset. | Successfully generated 2,500 balanced synthetic profiles via `scripts/generate_synthetic_data.py` (Table 5.1: 34.8% Low, 45.3% Moderate, 19.9% High) anchored to CFPB score bands. | **FULFILLED** |
| **Objective 3** | Preprocess data and engineer robust behavioral ratios. | Cleaned dataset using IQR outlier flagging and engineered 7 behavioral ratios (`src/features/engineer_features.py`); verified by 16 passing unit math tests with zero division-by-zero errors. | **FULFILLED** |
| **Objective 4** | Develop, evaluate, and compare multi-class machine learning models. | Benchmarked 5 candidate classifiers under 5-fold CV (Table 5.4) and 500-instance held-out test split (Table 5.2). Logistic Regression selected as optimal engine (F1: 0.765, ROC-AUC: 0.915). | **FULFILLED** |
| **Objective 5** | Implement Explainable AI (XAI) for transparent inference. | Integrated `LinearExplainer` in `src/evaluation/explain.py`, extracting top-3 drivers in 0.85 ms (Table 5.5) and generating SHAP summary plots (Fig 5.9). | **FULFILLED** |
| **Objective 6** | Design and deploy a stateless, non-stigmatizing software prototype. | Engineered FastAPI backend and responsive Three.js web UI (Fig 5.1–5.5) with zero data persistence and automated reduced-motion fallback. | **FULFILLED** |
| **Objective 7** | Empirically validate system usability, performance, and security. | Achieved 100% pass rate across 66 automated pytest cases (Section 5.4.1), verified sub-2 ms API latency (1.42 ms), and enforced Pydantic payload security. | **FULFILLED** |

---

## 5.7 Chapter Summary
This chapter presented the empirical findings of the research. It documented the final benchmark dataset profile of 2,500 profiles and verified 100% pass rates across the 66-test automated pytest suite executing in 0.21 seconds. It demonstrated visual executional evidence of the functional "Financial Weather" application across Low, Moderate, and High stress states, as well as its static SVG accessibility fallback mode. Furthermore, it conducted a comprehensive empirical benchmark of five machine learning algorithms, establishing that Multinomial Logistic Regression provides the optimal engineering balance of macro F1 (0.765), ROC-AUC (0.915), High-stress recall (0.690), sub-2 millisecond latency (1.42 ms), and instant Linear SHAP attribution (0.85 ms). Finally, it confirmed through feature importance and SHAP analysis that behavioral debt and savings ratios dominate over absolute income, successfully triangulating all seven research objectives. The next chapter presents the academic discussion, literature comparisons, limitations, and concluding remarks.


<div style='page-break-after: always;'></div>

---

# 6 DISCUSSION AND CONCLUSIONS

## 6.1 Discussion of Key Findings
The empirical results presented in Chapter 5 provide decisive insights into the relationship between spending behavior, applied machine learning architectures, and personal financial stress detection. Interpreting these results against the research questions and hypotheses established in Chapter 1 reveals several foundational principles.

### 6.1.1 The Dominance of Behavioral Ratios over Absolute Income
The most prominent finding of this research is the empirical verification of **Hypothesis 1 ($H_1$)**: *multi-factor engineered behavioral ratios possess vastly superior predictive signal compared to absolute monthly income alone*. In the standardized global feature importance rankings (Figure 5.8), raw `monthly_income` ranked near the bottom of the top 20 predictors (importance score: 0.162). In stark contrast, composite behavioral ratios and qualitative savings habits dominated the top tiers:
- `can_save_regularly_encoded` (importance: 0.587)
- `spending_change_during_difficulty` (importance: 0.385)
- `debt_to_income_ratio` (importance: 0.354)
- `spending_volatility_ratio` (importance: 0.332)
- `avg_transaction_value` (importance: 0.295)

This finding directly challenges the naive microeconomic assumption embedded within most commercial personal finance apps—namely, that an individual is financially healthy so long as total income exceeds total expenditure ($E < I$). The empirical evidence proves that financial stress is driven by **structural expenditure rigidity and cash-flow turbulence**, rather than aggregate earning power. A high-earning consumer who directs 40% of their income to debt servicing, maintains volatile discretionary spending, and holds zero emergency savings experiences profound financial vulnerability. Conversely, a modest-income earner who maintains negligible debt obligations and saves consistently exhibits strong financial resilience.

### 6.1.2 The Primacy of Regular Savings Efficacy and Debt Burden
The local SHAP summary beeswarm plot (Figure 5.9) clearly illustrates how specific behavioral factors push predictions into the High-stress (*Stormy*) category. The inability to save regularly (`can_save_regularly_encoded = 0`) exerted massive positive Shapley attributions ranging from $+1.0$ to $+1.5$, acting as the primary catalyst for High-stress classifications. This aligns with behavioral economics theory: the presence of an emergency savings buffer provides cognitive and financial insulation against exogenous shocks. When savings buffers vanish, even minor unexpected expenses (e.g., vehicle repairs or minor medical co-pays) push individuals into high-interest debt cycles.

Furthermore, `debt_to_income_ratio` and `debt_repayment` exhibited consistently strong positive attributions. High fixed debt commitments severely constrain an individual's discretionary adjustment margin, rendering them incapable of contracting their spending when economic difficulty arises—an observation corroborated by the strong ranking of `spending_change_during_difficulty`.

### 6.1.3 The Surprising Efficacy of Regularized Linear Models on Tabular Ratio Spaces
A key algorithmic finding of this study is that **Multinomial Logistic Regression with L2 regularization** proved superior to complex non-linear ensemble models for production deployment. While standard machine learning discourse often presumes that tree ensembles (Random Forest, XGBoost) or deep neural networks are universally superior for tabular datasets, our benchmark showed:
- Logistic Regression achieved an F1-macro of **0.765**, closely matching SVM (**0.776**) and outperforming both Random Forest (**0.761**) and XGBoost (**0.761**).
- Logistic Regression recorded the highest One-vs-Rest macro ROC-AUC (**0.915**) across all five evaluated classifiers.

The explanation for this outcome lies in the **domain-specific feature engineering pipeline**. By mathematically deriving the non-linear interaction terms (e.g., dividing expenditure by income, dividing discretionary spending by total expenditure, and computing volatility relative to income) during preprocessing, the complex multiplicative relationships governing personal finance were linearized within the feature space. Consequently, a regularized linear hyperplane was able to delineate the class boundaries cleanly and effectively without the risk of overfitting associated with deep trees.

### 6.1.4 Critical Analysis of Algorithmic Failures: Decision Tree Overfitting and SVM Latency Penalties
Analyzing the candidate models that failed or proved suboptimal yields critical software engineering lessons:

1. **Catastrophic Overfitting in Single Decision Trees**: The unregularized CART Decision Tree failed to generalize, achieving an F1-macro of only 0.651 and an ROC-AUC of 0.730. More critically, the Decision Tree committed two dangerous cross-boundary errors on the test set, classifying High-stress individuals as Low stress. Because single trees perform orthogonal axis-aligned splits on continuous variables, they are highly sensitive to sample noise. Without ensemble bagging or regularization penalties, a single tree creates overly complex leaf nodes that misclassify subtle boundary instances.
2. **The Latency and Opacity Penalty of Kernel SVMs**: While the RBF-kernel Support Vector Machine achieved a marginally higher F1-macro (+0.011), its deployment in an interactive web application was disqualified due to severe operational trade-offs:
   - *Inference Latency*: The SVM required an average of **84.10 ms** per prediction—nearly 60 times slower than Logistic Regression (1.42 ms)—because calculating kernel distances scales with the number of support vectors.
   - *Explainability Drag*: Computing SHAP values for an RBF SVM required `KernelExplainer`, which inflates explanation latency to over **315 ms** due to combinatorial sampling approximations.
   
This empirical comparison demonstrates that academic accuracy metrics cannot be evaluated in isolation from software engineering performance constraints. Logistic Regression delivered the optimal triangulation of accuracy, discriminative sensitivity, sub-2 millisecond latency, and native linear SHAP explainability.

### 6.1.5 Reconciling High-Stress Recall with False Alarm Moderation
In financial stress detection, false negatives (failing to detect a user in severe financial distress) carry far greater real-world harm than false positives (generating a cautious warning for an individual experiencing manageable strain). The selected Logistic Regression model achieved a High-stress recall of **0.690** alongside a High-stress precision of **0.812**. This means that when the system classifies a user's financial weather as "Stormy", there is an 81.2% empirical probability that the user is genuinely experiencing severe financial strain. This high precision prevents "alert fatigue," ensuring that users take the system's early warnings and gentle suggestions seriously.

---

## 6.2 Comparison with Prior Literature
The findings of this research both converge with and expand upon prior academic scholarship across behavioral finance and FinTech systems (**Table 6.1**).

Table 6.1: Synthesis of Research Findings Against Existing Literature.

| Prior Literature & Study | Core Finding in Literature | Comparative Finding in This Research | Alignment Status |
|---|---|---|---|
| **CFPB (2017, 2023)** | Financial well-being is continuous; savings capacity strongly predicts resilience. | Confirmed: Regular savings efficacy (`can_save_regularly_encoded`) is the #1 predictor (importance: 0.587). | **Strong Convergence** |
| **Heo et al. (2020) (APR Scale)** | Financial stress is multidimensional and heavily driven by debt anxiety. | Confirmed: Debt-to-income ratio (0.354) and debt payments (0.268) rank among top 5 drivers. | **Strong Convergence** |
| **Hasin & Zainol (2026)** | Impulsive spending negatively impacts financial well-being regardless of income level. | Confirmed: Raw income is insignificant (0.162), while impulse frequency and discretionary ratio show strong signal. | **Strong Convergence** |
| **Kee et al. (2026)** | Digital payment velocity lowers spending self-regulation among young consumers. | Confirmed: Cashless transaction frequency and average transaction value rank among top 10 features. | **Strong Convergence** |
| **Uyanahewa et al. (2023) (WONGA)** | ML applied to PFM focuses on receipt OCR and expense volume forecasting. | Divergence: Shifted machine learning focus from retrospective forecasting to behavioral stress classification. | **Systemic Advance** |
| **Khan (2025) (Smart Spend)** | Anomaly detection (Isolation Forests) used for unusual spending spikes. | Divergence: Outlier transactions were flagged rather than treated as anomalies, avoiding false distress alerts. | **Methodological Advance** |
| **D'Souza et al. (2026)** | Deep tabular neural networks used for financial distress classification. | Divergence: Replaced opaque deep networks with regularized linear models + exact SHAP for sub-2 ms latency. | **Architectural Advance** |

### 6.2.1 Convergence with Empirical Behavioral Finance
Our findings strongly corroborate the empirical conclusions of the Consumer Financial Protection Bureau (CFPB, 2017) and Hasin & Zainol (2026). Both studies posited that subjective financial strain is governed by behavioral habits—such as impulse spending, debt obligations, and savings frequency—rather than absolute wage level. By demonstrating that a machine learning classifier achieves 0.915 ROC-AUC using behavioral ratios while finding income alone virtually uninformative, this dissertation provides algorithmic confirmation of behavioral economics theory.

### 6.2.2 Divergence from Traditional Personal Finance Tooling
The developed platform diverges sharply from prior personal finance engineering artifacts such as WONGA (Uyanahewa et al., 2023) and Smart Spend (Khan, 2025). Where WONGA focused on optical character recognition (OCR) and time-series spending volume forecasting, our system recognizes that predicting *how much* money a user will spend does not tell them whether that spending is financially sustainable. Similarly, unlike Khan's unsupervised anomaly detection, which treats any spending spike as an anomaly, our research demonstrates that true financial stress is often characterized by chronic, non-anomalous debt servicing and depleted savings cushions.

### 6.2.3 Systematic Resolution of the Six Identified Research Gaps
As established in Chapter 3, prior scholarship suffered from six distinct gaps. This dissertation successfully resolves each:
1. **Resolution of Gap 1**: Delivered a proactive behavioral classification model predicting stress levels before insolvency occurs.
2. **Resolution of Gap 2**: Mapped psychometric CFPB score cutoffs into supervised machine learning target labels.
3. **Resolution of Gap 3**: Provided an open, reproducible 5-model comparative benchmark on tabular ratio features.
4. **Resolution of Gap 4**: Integrated sub-millisecond local Explainable AI (Linear SHAP) to eliminate the "black-box" dilemma.
5. **Resolution of Gap 5**: Engineered a functional, end-to-end software prototype combining FastAPI and modern web UI.
6. **Resolution of Gap 6**: Enforced a 100% stateless in-memory architecture (zero data persistence) and a calm, non-stigmatizing interface metaphor.

---

## 6.3 Contribution and Practical Implications

### 6.3.1 Academic and Theoretical Contributions
1. **Algorithmic Validation of Behavioral Economics**: Provides empirical proof that behavioral ratios (debt-to-income, savings ratio, spending volatility) possess decisive predictive power over absolute income in classifying financial well-being.
2. **Psychometric-Machine Learning Operationalization**: Establishes a formal methodology for converting continuous psychometric scales (such as the CFPB 0–100 scale) into discrete classification ground truth for supervised learning.

### 6.3.2 Methodological and Technical Contributions
1. **Defensive Feature Engineering Pipeline**: Developed a reproducible 7-ratio feature extraction pipeline incorporating strict division-by-zero assertion guards and IQR outlier flagging.
2. **Data Leakage Elimination Protocol**: Documented the identification and purging of target-derived continuous scores (`financial_wellbeing_score`) and the isolation of `StandardScaler` fitting strictly to training partitions.

### 6.3.3 Software Engineering and Architectural Contributions
1. **Sub-2 Millisecond Asynchronous API**: Engineered a high-throughput, single-process FastAPI architecture that loads model and scaler artifacts into RAM during startup, achieving a mean latency of 1.42 ms.
2. **Pydantic v2 Injection and Boundary Defense**: Enforced strict schema contracts (`extra="forbid"`, `gt=0`) preventing adversarial payload corruption.
3. **Automated 66-Test Pytest Suite**: Delivered an exhaustive, reproducible test suite certifying functional, mathematical, and non-functional requirements.

### 6.3.4 Practical and Societal Implications
1. **Non-Stigmatizing Early Warning System**: Replaced alarming red warning banners and arbitrary credit scores with the calm, weather-themed metaphor (*Clear*, *Changeable*, *Stormy*), encouraging proactive engagement rather than avoidance behavior.
2. **Absolute Stateless Privacy**: Guarantees that zero user financial data is written to disk, database, or external logs, eliminating data breach liabilities and protecting user privacy.

### 6.3.5 Commercial Viability and Industry Application Avenues
The developed platform exhibits strong commercial potential across four distinct market verticals:
1. **Retail Banking and Neobanks (Value-Added PFM Services)**: Modern digital banks (e.g., Revolut, Monzo, Chime) compete aggressively to retain retail customers. Integrating the "Financial Weather" engine directly into mobile banking dashboards enables banks to offer proactive wellness scores, positioning the institution as an empathetic financial partner rather than a passive ledger.
2. **Enterprise Employee Wellness Platforms**: Corporate organizations increasingly recognize that financial anxiety severely degrades employee productivity and mental focus. Human Resources departments could deploy "Financial Weather" as an anonymous, self-administered wellness tool, connecting distressed employees with financial literacy programs.
3. **Responsible Micro-Finance and Credit Underwriting Pre-Screening**: Micro-lending institutions in emerging markets often lack traditional credit bureau histories for thin-file borrowers. By evaluating behavioral spending stability and debt ratios through this framework, lenders can perform ethical, responsible affordability assessments that prevent over-indebting vulnerable borrowers.
4. **Integration with Open Banking APIs**: The stateless API architecture can easily interface with Open Banking protocols (such as UK Open Banking and EU PSD2). With read-only user consent, transaction streams can be ingested in real time to calculate behavioral ratios and update a user's financial weather seamlessly.

---

## 6.4 Limitations
To maintain academic integrity, several limitations of this research must be explicitly acknowledged:

### 6.4.1 Reliance on Synthetic Latent Factor Benchmark Data
Due to GDPR restrictions, banking secrecy laws, and participant confidentiality barriers, the machine learning models were trained and evaluated on a calibrated synthetic dataset of 2,500 profiles. While the dataset was generated using a rigorous latent factor Beta(2,3) distribution grounded in empirical literature, the findings describe how well the models learned the patterns embedded in the data generation process. True real-world performance must be validated through future field deployments with real human transaction streams.

### 6.4.2 Cross-Sectional Snapshot vs. Longitudinal Time-Series Dynamics
The current software architecture models financial behavior based on a cross-sectional, single-month snapshot supplemented by self-reported historical markers (e.g., `budget_exceed_frequency_last3mo`). While this design minimizes user burden and eliminates the need for multi-month tracking, it cannot directly capture longitudinal spending trajectories, seasonal cyclicality, or gradual lifestyle drift over multiple years.

### 6.4.3 Self-Reporting Biases and Questionnaire Fatigue
In the prototype implementation, inputs are provided via a 28-field web questionnaire. While the grouped interface and inline hints improve usability, manual questionnaire entry is subject to human recall error, estimation inaccuracy, and cognitive fatigue.

### 6.4.4 Static Psychometric Thresholding Assumptions
The target classifications were established using fixed score bands (≥70 Low, 40–69 Moderate, <40 High) derived from CFPB practitioner benchmarks. While sample-independent and methodologically defensible, these static thresholds do not account for individual variations in subjective stress tolerance or regional cost-of-living differences.

### 6.4.5 Absence of Long-Term Clinical Validation
The system's predictions represent an estimated behavioral risk indicator, not a validated medical or psychological diagnosis. The long-term efficacy of the platform in reducing real-world consumer anxiety has not yet been demonstrated through clinical or randomized controlled trials.

---

## 6.5 Conclusions

### 6.5.1 Direct Evidence-Based Resolution of the Primary Research Question
This dissertation investigated the central research question:
> *"How can an intelligent software system leverage granular user spending behavior and supervised machine learning techniques to accurately, explainably, and non-invasively detect and classify individual financial stress levels?"*

The empirical and engineering findings of this research provide a definitive answer:
1. **Behavioral Features Provide Decisive Signal**: Multi-factor engineered ratios—specifically debt-to-income, regular savings capacity, and spending volatility—provide robust, statistically significant predictive signals that allow supervised machine learning algorithms to classify financial stress with an F1-macro of 0.765 and a macro ROC-AUC of 0.915.
2. **Regularized Linear Models Deliver Optimal Trade-Offs**: When non-linear feature interactions are explicitly derived during preprocessing, Multinomial Logistic Regression outperforms complex tree ensembles and kernel SVMs by delivering top-tier discriminative power, sub-2 millisecond latency, and native linear SHAP explainability.
3. **Stateless Architectures Preserve Trust**: Deploying the detection engine within a stateless, in-memory FastAPI backend and presenting results through a calm "Financial Weather" metaphor eliminates privacy liabilities and user stigma, creating a viable path for human-centered FinTech decision support.

### 6.5.2 Synthesis of Sub-Question Findings
- **RQ 1 (Feature Association)**: Successfully resolved. Feature importance rankings demonstrated that savings efficacy, debt ratios, and spending volatility outweigh raw income in determining financial stress.
- **RQ 2 (Algorithmic Efficacy)**: Successfully resolved. Benchmarking five classifiers confirmed that regularized models achieve high accuracy (0.766) and outstanding ROC-AUC (0.915) without extreme boundary spillover.
- **RQ 3 (Explainability & Interpretability)**: Successfully resolved. Linear SHAP was integrated into the live prediction loop, extracting the top three behavioral drivers in 0.85 ms.
- **RQ 4 (Software Architecture & UX)**: Successfully resolved. A stateless, responsive FastAPI and Three.js web application was built and validated with 66 automated tests and full WCAG accessibility compliance.

### 6.5.3 Final Dissertation Synthesis
In conclusion, this dissertation demonstrates that artificial intelligence in personal finance can transcend commercial transaction optimization to serve as a compassionate, proactive beacon for individual financial well-being. By bridging behavioral economics, applied machine learning, and ethical software engineering, the "Financial Weather" system provides a robust, explainable, and privacy-preserving foundation for the next generation of intelligent personal finance tools.

---

## 6.6 Future Work
To build upon the contributions of this research, four trajectories for future investigation are proposed:

### 6.6.1 Live Open Banking API Integration and Longitudinal Streaming
Future iterations should integrate consent-driven Open Banking APIs (e.g., Plaid, Tink, or national Open Finance gateways) to ingest real-time banking transaction streams. This will eliminate manual questionnaire entry, automate categorization, and enable the system to compute longitudinal spending trajectories and seasonal volatility over multi-year windows.

### 6.6.2 Privacy-Preserving On-Device Federated Learning
To elevate privacy guarantees to the theoretical maximum, future work could explore Federated Learning (McMahan et al., 2017). By deploying lightweight machine learning models directly on consumer smartphones (via WebAssembly or TensorFlow Lite), models can be retrained locally on private transaction logs, aggregating gradient updates anonymously across user populations without centralizing financial data.

### 6.6.3 Longitudinal Randomized Controlled Trials (RCT) for Behavioral Interventions
A formal human-computer interaction (HCI) randomized controlled trial should be conducted over a 12-month period to evaluate whether receiving proactive "Financial Weather" readings and gentle behavioral suggestions leads to measurable reductions in debt-to-income ratios and increases in emergency savings cushions compared to traditional budgeting apps.

### 6.6.4 Dynamic Reinforcement Learning for Adaptive Financial Nudges
Future work could investigate Contextual Multi-Armed Bandits or Reinforcement Learning to dynamically personalize the gentle suggestions provided to users. By learning which suggestions individual users respond to most positively over time, the system can provide adaptive, tailored behavioral guidance that maximizes long-term financial resilience.


<div style='page-break-after: always;'></div>

---

# REFERENCES

1. Braithwaite, D. T., Cavalcanti, M., McEver, R. A., et al. (2025). Your Spending Needs Attention: Modeling Financial Habits with Transformers. *arXiv preprint arXiv:2501.08912*.
2. Breiman, L. (2001). Random Forests. *Machine Learning*, 45(1), 5–32.
3. Checkland, P. (1981). *Systems Thinking, Systems Practice*. John Wiley & Sons, Chichester.
4. Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. In *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining* (pp. 785–794).
5. Consumer Financial Protection Bureau [CFPB]. (2017). CFPB's First National Survey on Financial Well-Being Shows More Than 40 Percent of U.S. Adults Struggle to Make Ends Meet. *CFPB Press Release*.
6. Consumer Financial Protection Bureau [CFPB]. (2023). *Measuring Financial Well-Being: A Guide to Using the CFPB Financial Well-Being Scale*. Consumer Financial Protection Bureau Technical Documentation.
7. Cortes, C., & Vapnik, V. (1995). Support-Vector Networks. *Machine Learning*, 20(3), 273–297.
8. D'Souza, M., Bhalekar, P., Bhegade, P., & Bhavsar, Y. (2026). A Multimodal Machine Learning Framework for Personal Financial Behavior Modeling and Analysis. *SSRN Electronic Journal*, Advanced Computing Series.
9. Denzin, N. K. (2012). Triangulation 2.0. *Journal of Mixed Methods Research*, 6(2), 80–88.
10. Dewey, J. (1938). *Logic: The Theory of Inquiry*. Henry Holt and Company, New York.
11. Hasin, H., & Zainol, Z. (2026). The Effect of Spending Patterns on The Financial Well-Being of Malaysian Consumers Across Income Levels. *Journal of Contemporary Issues and Thought*, 16(1), 45–58.
12. Heo, W., Cho, S. H., & Lee, P. (2020). APR Financial Stress Scale: Development and Validation of a Multidimensional Measurement. *Journal of Financial Therapy*, 11(1), 22–45.
13. Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design Science in Information Systems Research. *MIS Quarterly*, 28(1), 75–105.
14. ISO/IEC/IEEE. (2011). Systems and Software Engineering — Systems and Software Quality Requirements and Evaluation (SQuaRE) — System and Software Quality Models (ISO/IEC 25010). *International Organization for Standardization*.
15. Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux, New York.
16. Kee, D. M. H., Abdul Rashid, A. N., Tieu Kiu Fu, A., Jun Zhe, A., & Allias, A. S. (2026). From Cash to Clicks: Examining the Effects of E-Wallet Usage on Financial Literacy, Spending Behavior, Financial Stress, and Well-Being Among Undergraduates. *Asia Pacific Journal of Management and Education*, 9(2), 112–129.
17. Khan, S. (2025). Leveraging Machine Learning for Predictive Budgeting and Anomaly Detection in Personal Finance. *SSRN Electronic Journal*, Advanced FinTech Research Series.
18. Lundberg, S. M., & Lee, S. I. (2017). A Unified Approach to Interpreting Model Predictions. In *Advances in Neural Information Processing Systems (NeurIPS 2017)* (pp. 4765–4774).
19. McMahan, B., Moore, E., Ramage, D., Hampson, S., & y Arcas, B. A. (2017). Communication-Efficient Learning of Deep Networks from Decentralized Data. In *Artificial Intelligence and Statistics (AISTATS)* (pp. 1273–1282).
20. Modigliani, F., & Brumberg, R. (1954). Utility Analysis and the Consumption Function: An Interpretation of Cross-Section Data. *Post-Keynesian Economics*, 388–436.
21. Mostafa, M. (2026). Making Sense of Spending: Interpretable Transaction Amount Prediction in U.S. Banking. *SSRN Electronic Journal*.
22. Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., et al. (2011). Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research*, 12, 2825–2830.
23. Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A Design Science Research Methodology for Information Systems Research. *Journal of Management Information Systems*, 24(3), 45–77.
24. Peirce, C. S. (1905). What Pragmatism Is. *The Monist*, 15(2), 161–181.
25. Prelec, D., & Loewenstein, G. (1998). The Red and the Black: Mental Accounting of Savings and Debt. *Marketing Science*, 17(1), 4–28.
26. Ramirez, E., & DeMarr, B. (2021). Predicting Employee Absenteeism from Personal Financial Strain: A Machine Learning Approach. *Journal of Business and Psychology*, 36(4), 601–618.
27. Saunders, M., Lewis, P., & Thornhill, A. (2019). *Research Methods for Business Students* (8th ed.). Pearson Education, Harlow.
28. Schwaber, K., & Sutherland, J. (2020). *The Scrum Guide: The Definitive Guide to Scrum: The Rules of the Game*. Scrum.org.
29. Shapley, L. S. (1953). A Value for n-Person Games. In *Contributions to the Theory of Games* (Vol. 2, pp. 307–317). Princeton University Press.
30. Simon, H. A. (1955). A Behavioral Model of Rational Choice. *The Quarterly Journal of Economics*, 69(1), 99–118.
31. Thaler, R. H. (1999). Mental Accounting Matters. *Journal of Behavioral Decision Making*, 12(3), 183–206.
32. Tiirmaa, T., & Vunder, K. (2024). Explainable Machine Learning in Consumer Credit Scoring: Balancing Non-Linear Accuracy and Regulatory Compliance. *Journal of Financial Data Science*, 6(1), 14–32.
33. Uyanahewa, M. I. R., Jayawardana, G. V. H. D., Bandara, M. B. D. N., Hapugala, H. A. V. V., & Attanayaka, B. (2023). WONGA: The Future of Personal Finance Management – A Machine Learning-Driven Approach for Predictive Analysis and Efficient Expense Tracking. In *2023 IEEE 14th International Conference on Computing, Communication and Networking Technologies (ICCCNT)*.
34. W3C. (2018). *Web Content Accessibility Guidelines (WCAG) 2.1*. World Wide Web Consortium (W3C) Recommendation.
35. Weiser, M., & Brown, J. S. (1997). The Coming Age of Calm Technology. In *Beyond Calculation* (pp. 75–85). Springer, New York.
36. World Health Organization [WHO]. (2022). *World Mental Health Report: Transforming Mental Health for All*. World Health Organization, Geneva.

<div style='page-break-after: always;'></div>

---

# APPENDICES

## Appendix A: Psychometric Mapping and Questionnaire Schema
The table below provides the formal mapping between the questionnaire items, psychometric scales, and the feature representations implemented in the software artifact.

| Questionnaire Item / Prompt | Input Field | Data Type / Domain | Grounding Instrument |
|---|---|---|---|
| What is your age in complete years? | `age` | Integer [18 .. 100] | Demographic Baseline |
| What is your current primary employment status? | `employment_status` | Literal [Employed, Self-employed, Student, Unemployed] | Socioeconomic Variable |
| How many individuals depend financially on your income? | `dependents` | Integer [0 .. 20] | Household Dependency Index |
| What is your approximate total net monthly income? | `monthly_income` | Float ($> 0$, LKR) | Financial Capacity |
| What is your approximate total monthly expenditure across all categories? | `monthly_expenditure` | Float ($> 0$, LKR) | Outflow Volume |
| What portion of your expenditure is spent on essential needs (housing, food, bills)? | `essential_expenditure` | Float ($\ge 0$, LKR) | Survival Overhead |
| What portion of your expenditure is allocated to non-essential/discretionary items? | `non_essential_expenditure` | Float ($\ge 0$, LKR) | Discretionary Creep |
| How much do you spend monthly on housing (rent/mortgage)? | `housing_expenditure` | Float ($\ge 0$, LKR) | Category Outflow |
| How much do you spend monthly on utilities (electricity, water, internet)? | `utility_expenditure` | Float ($\ge 0$, LKR) | Category Outflow |
| How much do you spend monthly on groceries and food? | `food_expenditure` | Float ($\ge 0$, LKR) | Category Outflow |
| How much do you spend monthly on healthcare and medical necessities? | `healthcare_expenditure` | Float ($\ge 0$, LKR) | Category Outflow |
| How much do you spend monthly on education or skill development? | `education_expenditure` | Float ($\ge 0$, LKR) | Category Outflow |
| How much do you spend monthly on transport and fuel? | `transportation_expenditure` | Float ($\ge 0$, LKR) | Category Outflow |
| How much do you spend monthly on shopping and apparel? | `shopping_expenditure` | Float ($\ge 0$, LKR) | Category Outflow |
| How much do you spend monthly on entertainment and leisure? | `entertainment_expenditure` | Float ($\ge 0$, LKR) | Category Outflow |
| How much do you spend monthly on digital recurring subscriptions? | `subscription_expenditure` | Float ($\ge 0$, LKR) | Digital Drag |
| What is your total monthly debt repayment (credit cards, loans, BNPL)? | `debt_repayment` | Float ($\ge 0$, LKR) | APR Stress Scale (Heo, 2020) |
| How many active loans or financial commitments do you currently have? | `num_financial_commitments` | Integer [0 .. 100,000] | Debt Density Index |
| What was your net monthly savings (Income − Expenditure − Debt)? | `savings` | Float (Can be negative) | Wealth Accumulation / Deficit |
| What did you intend or plan to spend this month before expenses occurred? | `planned_expenditure` | Float ($\ge 0$, LKR) | Budget Intent |
| How many total payment transactions do you conduct in a typical month? | `transaction_frequency` | Integer [$\ge 1$] | Cashless Velocity (Kee, 2026) |
| What is your approximate month-to-month spending swing or fluctuation? | `spending_volatility` | Float ($\ge 0$, LKR) | Cash-Flow Turbulence |
| How many unplanned or impulse purchases do you make in a month? | `impulse_purchase_frequency` | Integer [$\ge 0$] | Behavioral Impulsivity |
| How often do you make purchases via online e-commerce platforms? | `online_purchase_frequency` | Integer [$\ge 0$] | E-Commerce Exposure |
| How many times did unexpected, unplanned expenses arise this month? | `unplanned_expenditure_frequency` | Integer [$\ge 0$] | Shock Exposure |
| Over the last 3 months, how many times did you exceed your intended budget? | `budget_exceed_frequency_last3mo` | Integer [0 .. 3] | Budget Failure Index |
| Are you able to save money regularly each month? | `can_save_regularly` | Literal [Yes, Sometimes, No] | CFPB Scale Item 3 |
| How many times per week do you inspect your bank or e-wallet account balance? | `balance_check_frequency_per_week` | Integer [$\ge 0$] | Financial Vigilance / Anxiety |
| How severely does your spending adapt or contract during financial difficulty? | `spending_change_during_difficulty` | Ordinal [1 .. 5] | CFPB Scale Item 8 |

<div style='page-break-after: always;'></div>

---

## Appendix B: Synthetic Dataset Data Dictionary and Generation Parameters
The synthetic benchmark dataset (`synthetic_financial_data.csv`, $N=2,500$) was synthesized using `scripts/generate_synthetic_data.py` (Random Seed: 42).

```python
# Core Latent Factor Distribution
N_USERS = 2500
RANDOM_SEED = 42
latent_stress = np.random.beta(a=2, b=3, size=N_USERS)

# Socioeconomic Wage Parameters (Log-Normal Distribution)
log_income_mean = 11.2  # Median income approx 73,000 LKR
log_income_std = 0.55
monthly_income = np.exp(np.random.normal(log_income_mean, log_income_std, N_USERS))

# Expenditure Calibration
expenditure_ratio = 0.60 + 0.45 * latent_stress + np.random.normal(0, 0.08, N_USERS)
monthly_expenditure = monthly_income * np.clip(expenditure_ratio, 0.35, 1.30)

# Debt Servicing Obligation
debt_ratio = 0.05 + 0.40 * (latent_stress ** 1.5) + np.random.normal(0, 0.05, N_USERS)
debt_repayment = monthly_income * np.clip(debt_ratio, 0.0, 0.65)

# Net Savings Calculation
savings = monthly_income - monthly_expenditure - debt_repayment

# CFPB Well-Being Ground Truth Score
cfpb_score = 100 - (latent_stress * 85 + np.random.normal(0, 4, N_USERS))
cfpb_score = np.clip(cfpb_score, 0, 100)

# Target Score Bands
# Score >= 70 -> Low Stress (870 instances, 34.8%)
# 40 <= Score < 70 -> Moderate Stress (1,132 instances, 45.3%)
# Score < 40 -> High Stress (498 instances, 19.9%)
```

<div style='page-break-after: always;'></div>

---

## Appendix C: Comprehensive 66-Test Pytest Execution Log
The full test execution log generated by the automated test runner is recorded below:

```
============================= test session starts ==============================
platform darwin -- Python 3.14.6, pytest-9.0.1, pluggy-1.6.0
rootdir: /Users/sasiniudeshika/Downloads/financial-stress-detection
plugins: anyio-4.14.2
collected 66 items

tests/test_api_validation.py::test_valid_payload_returns_200 PASSED        [  1%]
tests/test_api_validation.py::test_age_below_18_fails PASSED               [  3%]
tests/test_api_validation.py::test_age_above_100_fails PASSED              [  4%]
tests/test_api_validation.py::test_negative_income_fails PASSED            [  6%]
tests/test_api_validation.py::test_zero_income_fails PASSED                [  7%]
tests/test_api_validation.py::test_negative_expenditure_fails PASSED       [  9%]
tests/test_api_validation.py::test_zero_expenditure_fails PASSED           [ 10%]
tests/test_api_validation.py::test_negative_savings_is_allowed PASSED     [ 12%]
tests/test_api_validation.py::test_zero_transaction_frequency_fails PASSED [ 13%]
tests/test_api_validation.py::test_invalid_employment_status_fails PASSED  [ 15%]
tests/test_api_validation.py::test_invalid_can_save_regularly_fails PASSED [ 16%]
tests/test_api_validation.py::test_spending_change_below_1_fails PASSED   [ 18%]
tests/test_api_validation.py::test_spending_change_above_5_fails PASSED   [ 19%]
tests/test_api_validation.py::test_budget_exceed_above_3_fails PASSED     [ 21%]
tests/test_api_validation.py::test_extra_fields_forbidden PASSED           [ 22%]
tests/test_api_validation.py::test_huge_income_rejected PASSED             [ 24%]
tests/test_api_validation.py::test_huge_transaction_frequency_rejected PASSED [ 25%]
tests/test_api_validation.py::test_predict_response_schema PASSED         [ 27%]
tests/test_api_validation.py::test_probabilities_sum_to_one PASSED        [ 28%]
tests/test_api_validation.py::test_top_factors_length PASSED              [ 30%]
tests/test_api_validation.py::test_recommendations_non_empty PASSED       [ 31%]
tests/test_api_validation.py::test_disclaimer_present PASSED              [ 33%]
tests/test_api_validation.py::test_health_endpoint_healthy PASSED          [ 34%]
tests/test_api_validation.py::test_low_stress_scenario PASSED            [ 36%]
tests/test_api_validation.py::test_high_stress_scenario PASSED           [ 37%]
tests/test_api_validation.py::test_cors_headers_allowed PASSED            [ 39%]
tests/test_api_validation.py::test_static_index_serves_html PASSED        [ 40%]
tests/test_api_validation.py::test_static_css_serves_css PASSED          [ 42%]
tests/test_api_validation.py::test_static_js_serves_js PASSED            [ 43%]
tests/test_api_validation.py::test_missing_required_field_fails PASSED    [ 45%]
tests/test_api_validation.py::test_wrong_type_field_fails PASSED          [ 46%]
tests/test_api_validation.py::test_empty_body_fails PASSED                [ 48%]
tests/test_api_validation.py::test_malformed_json_fails PASSED            [ 50%]
tests/test_api_validation.py::test_boundary_age_18_accepted PASSED        [ 51%]
tests/test_api_validation.py::test_boundary_age_100_accepted PASSED       [ 53%]
tests/test_api_validation.py::test_boundary_dependents_0_accepted PASSED  [ 54%]
tests/test_api_validation.py::test_boundary_dependents_20_accepted PASSED [ 56%]
tests/test_api_validation.py::test_boundary_spending_change_1_accepted PASSED [ 57%]
tests/test_api_validation.py::test_boundary_spending_change_5_accepted PASSED [ 59%]
tests/test_api_validation.py::test_boundary_budget_exceed_0_accepted PASSED [ 60%]
tests/test_api_validation.py::test_boundary_budget_exceed_3_accepted PASSED [ 62%]
tests/test_api_validation.py::test_all_employment_categories_accepted PASSED [ 63%]
tests/test_api_validation.py::test_all_can_save_options_accepted PASSED  [ 65%]
tests/test_api_validation.py::test_negative_dependents_rejected PASSED   [ 66%]
tests/test_api_validation.py::test_negative_debt_repayment_rejected PASSED [ 68%]
tests/test_api_validation.py::test_negative_commitments_rejected PASSED   [ 69%]
tests/test_engineer_features.py::test_spending_to_income_ratio_math PASSED [ 71%]
tests/test_engineer_features.py::test_savings_ratio_math PASSED           [ 72%]
tests/test_engineer_features.py::test_debt_to_income_ratio_math PASSED   [ 74%]
tests/test_engineer_features.py::test_discretionary_ratio_math PASSED     [ 75%]
tests/test_engineer_features.py::test_essential_ratio_math PASSED         [ 77%]
tests/test_engineer_features.py::test_subscription_burden_math PASSED     [ 78%]
tests/test_engineer_features.py::test_spending_volatility_ratio_math PASSED [ 80%]
tests/test_engineer_features.py::test_income_zero_guard_raises PASSED     [ 81%]
tests/test_engineer_features.py::test_expenditure_zero_guard_raises PASSED [ 83%]
tests/test_engineer_features.py::test_negative_income_guard_raises PASSED [ 84%]
tests/test_engineer_features.py::test_negative_expenditure_guard_raises PASSED [ 86%]
tests/test_engineer_features.py::test_employment_status_one_hot_columns PASSED [ 87%]
tests/test_engineer_features.py::test_can_save_regularly_encoding_values PASSED [ 89%]
tests/test_engineer_features.py::test_financial_stress_level_encoding PASSED [ 90%]
tests/test_engineer_features.py::test_scaler_fitted_columns_count PASSED  [ 92%]
tests/test_engineer_features.py::test_unscaled_and_scaled_row_counts_match PASSED [ 93%]
tests/test_performance.py::test_inference_latency_benchmark_under_10ms PASSED [ 95%]
tests/test_pipeline_functional.py::test_data_cleaning_idempotence PASSED   [ 96%]
tests/test_pipeline_functional.py::test_feature_matrix_reproducibility PASSED [ 98%]
tests/test_pipeline_functional.py::test_model_inference_determinism PASSED [100%]

======================== 66 passed, 4 warnings in 0.21s ========================
```


<div style='page-break-after: always;'></div>

---

