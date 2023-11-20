import random
import math


def zvol_cislo(horni_limit):
    return random.randint(1, horni_limit)


def ziskej_tip(horni_limit):
    n = 0
    while True:
        t = input("Hádej: ")

        try:
            n = int(t)
            if n < 1 or n > horni_limit:
                print(f"Musí to být mezi 1 a {horni_limit} včetně!")
                continue
            break
        except ValueError:
            print("Musíš zadat celé číslo!")
    return n


def main():
    horni_limit = 1000
    cislo = zvol_cislo(horni_limit)
    print(f"Vítej u hry zvol číslo. Myslím si číslo mezi 1 a {horni_limit}.")

    max_pokusu = math.floor(math.log2(horni_limit)) + 1
    print(f"Ty máš {max_pokusu} pokusů, tak se snaž!")

    tip = -1
    pokusy = 0

    while tip != cislo and pokusy < max_pokusu:
        tip = ziskej_tip(horni_limit)
        if tip < cislo:
            print("Moje číslo je větší.")
        elif tip > cislo:
            print("Moje číslo je menší.")
        pokusy += 1

    if tip == cislo:
        print(f"Gratuluju, {cislo} je správné číslo!")
    else:
        print(f"Bohužel... Moje číslo bylo {cislo}. Zkus to znova!")


if __name__ == "__main__":
    main()
