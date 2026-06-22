import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = {
    "hours": [1,2,3,4,5,6,7,8,9,10],
    "marks": [20,30,35,45,55,65,75,80,90,95]
}

df = pd.DataFrame(data)

X = df[["hours"]]
y = df["marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)

y_pred = model.predict(X_test)

print("\nPredictions:")
print(y_pred)

print("\nR2 Score:")
print(r2_score(y_test, y_pred))

new_prediction = model.predict([[12]])

print("\nPrediction for 12 hours:")
print(new_prediction)