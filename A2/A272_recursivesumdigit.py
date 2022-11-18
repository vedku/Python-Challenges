def sum(num):
    ans = 0
    for i in str(num):
        ans += int(i)
    return ans
num = input(("Number here plz:"))
print(sum(num))
