list1 = ["John", 123123123123123123, "James"]
list2 = ["John", "James"]
diff = []
for i in list1:
    if i not in list2:
        diff.append(i)
print(diff)
