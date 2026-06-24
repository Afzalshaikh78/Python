# #knn 
# import numpy as np

# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score

# X = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
# y = np.array([0,0,0,0,1,1,1,1,1,1])

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
# )

# model = KNeighborsClassifier(
#     n_neighbors=3
# )

# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# print("Accuracy:", accuracy_score(y_test, y_pred))

# print("Prediction for 4 hours:")
# print(model.predict([[4]]))

# print("Prediction for 8 hours:")
# print(model.predict([[8]]))


#svm

# from sklearn.svm import SVC
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import numpy as np

# X = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
# y = np.array([0,0,0,0,1,1,1,1,1,1])

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
# )

# model = SVC(kernel="linear")

# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# print("Accuracy:", accuracy_score(y_test, y_pred))

# print("Prediction for 4 hours:")
# print(model.predict([[4]]))

# print("Prediction for 8 hours:")
# print(model.predict([[8]]))


#cross validation
# from sklearn.model_selection import cross_val_score
# from sklearn.linear_model import LogisticRegression
# import numpy as np

# X = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
# y = np.array([0,0,0,0,1,1,1,1,1,1])

# model = LogisticRegression()

# scores = cross_val_score(
#     model,
#     X,
#     y,
#     cv=5
# )

# print(scores)
# print("Mean Accuracy:", scores.mean())


# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import GridSearchCV
# import numpy as np

# X = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
# y = np.array([0,0,0,0,1,1,1,1,1,1])

# model = RandomForestClassifier(random_state=42)

# param_grid = {
#     "n_estimators": [10, 50, 100],
#     "max_depth": [1, 2, 3]
# }

# grid = GridSearchCV(
#     estimator=model,
#     param_grid=param_grid,
#     cv=3,
#     scoring="accuracy"
# )

# grid.fit(X, y)

# print("Best Params:", grid.best_params_)
# print("Best Score:", grid.best_score_)


#scaling

# from sklearn.preprocessing import StandardScaler
# import pandas as pd

# data = pd.DataFrame({
#     "age": [20, 30, 40, 50],
#     "salary": [20000, 50000, 80000, 120000]
# })

# scaler = StandardScaler()

# scaled_data = scaler.fit_transform(data)

# print(scaled_data)


#K mean 
import pandas as pd

from sklearn.cluster import KMeans

data = pd.DataFrame({
    "age": [20,22,25,45,48,50],
    "spending": [2000,2500,3000,20000,22000,25000]
})

model = KMeans(
    n_clusters=2,
    random_state=42
)

model.fit(data)

print("Labels:")
print(model.labels_)

print("\nCenters:")
print(model.cluster_centers_)

print("\nNew Customer:")
print(model.predict([[23,2800]]))