# Passing functions as arguments, and using map, filter, and reduce
# Function to add two numbers
def add(a, b):
    return a + b   
# Higher-order function that takes a function as an argument
def apply_operation(a, b, operation):
    return operation(a, b)
# Using the higher-order function
result = apply_operation(5, 3, add)
print("Result:", result)



# List of numbers
nums = [1, 2, 3, 4]
# Using map to square each number
squared = map(lambda x: x ** 2, nums)
print(list(squared))



# List of numbers
nums = [1, 2, 3, 4, 5, 6]
# Using filter to get only even numbers
evens = filter(lambda x: x % 2 == 0, nums)
print(list(evens))


from functools import reduce
# List of numbers
nums = [1, 2, 3, 4]
# Using reduce to calculate the product of all numbers
product = reduce(lambda x, y: x * y, nums)
print("Product:", product)

