from turtle import *
bgcolor('cyan')
speed(0)
for i in range(300,-300,-10):
    penup()
    goto(-400,i)
    pendown()
    fd(600)
rt(90)
for l in range(-400,210,10):
    penup()
    goto(l,300)
    pendown()
    fd(590)
