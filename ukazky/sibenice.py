import random


def nacti_slovnik(slovnik="slovnik.txt"):
    with open(slovnik, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def rekni_si_o_pismenko(uz_bylo):
    tip = input("Hádej písmenko: ")

    while len(tip) != 1 or tip in uz_bylo:
        if tip in uz_bylo:
            tip = input("To už bylo, hádej znovu: ")
        elif len(tip) > 1:
            tip = input("To je moc dlouhý! Hádej znovu, jen jedno písmenko: ")
        elif len(tip) == 0:
            tip = input("Napiš písmenko a zmáčkni enter: ")
    return tip


def main():
    slova = nacti_slovnik()
    index = random.randint(0, len(slova) - 1)
    tajenka = slova[index]
    # print(f"Vybral jsem slovo: {tajenka}")

    uhodnuto = False
    zkusil = {}

    spatnych_pokusu = 0
    max_spatnych_pokusu = 10
    vyhra = True

    while True:
        uhodnuto = True
        for t in tajenka:
            if t in zkusil:
                print(t, end=" ")
            else:
                print("_", end=" ")
                uhodnuto = False
        print()
        if uhodnuto:
            break

        tip = rekni_si_o_pismenko(zkusil)
        zkusil[tip] = True

        if tip in tajenka:
            print("Výborně!")
        else:
            spatnych_pokusu += 1
            if spatnych_pokusu < max_spatnych_pokusu:
                print("Samá voda! Zbývá špatných pokusů:",
                      max_spatnych_pokusu - spatnych_pokusu)
            else:
                print("Špatně! Končíš na šibenici!!!")
                vyhra = False
                break

    if vyhra:
        print(f"Gratuluji! Získáváš medaili za uhodnuté heslo {tajenka}")
    else:
        print(f"Heslo bylo: {tajenka}")


if __name__ == "__main__":
    main()
