# Model Selection

**Selected model: Logistic Regression**

Across the five candidates, SVM edges out Logistic Regression on raw
F1-macro (0.776 vs 0.765) and High-stress recall (0.70 vs 0.69), but the
margins are small (roughly one percentage point), and Logistic Regression
actually has the best macro ROC-AUC of all five models (0.915), the
second-best High-stress F1 (0.746, behind only SVM's 0.753), and clearly
outperforms the tree-based models (Decision Tree, Random Forest, XGBoost)
on every headline metric. On interpretability and inference speed,
Logistic Regression is the clear winner: its coefficients are directly
readable (each standardized feature's contribution to each class is a
single number), it integrates naturally with SHAP's efficient linear
explainer, and it predicts roughly 60x faster than the RBF-kernel SVM in
a benchmark on the same 500-row test set (~1.4ms vs ~84ms) — relevant
given the proposal's own requirement for a responsive, explainable
user-facing prototype that reports "key contributing factors" per
prediction (Stage 4: Demonstration) and addresses the explainability
research gap (Gap 4). Given SVM's advantage is marginal and comes at the
cost of both interpretability and a two-order-of-magnitude slowdown at
inference, Logistic Regression is recommended as the model to carry
forward into the prototype.
