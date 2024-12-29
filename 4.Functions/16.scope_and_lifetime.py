# Local and global variables, and the lifetime of variables
x = 10  # Global variable
# Function demonstrating local scope
def modify_variable():
    x = 5  # Local variable (different from global x)
    print("Inside function:", x)
modify_variable()  
print("Outside function:", x) 


x = 10  # Global variable

# Function to modify global variable
def modify_global():
    global x  # Indicating that we are modifying the global variable
    x = 5
    print("Inside function:", x)

modify_global() 
print("Outside function:", x) 