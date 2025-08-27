# Perform the outlier dectection for the given dataset. 
# Dataset: datasetExample.csv
# - Load the data into a Pandas DataFrame
# - Detect outliers in the dataset

import pandas as pd

df = pd.read_csv("datasetExample.csv")

print("Data Preview:\n", df.head())

for col in df.select_dtypes(include='number').columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    print(f"\nOutliers in '{col}':")
    print(outliers[[col]])
