# import pandas as pd
# import matplotlib.pyplot as plt


# url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

# df = pd.read_csv(url)

# plt.figure(figsize=(8, 5))
# plt.hist(df["Fare"], bins=30, color="steelblue", edgecolor="white")
# plt.title("Fare Distribution")
# plt.xlabel("Fare")
# plt.ylabel("Count")
# plt.show()

import numpy as np

A = np.array([[1,2],
              [3,4]])

A_inv = np.linalg.inv(A)
identify = A @ A_inv
print(identify)
print(A_inv)