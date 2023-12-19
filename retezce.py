vstup = input("Zadej vstup: ")

vstup_pozpatku = ""

for i in range(len(vstup)):
    # i = 0, 1, 2, .... len(vstup) - 1
    pozice = len(vstup) - 1 - i
    pismenko = vstup[pozice]
    vstup_pozpatku = vstup_pozpatku + pismenko

if vstup == vstup_pozpatku:
    print("ano, je to palindrom")
else:
    print("neni to palindrom")

# print(vstup[0:len(vstup) // 2].upper())
# print(vstup[len(vstup) // 2:len(vstup)].lower())




#druhy_vstup = int(input("Zadej druhy vstup (číslo): "))
#treti_vstup = int(input("Zadej třetí vstup (číslo): "))

# if len(vstup) >= druhy_vstup and druhy_vstup > 0:
#     print(vstup[druhy_vstup - 1])




#
# print(prvni_vstup * druhy_vstup)
#
# # if str(prvni_vstup).isalpha():
# #     print("ano, jsou tam jenom písmenka")
#
# if str(prvni_vstup).isdigit():
#     print("jsou tam jenom čísla")

