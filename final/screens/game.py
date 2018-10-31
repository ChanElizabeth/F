import pygame
import sys
from objects import arrow as arw
import mapLoader as ml
#from danceBg import *

def game(Button, Statarrow, gameOver, level):
    if level == "easy":
        map = ml.MapLoader("maps/easy.txt")

        pygame.display.set_caption("Dance Game")
        screen = pygame.display.set_mode((800, 600))


        leftA = Statarrow("images/arrowleft.bmp")
        downA = Statarrow("images/arrowdown.bmp")
        upA = Statarrow("images/arrowup.bmp")
        rightA = Statarrow("images/arrowright.bmp")

        gameBg = pygame.image.load("images/bg.gif")
        gameBg = pygame.transform.scale(gameBg, (800, 600))
        #gameBg = DanceBg("images/bg.gif")

        #initialize the coordinate of the background
        #x = 0
        #y = 0
        # x1 = gameBg.width
        # y1 = 0
        pygame.init()

        gameClock = pygame.time.Clock()

        arrow1 = arw.Arrow(screen, 1, 60, 475, 150, 100, 8)
        arrow2 = arw.Arrow(screen, 2, 225, 475, 150, 100, 8)
        arrow3 = arw.Arrow(screen, 3, 425, 475, 150, 100, 8)
        arrow4 = arw.Arrow(screen, 4, 600, 475, 150, 100, 8)

        arrow1_group = pygame.sprite.LayerUpdates()
        arrow2_group = pygame.sprite.LayerUpdates()
        arrow3_group = pygame.sprite.LayerUpdates()
        arrow4_group = pygame.sprite.LayerUpdates()

        #tickRate = 40
        #arrow_group = pygame.time.get_ticks()
        time = 0
        while True:
            #game phase goes faster after every frame
            #gameClock.tick(tickRate)
            #ickRate += 0.01
             #change the coordinate of the bg_Image, and draws the background
            # x -= 5
            # x1 -= 5
            # gameBg.draw(screen, x, y)
            # gameBg.draw(screen, x1, y1)
            # if x < -gameBg.width:
            #     x = 0
            # if x1 < 0:
            #     x1 = gameBg.width
            time+= 0.05
            laRect = pygame.draw.rect(screen, (0, 0, 0), (60,75, 210, 175))
            daRect = pygame.draw.rect(screen, (0, 0, 0), (225, 75, 375, 175))
            uaRect = pygame.draw.rect(screen, (0, 0, 0), (425, 75, 575, 175))
            raRect = pygame.draw.rect(screen, (0, 0, 0), (600, 75, 750, 175))
            screen.blit(gameBg, (0, 0))
            lefA = screen.blit(leftA.statarrow, (60, 75))
            dowA = screen.blit(downA.statarrow, (225, 75))
            uA = screen.blit(upA.statarrow, (425, 75))
            rigA = screen.blit(rightA.statarrow, (600, 75))

            for i in map.getSecs():
                keysattime = map.getKeys(i)
                #k = pygame.key.get_pressed()
                if keysattime[0]:
                    arrow1_group.LayeredUpdates.add(arrow1)
                if keysattime[1]:
                    arrow2_group.LayeredUpdates.add(arrow2)

                if keysattime[2]:
                    arrow3_group.LayeredUpdates.add(arrow3)

                if keysattime[3]:
                    arrow4_group.LayeredUpdates.add(arrow4)

            print(arrow1_group)

            for arrow1 in arrow1_group:
                if arrow1 == "1":
                #arrow1_group.draw(screen)
                    arrow1_group.LayerUpdates.draw(screen)
            for arrow2 in arrow2_group:
                if arrow2 == "1":
                #arrow2_group.draw(screen)
                    arrow2_group.LayerUpdates.draw(screen)

            for arrow3 in arrow3_group:
                if arrow3 == "1":
                #arrow3_group.draw(screen)
                    arrow3_group.LayerUpdates.draw(screen)

            for arrow4 in arrow4_group:
                if arrow4 == "1":
                #arrow4_group.draw(screen)
                    arrow4_group.LayerUpdates.draw(screen)

            ev = pygame.event.wait()

            if ev.type == pygame.QUIT:
                sys.exit()

            pygame.display.update()
            gameClock.tick(50)
'''


    if level == "medium":
        print("f")
    if level == "hard":
        print("phello")
'''
