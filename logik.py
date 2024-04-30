import random

POZIC = 5
BAREV = 8

zadani = []
for i in range(POZIC):
    zadani.append(random.randint(0, BAREV - 1))
print(zadani)

krok = 0

hotovo = False
while not hotovo:
    tip_retezec = input("Dodej tip: ")
    tip = []
    for d in tip_retezec:
        tip.append(int(d))
    if len(tip) != POZIC:
        print("spatne")
        continue

    krok += 1

    cerny = 0
    for i in range(POZIC):
        if tip[i] == zadani[i]:
            cerny += 1

    bily = 0
    for i in range(BAREV):
        v_tipu = 0
        v_zadani = 0
        for j in range(POZIC):
            if tip[j] == zadani[j]:
                continue

            if tip[j] == i:
                v_tipu += 1
            if zadani[j] == i:
                v_zadani += 1

        bily += min(v_tipu, v_zadani)

    print(cerny, bily)

    if cerny == POZIC:
        hotovo = True

print("Splněno po ", krok, "krocích")