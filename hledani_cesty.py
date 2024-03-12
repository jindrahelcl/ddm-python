
mistnosti = ["0-obývák", "1-chodba", "2-sklep", "3-trůnní sál","4-jídelna","5-terasa","6-půda","7-kumbál","8-sídlo","9-ložnice","10-chodba","11-tajemna komnata"]
chodby = [[1, 2,4], [0,4,6], [0,11], [1, 2],[1,0,5,7],[4,6,10],[1,5],[4],[10],[10],[9,8,5],[2]]

start = 0
konec = 5

pozice = start
cesty = [[start]]
nalezena_cesta = None

while cesty:
    cesta = cesty.pop(0)
    posledni_mistnost = cesta[-1]

    if konec == posledni_mistnost:
        nalezena_cesta = cesta
        break

    moznosti = []
    for m in chodby[posledni_mistnost]:
        if m not in cesta:
            moznosti.append(m)

    for m in moznosti:
        cesty.append(cesta + [m])

    print(cesty)


if nalezena_cesta is not None:
    print("nalezena cesta: ")
    print(nalezena_cesta)
    for m in nalezena_cesta:
        print(mistnosti[m])




#
# while pozice != konec:
#     moznosti = chodby[pozice]
#
#     for m in moznosti:
#         if m not in navstiveno:
#             # ted tam muzu jit.
#             pozice = m
#             break
#
#     print("jdu do ", mistnosti[pozice])
#









