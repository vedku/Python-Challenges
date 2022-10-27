while True:
    register = ['Aman Ahmad Sanusi','Han Yuan Chew','Elena Foong','Hae Joon (Ray)  Kang','Ved KUWADEKAR','Amanda Lee','Benjamin Lee','Lauren Lee','Bryan Lim','Ryan Ng','Sewon Park','Isaac Pau','Alexander Paul','Samyuktha Rachakonda','Haziq Rumzy','Sanchi Sharma','Shrey Somani','Conor Tan','Come  Vaubourg']

    def search(position):
        for i in range(len(register)):
            if register[i] == position:
                return i
        return -1

    position = input("What student do you want to find the position of?:")
    numberofstudents = len(register)
    output = search(position)
    if position == -1:
        raise Exception ("That student is either not in the class, you have misspelt their name, or have input an unsupported data type")
    else:
        print("The student," , position, "is at position,", output)
