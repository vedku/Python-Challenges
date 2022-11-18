char_num = 0
with open("thegreatgatsby.txt","r") as Gatsby:
    for line in Gatsby:
        words = line.split()
    for i in words:
        char_num += len(i)
print(char_num/len(words))
