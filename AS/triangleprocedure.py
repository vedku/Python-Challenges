#this makes equilateral triangles. Lines 10-12 can be modified to create right angled, isosceles or scalene triangles.
import turtle

def triangle_draw(x,y,sz):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(3):
        turtle.forward(sz)
        turtle.left(900)
        turtle.right(60)
        
triangle_draw(0,0,10)
for y in range (-100,100,20):
    for x in range (-100,100,20):
        triangle_draw(x,y,10)

turtle.mainloop()
