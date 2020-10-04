from turtle import *

shape('circle')
color('yellow')
pencolor('green')
begin_fill() 
for _ in range(4): 
  forward(100) 
  right(90)
end_fill()

mainloop()