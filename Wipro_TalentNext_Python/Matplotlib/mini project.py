#  Perform Exploratory Data Analysis on the Diabetes dataset.

# Perform the following task
# - Load the data into a DataFrame
# - Perform data preprocessing
# - Handle categorical data
# - Perform univariate analysis
# - Perform bivariate analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Diabetes.csv")
print("Shape:", df.shape)
print("Info:\n", df.info())
print("Summary:\n", df.describe())

print("Missing values:\n", df.isnull().sum())

cols_with_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[cols_with_zero] = df[cols_with_zero].replace(0, pd.NA)

df.fillna(df.median(numeric_only=True), inplace=True)

print("Value counts:\n", df['Outcome'].value_counts())

for col in df.columns[:-1]: 
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

sns.boxplot(x='Outcome', y='Glucose', data=df)
plt.title("Glucose by Outcome")
plt.show()

sns.violinplot(x='Outcome', y='BMI', data=df)
plt.title("BMI by Outcome")
plt.show()
