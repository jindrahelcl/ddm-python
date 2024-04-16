import random

seznam_cisel = []
maximum = 30
pocet = 5

for i in range(pocet):
    seznam_cisel.append(random.randint(0, maximum))

print(seznam_cisel)

def setrid(seznam):

    prohozeno = True
    while prohozeno:
        prohozeno = False

        # projdeme seznam:
        for i in range(len(seznam) - 1):
            a = seznam[i]
            b = seznam[i + 1]

            # vezmu cislo a porovnam s cislem za mnou.
            print(a, b)
            if a > b:
                # kdyz je ten za mnou mensi, tak chci prohodit
                seznam[i] = b
                seznam[i + 1] = a
                prohozeno = True

setrid(seznam_cisel)
print(seznam_cisel)