from inputimeout import inputimeout, TimeoutOccurred
import random

for pokus in range(10):
    s1 = random.randint(1, 10)
    s2 = random.randint(1, 10)

    try:
        vstup = inputimeout(prompt=f"kolik je {s1} + {s2}?", timeout=5)
    except TimeoutOccurred:
        print("nestihnul")
        break


    if vstup == s1 + s2:
        print("ok")
    else:
        print("chyba!!!")
        break

