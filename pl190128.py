import turtle

turtle.pen()
for i in range(5):
    turtle.goto(0,-i*36)
    turtle.circle(100+i)
turtle.circle(100)
turtle.done()

turtle.pen()
my_colors = ("red","green","yellow","black")
turtle.width(10)
turtle.speed(5)
for i in range(10):
    turtle.penup()
    turtle.goto(0,-i*20)
    turtle.pendown()
    turtle.color(my_colors[i%len(my_colors)])
    turtle.circle(100+i*20)

turtle.done()
