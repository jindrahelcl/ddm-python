from turtle import *
shape("turtle")
speed(10)
color("blue")

def ctverec(velikost):
    for i in range(4):
        left(90)
        forward(velikost)

def otazka():
    tvar = ""
    while tvar != "čtverec" and tvar != "trojúhelník":
        tvar = textinput("ahoj", "co mam kreslit: ")
    return tvar

tvar = otazka()
if tvar == "čtverec":
    ctverec(50)
else:
    trojuhelnik()

exitonclick()