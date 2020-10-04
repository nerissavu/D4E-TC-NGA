from turtle import *

shape('circle')
color('yellow')
pencolor('green')
speed(10)
for i in range(1,10,1):
    for u in range(i+2):
        forward(100)
        left(360/(i+2))
mainloop()