# Function to multiply two numbers
def multiply(a, b):
    return a * b  # Return the product of a and b

result = multiply(5, 3)  # Call the function and store the result
print("Product:", result)



# Function to calculate sum and product
def calculate_stats(a, b):
    return a + b, a * b  # Return both sum and product

# Calling the function and unpacking the result
sum_result, product_result = calculate_stats(4, 6)
print("Sum:", sum_result) 
print("Product:", product_result)  


