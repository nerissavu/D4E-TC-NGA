from turtle import *

shape('circle')
color('yellow')
pencolor('green')
speed(90)
for i in range(0,1000,5):
	forward(i)
	left(90)
mainloop()