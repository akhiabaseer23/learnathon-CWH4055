#STRING SLICING

s = 'HelloWorld'
print(s[:])
print(s[::])

#Reverse a String using Slicing

reverse_str = s[::-1]
print(reverse_str)

#STRING FUNCTIONS

#Here are some examples for string functions
print(s.upper())
print(s.lower())
print(s.capitalize())
print(len(s))


#program that takes a sentence as input and extracts the substring between the 5th and 10th characters (inclusive).
#  Print the extracted substring.

sentence = input("Enter a sentence: ")
# Check if the sentence has at least 10 characters
if len(sentence) >= 10:
    extracted_substring = sentence[4:10]  # Note: Python uses 0-based indexing
    print("Extracted Substring:", extracted_substring)
else:
    print("Input sentence should have at least 10 characters.")


#program to REVERSE A STRING

input_string = "python is fun"
# Reversing the string using slicing
reversed_string = input_string[::-1]
# Displaying the result
print(f"The reversed string is: {reversed_string}")


#program to check for alpha numeric characters

input_string = "Python123"
# Checking if the string is alphanumeric
is_alphanumeric = input_string.isalnum()
# Displaying the result
print(f"The string contains only alphanumeric characters: {is_alphanumeric}")


# program to find how many times abra has occurred in the string ‘abracadabracobra’

input_string = "abracadabra"
# Counting occurrences of 'abra'
substring_count = input_string.count('abra')
# Displaying the result
print(f"The number of times 'abra' appears is: {substring_count}")
