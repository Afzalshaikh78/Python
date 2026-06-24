import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
X = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
y = np.array([0,0,0,0,1,1,1,1,1,1])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("=== accuracy_score ===")
print(accuracy_score(y_test, y_pred))

print("\n=== confusion_matrix ===")
print(confusion_matrix(y_test, y_pred))

print("\n=== classification_report ===")
print(classification_report(y_test, y_pred))

print("=== predict_proba([[4]]) ===")
print(model.predict_proba([[4]]))

print("\n=== predict_proba([[8]]) ===")
print(model.predict_proba([[8]]))