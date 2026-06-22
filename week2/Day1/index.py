import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Study hours → exam score (same data as the widget above)
X = np.array([10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]).reshape(-1,1)
y = np.array([72,88,115,142,158,190,210,238,255,278,305,318,355,370,398])

# Step 1: split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 2: create + train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 3: inspect what it learned
print(f"Slope (w):     {model.coef_[0]:.2f}")
print(f"Intercept (b): {model.intercept_:.2f}")

# Step 4: evaluate on test set
y_pred = model.predict(X_test)
print(f"MSE:  {mean_squared_error(y_test, y_pred):.2f}")
print(f"R²:   {r2_score(y_test, y_pred):.4f}")

# Step 5: predict a new value
new_hours = np.array([[47]])
print(f"Predicted score for 47 hours: {model.predict(new_hours)[0]:.1f}")