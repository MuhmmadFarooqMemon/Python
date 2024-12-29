# Program to check if a number is positive, negative, or zero
no = float(input("Enter a number: "))  # Input a number
if no > 0:
    print("The number is positive.")
elif no < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Program to check if a number is even or odd
if no % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# Program to check the age category
age = int(input("Enter your age: "))  # Input the age
if age < 12:
    print("You are a child.")
elif 12 <= age <= 19:
    print("You are a teenager.")
else:
    print("You are an adult.")
