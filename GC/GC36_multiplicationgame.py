import random
import time
list = [0,1,2,3,4,5,6,7,8,9,10,11,12]
x = random.choice(list)
y = random.choice(list)
print("What is", x, "multiplied by", y)
time.sleep(3)
print(x*y)
