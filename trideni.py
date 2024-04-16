import random
import time

random.seed(0)
seznam_cisel = []
maximum = 100
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
            if a > b:
                # kdyz je ten za mnou mensi, tak chci prohodit
                seznam[i] = b
                seznam[i + 1] = a
                prohozeno = True

def setrid_lepe(seznam):
    if len(seznam) == 1:
        return seznam

    prvni_pulka = setrid_lepe(seznam[:len(seznam) // 2])
    druha_pulka = setrid_lepe(seznam[len(seznam) // 2:])

    # spojit
    i, j = 0, 0
    setrideny_seznam = []

    while i < len(prvni_pulka) or j < len(druha_pulka):
        if i == len(prvni_pulka):
            setrideny_seznam.extend(druha_pulka[j:])
            j = len(druha_pulka)
            continue

        elif j == len(druha_pulka):
            setrideny_seznam.extend(prvni_pulka[i:])
            i = len(prvni_pulka)
            continue

        a = prvni_pulka[i]
        b = druha_pulka[j]

        if a < b:
            setrideny_seznam.append(a)
            i += 1
        else:
            setrideny_seznam.append(b)
            j += 1

    return setrideny_seznam

start = time.time()
setrizeno = setrid_lepe(seznam_cisel)
konec = time.time()
print(setrizeno)
print("trvalo to", konec - start, "sekund")
