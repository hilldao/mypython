import turtle
import os

##Draw square
def draw_square(new_turtle):
    for i in range(1,5):
        new_turtle.forward(100)
        new_turtle.right(90)      

##Draw rhombus    
def draw_rhombus(new_turtle):
    new_turtle.forward(100)
    new_turtle.right(30) 
    new_turtle.forward(100)
    new_turtle.right(150)
    new_turtle.forward(100)
    new_turtle.right(30)
    new_turtle.forward(100)
    new_turtle.right(150)

##Draw triangle    
def draw_triangle(length,new_trutle):
    for i in range (1,4):
        new_trutle.forward(length)
        new_trutle.left(120)

##Draw triangle inside       
def draw_inside(level,in_length,new_trutle):
     if level == 1:
        draw_triangle(in_length/2,new_trutle)
        new_trutle.forward(in_length/2)
        draw_triangle(in_length/2,new_trutle)
        new_trutle.left(120)
        new_trutle.forward(in_length/2)
        new_trutle.right(120)
        draw_triangle(in_length/2,new_trutle)
        new_trutle.forward(in_length/2)
        new_trutle.right(60)
        new_trutle.forward(in_length/2)
        new_trutle.right(120)
        new_trutle.forward(in_length)
        new_trutle.right(180)
        

     else :
          new_level = level - 1
          new_length = in_length/2
          draw_inside(new_level,new_length,new_trutle)
          new_trutle.forward(new_length)
          draw_inside(new_level,new_length,new_trutle)
          new_trutle.left(120)
          new_trutle.forward(new_length)
          new_trutle.right(120)
          draw_inside(new_level,new_length,new_trutle)
          new_trutle.forward(new_length)
          new_trutle.right(60)
          new_trutle.forward(new_length)
          new_trutle.right(120)
          new_trutle.forward(2*new_length)
          new_trutle.right(180)

##Total Draw action         
def draw_art():
    window = turtle.Screen()
    window.bgcolor("gray")
    cwd = os.getcwd()
    print('Current path is'+cwd)
    os.chdir('D:\Work\Python Scripts')
    window.register_shape("run.gif")
    brad = turtle.Turtle()
    jason = turtle.Turtle()
    brad.shape("run.gif")
    brad.color("black")
    brad.speed(60)
    in_length=640
    brad.penup()
    brad.goto(-in_length/2,-in_length/2)
    brad.pencolor("yellow")
    brad.pendown()
    draw_inside(6,in_length,brad)


    window.exitonclick()  


draw_art()

"""
    for i in range(1,72):
        draw_rhombus(brad)
        brad.right(5)

    brad.goto(0,-300)

    
    jason.shape("turtle")
    jason.color("red")
    jason.speed(3)
    jason.goto(80,80)
    
   
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.circle(100)
    brad.right(180)
    brad.circle(200)
    brad.circle(100)
    brad.right(180)
    brad.circle(90)
    brad.right(120)
    brad.forward(100)
    brad.right(120)
    brad.forward(100)
    brad.right(120)
    brad.forward(100)
    for i in range(5):
         jason.forward(100)
         jason.right(144)
    jason.up()
       new_length = in_length/2
       draw_inside(new_level,new_length,new_trutle)
       new_trutle.right(60)
       new_trutle.forward(new_length)
       draw_inside(new_level,new_length,new_trutle) 
       new_trutle.left(60)
       new_trutle.forward(new_length)
       draw_inside(new_level,in_length,new_trutle) """


