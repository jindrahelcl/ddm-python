
class Strela:
    def __init__(self, pozice, smer, rychlost=20):
        self.pozice = pozice
        self.smer = smer
        self.rychlost = rychlost

    def nakresli(self, screen):
        screen.blit(screen, self.pozice)

    def posun(self):
        self.pozice[0] += self.rychlost