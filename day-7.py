#FOR LOOP

languages = ['Swift', 'Python', 'Go']
# access elements of the list one by one
for lang in languages:
    print(lang)

#WHILE LOOP 

# Print numbers until the user enters 0
number = int(input('Enter a number: '))

# iterate until the user enters 0
while number != 0:
    print(f'You entered {number}.')
    number = int(input('Enter a number: '))

print('The end.')


#Infinite While loop

age = 32
# The test condition is always True
while age > 18:
    print('You can vote')

#BREAK STATEMENT 

for i in range(5):
    if i == 3:
        break
    print(i)

#CONTINUE STATEMENT 

for i in range(5):
    if i == 3:
        continue
    print(i)


#multiplicaion table using FOR LOOP 
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


#Sum of Even Numbers using WHILE LOOP
sum_even = 0
counter = 2

while counter <= 50:
    sum_even += counter
    counter += 2

print("Sum of even numbers from 1 to 50:", sum_even)

# Factorial Calculation using FOR LOOP 
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is: {factorial}")

# Generating * pattern using FOR LOOP
for i in range(1, 7):
    for j in range(i):
        print("*", end="")
    print()

#prime no.
num = int(input("Enter a number: "))

if num < 2:
    print(f"{num} is not a prime number.")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")