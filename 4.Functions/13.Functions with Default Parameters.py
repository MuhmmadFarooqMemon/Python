# Functions with Default Parameters
def greet_person(name="Guest"):
    print(f"Hello, {name}!")
greet_person()  #If no argument is passed for name, it will default to "Guest".
greet_person("Farooq") #If argument is passed for name, it will update to "value".


# Keyword Arguments
# Pass arguments using keywords. This allows you to specify which argument you are providing, regardless of their position in the function definition.
def greet(name,age):
    print("Name",name,"Age :",age)
greet("Farooq",22)      # Using keyword arguments