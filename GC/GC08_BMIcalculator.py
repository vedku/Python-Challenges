def height():
    height = float(input("How tall are you? (M):"))
    return height

def weight():
    weight = int(input("How much do you weigh? (kg):"))
    return weight

weight = weight()
height = height()
BMI = weight/height**2
print(BMI)

if BMI < 18.5:
    print("You are underweight!")
elif 18.5 <= BMI < 25:
    print("You are at normal weight!")
elif 25 <= BMI < 30:
    print("You are overweight!")
elif BMI > 30:
    print("You are obese!")
