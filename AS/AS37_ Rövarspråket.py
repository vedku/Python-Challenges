MyStr = input()
Robber = ""
vowel = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
for char in MyStr:
    if char not in vowel:
        Robber += char
    else:
        Robber += char + "o"+ char



print(Robber)
