#Q1) Perform data preprocessing on melb_data.csv dataset with statistical perspective. (using sk-learn)

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("melb_data.csv")

print("Shape:", df.shape)
print("Columns:", df.columns)
print("Info:\n")
df.info()

print("Summary:\n", df.describe(include='all'))

missing = df.isnull().sum()
print("Missing values:\n", missing[missing > 0])

df.fillna(df.median(numeric_only=True), inplace=True)

for col in df.select_dtypes(include='number').columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR)]
    print(f"Outliers in {col}: {len(outliers)}")

df_encoded = pd.get_dummies(df, drop_first=True)

scaler = StandardScaler()
num_cols = df_encoded.select_dtypes(include='number').columns
df_encoded[num_cols] = scaler.fit_transform(df_encoded[num_cols])

print("Preprocessed Data:\n", df_encoded.head())


#Q2) Perform data preprocessing on melb_data.csv dataset with statistical perspective. (using Panda)

import pandas as pd
import numpy as np

df = pd.read_csv("melb_data.csv")

print("Shape:", df.shape)
print("Columns:", df.columns)
print("Data types:\n", df.dtypes)
print("First few rows:\n", df.head())

print("Statistical Summary:\n", df.describe(include='all'))

missing = df.isnull().sum()
print("Missing Values:\n", missing[missing > 0])

df.fillna(df.median(numeric_only=True), inplace=True)

for col in df.select_dtypes(include='object').columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

for col in df.select_dtypes(include='number').columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    print(f"Outliers in {col}: {len(outliers)}")

df_encoded = pd.get_dummies(df, drop_first=True)

numeric_cols = df_encoded.select_dtypes(include='number').columns
df_encoded[numeric_cols] = (df_encoded[numeric_cols] - df_encoded[numeric_cols].mean()) / df_encoded[numeric_cols].std()

print("Preprocessed Data:\n", df_encoded.head())
