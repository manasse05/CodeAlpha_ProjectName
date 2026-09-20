import pandas as pd

df = pd.read_csv("dataset.csv")

print("Nombre de lignes :", len(df))
print("Nombre de colonnes :", len(df.columns))

print("\nColonnes :")
print(df.columns.tolist())

print("\nValeurs manquantes :")
print(df.isnull().sum())

print("\nDoublons :", df.duplicated().sum())

print("\nTypes de données :")
print(df.dtypes)

print("\nPremières lignes :")
print(df.head())