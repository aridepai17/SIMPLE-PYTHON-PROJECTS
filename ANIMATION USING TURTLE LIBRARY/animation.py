import turtle

turtle.bgcolor("black")
turtle.pensize(1)
turtle.speed(0.5)
color = ["red", "yellow", "green", "blue", "orange", "purple"]

for a in range(10):
    for i in color:
        turtle.color(i)
        turtle.circle(100)
        turtle.left(10)
        
turtle.mainloop()
