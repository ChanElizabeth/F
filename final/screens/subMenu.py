import pygame
import sys

def subMenu(Button, Statarrow, game, gameOver):
    print("placeholder")
    pygame.display.set_caption("Game Level")
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.SysFont("Arial", 50)
    text = font.render("Choose the game level", True, (255, 255, 255))

    easyBtn = Button("images/easybutton.png")
    medBtn = Button("images/medbutton.png")
    hardBtn = Button("images/hardbutton.png")

    levelBg = pygame.image.load("images/levelbg.jpg")
    levelBg = pygame.transform.scale(levelBg, (800, 600))

    pygame.init()

    while True:
        easyRect = pygame.draw.rect(screen, (0, 0, 0), (60,475, 210, 575))
        medRect = pygame.draw.rect(screen, (0, 0, 0), (325, 475, 475, 575))
        hardRect = pygame.draw.rect(screen, (0, 0, 0), (600, 475, 750, 575))
        screen.blit(levelBg, (0, 0))
        screen.blit(text, (250, 50))
        screen.blit(easyBtn.button, (60, 475))
        screen.blit(medBtn.button, (325, 475))
        screen.blit(hardBtn.button, (600, 475))

        ev = pygame.event.wait()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if easyRect.collidepoint(pygame.mouse.get_pos()):
                game(Button, Statarrow, gameOver, "easy") #call sub menu
            if medRect.collidepoint(pygame.mouse.get_pos()):
                game(Button, Statarrow, gameOver, "medium") #call sub menu
            if hardRect.collidepoint(pygame.mouse.get_pos()):
                game(Button, Statarrow, gameOver, "hard") #call sub menu
        if ev.type == pygame.QUIT:
            sys.exit()

        pygame.display.update()
