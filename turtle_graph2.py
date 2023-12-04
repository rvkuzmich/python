#Напишите инструкции черепашьей графики, чтобы нарисовать квадрат со стороной 100 пикселов и круг в центре квадрата. Радиус круга должен составить 80 пикселов.
#Круг должен быть заполнен красным цветом. (Квадрат не должен быть заполнен цветом.)
import turtle
turtle.hideturtle()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.penup
turtle.goto(50, 50)
turtle.pendown
turtle.fillcolor(‘red’)
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()
