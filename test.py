import turtle 

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.pencolor('green')
a = 0
b = 0
#turtle.tracer(0) #remove this line to show the bois how it runs

turtle.speed(0)


while True:
    t.forward(a)
    t.right(b)
    a += 3
    b += 1
    if b == 210:
        break

turtle.done()