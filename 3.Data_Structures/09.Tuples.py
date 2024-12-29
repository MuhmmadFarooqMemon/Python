# Creating a tuple with different data types
person = ("Farooq", 22, 5.7)
print("Original tuple :",person)


#Accessing Tuple Elements
print("First Tuple  :",person[0])
print("Second Tuple :",person[1])

# Tuple Slicing
# Slicing from index 1 to 3 (excluding 3)
print("Sliced Tuple :",person[1:3])

# Concatenating Tuples
tuple1 = ("apple", "banana")
tuple2 = ("cherry", "date")
combined_tuple = tuple1 + tuple2
print("Concentrated Tuple:",combined_tuple)

#  Repeating a Tuple
tuple = ("apple", "banana")
repeated_tuple = tuple * 3
print("Repeated Tuple:",repeated_tuple)

# Tuple Unpacking
name, age, height = person
print("Name:",name)   
print("Age:",age)    
print("Height:",height) 

#Checking Membershhip
print("Farooq Is In Tuple??","Farooq" in person) 

# Creating a nested tuple
        #(Index:   0   , (  0     ,      1  ),       2)
nested_tuple = ("apple", ("banana", "cherry"), "orange")
print("Nested Tuple:",nested_tuple[2]) # Accessing the second element of the tuple, which is itself a tuple
print("Accessing nested tuple element:",nested_tuple[1][0]) # Accessing the first element of the nested tuple (the tuple inside the main tuple)