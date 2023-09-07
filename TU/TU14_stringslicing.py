MyOwnVariable = "Cattery"

forward_1 = MyOwnVariable[:3] #returns the first three characters
forward_2 = MyOwnVariable[1:6] #returns characters 1 to 6
forward_3 = MyOwnVariable[::2] #returns every second character

backward_1 = MyOwnVariable[-3:] #returns the last three characters
backward_2 = MyOwnVariable[::-1] #returns the word in reverse order
backward_3 = MyOwnVariable[::-2] #returns every second character backwards

print(forward_1, forward_2, forward_3, backward_1, backward_2, backward_3)
