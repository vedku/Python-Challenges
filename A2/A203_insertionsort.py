def insert(list):
    for i in range(1,len(list)):
        value = list[i]
        j = i - 1
        while j>=0:
            if value < list[j]:
                list[j+1] = list[j]
                list[j] = value
                j -= 1
            else:
                break
meow = [9,2,4,12,53,34569834,1]
insert(meow)
print(meow)
