from turtle import Turtle, Screen
import random
colours=["red", "green yellow", "sky blue",  "indian red",  "orange red",  "purple", "salmon", "dark olive green", "magenta", "dark orange",  "beige", "royal blue", "dark green","forest green", "firebrick" ]
leonardo_the_turtle=Turtle()
leonardo_the_turtle.pensize(4)


leonardo_the_turtle.shape("turtle")



a = random.random()
b = random.random()
c = random.random()

leonardo_the_turtle.color(a,b,c)
 



i = 2
while i < 8:
  
  i += 1
  for x in range(i):
    
    leonardo_the_turtle.pencolor((random.choice(colours)))
    leonardo_the_turtle.forward(60)
    leonardo_the_turtle.left(-360/i)
    