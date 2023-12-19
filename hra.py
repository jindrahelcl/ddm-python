mistnosti = ["obývák", "chodba", "sklep", "trůnní sál"]
chodby = [[1, 2], [0, 3], [0], [1, 2]]

zlato = [1, 10, 0, 300]

hrac = 0
skore = 0

def hotovo():
    return sum(zlato) == 0

while not hotovo():
    print("hráč je v místnosti:", mistnosti[hrac])
    print("hráč má", skore, "zlata")
    print("zbývá zlata:", sum(zlato))

    kam_lze_jit = chodby[hrac]
    for i, moznost in enumerate(kam_lze_jit):
        print("Moznost", i + 1, ": ", mistnosti[moznost])

    if zlato[hrac] > 0:
       print("Moznost X : sebrat", zlato[hrac], "zlata")

    vstup = input("> ")
    # vstup_ok = False
    # while not vstup_ok:
    #     vstup = input("> ")
    #
    #     if vstup == "x" and zlato[hrac] > 0:
    #         vstup_ok = True
    #         break

    if vstup == "x":
        skore += zlato[hrac]
        zlato[hrac] = 0
    else:
        index_moznosti = int(vstup)







    break
