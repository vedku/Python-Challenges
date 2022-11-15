word = input("Input word here: ")
number_of_vowels = 0
for letter in 'aeiou':
   if letter in word:
       number_of_vowels += word.count(letter)
print(number_of_vowels)
