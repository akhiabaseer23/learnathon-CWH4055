#Python if Statement

number = int(input('Enter a number: '))
# check if number is greater than 0
if number > 0:
    print(f'{number} is a positive number.')
print('A statement outside the if statement.')


#Python if…else Statement

number = int(input('Enter a number: '))
if number > 0:
    print('Positive number')
else:
    print('Not a positive number')


# Python if…elif…else Statement

number = -5
if number > 0:
    print('Positive number')
elif number < 0:
    print('Negative number')
else:
    print('Zero')

#Python Nested if Statements

number = 5

# outer if statement
if number >= 0:
    # inner if statement
    if number == 0:
      print('Number is 0')
    
    # inner else statement
    else:
        print('Number is positive')

# outer else statement
else:
    print('Number is negative')


#program that checks if a given number is positive, negative, or zero. If it's positive, print "Positive number." If it's negative, print "Negative number." If it's zero, print "Zero."

number = float(input("Enter a number: "))

if number > 0:
    print("Positive number.")
elif number < 0:
    print("Negative number.")
else:
    print("Zero.")


#Create a program that takes a student's exam score as input. Classify the student's performance as follows:
'''If the score is greater than or equal to 90, print "A"
If the score is between 80 and 89, print "B"
If the score is between 70 and 79, print "C"
If the score is between 50 and 69, print "D"
If the score is below 50, print "F"
Solution'''

score = float(input("Enter the exam score: "))
if score >= 90:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
else:
    print("F")


#program that determines whether a given year is a leap year or not. A leap year is either divisible by 4 but not divisible by 100, or it is divisible by 400.

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#Python program that determines the price of a movie ticket based on the age and time of the show.
#The program should take the age and time (in 24-hour format) as inputs and use the **`match`** statement to calculate and print the ticket price according to the following rules:

'''- For age 0-5, the ticket is free.
- For age 6-12, the ticket is $10.
- For age 13-18, the ticket is $15.
- For age 19 and above, the ticket is $20.
- For shows before 12:00 PM, there is a $5 discount on the ticket.'''



age = int(input("Enter your age: "))
show_time = int(input("Enter the show time (in 24-hour format): "))

match age:
    case 0 | 1 | 2 | 3 | 4 | 5:
       ticket_price =  0  # Free ticket for ages 0-5
    case 6 | 7 | 8 | 9 | 10 | 11 | 12:
       ticket_price =  10  # $10 ticket for ages 6-12
    case 13 | 14 | 15 | 16 | 17 | 18:
       ticket_price =  15  # $15 ticket for ages 13-18
    case _:
       ticket_price =  20  # $20 ticket for age 19 and above

# Apply discount for shows before 12:00 PM
if show_time < 12:
    ticket_price -= 5

print(f"The ticket price is ${ticket_price}.")