from math import pi
def area(r):
    ans = pi*r**2
    print("Your circle's area is", ans)
def circumference(r):
    ans = pi*(2*r)
    print("Your circle's circumference is", ans)
radius = int(input("what is the radius of your circle?:"))
area(radius)
circumference(radius)
