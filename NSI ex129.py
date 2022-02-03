from turtle import *

r = 20

t = [[False, False, True],
     [False, False, True],
     [True, True, True]]

def square(x, y, c):
    fillcolor(c)
    color(c)
    
    up()
    goto(x, y)
    down()
    
    begin_fill()
    for i in range(4):
        forward(r)
        right(90)
    end_fill()

for i in range(len(t)):
    for j in range(len(t[0])):
        c = "white"
        if t[i][j]:
            c = "black"
            
        square(j * r, -i * r, c)