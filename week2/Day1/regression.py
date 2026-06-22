import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score
)

# Exam score → pass/fail (1 = pass, 0 = fail)
X = np.array([20,25,30,35,38,42,45,48,50,52,55,58,62,65,70,75]).reshape(-1,1)
y = np.array([0,  0,  0,  0,  0,  0,  1,  0,  1,  1,  1,  1,  1,  1,  1,  1])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Train — same API as LinearRegression!
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict classes (applies 0.5 threshold by default)
y_pred = model.predict(X_test)

# Predict probabilities (the raw sigmoid output)
y_proba = model.predict_proba(X_test)
# y_proba[:, 1] gives P(class=1) for each sample

print(f"Coefficients: {model.coef_[0]}")
print(f"Intercept:    {model.intercept_[0]:.4f}")
print()

# Full report — accuracy, precision, recall, F1 all at once
print(classification_report(y_test, y_pred, target_names=['Fail', 'Pass']))
print("Confusion matrix:")
print(confusion_matrix(y_test, y_pred))
print(f"ROC-AUC: {roc_auc_score(y_test, y_proba[:, 1]):.4f}")

# Custom threshold — lower to catch more positives
threshold = 0.3
y_pred_custom = (y_proba[:, 1] >= threshold).astype(int)