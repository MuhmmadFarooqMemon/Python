# Program to demonstrate arithmetic operators
# Prompting the user to input two numbers and converting them to float
no1 = float(input("Enter the First Number: "))  # First number as a float
no2 = float(input("Enter the Second Number: "))  # Second number as a float
# Performing and displaying results of arithmetic operations
print("Sum:", no1 + no2)  # Adding the two numbers
print("Difference:", no1 - no2)  # Subtracting the second number from the first
print("Product:", no1 * no2)  # Multiplying the two numbers
print("Quotient:", no1 / no2)  # Dividing the first number by the second
print("Modulus:", no1 % no2)  # Finding the remainder of the division
print("Exponentiation:", no1 ** no2)  # Raising the first number



# Comparsion
# Prompting the user to input two numbers and converting them to float
no1 = float(input("Enter the First Number: "))  # First number as a float
no2 = float(input("Enter the Second Number: "))  # Second number as a float
# Printing the header for comparison result
print("Comparison Of Two Numbers")
# Comparing the two numbers using conditional statements
if no1 == no2:  # If both numbers are equal (==)
    print("Equal Numbers")  # Display if they are equal
elif no1 > no2:  # If the first number is greater than the second
    print(no1, "Is Greater Than", no2)  # Display the first number as greater
elif no2>no1:  # If the first number is less than the second
    print(no2, "Is Greater Than", no1)  # Display the second number as greater
elif no1!=no2:# If both numbers are not equal (!=)
    print("Both Numbers Are Not Equal.")



#Logical operators
# Prompting the user to input a number
num = int(input("Enter a number: "))  # Input a number and convert it to an integer


# Using the 'and' logical operator
# Checks if the number is between 10 and 20 (inclusive)
if num >= 10 and num <= 20:
    print("The number is between 10 and 20 (inclusive).")
else:
    print("The number is not between 10 and 20.")
# Using the 'or' logical operator
# Checks if the number is less than 5 or greater than 50
if num < 5 or num > 50:
    print("The number is either less than 5 or greater than 50.")
else:
    print("The number is between 5 and 50.")
# Using the 'not' logical operator
# Checks if the number is not equal to 0
if not num == 0:
    print("The number is not zero.")
else:
    print("The number is zero.")