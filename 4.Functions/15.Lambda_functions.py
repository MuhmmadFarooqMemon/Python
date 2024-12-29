# Anonymous functions and their use cases
# Define a lambda function for squaring a number
square = lambda x: x ** 2

# Using the lambda function
print("Square of 5:", square(5))  

# List of student dictionaries
students = [{"Name": "Farooq", "age": 22}, {"Name": "Saim", "age": 20}]

# Sorting students by age using lambda
sorted_students = sorted(students, key=lambda x: x["age"])

print(sorted_students)  

# List of numbers
nums = [1, 2, 3, 4]

# Doubling numbers using map and lambda
doubled = map(lambda x: x * 2, nums)

print(list(doubled))

