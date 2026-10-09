"""Chapter 2: Objectives Module for Honours Thesis.
Conforms strictly to Senate approved structure:
2.1 General objective or aim
2.2 Specific objectives (matched to method and result)
"""

CONTENT = """# 2 OBJECTIVES

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
"""
