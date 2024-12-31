#FUNCTIONS

#Create a Function
def greet():
    print('Hello World!')

# call the function

greet()
print('Outside function')

#Python Function Arguments
def greet(name):
    print("Hello", name)

# pass argument
greet("John")


# Function to Add Two Numbers

# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

# function call with two values
add_numbers(5, 4)

#The RETURN STATEMENT 

# function definition
def find_square(num):
    result = num * num
    return result

# function call
square = find_square(3)

print('Square:', square)


#The pass Statement

def future_function():
    pass

# this will execute without any action or error
future_function()  


# LIBRARY Function
import math

# sqrt computes the square root
square_root = math.sqrt(4)

print("Square Root of 4 is",square_root)

# pow() comptes the power
power = pow(2, 3)

print("2 to the power 3 is",power)

'''Creating a function called **`grade_converter`** that takes a numerical grade as an argument and returns the corresponding letter grade (A, B, C, D, F) based on the standard grading scale.
- If the score is greater than or equal to 90, print "A"
- If the score is between 80 and 89, print "B"
- If the score is between 70 and 79, print "C"
- If the score is between 50 and 69, print "D"
- If the score is below 50, print "F" '''

def grade_converter(numerical_grade):
    if numerical_grade >= 90:
        return 'A'
    elif numerical_grade >= 80:
        return 'B'
    elif numerical_grade >= 70:
        return 'C'
    elif numerical_grade >= 50:
        return 'D'
    else:
        return 'F'
letter_grade = grade_converter(85)
print(f"Letter Grade: {letter_grade}")

'''defining a function called outer_function. Inside outer_function, declare a variable x with a value of 10.
   Then, define another function called inner_function inside outer_function. 
   Inside inner_function, declare a variable y with a value of 5.
   Return the sum of x and y from inner_function. Finally, call outer_function and print the result.
Solution'''

def outer_function():
    x = 10  # Variable in the outer function's scope
    
    def inner_function():
        y = 5  # Variable in the inner function's scope
        return x + y  # Accessing x from the outer function's scope
    
    result = inner_function()
    return result

# Example Usage:
result_value = outer_function()
print(f"Result: {result_value}")