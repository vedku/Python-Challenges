import random
options = ("c", "s")
while True:
    a = input("Would you like to confess[c] or stay silent[s]:")
    b = random.choice(options)
    if a == "c" and b == "s":
        print("a's prison sentence is 0 years as they snitched")
        print("b's prison sentence is 20 years as they were a real one and stayed quiet")
    elif b == "c" and a == "s":
        print("b's prison sentence is 0 years as they snitched")
        print("a's prison sentence is 20 years as they were a real one and stayed quiet")
    elif a == "s" and b == "s":
        print("a and b will be in prison for 1 year each")
    elif a == "c" and b == "c":
        print("a and b will be in prison for 5 years each")
    cont = input("would you like to continue? (y/n):")
    if cont == "n":
        break
