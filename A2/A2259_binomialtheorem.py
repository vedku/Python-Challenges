def expand(co_a, co_b, n):
    if n == 1:
        print("(",co_a,"a", "+", co_b,"b" ") ^", n)
        print("Is Equal to")
        print(co_a,"a", "+", co_b,"b")
    elif n > 1:
        for i in range(n):
            a_value = co_a**2
            b_value = 2*(co_a*co_b)
            c_value = co_b**2
            #print("the amount of times this is printed is the amount of times it needs to be multiplied by itself")
            print(a_value, b_value, c_value)

print("(a+b)^n")
co_a = int(input("What is the coefficient of a?:"))
co_b = int(input("What is the coefficient of b?"))
n = int(input("What is the value of n?:"))
expand(co_a, co_b, n)
