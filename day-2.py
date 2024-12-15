#ESCAPE SEQUENCE

print("This is a multi-line message using the newline character.\n"
"Tabbed text can be created using the tab character.\t"
"Quotes can be included using escape characters like this: \"Hello!\"\n")

#let us see an example using newline char '\n'

print("I like manogoes\nI like oranges")

#Example using tab character

print("python is a dynamic and\thigher level interpreted language")

#PROGRAM to CALCULATE the TOTAL COST OF ITEMS INCLUDING TAX

# Get user input for the number of items and cost per item
num_items = int(input("Enter the number of items: "))
cost_per_item = float(input("Enter the cost per item: $"))



# Calculate the total cost without tax
total_cost_before_tax = num_items * cost_per_item

# Assume a 10% tax rate
tax_rate = 0.1
tax_amount = total_cost_before_tax * tax_rate

# Calculate the total cost including tax
total_cost_after_tax = total_cost_before_tax + tax_amount

# Display the results
print("\nResults:")
print("Total cost before tax: ${:.2f}".format(total_cost_before_tax))
print("Tax amount (10%): ${:.2f}".format(tax_amount))
print("Total cost after tax: ${:.2f}".format(total_cost_after_tax))


#PROGRAM TO CALCULATE AREA OF RECTANGLE

# Get user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate area
area = length * width

# Display the results
print("\nResults:")
print("Area of the rectangle: {:.2f} square units".format(area))


#PROGRAM TO SWAP TWO VARIABLES


# Input variables
a = int(input("Enter the value of variable 'a': "))
b = int(input("Enter the value of variable 'b': "))

# Displaying the values before swapping
print("Before swapping:")
print("a =", a)
print("b =", b)

# Swapping the values 
a = a + b
b = a - b
a = a - b

# Displaying the values after swapping
print("\nAfter swapping:")
print("a =", a)
print("b =", b)