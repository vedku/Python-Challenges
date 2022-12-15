from random import shuffle
floors = int(input())
order = []
for i in range(1, floors+1):
    order.append(i)
print(order)
shuffle(order)
print(order)
