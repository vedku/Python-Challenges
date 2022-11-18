def expand(co_a, co_b, n):
    if n == 1:
        print("(",co_a,"a", "+", co_b,"b" ") ^", n)
        print("Is Equal to")
        print(co_a,"a", "+", co_b,"b")
    elif n > 1:
        for i in range(n):
            a_value = co_a*co_a
            ab_value = (co_a*co_b) + (co_a*co_b)
            b_value = co_b*co_b
            print(a_value,"a^2", ab_value,"ab", b_value,"b^2")

print("(a+b)^n")
co_a = int(input("What is the coefficient of a?:"))
co_b = int(input("What is the coefficient of b?"))
n = int(input("What is the value of n?:"))
expand(co_a, co_b, n)
