def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

x = int(input("input number 1:"))
y = int(input("input number 2:"))
print(gcd(x, y))
