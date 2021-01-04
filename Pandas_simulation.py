# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21  22:14:40 2020

@author: shima
"""
# Import numpy as np
import numpy as np

# Use seed() to set the seed; as an argument, pass 123
np.random.seed(123)

# Generate the first random float with rand() and print it out
print(np.random.rand())

# Use randint() to simulate a dice
print(np.random.randint(1, 7))

# Use randint() again
print(np.random.randint(1, 7))

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1, 7)

# Finish the control construct
if dice <= 2 : #If dice is 1 or 2, you go one step down
    step = step - 1
elif dice < 6 : #if dice is 3, 4 or 5, you go one step up
    step = step + 1
else : #Else, you throw the dice again. The number of eyes is the number of steps you go up
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)

# Random walk, head or tails
# Numpy is imported, seed is set
import numpy as np
# Initialize random_walk
random_walk = [0]

# the loop should run 100 times
for x in range(100) :
    # Set step: last element in random_walk, On each iteration, set step equal to the last element in the random_walk list. You can use the index -1 for this
    step = random_walk[-1]
# Next, let the if-elif-else construct update step
    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

# Now considewr also we can not go below zero
# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step -1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)

# Now also use matplotlib to build a line plot
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()

#Distribution
# To get an idea about how big your chances are of reaching 60 steps, you can repeatedly simulate the random walk and collect the results. 
# Numpy is imported; seed is set
np.random.seed(123)

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for i in range(10) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Use np.array() to convert all_walks to a Numpy array, np_aw
# Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t, Call the result np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t) # Now every row in np_all_walks represents the position after 1 throw for the 10 random walks
plt.show()


# Print all_walks
print(all_walks)


# Implement Clumsiness
# simply update the range() function in the top-level for loop
# You're a bit clumsy and you have a 0.1% chance of falling down
# Generate a random float between 0 and 1. If this value is less than or equal to 0.001, you should reset step to 0
# Simulate random walk 250 times
all_walks = []
for i in range(250) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.001 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()

# Plot the distribution
# numpy and matplotlib imported, seed set
np.random.seed(123)
# Simulate random walk 500 times
all_walks = []
for i in range(500) :  # Simulate the random walk 500 times
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np.array(np_aw_t[-1])

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()

# Now what's the estimated chance? fraction of simulations that ended higher than step 30
print(np.mean(ends > 30))