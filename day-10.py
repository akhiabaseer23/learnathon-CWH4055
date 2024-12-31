#LIST

#Create a Python List

 # a list of three elements
ages = [19, 26, 29]
print(ages)

#Using INDEX numbers to access elements

# Access the first element
print(ages[0]) 
# Access the third element
print(ages[2])   


#Add Elements to a Python List using append() method

fruits = ['apple', 'banana', 'orange']
print('Original List:', fruits)
# using append method 
fruits.append('cherry')
print('Updated List:', fruits)

#Remove an Item From a List
fruits.remove('apple')
print(fruits)


#TUPLES

#Create a Python Tuple

numbers = (1, 2, -5)
print(numbers)

#Using index numbers to access tuple items
print(numbers[0])
print(numbers[2])


#get the largest number from a list

a=[1,7,10,34,2,8]
max = a[ 0 ]
for i in a:
	if i > max:
		max = i
print("Largest Number :",max)


#clone or copy a list

old_list = [10, 22, 44, 23, 4]
new_list = list(old_list)
print("Old List : ",old_list)
print("New List : ",new_list)


#find the repeated items of a tuple

t = (2,34,45,6,7,2,4,5,78,34,2)
print(t)
count = t.count(2)
print(count)