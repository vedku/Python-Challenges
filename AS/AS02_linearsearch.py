while True:
    register = [#put your own list here]

    def search(position):
        for i in range(len(register)):
            if register[i] == position:
                return i
        return -1

    position = input("What student do you want to find the position of?:")
    numberofstudents = len(register)
    output = search(position)
    if position not in register:
        raise Exception("That student is either not in the class, you have misspelt their name, or have input an unsupported data type")
    else:
        print("The student," , position, "is at position,", output)
