import random
seznam_slov = []
with open("slova.txt", "r") as f:
    for radek in f:
        radek = radek.strip()
        seznam_slov.append(radek)
hadam_slovo = random.choice(seznam_slov)

tipy = []
hotovo = False

while not hotovo:
    tip = input("rekni pismenko: ")
    if len(tip) != 1:
        print("spatne")
        continue
    tipy.append(tip)
    uhodnuto = []
    hotovo = True
    for p in hadam_slovo:
        if p in tipy:
            uhodnuto.append(p)
        else:
            uhodnuto.append("_")
            hotovo = False

    slovo = " ".join(uhodnuto)
    print(slovo)

print("Gratuluju")




