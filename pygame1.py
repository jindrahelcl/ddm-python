import sys
import pygame
import barvy

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60

bg = pygame.image.load("obrazky/sachy/chessboard2.png")
bg_w = bg.get_width()
bg_h = bg.get_height()


nahoru = pygame.K_w
dolu = pygame.K_s
vpravo = pygame.K_d
vlevo = pygame.K_a


pozice = [50, 50]
rychlost = [0, 0, 0, 0]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.KEYDOWN:
            # zmackl klavesu
            if event.key == nahoru:
                rychlost[0] = 5
            if event.key == dolu:
                rychlost[1] = 5
            if event.key == vlevo:
                rychlost[2] = 5
            if event.key == vpravo:
                rychlost[3] = 5


        if event.type == pygame.KEYUP:
            # pustil klavesu
            if event.key == nahoru:
                rychlost[0] = 0
            if event.key == dolu:
                rychlost[1] = 0
            if event.key == vlevo:
                rychlost[2] = 0
            if event.key == vpravo:
                rychlost[3] = 0

    screen.fill(barvy.WHITE)
    screen.blit(bg, (0, 0))
    screen.blit(bg, (bg_w, 0))
    screen.blit(bg, (bg_w * 2, 0))

    # gravitace
    rychlost[1] += 0.5

    pozice[1] += rychlost[1] - rychlost[0]
    pozice[0] += rychlost[3] - rychlost[2]

    if pozice[0] < 0:
        pozice[0] = 0
    if pozice[1] < 0:
        pozice[1] = 0
    if pozice[0] > width - 60:
        pozice[0] = width - 60
    if pozice[1] > height - 30:
        pozice[1] = height - 30
        rychlost[1] = 0

    obdelnik = pygame.Rect(pozice[0], pozice[1], 60, 30)

    pygame.draw.rect(screen, barvy.RED, obdelnik)

    pygame.display.update()
    clock.tick(fps)







