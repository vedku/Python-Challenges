number_with_check_digit = input("Input a number with 5 digits:")
num1 = int(number_with_check_digit[0])
num2 = int(number_with_check_digit[1])
num3 = int(number_with_check_digit[2])
num4 = int(number_with_check_digit[3])
x1 = (num1*5)
x2 = (num2*4)
x3 = (num3*3)
x4 = (num4*2)
full_numbers = (x1+x2+x3+x4)
modulo = full_numbers%11
end = 11-modulo
number=int(number_with_check_digit[4])
if end==number:
    print("Check digit confirmed")

