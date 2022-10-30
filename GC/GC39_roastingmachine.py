import random
continuation = "y"
while continuation in ("y"):
    name = input("What's your name, sonny boy?:")
    roasts = ["You are being insulted, " + name ,"Hey," + name + "you are n00b."]
    output = random.choice(roasts)
    print(output)
    continuation = input("Do you wanna get roasted again? (y/n):")
