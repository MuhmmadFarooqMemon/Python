def say_Hello():        #creating function
    print("Hello,World")
say_Hello() #calling function


# A function named greet_user that accepts a user's name as a parameter and prints a greeting like: "Hello, 'Your Name'!"
def greet_user(name):
    print("Hello,",name)
greet_user('Farooq Memon')



# A function called add_numbers that takes two numbers as arguments and returns their sum.
def add_numbers(a,b):
    return a+b
# Calling Function
result=add_numbers(2,3)
print("Sum Of Two Numbers :",result)

# A function called square that takes a single number as input and returns its square.
def square(num):
    return num ** 2
# Calling the function
print("Square:", square(4))


# A function named introduce_yourself that accepts name and age as parameters. Make age have a default value of 18.
def introduce_yourself(Name,age=18):
    print("My Name Is : ",Name,"And Age Is : ",age)
introduce_yourself('Ali')
introduce_yourself('Farooq',22)



# A function named calculate_rectangle_area that takes length and width as keyword arguments and returns the area of a rectangle.

def calculate_rectangle_area(length, width):
    return length * width
# Calling the function with keyword arguments
area = calculate_rectangle_area(length=10, width=5)
print("Area:", area)




# def Is The Keyword To Create A Function
# function name with round brackets () is the way for calling function
# You can Add Multiple Attributes in functions
