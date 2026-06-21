import pandas as pd

df = pd.read_csv('01_District_wise_crimes_committed_IPC_2001_2012.csv')  # match your real filename

# print(df.shape)
# print(df.columns.tolist())
# print(df.dtypes)
# print(df.isnull().sum())

print(df['DISTRICT'].value_counts().head(15))
print(df[df['DISTRICT'] == 'NORTH'][['STATE/UT', 'DISTRICT']].drop_duplicates())