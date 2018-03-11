# CTI-110 P2HW2 - Tip Tax Total Luis Ventura 2/25/2018

# Find the total cost of the meal

foodCost = float(input("Enter the amount charged for the food: "))

# Calculate tip (18%)
tipAmount = foodCost * .18

# Calculate sales tax (7%)
salesTax = foodCost * .07

# Calculate the total cost
totalCost = (foodCost + tipAmount + salesTax)


# Display the total amount of meal cost
print ("Amount of the meal cost: $", foodCost )

# Display the tip
print ("Tip Amount: $", tipAmount )

# Display the sales tax
print ("Sales Tax: $", salesTax )


# Display the total puchase amount
print ("Amount of the meal total cost: $", totalCost )
