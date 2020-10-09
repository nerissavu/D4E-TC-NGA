from turtle import *
shape('circle')
speed(10)
for i in range(1,10,1):
    if i % 2 == 0:
        color('blue')
    else:
        color('red')
    for u in range(i+2):
            forward(100)
            left(360/(i+2))
mainloop()