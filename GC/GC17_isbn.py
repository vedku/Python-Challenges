#this is from my year 11 pre release lmao

frequent_parking_number = input("Input your frequent parking number:")
num1 = int(frequent_parking_number[0])
num2 = int(frequent_parking_number[1])
num3 = int(frequent_parking_number[2])
num4 = int(frequent_parking_number[3])
x1 = (num1*5)
x2 = (num2*4)
x3 = (num3*3)
x4 = (num4*2)
full_numbers = (x1+x2+x3+x4)
modulo = full_numbers%11
end = 11-modulo
number = int(frequent_parking_number[4])
if end == number:
    print("Check digit confirmed, you are eligible for a discount!")
