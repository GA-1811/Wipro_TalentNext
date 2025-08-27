#Q1) Perform Exploratory Data Analysis on the Mall_Customers dataset.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Mall_Customers.csv")

print(df.info())
print(df.describe())

sns.countplot(x='Gender', data=df)
plt.title("Gender Distribution")
plt.show()

sns.histplot(df['Age'], bins=10, kde=True)
plt.title("Age Distribution")
plt.show()

sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Gender', data=df)
plt.title("Spending Score vs Income")
plt.show()


#Q2) Perform Exploratory Data Analysis on the Salary_Data dataset.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Salary_Data.csv")

print(df.describe())

sns.scatterplot(x='YearsExperience', y='Salary', data=df)
plt.title("Experience vs Salary")
plt.show()

sns.regplot(x='YearsExperience', y='Salary', data=df)
plt.title("Regression Line")
plt.show()


#Q3) Perform Exploratory Data Analysis on the Social_Network_Ads dataset.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Social_Network_Ads.csv")

print(df.info())
print(df.describe())

sns.scatterplot(x='Age', y='EstimatedSalary', hue='Purchased', data=df)
plt.title("Age vs Salary (Purchased)")
plt.show()

sns.countplot(x='Gender', hue='Purchased', data=df)
plt.title("Purchase by Gender")
plt.show()
