import random
list = []
for i in range(50):
    x = random.randint(1,100)
    list.append((x))
print(list)
print(min(list), "is the minimum")
print(max(list), "is the maximum")
print(sum(list)/len(list), "is the mean")
