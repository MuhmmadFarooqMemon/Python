# Creating a Dictionary
# create a dictionary by using curly braces {}
person = {
    "Name": "Farooq",
    "Age": 22,
    "City": "Karachi"
}
print(person)

# Accessing Dictionary Values
# Access the value associated with a key using square brackets [].
print(person["Name"])
print(person["Age"])

# Modifying Dictionary Values
# The value associated with a key by simply assigning a new value to that key.
person["Name"]="Muhammad Farooq Memon"
print(person["Name"])

# Adding New Key-Value Pairs
# Add new key-value pairs to the dictionary.
person["Profession"] = "Python Developer"
print(person)


# Removing a key-value pair using del
del person["City"]
print(person)

# Removing a key-value pair using pop()
profession = person.pop("Profession")
print(profession)
print(person)


# Checking if a key exists
# If a key exists in the dictionary using the in operator.
print("Name" in person)  
print("City" in person)  

# Getting All Keys, Values, and Items
# All the keys, values, or key-value pairs using keys(), values(), and items() methods.
# Getting all keys
print(person.keys())
# Getting all values
print(person.values()) 
# Getting all key-value pairs
print(person.items())



# Nested dictionary example
# A dictionary can contain other dictionaries as values (nested dictionaries).
employees = {
    # Dictionary for employee1
    "employee1": {
        "Name": "Farooq",  # Name of the employee
        "Age": 22,       # Age of the employee
        "Position": "Developer"  # Position of the employee
    },
    # Dictionary for employee2
    "employee2": {
        "Name": "Saim",  # Name of the employee
        "Age": 21,       # Age of the employee
        "Position": "Designer"  # Position of the employee
    }
}

# Accessing and printing the name of 'employee1' from the nested dictionary
print(employees["employee1"]["Name"])
# Accessing and printing the name and position of 'employee2' from the nested dictionary
print(employees["employee2"]["Name"],employees["employee2"]["Position"])


