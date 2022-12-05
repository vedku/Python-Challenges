import random
studentnum = int(input("How many students:"))
comments = ("well done!", "revise more", "outstanding!", "incomplete???")
for i in range(studentnum):
    print(random.choice(comments))
