import pandas as pd
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

plt.figure(figsize=(8, 5))
plt.hist(df["Fare"], bins=30, color="steelblue", edgecolor="white")
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Count")
plt.show()