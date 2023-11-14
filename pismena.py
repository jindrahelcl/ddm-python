from turtle import *

# Umíme: a, f, h, i, j, k, l, m, o, p, r, s, x, y, z


# Joshua

def pismeno_i():
    left (90)
    forward(100)
    left (180)
    forward(100)
    left(90)

def pismeno_m():
    left(90)
    forward(100)
    left(225)
    forward(40)
    left(90)
    forward(40)
    right(45)
    right(90)
    forward(100)
    left(90)

def pismeno_z():
    forward(50)
    left(180)
    forward(50)
    right(180)
    left(67.5)
    forward(111.8)
    right(180)
    right(67.5)
    forward(50)
    left(90)
    penup()
    forward(100)
    left(90)
    forward(50)
    pendown()



# Honza P.
def pismeno_f (velikost=20):
    left (90)
    forward(5*velikost)
    right(90)
    forward(2*velikost)
    right (180)
    forward(2*velikost)
    left(90)
    forward(2*velikost)
    left(90)
    forward(2*velikost)
    left(180)
    forward(2*velikost)
    left(90)
    forward(3*velikost)
    left(90)
    penup()
    forward(30)
    pendown()


def pismeno_k(velikost=20):
    left(90)
    forward(2.5*velikost)
    right(45)
    forward(3*velikost)
    right(180)
    forward(3*velikost)
    left(90)
    forward(3*velikost)
    left(180)
    forward(3*velikost)
    right(45)
    forward(2.5*velikost)
    left(180)
    forward(5*velikost)
    left(90)
    penup()
    forward(30)
    pendown()

def pismeno_p (velikost=20):
    left(90)
    forward(5*velikost)
    right(90)
    for i in range(59):
        right(3)
        forward(0.06*velikost)
    right(3)
    left(90)
    forward(2.7*velikost)
    left(90)
    penup()
    forward(25)
    pendown()

def pismeno_o (velikost=20):
    penup()
    forward(2*velikost)
    pendown()
    for i in range(45):
        left(2)
        forward(0.06*velikost)
    forward(0.45*velikost)
    for i in range(90):
        left(2)
        forward(0.06*velikost)
    forward(0.45*velikost)
    for i in range(45):
        left(2)
        forward(0.06*velikost)
    penup()
    forward(2*velikost)
    pendown()


# Matyáš
def pismeno_y():
    penup()
    forward(25)
    pendown()
    left(90)
    forward(50)
    left(30)
    forward(50)
    left(180)
    penup()
    forward(50)
    left(120)
    pendown()
    forward(50)
    penup()
    right(180)
    forward(50)
    left(30)
    forward(50)
    left(90)
    forward(25)
    pendown()

def pismeno_l():
    forward(50)

    penup()
    right(180)
    forward(50)
    right(90)
    pendown()
    forward(100)
    right(180)
    penup()
    forward(100)
    left(90)
    forward(50)


# Patrick
def letter_H():
    left(90)
    forward(50)
    left(180)
    forward(100)
    left(180)
    forward(50)
    right(90)
    forward(40)
    right(90)
    forward(50)
    left(180)
    forward(100)
    left(180)
    forward(100)
    left(90)



def pismeno_a():
    left(90)
    forward(100)
    right(90)
    forward(50)
    # tady nakresli zbytek
    right(90)
    forward(100)
    right(180)
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(100)
    right(180)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    left(90)

def pismeno_x():
    penup()
    right(30)
    forward(60)
    right(90)
    pendown()
    forward(120)
    right(180)
    forward(60)
    right(120)
    forward(60)
    right(180)
    forward(120)
    right(180)
    forward(120)
    left(90)


# Zoe

def pismeno_j():
    right(90)
    for i in range (180):
       left(1)
       forward(0.5)
    forward(100)
    left(90)
    forward(50)
    penup()
    left(90)
    forward(100)
    left(90)
    forward(50)
    pendown()



def pismeno_r():
    left(90)
    forward(100)
    right(90)
    for i in range (180):
        right(1)
        forward(0.5)
    left(130)
    forward(65)
    left(50)



def pismeno_s():
    penup()
    left(90)
    forward(80)
    right(90)
    forward(50)
    left(175)
    pendown()
    for i in range(180):
        left(1)
        forward(0.5)
    for i in range(180):
        right(1)
        forward(0.5)
    penup()
    left(180)
    forward(60)
    pendown()


speed(10)
penup()
goto(-600,200)
pendown()

# Umíme: a, f, h, i, j, k, l, m, o, p, r, s, x, y, z

# letter_H()
# penup()
# forward(20)
# pendown()
#
#
# pismeno_y()
# penup()
# forward(20)
# pendown()

pismeno_a()
penup()
forward(20)
pendown()


pismeno_k()
penup()
forward(20)
pendown()

pismeno_a()
penup()
forward(20)
pendown()

# pismeno_s()
# penup()
# forward(20)
# pendown()

pismeno_p()
penup()
forward(20)
pendown()

pismeno_f()
penup()
forward(20)
pendown()

pismeno_m()
penup()
forward(20)
pendown()

pismeno_i()
penup()
forward(20)
pendown()

pismeno_k()
penup()
forward(20)
pendown()

pismeno_z()
penup()
forward(20)
pendown()

pismeno_j()
penup()
forward(20)
pendown()

pismeno_x()
penup()
forward(20)
pendown()

pismeno_o()
penup()
forward(20)
pendown()

pismeno_l()
penup()
forward(20)
pendown()

pismeno_r()
penup()
forward(20)
pendown()



exitonclick()
