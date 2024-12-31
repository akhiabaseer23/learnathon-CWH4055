#RECURSIONS 

#Recursive Function

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 3
print("The factorial of", num, "is", factorial(num))


#PYTHON LOCAL VARIABLES

def greet():

    # local variable
    message = 'Hello'
    
    print('Local', message)
greet()


#PYTHON GLOBAL VARIABLES

# declare global variable
message = 'Hello'
def greet():
    # declare local variable
    print('Local', message)
greet()
print('Global', message)

#Changing Global Variable From Inside a Function using global
# global variable
c = 1 
def add():

    # use of global keyword
    global c

    # increment c by 2
    c = c + 2 

    print(c)
add()


#Recursive function to find the sum of digits of a positive integer.

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

# Example usage:
number = 12345
result = sum_of_digits(number)
print(f"The sum of digits in {number} is: {result}")


#Recursive function to reverse a string.

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

# Example usage:
text = "Hello, World!"
result = reverse_string(text)
print(f"The reversed string is: {result}")


#Recursive function to calculate the power of a number (e.g., x^n)?

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

result = power(2, 3)
print(result)
