while True:
    x = int(input("x value:"))
    y = int(input("y value:"))
    def and_l():
        if x == 1 and y ==1:
            print("1")
        else:
            print("0")

    def or_l():
        if x == 1 or y ==1:
            print("1")
        else:
            print("0")

    def nor_l():
        if x ==1 and y ==1:
            print("0")
        elif x ==1 and y == 0:
            print("0")
        elif x ==0 and y ==1:
            print("0")
        if x ==0 and y ==0:
            print("1")

    def xor_l():
        if x == 0 and y == 0:
            print("0")
        if x == 1 and y == 0:
            print("1")
        if x == 0 and y == 1:
            print("1")
        if x == 1 and y == 1:
            print("0")

    def not_l():
        if x ==1:
            print("0")
        elif x == 0:
            print("1")
    choice = input("what gate do u wanna try")
    if choice == "and":
        and_l()
    if choice == "or":
        or_l()
    if choice == "nor":
        nor_l()
    if choice == "xor":
        xor_l()
    if choice == "not":
        not_l()
