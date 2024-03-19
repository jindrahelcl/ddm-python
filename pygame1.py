import sys
import pygame
import barvy

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
fps = 60

nahoru = pygame.K_w
dolu = pygame.K_s
vpravo = pygame.K_d
vlevo = pygame.K_a


pozice = [50, 50]
rychlost = [0, 0]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # zmackl klavesu
            if event.key == nahoru:
                rychlost[1] = -5
            if event.key == dolu:
                rychlost[1] = 5
            if event.key == vlevo:
                rychlost[0] = -5
            if event.key == vpravo:
                rychlost[0] = 5


        if event.type == pygame.KEYUP:
            # pustil klavesu
            if event.key == nahoru:
                rychlost[1] = 0
            if event.key == dolu:
                rychlost[1] = 0
            if event.key == vlevo:
                rychlost[0] = 0
            if event.key == vpravo:
                rychlost[0] = 0


    screen.fill(barvy.WHITE)

    pozice[0] += rychlost[0]
    pozice[1] += rychlost[1]

    pygame.draw.rect(
        screen, barvy.RED,
        (pozice[0], pozice[1], 60, 30))

    pygame.display.update()
    clock.tick(fps)







