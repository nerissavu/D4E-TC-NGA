from turtle import *
shape('circle')
speed(-1)

color('blue')

for i in range(50):
    for u in range(4):
        forward(100-2*i)
        left(90)  

    left(10)

mainloop()
