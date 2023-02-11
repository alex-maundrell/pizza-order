# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25

# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.
bill = 0

size = input("What size of pizza would you like? S, M, L: ").lower()
pep = input("Would you like pepperoni? Y or N: ").lower()
x_cheese = input("Would you like extra cheese? Y or N: ").lower()

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    print("You did not enter a valid size. See ya...")

if pep == "y" and size == "s":
    bill += 2
elif pep == "y" and size == "m":
    bill += 3
elif pep == "y" and size == "l":
    bill += 3

if x_cheese == "y":
    bill += 1

print(f"Your total bill is: ${bill}")
