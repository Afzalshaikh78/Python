import pandas as pd





data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40],
    "city": ["Bengaluru", "Mumbai", "Delhi", "Chennai"],
    "salary": [50000, 60000, 75000, 90000]
}

# df = pd.DataFrame(data)
# print(df[["name","age"]])

# import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
# print(df.info())
df = df.drop(columns=['Cabin'])
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
# print(df.isnull().sum())
# print(df.groupby("Age").avg())

#average age of the passengers survived
print(df.groupby("Sex")["Survived"].mean())   


#average age by passenger class
print(df.groupby("Pclass")["Age"].mean())


