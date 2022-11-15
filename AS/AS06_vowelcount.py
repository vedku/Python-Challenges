a = ("a", "A")
e = ("e", "E")
i = ("i", "I")
o = ("o", "O")
u = ("u", "U")

#number of vowels
no_a = 0
no_e = 0
no_i = 0
no_o = 0
no_u = 0
total_vowels = (no_a + no_e + no_i + no_o + no_u)
word = input("Input:")

if "A" or "a" in word:
    no_a += 1
if "E" or "e" in word:
    no_e += 1
if "I" or "i" in word:
    no_i += 1
if "o" or "O" in word:
    no_o += 1
if "U" or "u" in word:
    no_u += 1


print("Your word had:", no_a, "a's", no_e, "e's", no_i, "i's", no_o, "o's, and", no_u, "u's")
print("In total, your word had", total_vowels, "vowels in total.")
