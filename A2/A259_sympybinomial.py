import sympy
a, b = sympy.symbols("a b")
print("(a+b)^n")
ac = int(input("What is the coefficient of a?:"))
bc = int(input("What is the coefficient of b?:"))
formula = ((ac*a) + (bc*b)) ** int(input("What is the value of n?:"))
print(f"\n{formula.expand()}")
