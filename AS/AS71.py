usable_characters = ['1','0']
password = ""
copycat = ""
length = int(input("How long do u want your password to be?:"))
import random
while True:
    for i in range(length):
        password += random.choice(usable_characters)
    for i in range(length):
        copycat += random.choice(usable_characters)
    if password == copycat:
        print(password)
        print(copycat)
        print("they match!!!1!!!1!")
    break
