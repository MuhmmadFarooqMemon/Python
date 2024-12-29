# Creating a Set
# Create a set by using curly braces {} or the set() constructor.

# Creating a set with curly braces
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Creating a set using the set() constructor
numbers = set([1, 2, 3, 4, 5])
print(numbers)

# Operations on Sets
# 1. Adding Elements
# Add individual elements using the add() method.
fruits.add("orange")
print("Fruits after adding orange:",fruits)  


# 2.Removing Elements
# Remove elements using remove() or discard(). 
# The remove() method will raise an error 
# if the element doesn't exist, while discard() will not rase An Error.
fruits.remove("banana")
fruits.discard("grape")  # No error, even though "grape" is not in the set
print("Fruits after Removing banana:",fruits)

# 3.Set Operations
# Union: Combines two sets, removing duplicates.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2) # Or use set1 | set2
print("Union of set1 and set2:",union_set)

# 4.Intersection: Returns the elements that are present in both sets.
intersection_set = set1.intersection(set2) # Or use set1 & set2
print("Intersection of set1 and set2:",intersection_set)

# 5.Difference: Returns the elements that are in the first set but not in the second.
difference_set = set1.difference(set2)  # Or use set1-set2
print("Difference between set1 and set2:",difference_set)

# 6.Symmetric Difference: Returns elements that are in either of the sets, but not in both.
symmetric_difference_set = set1 ^ set2  # Or use set1.symmetric_difference(set2)
print("Symmetric difference between set1 and set2:",symmetric_difference_set)

# 7.Checking for Membership
# Check if an element is in a set using the in keyword.
print("Checking 3 In Set1",3 in set1) 
print("Checking 6 In Set1",6 in set1) 

# 8.Set Length
# Get the number of elements in a set using the len() function.
print("Length Of Set1 =",len(set1))


# 9.Set Copy
# Create a copy of a set using the copy() method
set_copy = set1.copy()
print(set_copy)  

