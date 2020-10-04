from turtle import *

shape('circle')
color('yellow')
pencolor('green')
begin_fill() 
for _ in range(3): 
  left(120)  
  forward(100) 
end_fill()

mainloop()