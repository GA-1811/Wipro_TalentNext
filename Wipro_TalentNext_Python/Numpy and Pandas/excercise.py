#Q1) Create a two-dimensional 3×3 NumPy array and perform ndim, slicing, shape on it.

import numpy as np

arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("ndim:", arr_2d.ndim)
print("shape:", arr_2d.shape)     
print("Sliced array:\n", arr_2d[1:, :2])

#Q2) Create a one-dimensional array and perform ndim, shape, reshape on it.

import numpy as np

arr_1d = np.array([10, 20, 30, 40, 50, 60])

print("ndim:", arr_1d.ndim) 
print("shape:", arr_1d.shape)    
 
reshaped = arr_1d.reshape(2, 3)
print("Reshaped array:\n", reshaped)

#Q3) Pandas-DatarFrame
#- Import Pandas
# - Load the dataset into a DataFrame named cars
# - Inspect the first 10 rows
# - Print the entire DataFrame
# - Inspect the last 5 rows
# - Get meta information about the DataFrame

import pandas as pd

cars = pd.read_csv("cars.csv")

print("First 10 rows:\n", cars.head(10))
print("Full DataFrame:\n", cars)
print("Last 5 rows:\n", cars.tail())
print("Info:\n")
cars.info()

#Q4) Download 50-Startup Dataset
# - Load the dataset into a DataFrame
# - Display the statistical summary
# - Check correlation between dependent and independent variables

import pandas as pd

startups = pd.read_csv("50_startups.csv")

print("Summary:\n", startups.describe())
print("Correlation:\n", startups.corr())
