list = []
def factorial(a):
    if(a == 0 or a == 1):
        return 1
    else:
        ans = 1
        for i in range (1, a+1):
            ans = i
        return int(ans)
def expand(n):
    empt = ""
    if n == 0:
        print("1")
    elif n == 1:
        print("(","a", "+","b" ") ^", n)
        print("Is Equal to")
        print("a", "+","b")
    elif n > 1:
        for i in range(0,n+1):
            list.append(factorial(n)/(factorial(n-i)*factorial(i)))
            empt = empt + str(int(list[i])) + "a" + "^" + str(n-i)
            if i == 0:
                empt = empt + " +"
                continue
            elif i > 0:
                empt = empt + "b" + "^" + str(i)
            empt = empt + " +"
        return empt


print("(a+b)^n")
n = int(input("What is the value of n?:"))
print(expand(n))
