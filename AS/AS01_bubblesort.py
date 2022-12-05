def bubblesort(list):
    for i in range(len(list)-1,0,-1):
        for k in range(i):
            if list[k]>list[k+1]:
                bruh = list[k]
                list[k]=list[k+1]
                list[k+1] = bruh

list = [2,3,4,88,34,21,2345,875,4567,9,99,23452345,999,9,99999,999999]
bubblesort(list)
print(list)
