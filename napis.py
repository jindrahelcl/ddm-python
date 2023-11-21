from abeceda import *
slovo = textinput("AAA", "Zadej slovo: ")

def mezera():
    penup()
    forward(20)
    pendown()

for pismeno in slovo:
    if pismeno == "a":
        pismeno_a()
    elif pismeno == "h":
        pismeno_h()
    elif pismeno == "o":
        pismeno_o()
    elif pismeno == "j":
        pismeno_j()

    mezera()


exitonclick()