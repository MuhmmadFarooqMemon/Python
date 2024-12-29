#Introduction to lists and basic operations.
# Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)


# Accessing elements
# Index =[0      ,    1    ,     2   ]
fruits = ["apple", "banana", "cherry"]
print("At Index 0 ",fruits[0])  #apple (index 0)
print("At Index 1",fruits[1])  #banana (index 1)
print("At Index 2",fruits[2])  #Cherry (index 2)

# Modifying elements
fruits = ["apple", "banana", "cherry"]
fruits[0] = "mango"   #Modifying At Index 0 (Apple To Mango)
print("Modifyed List",fruits)

# Append a single item
fruits.append("orange")   #Appending A New Fruit At Last Position
print("Inserting A New Friut ",fruits) 

# Insert an item at a specific position
fruits.insert(1, "kiwi")   #Inserting AT Index 1 
print("Insert A New Fruit At Index 1",fruits)  


# Remove an item by value
fruits.remove("banana")
print("Remove Banana From List ",fruits)

# Remove an item by index (default is the last item)
fruits.pop(2)  # Removes the item at index 2 (cherry)
print("Removing A Fruit With The Help Of Index ",fruits) 

# Clear the entire list
fruits.clear()
print("List Cleared ",fruits)

#Length Of A List
fruits = ["mango", "kiwi", "orange"]
print("Length Of List Is ",len(fruits))

#Reverse A List
fruits.reverse()
print("Reverse List :",fruits) 

# Checking if an Item Exists in a List
print("kiwi" in fruits) 
print("banana" in fruits) 


# List Concatenation and Repetition You can combine lists using + or repeat them using *.
fruits1 = ["apple", "banana"]
fruits2 = ["orange", "kiwi"]
# Concatenation
combined_fruits = fruits1 + fruits2
print(combined_fruits) 
# Repetition
repeated_fruits = fruits1 * 2
print(repeated_fruits)


#Sum Of Numbers In A List
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print("The sum is:", total)

#Finding Largest And Smallest Number In Te List
print("Largest number:", max(numbers))  
print("Smallest number:", min(numbers))