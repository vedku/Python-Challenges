import random
words = ["average",
"entertaining",
"oven",
"murky",
"knotty",
"collar",
"call",
"talented",
"dependent",
"enter",
"corn",
"giddy"]
length = int(input("How many words would you like your passphrase to be?:"))
for i in range(length):
    print(random.choice(words))
