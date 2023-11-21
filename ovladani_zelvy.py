from turtle import *

wn = Screen()
wn.tracer(0)

def nahoru():
    forward(10)
    wn.update()

def dolu():
    left(180)
    forward(10)
    left(180)
    wn.update()

def vlevo():
    left(90)
    forward(10)
    right(90)
    wn.update()

def vpravo():
    right(90)
    forward(10)
    left(90)
    wn.update()

left(90)
wn.update()
wn.onkey(nahoru, "Up")
wn.onkey(dolu, "Down")
wn.onkey(vlevo, "Left")
wn.onkey(vpravo, "Right")

wn.listen()
wn.mainloop()