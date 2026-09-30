import pandas as pd

df = pd.read_csv('unemployment_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

print("Shape:", df.shape)
print("\nColumn info:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())
print("\nSummary statistics:")
print(df.describe())
print("\nDate range:", df['Date'].min(), "to", df['Date'].max())
print("\nStates covered:", df['Region'].nunique())
print("Area types:", df['Area'].unique())
