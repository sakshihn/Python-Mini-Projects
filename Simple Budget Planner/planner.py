#Planning a budget for the month as a hosteller
rent = int(input("Enter the rent of the month: "))
food = int(input("Enter the food expenses of the month: "))
shopping = int(input("Enter the shopping expenses of the month: "))
accessories = int(input("Enter the accessories expenses of the month: "))
Groceries = int(input("Enter the groceries expenses of the month: "))

tummy = food + Groceries

total = rent + tummy + shopping + accessories

print("The total expences of the month is: ",total)