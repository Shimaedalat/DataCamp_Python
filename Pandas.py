# -*- coding: utf-8 -*-
"""
Created on Mon Dec  21 20:39:36 2020

@author: shima
"""
# Importing the data with tabular structure 
# Either creatring data frame with pd.dataframe(dict) Or import big data

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':names, 'drives_right':dr, 'cars_per_cap': cpc}


# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

# Import the cars.csv data: cars
# cars = pd.read_csv('cars.csv') starts with numbers of rows


# Fix import by including index_col
# cars = pd.read_csv('cars.csv', index_col = 0) starts with first column, containing the countries names

# Double [] is used to access specific column in data, ending up with a sub data frame
print(cars[["country"]])

# To access the rows slicing is used,*remember the end of the slice is exclusive*
cars[1:4] # refers to row 2,3,4 instead of 2,3,4,5

# loc function in pandas lets us to select part of data based on the lable in2D also
#loc( label-based), iloc(integer position based)
print(cars.loc[[2]])

# Call the japan and Indea rows, here 2 and 3 are the name of rows
print(cars.loc[[2,3]])

# Now call the same rows using indexing
print(cars.iloc[[2,3]])

# Comparison operator works on the same type only, the only exception is integer and float 
# Comparison of booleans
print(True == False)

# not equal != , equali == 
# Write Python code to check if -5 * 15 is not equal to 75
print(-5 * 15 != 75)

# Ask Python whether the strings "pyscript" and "PyScript" are equal
print('pyscript' == 'PyScript')


# Write code to see if True and 1 are equal
print(True == 1)

# Comparison of integers
x = -3 * 6
print(x >= -10)

# Comparison of strings
y = "test"
print('test' <= y)

# Comparison of booleans
print(True > False)

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)

