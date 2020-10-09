from turtle import *
shape('circle')
speed(10)

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(1,6,1):
    for u in range(i+2):
        color(str(colors[i-1]))
        forward(100)
        left(360/(i+2))
mainloop()
