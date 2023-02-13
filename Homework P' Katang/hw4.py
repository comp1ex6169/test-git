import math
import turtle
rad1 = float(input("Enter Radius: "))
x = float(input("Enter X: "))
y = float(input("Enter Y: "))
pi = math.pi
area = pi*rad1*rad1
print(area)
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
turtle.circle(rad1)
turtle.write(area)
turtle.done()