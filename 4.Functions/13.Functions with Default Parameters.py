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



#  Positional and Keyword Arguments
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

# Positional arguments
describe_pet("Buddy", "cat")  

# Keyword arguments
describe_pet(animal_type="rabbit", pet_name="Snowy")  


#Default Arguments
def calculate_price(price, discount=10):
    return price - (price * discount / 100)

print("Price after discount:", calculate_price(100))  # Uses default discount
print("Price after discount:", calculate_price(100, 20))  # Overrides discount
