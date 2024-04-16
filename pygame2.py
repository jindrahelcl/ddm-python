import pygame
import sys

# inicializace

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

hrac = pygame.Surface((40, 40))
hrac.fill((200, 0, 0))

cil = pygame.Surface((60, 60))
cil.fill((0, 0, 200))


pozice = [10, 100]
pohyb = [False, False, False, False]

strela = pygame.Surface((10, 10))
strela.fill((100, 100, 200))

vystrelene_strely = []

def vystrel(pozice_hrace):
    pozice_strely = [pozice_hrace[0] + 40, pozice_hrace[1] + 20]
    vystrelene_strely.append(pozice_strely)


# beh - nekonecny cyklus
while True:
    screen.fill((255, 255, 255))

    pozice[0] += 2 * (pohyb[1] - pohyb[0])
    pozice[1] += 2 * (pohyb[3] - pohyb[2])

    for s in vystrelene_strely:
        s[0] += 20

        if pygame.Rect(s[0], s[1], 10, 10).colliderect((600, 300, cil.get_width(), cil.get_height())):
            vystrelene_strely.remove(s)
            cil.fill((0, 255, 0))

    screen.blit(hrac, pozice)
    screen.blit(cil, (600, 300))

    # kontrola vstupů
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pohyb[0] = True
            if event.key == pygame.K_RIGHT:
                pohyb[1] = True
            if event.key == pygame.K_UP:
                pohyb[2] = True
            if event.key == pygame.K_DOWN:
                pohyb[3] = True
            if event.key == pygame.K_SPACE:
                vystrel(pozice)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pohyb[0] = False
            if event.key == pygame.K_RIGHT:
                pohyb[1] = False
            if event.key == pygame.K_UP:
                pohyb[2] = False
            if event.key == pygame.K_DOWN:
                pohyb[3] = False

    # vykresleni strel
    for pozice_strely in vystrelene_strely.copy():
        print(pozice_strely)
        screen.blit(strela, pozice_strely)
        if pozice_strely[0] > 900:
            vystrelene_strely.remove(pozice_strely)

    pygame.display.update()
    clock.tick(60)




