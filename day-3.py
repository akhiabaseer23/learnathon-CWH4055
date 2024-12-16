#KEYWORDS

#PRINTING ALL THE KEYWORDS

import keyword
print(keyword.kwlist)


#TYPE CONVERSIONS.........

#IMPLICIT TYPE CONVERSION

integer_number = 123
float_number = 1.23
new_number = integer_number + float_number
# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))

#EXPLICIT TYPE CONVERSION 

num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))


#STRINGS IN PYTHON


#Example: Python String
# create string type variables

name = "Python"
print(name)

message = "I love Python."
print(message)

#Access String Characters in Python

greet = 'hello'

# access 1st index element
print(greet[1]) 

#NEGATIVE INDEXING
greet = 'hello'

# access 4th last element
print(greet[-4]) # "e"

#SLICING


#Slicing: Access a range of characters in a string by using the slicing operator colon :greet = 'Hello'

# access character from 1st index to 3rd index
print(greet[1:4])  # "ell"

# multiline string 
message = """
Never gonna give you up
Never gonna let you down
"""
print(message)

#Python String Operations

#Compare Two Strings

str1 = "Hello, world!"
str2 = "I love Swift."
str3 = "Hello, world!"

# compare str1 and str2
print(str1 == str2)

# compare str1 and str3
print(str1 == str3)


#Join Two or More Strings

greet = "Hello, "
name = "Jack"

# using + operator
result = greet + name
print(result)

#Python String Length

greet = 'Hello'

# count length of greet string
print(len(greet))

#Python String Formatting (f-Strings)

name = 'Cathy'
country = 'UK'
print(f'{name} is from {country}')



#PROGRAM TO CONCATENATE TWO STRINGS


# Input
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Concatenate strings
result_string = string1 + string2

# Output
print("Concatenated string:", result_string)


#PROGRAM TO FIND LENGTH OF A STRING


input_string = input("Enter a string: ")

# Find length of the string
string_length = len(input_string)

print("Length of the string:", string_length)


#PROGRAM TO REVERSE A STRING

input_string = input("Enter a string: ")
# Reverse the string
reversed_string = input_string[::-1]
print("Reversed string:", reversed_string)


#PROGRAM TO CONVERT STRING TO UPPERCASE

# Program to convert a string to uppercase

# Input
input_string = input("Enter a string: ")

# Convert to uppercase
uppercase_string = input_string.upper()

# Output
print("Uppercase string:", uppercase_string)
