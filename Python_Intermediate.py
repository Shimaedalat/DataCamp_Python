# -*- coding: utf-8 -*-
"""
Created on Mon Dec  21 20:50:22 2020

@author: shima
"""
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Creating variables year and pop
year = [1950, 1970, 1990, 2020]
pop = [2.519, 3.692, 5.263, 6.972]

# Print the last item from year and pop
print(year[-1])
print(pop[-1])

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year,pop)

# Display the plot with plt.show()
plt.show()

# Change the line plot below to a scatter plot
plt.scatter(year,pop)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()

# Import package
import matplotlib.pyplot as plt

# Build Scatter plot
plt.scatter(year,pop)

# Show plot
plt.show()

# Build histogram with 5 bins
plt.hist(year,bins=5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(pop,bins=20)

# Show and clean up again
plt.show()
plt.clf()

# Labels
# Basic scatter plot, log scale
plt.scatter(year,pop)
plt.xscale('log') 

# Strings
xlab = 'Years'
ylab = 'Population'
title = 'Year vs. Population Trend'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)

# After customizing, display the plot
plt.show()

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)

# After customizing, display the plot
plt.show()

# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop*2

# Add grid() call
plt.grid(True)

# Update: set s argument to np_pop
plt.scatter(pop, year, s = np_pop)
plt.show()

# Applying dictionaries
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = { 'spain':'madrid','france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print europe
print(europe)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print('italy' in europe) #True

# Add poland to europe
europe['poland'] = 'warsaw'

# Print europe
print(europe)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del europe['australia']

# Print europe
print(europe)

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital':'rome','population':59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)