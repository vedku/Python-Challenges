import random
balance = random.randint(5,5000000)
x = int(input("How much would you like to withdraw?"))
if x%5 != 0:
    print("You can only withdraw a value which is a multiple of 5")
    x = int(input("How much would you like to withdraw?"))
else:
    balance -= (x+0.5)
    print("Your new balance is:", balance)
