import random

x = random.randint(1, 1000)
print(x)


pokusy = 0
while True:
    hadane_cislo = int(input("Hádej číslo"))
    pokusy += 1

    if hadane_cislo == x:
        print("vyhráls!")
        break

    if hadane_cislo > x:
        print("dej menší")

    if hadane_cislo < x:
        print("dej vetsi")


