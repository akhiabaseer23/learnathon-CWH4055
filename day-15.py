#CONSTRUCTORS 

#Types of Constructors 
#Parameterized Constructor

class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")


#Default Constructor

class Details:
  def __init__(self):
    print("animal Crab belongs to Crustaceans group")
obj1=Details()


#DECORATORS
 
#Use-Case Scenario

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b


'''Define a Python class called **`Book`** with the following requirements:

- The class should have attributes **`title`**, **`author`**, and **`published_year`**.
- Implement a constructor method that initializes these attributes.
- Implement a method called **`display_info()`** that prints out the book's information in a formatted manner. '''


class Book:
    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Published Year: {self.published_year}")

# Example usage:
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book1.display_info()



'''Implement a Python decorator called time_it that calculates and prints the execution time of a function. 
The decorator should be used to decorate a function of your choice.'''

import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time} seconds")
        return result
    return wrapper

# Example usage:
@time_it
def calculate_sum(n):
    sum_result = sum(range(n))
    return sum_result

result = calculate_sum(1000000)
print("Result:", result)
