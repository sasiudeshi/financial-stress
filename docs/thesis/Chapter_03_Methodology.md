# CHAPTER 03: METHODOLOGY

## 3.1 Research Paradigm Justification: Pragmatism and Positivism
In software engineering and applied artificial intelligence research, the underlying research philosophy dictates how the investigator conceptualizes reality (ontology), acquires valid knowledge (epistemology), and values human purpose (axiology) (Saunders et al., 2019). The academic inquiry undertaken in this dissertation is fundamentally situated within the philosophical paradigm of **Pragmatism**, complemented by operational elements of **Positivism**.

### Ontological and Epistemological Justification
Classical research paradigms often enforce a rigid dichotomy:
- **Positivism** asserts that an objective, measurable reality exists independently of human observation. Knowledge is acquired through empirical observation, deductive hypothesis testing, mathematical modeling, and statistical verification.
- **Interpretivism** contends that reality is socially constructed through subjective meanings, human perceptions, and lived cultural experiences, rejecting purely mathematical reductionism.

While financial well-being undeniably possesses subjective psychological qualities (as an individual's personal perception of stress), the primary objective of this dissertation is not merely to describe human sentiment. Rather, it is to **engineer an intelligent, functional software artifact** capable of acting upon empirical data to solve a concrete real-world problem. 

**Pragmatism** (Dewey, 1938; Peirce, 1905) rejects unhelpful philosophical dogmatism. It posits that the truth, validity, and value of a theory or software system are determined by its practical consequences, operational utility, and real-world efficacy. Under a pragmatist paradigm, the researcher integrates diverse methodological tools—combining mathematical feature engineering, algorithmic benchmarking, human-centered user experience design, and ethical reflection—to address complex problems.

Simultaneously, the quantitative and algorithmic evaluation of machine learning models demands strict **Positivist rigor**. The predictive efficacy of candidate classifiers (Logistic Regression, Support Vector Machines, Random Forests, XGBoost, Decision Trees) cannot be evaluated subjectively; it must be quantified using immutable statistical metrics, including Accuracy, Precision, Recall, F1-Scores, Confusion Matrices, and Area Under the Receiver Operating Characteristic Curve (ROC-AUC). 

Therefore, this research adopts a **Pragmatist-Positivist synergy**:
1. *Positivist Epistemology*: Applied to data preprocessing, outlier detection, supervised model training, and quantitative performance evaluation.
2. *Pragmatist Axiology*: Applied to the human-centered translation of model predictions into non-stigmatizing visual metaphors ("Financial Weather"), local explainability attributions (SHAP), and actionable, gentle behavioral nudges.

---

## 3.2 Research Approach: Deductive Reasoning and Empirical Investigation
Research approaches are broadly categorized into inductive, deductive, and abductive strategies:
- **Inductive Approach**: Begins with open-ended observations to construct new theoretical models or discover emerging patterns.
- **Deductive Approach**: Originates from established theories and conceptual frameworks, formulates specific hypotheses or engineering requirements, and subjects them to empirical testing.

This study rigorously follows a **Deductive Empirical Approach**. 

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
2. **Operational Hypothesis Formulation**: The study hypothesizes that:
   - *Hypothesis 1 ($H_1$)*: Engineered behavioral ratios (e.g., debt-to-income, discretionary spending ratio, spending volatility) contain superior predictive power for detecting financial stress compared to absolute income alone.
   - *Hypothesis 2 ($H_2$)*: Regularized multi-class machine learning models can classify financial stress levels with an F1-macro score exceeding 0.75 and an ROC-AUC exceeding 0.90.
   - *Hypothesis 3 ($H_3$)*: Explainable AI mechanisms (SHAP) can extract faithful, interpretable local feature drivers without violating real-time API latency thresholds (<10 ms).
3. **Artifact Construction and Verification**: Machine learning models and software architectures are implemented to operationalize these hypotheses.
4. **Empirical Verification**: The hypotheses are subjected to rigorous empirical testing on a held-out test dataset, validating or falsifying the architectural and algorithmic decisions.

---

## 3.3 Research Strategy: Design Science Research (DSR)
Given that the primary deliverable of this dissertation is an innovative, functional software solution, the research adopts **Design Science Research (DSR)** as its overarching research strategy (Hevner et al., 2004).

Unlike traditional behavioral science, which seeks to *explain and predict* natural or organizational phenomena, Design Science Research seeks to *create and evaluate* purposeful information technology artifacts designed to solve identified business and human problems. As articulated by Hevner et al. (2004), an IT artifact encompasses constructs (conceptual vocabularies), models (mathematical representations), methods (algorithmic pipelines), and instantiations (functional, running software systems).

This dissertation delivers all four DSR artifact dimensions:
- **Constructs**: Standardized behavioral spending concepts and psychometric stress categories (*Low*, *Moderate*, *High*).
- **Models**: Calibrated latent factor data models and multi-class classification mathematical formulations.
- **Methods**: The 13-stage reproducible data preprocessing, feature engineering, and SHAP attribution pipeline.
- **Instantiation**: The working **"Financial Weather"** software prototype, comprising the FastAPI asynchronous backend, Pydantic data validation layer, and interactive WebGL/SVG user interface.

---

## 3.4 Fact Collection and Data Generation Mechanisms
A critical imperative of any machine learning research is establishing high-integrity, representative data. 

### 3.4.1 Primary Data Collection Architecture & Instrument Design
The conceptual design of this research includes a comprehensive, non-invasive primary questionnaire instrument based on the CFPB Financial Well-Being Scale and behavioral finance literature. The instrument captures:
1. **Demographic Indicators**: Age, employment category, and number of financial dependents.
2. **Core Financial Aggregates**: Monthly income, total monthly expenditure, essential expenditure, discretionary expenditure, debt repayments, and savings.
3. **10-Category Breakdown**: Housing, utilities, food/groceries, healthcare, education, transportation, shopping, entertainment, subscription services, and other miscellaneous outlays.
4. **Behavioral Markers**: Transaction frequencies, impulse purchasing habits, online shopping intensity, budget deviation frequency over the past three months, regular saving ability, account checking frequency, and reported spending adaptations during financial difficulty.

### 3.4.2 Latent Factor Model for Synthetic Population Generation
While primary questionnaire data collection remains the gold standard, real-world personal financial data is severely restricted by privacy regulations (GDPR, CCPA), banking security barriers, and the pervasive reluctance of human participants to disclose sensitive income and debt figures. Furthermore, academic research timelines require an immediate, reproducible benchmark dataset to develop and validate the machine learning architecture.

To resolve this challenge ethically and rigorously, a **latent factor data generation model** was developed (`scripts/generate_synthetic_data.py`). Rather than randomly fabricating values or using naive uniform distributions, the generator simulates 2,500 realistic user profiles anchored to a hidden, continuous financial stress latent variable $s \in [0, 1]$.

#### Mathematical Formulation of Latent Stress
The hidden stress factor $s$ is drawn from a Beta distribution:
$$s \sim \text{Beta}(\alpha = 2, \beta = 3)$$

The shape parameters $\alpha = 2, \beta = 3$ induce a right-skewed distribution across the synthetic population. This accurately mirrors real-world socioeconomic demographics: the majority of individuals cluster around low-to-moderate financial stress, while an acute minority experiences extreme financial strain ($s > 0.8$).

#### Calibrated Feature Generation with Stochastic Noise
Every observable behavioral feature $x_i$ is mathematically modeled as a monotonic function of latent stress $s$, perturbed by independent Gaussian noise $\epsilon \sim \mathcal{N}(0, \sigma^2)$ to reflect natural human behavioral variability:
1. **Monthly Income ($I$)**: Generated from a log-normal distribution to reflect national income wage dispersion:
   $$I = \exp\left(\mu_{\ln} + \sigma_{\ln} \cdot \mathcal{N}(0, 1)\right)$$
   Crucially, income is deliberately given a near-zero direct correlation with latent stress $s$. This operationalizes the core research thesis: *high income does not preclude severe financial stress, nor does modest income guarantee distress*.
2. **Monthly Expenditure ($E$)**: Function of income, modulated by latent stress:
   $$E = I \cdot \left(0.60 + 0.45 \cdot s + \mathcal{N}(0, 0.08)\right)$$
3. **Debt Repayments ($D$)**: Positively correlated with latent stress:
   $$D = I \cdot \left(0.05 + 0.40 \cdot s^{1.5} + \mathcal{N}(0, 0.05)\right)$$
4. **Savings ($S$)**: Formulated as the exact accounting balance:
   $$S = I - E - D$$
   *Note*: Savings can become **negative**, representing deficit spending and credit-fueled debt accumulation.
5. **Behavioral Indicators**:
   - `can_save_regularly`: Stochastically assigned based on $s$; high stress strongly favors "No", whereas low stress favors "Yes".
   - `impulse_purchase_frequency`: $\lambda = 2 + 8 \cdot s$.
   - `spending_volatility`: Increases non-linearly with $s$.
   - `spending_change_during_difficulty`: Scaled from 1 to 5, where high-stress individuals report severe disruption.

```
+-------------------------------------------------------------------------------+
|                      LATENT STRESS FACTOR s ~ Beta(2,3)                       |
+-------------------------------------------------------------------------------+
         |                                |                               |
         v                                v                               v
+------------------+            +-------------------+           +---------------+
| Financial Flows  |            | 10-Category Split |           |  Behavioral   |
| - Income (LogN)  |            | - Housing, Food   |           |  Indicators   |
| - Expenditure(s) |            | - Utilities, Debt |           | - Impulse Freq|
| - Debt Service(s)|            | - Discretionary   |           | - Can Save Reg|
| - Savings (I-E-D)|            | - Subscriptions   |           | - Volatility  |
+------------------+            +-------------------+           +---------------+
         \                                |                               /
          \                               |                              /
           v                              v                             v
+-------------------------------------------------------------------------------+
|              CFPB Financial Well-Being Score = 100 - (s * 85 + e)             |
|                  Low (>= 70)  |  Moderate (40-69)  |  High (< 40)             |
+-------------------------------------------------------------------------------+
```

### 3.4.3 Establishing Ground-Truth Target Labels
The continuous financial well-being score is derived directly from latent stress:
$$\text{Score} = 100 - \left(85 \cdot s + \mathcal{N}(0, 4)\right), \quad \text{clamped to } [0, 100]$$

To establish discrete target classes for supervised machine learning, fixed score bands derived from CFPB practitioner benchmarks are applied (`scripts/apply_target_labels.py`):
$$\text{Class} = \begin{cases} 
\text{Low Financial Stress} & \text{if } \text{Score} \ge 70 \\ 
\text{Moderate Financial Stress} & \text{if } 40 \le \text{Score} < 70 \\ 
\text{High Financial Stress} & \text{if } \text{Score} < 40 
\end{cases}$$

Across the 2,500 generated records, this produces a well-balanced, realistic class distribution:
- **Low Stress**: 870 instances (34.8%)
- **Moderate Stress**: 1,132 instances (45.3%)
- **High Stress**: 498 instances (19.9%)

> [!IMPORTANT]
> **Data Transparency and Academic Rigor**: The synthetic nature of this dataset is explicitly acknowledged as a deliberate engineering decision. It eliminates ethical hazards surrounding real banking secrets, provides verifiable ground truth for algorithmic benchmarking, and matches the exact feature schema of the proposed primary survey.

---

## 3.5 Peffers DSRM Execution Workflow
This research rigorously follows the six-stage Design Science Research Methodology (DSRM) framework articulated by Peffers et al. (2007) (**Figure 3.1**).

![Figure 3.1: Peffers et al. Design Science Research Methodology (DSRM) Framework](../../reports/figures/dsrm_framework.png)

**Table 3.1** maps each Peffers DSRM stage directly to the concrete executions, artifacts, and chapters of this dissertation.

| DSRM Stage | Core Operational Activity | Primary Deliverables / Artifacts | Dissertation Alignment |
|---|---|---|---|
| **Stage 1: Problem Identification** | Define the limitations of reactive budgeting; examine the socioeconomic crisis of personal financial stress. | Formal Problem Statement, Domain Deficiencies, Research Questions. | Chapter 01 (Sections 1.2–1.4), Chapter 02 (Section 2.3). |
| **Stage 2: Define Objectives** | Establish quantitative performance, explainability, latency, and privacy goals for an intelligent detection artifact. | Specific Research Objectives (1.7.1–1.7.7), Scope Boundary Matrix. | Chapter 01 (Sections 1.6–1.7, 1.10). |
| **Stage 3: Design & Development** | Design the dual-pipeline architecture; engineer 7 behavioral ratios; train 5 candidate ML models; build FastAPI backend and web UI. | `src/features/engineer_features.py`, `src/models/train_models.py`, `src/app/api.py`, `src/app/static/`. | Chapter 04 (SRS & UML), Chapter 05 (Implementation). |
| **Stage 4: Demonstration** | Deploy the working prototype; demonstrate end-to-end real-time inference on diverse consumer profiles. | Functional Web Application ("Financial Weather"), Interactive Scenarios, Three.js Rendering. | Chapter 05 (Section 5.2), Chapter 06 (Section 6.4). |
| **Stage 5: Evaluation** | Benchmark candidate models on held-out test data (F1, ROC-AUC); execute 66 automated pytest cases; conduct latency profiling. | Model Comparison Benchmark (`model_comparison.csv`), Confusion Matrices, SHAP Plots, Pytest Log. | Chapter 06 (Testing & Empirical Evaluation). |
| **Stage 6: Communication** | Disseminate research contributions, system documentation, user manuals, and future recommendations. | Academic Dissertation, System Documentation, Setup Guide, Open Source Repo. | Chapter 07 (Concluding Remarks), Appendices. |

*Table 3.1: DSRM Research Execution Matrix Mapped to Project Milestones.*

---

## 3.6 Project Management Methodology: Agile Scrum Framework
To ensure continuous delivery, rigorous testing, and adaptive refinement of both the machine learning pipeline and the software prototype, the project adopted the **Agile Scrum Framework** (Schwaber & Sutherland, 2020).

### Sprint Decomposition
The twelve-month research and development lifecycle (November 2025 to November 2026) was organized into six structured bi-monthly sprints:
- **Sprint 1 (Nov – Dec 2025)**: *Inception & Literature Synthesis*. Domain research, psychometric instrument review, problem formulation, and thesis proposal defense.
- **Sprint 2 (Jan – Feb 2026)**: *Methodological Design & Data Modeling*. Formulation of the latent factor data generator, establishing CFPB score bands, and defining the 35-variable schema.
- **Sprint 3 (Mar – Apr 2026)**: *Data Pipeline & Preprocessing Engine*. Building data cleaning, IQR outlier flagging, 7 behavioral ratio feature engineering, and train/test stratification.
- **Sprint 4 (May – Jun 2026)**: *Algorithmic Modeling & Benchmarking*. Training and cross-validating the five candidate classifiers (LogReg, SVM, RF, XGB, DT); tuning hyperparameters.
- **Sprint 5 (Jul – Aug 2026)**: *Explainability & Software Artifact Development*. Integrating SHAP explainer, developing the FastAPI backend, and engineering the "Financial Weather" frontend interface.
- **Sprint 6 (Sep – Nov 2026)**: *Testing, Usability & Dissertation Compilation*. Executing the 66-test pytest suite, performance latency benchmarking, final academic thesis authoring, and viva presentation defense.

### 3.6.1 Project Timeline (Gantt Chart Analysis)
The sequential execution and task concurrency across the twelve-month development period are depicted in the formal **Project Gantt Chart** (**Figure 3.2**).

![Figure 3.2: Project Timeline & Milestone Schedule (Gantt Chart)](../../reports/figures/project_gantt.png)

---

### 3.6.2 Ethical Considerations, Responsible AI, and Privacy Guarantees
Handling personal financial information imposes severe ethical and legal obligations. The development of the "Financial Weather" platform was governed by strict ethical principles:

1. **Strictly Non-Diagnostic Framing**:
   Financial stress detection systems must never impersonate clinical psychology or formal financial auditing. The system's output is explicitly framed as an **"estimated financial stress indicator"**. Every response payload—both in the API schema and on the visual interface—carries a mandatory disclaimer:
   > *"This is an automated estimate based on spending patterns, not a financial or psychological diagnosis."*
2. **Absolute Data Minimization and Stateless Execution**:
   In strict compliance with Article 5 of the General Data Protection Regulation (GDPR), the system enforces total data minimization. The application collects zero personally identifiable information (PII): no names, email addresses, phone numbers, national identity numbers, bank account numbers, or credit card tokens are solicited or accepted. Furthermore, the backend operates **completely statelessly in RAM**. No database exists; inputs are discarded immediately upon response generation.
3. **Mitigation of Algorithmic Bias and Class Fairness**:
   To ensure that the machine learning models do not discriminate against specific income tiers or employment backgrounds, the synthetic dataset incorporates diverse representations across employment statuses (Employed, Self-Employed, Student, Unemployed). Models were evaluated using **macro-averaged metrics** to prevent majority-class bias.
4. **Algorithmic Transparency via Explainable AI**:
   To combat the ethical hazard of "black-box" decision-making, the system couples every classification with local feature attribution (Linear SHAP). Users are informed of the exact behavioral drivers behind their rating, empowering them to verify and understand the outcome.
5. **Calm, Non-Stigmatizing Design Language**:
   Reflecting ethical user interface design, the platform eschews aggressive alert sirens or punitive red banners. Utilizing the neutral, evocative metaphor of **"Financial Weather"** (*Clear*, *Changeable*, *Stormy*), the interface communicates reality constructively, mitigating user anxiety and fostering proactive engagement.

---

## 3.7 Chapter Summary
This chapter detailed the research methodology governing this dissertation. It established the epistemological and ontological justification for combining Pragmatism with Positivism and substantiated the Deductive Empirical Approach. It positioned the work within Design Science Research (DSR), detailing the four artifact dimensions produced. The chapter elaborated the latent factor data generation model and CFPB-grounded target labeling methodology, followed by a comprehensive mapping of the Peffers DSRM execution workflow. Finally, it described the Agile Scrum project management structure, presented the project Gantt chart, and outlined the strict ethical, privacy, and responsible AI protocols underpinning the software artifact.
