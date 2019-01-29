import turtle

turtle.pen()
for i in range(5):
    turtle.goto(0,-i*36)
    turtle.circle(100+i)
turtle.circle(100)
turtle.done()


