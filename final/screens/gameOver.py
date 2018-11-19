import pygame
import sys

def gameOver(Button, hitted, missed):
    pygame.display.set_caption("Dance Game")
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.SysFont(None, 50)
    text = font.render("Groove Over. Restart?", True, (255, 255, 255))
    score_text = font.render("scores:"+str(hitted), True, (255, 255, 255))
    miss_text = font.render("miss:"+str(missed), True, (255, 255, 255))

    restartBtn = Button("images/restartbutton.bmp")
    quitBtn = Button("images/quitbutton.png")

    gameoverbg = pygame.image.load("images/gameoverbg.bmp")
    gameoverbg = pygame.transform.scale(gameoverbg, (800, 600))

    pygame.init()

    while True:
        restartRect = pygame.draw.rect(screen, (0, 0, 0), (200,300, 350, 400))
        quitRect = pygame.draw.rect(screen, (0, 0, 0), (450,300, 600, 400))
        screen.blit(gameoverbg, (0, 0))
        screen.blit(text, (200, 75))
        screen.blit(restartBtn.button, (200, 200))
        screen.blit(quitBtn.button, (450, 200))
        screen.blit(score_text, (300, 450))
        screen.blit(miss_text, (300, 500))

        ev = pygame.event.wait()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if restartRect.collidepoint(pygame.mouse.get_pos()):
                main(Button, Statarrow, mainMenu, subMenu, game, gameOver)
            if quitRect.collidepoint(pygame.mouse.get_pos()):
                sys.exit()

        if ev.type == pygame.QUIT:
            sys.exit()

        pygame.display.update()
