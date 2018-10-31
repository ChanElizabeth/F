import pygame
import sys

def mainMenu(Button, Statarrow, subMenu, game, gameOver):
    pygame.display.set_caption("Dance Game")
    screen = pygame.display.set_mode((800, 600))

    startBtn = Button("images/play game.bmp")

    menuBg = pygame.image.load("images/dancebg.jpg")
    menuBg = pygame.transform.scale(menuBg, (800, 600))

    pygame.init()

    while True:
        startRect = pygame.draw.rect(screen, (0, 0, 0), (325, 450, 475, 550))
        screen.blit(menuBg, (0, 0))
        screen.blit(startBtn.button, (325, 450))

        ev = pygame.event.wait()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if startRect.collidepoint(pygame.mouse.get_pos()):
                subMenu(Button, Statarrow, game, gameOver)
        if ev.type == pygame.QUIT:
            sys.exit()

        pygame.display.update()
