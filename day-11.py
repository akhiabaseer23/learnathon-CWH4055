#SETS

# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)


# create an empty set
empty_set = set()
# create an empty dictionary
empty_dictionary = { }

# check data type of empty_set
print('Data type of empty_set:', type(empty_set))
# check data type of dictionary_set
print('Data type of empty_dictionary:', type(empty_dictionary))


#Add Items to a Set
numbers = {21, 34, 54, 12}

print('Initial Set:',numbers)

# using add() method
numbers.add(32)

print('Updated Set:', numbers) 

#Remove an Element from a Set

languages = {'Swift', 'Java', 'Python'}

print('Initial Set:',languages)
# remove 'Java' from a set
removedValue = languages.discard('Java')
print('Set after remove():', languages)


#add members in a set

animal = {"Lion","Cat"}
print(animal)
animal.add("Dog")
print("Add single element : ",animal)
animal.update(["Ponda", "Tiger"])
print("Add multiple items : ",animal)


#remove item(s) from a given set

# Given sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Perform set operations
union_result = set_a.union(set_b)
intersection_result = set_a.intersection(set_b)
difference_result = set_a.difference(set_b)
symmetric_difference_result = set_a.symmetric_difference(set_b)

# Print results
print("1. Union:", union_result)
print("2. Intersection:", intersection_result)
print("3. Difference (set_a - set_b):", difference_result)
print("4. Symmetric Difference:", symmetric_difference_result)