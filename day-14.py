#CLASSES 

#Create a class named MyClass, with a property named x:
class MyClass:
    x = 5

#CREATING AN OBJECT

#Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)

#The __init__() Function

#Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#Object Methods

#create a method in the Person class:
#Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()



#Python class called Rectangle with attributes length and width, and methods to calculate its area and perimeter.

class Rectangle:
    def init(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


#Create a Python class called Student with attributes name, age, and grades, and methods to add grades, 
# calculate average grade, and display student information.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return "No grades available"

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grades:", self.grades)
        print("Average Grade:", self.calculate_average_grade())




#Implement a Python class called Employee with the following requirements:
'''The class should have attributes name, salary, and bonus_percentage.
The constructor should initialize the attributes name, salary, and bonus_percentage.
The class should have a method called calculate_bonus() that calculates and 
returns the bonus amount based on the salary and bonus percentage.
Implement a subclass called Manager which inherits from Employee.The Manager class should have an additional attribute department.
Override the calculate_bonus() method in the Manager class to include a bonus of 10% of the salary.
Create an instance of the Employee class and two instances of the Manager class with different attributes.
 Then, print out the bonus amount for each employee.'''

class Employee:
    def __init__(self, name, salary, bonus_percentage):
        self.name = name
        self.salary = salary
        self.bonus_percentage = bonus_percentage

    def calculate_bonus(self):
        return self.salary * (self.bonus_percentage / 100)

class Manager(Employee):
    def __init__(self, name, salary, bonus_percentage, department):
        super().__init__(name, salary, bonus_percentage)
        self.department = department

    def calculate_bonus(self):
        base_bonus = super().calculate_bonus()
        return base_bonus + (self.salary * 0.1)

employee1 = Employee("John", 50000, 5)
manager1 = Manager("Alice", 80000, 7, "HR")
manager2 = Manager("Bob", 75000, 6, "Finance")

print("Employee 1 Bonus:", employee1.calculate_bonus())
print("Manager 1 Bonus:", manager1.calculate_bonus())
print("Manager 2 Bonus:", manager2.calculate_bonus())  
