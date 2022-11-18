def expand(co_a, co_b, n):
    if n == 1:
        print("(",co_a,"a", "+", co_b,"b" ") ^", n)
        print("Is Equal to")
        print(co_a,"a", "+", co_b,"b")
    elif n > 1:
        for i in range(n):
            ans = co_a*co_a, "+", co_a*co_b
            #print("the amount of times this is printed is the amount of times it needs to be multiplied by itself")
            print(ans)

print("(a+b)^n")
co_a = int(input("What is the coefficient of a?:"))
co_b = int(input("What is the coefficient of b?"))
n = int(input("What is the value of n?:"))
expand(co_a, co_b, n)
