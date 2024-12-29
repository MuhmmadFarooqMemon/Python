# Importing and using standard modules
# Importing the math module
import math
# Using math functions
print("Square root of 16:", math.sqrt(16))  #For Square root
print("Value of pi:", math.pi)              #For Pi
print("Cosine of 0 degrees:", math.cos(0))  #For Cosine
print("Sine of 0 degrees:", math.sin(0))  #For Sine
print("Tan of 0 degrees:", math.tan(0))  #For Tan



# Importing the random module
import random
# Generating random numbers
print("Random number between 1 and 10:", random.randint(1, 10))
print("Random float between 0 and 1:", random.random())
# Randomly selecting an item from a list
colors = ["red", "blue", "green", "yellow"]
print("Random color:", random.choice(colors))





# Importing specific functions from the math module
from math import sqrt, pi  # Import only sqrt and pi for direct usage
# Using imported functions directly
print("Square root of 25:", sqrt(25))  # Calculates square root directly without module prefix
print("Value of pi:", pi)  # Access pi directly without math prefix


