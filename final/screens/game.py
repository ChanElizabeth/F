import pygame
import sys
from objects import arrow as arw
import mapLoader as ml

def draw(screen, scores):
    font = pygame.font.SysFont(None, 50)
    score_text = font.render("score:"+str(scores), True, (255, 255, 255))
    screen.blit(score_text, (600,35))

def game(Button, Statarrow, gameOver, level):
    if level == "easy":
        map = ml.MapLoader("maps/easy.txt")

        pygame.display.set_caption("Dance Game")
        screen = pygame.display.set_mode((800, 600))


        leftA = Statarrow("images/arrowleft.bmp", 60, 75)
        downA = Statarrow("images/arrowdown.bmp", 225, 75)
        upA = Statarrow("images/arrowup.bmp",425, 75)
        rightA = Statarrow("images/arrowright.bmp",600, 75)

        gameBg = pygame.image.load("images/Gbg.png")
        gameBg = pygame.transform.scale(gameBg, (800, 600))

        pygame.init()

        gameClock = pygame.time.Clock()

        arrow1_group = pygame.sprite.LayeredUpdates()
        arrow2_group = pygame.sprite.LayeredUpdates()
        arrow3_group = pygame.sprite.LayeredUpdates()
        arrow4_group = pygame.sprite.LayeredUpdates()

        timer = 0
        musictimer = 0
        i = 1
        hitted = 0
        missed = 0

        music_play = False

        while True:

            screen.blit(gameBg, (0, 0))
            lefA = screen.blit(leftA.image, (60, 75))
            dowA = screen.blit(downA.image, (225, 75))
            uA = screen.blit(upA.image, (425, 75))
            rigA = screen.blit(rightA.image, (600, 75))

            if not music_play:
                try:
                    pygame.mixer.music.load("sound/BOOMBAYAH.mp3")
                    pygame.mixer.music.play()
                    music_play = True
                except IndexError:
                    pygame.mixer.music.stop()
                    music_play = False

            timer += 0.09
            if timer > 1:
                try:
                    keysattime = map.getKeys(i)
                    #if keysattime[0] == '0':
                    #    arrow0 = arw.Arrow(screen, 0, 0, 0, 150, 100, 8)
                    #    arrow1_group.add(arrow0)
                    if keysattime[0] == '1':
                        arrow1 = arw.Arrow(screen, 1, 60, 475, 150, 100, 8)
                        arrow1_group.add(arrow1)

                    #if keysattime[1] == '0':
                    #    arrow0 = arw.Arrow(screen, 0, 0, 0, 150, 100, 8)
                    #    arrow2_group.add(arrow0)
                    if keysattime[1] == '1':
                        arrow2 = arw.Arrow(screen, 2, 225, 475, 150, 100, 8)
                        arrow2_group.add(arrow2)

                    #if keysattime[2] == '0':
                    #    arrow0 = arw.Arrow(screen, 0, 0, 0, 150, 100, 8)
                    #    arrow3_group.add(arrow0)
                    if keysattime[2] == '1':
                        arrow3 = arw.Arrow(screen,3, 425, 475, 150, 100, 8)
                        arrow3_group.add(arrow3)

                    #if keysattime[3] == '0':
                    #    arrow0 = arw.Arrow(screen, 0, 0, 0, 150, 100, 8)
                    #    arrow4_group.add(arrow0)
                    if keysattime[3] == '1':
                        arrow4 = arw.Arrow(screen, 4, 600, 475, 150, 100, 8)
                        arrow4_group.add(arrow4)
                    i += 1
                    timer = 0
                except IndexError:
                    None

            musictimer += 0.09
            if musictimer > 113:
                pygame.mixer.music.stop()
                gameOver(Button, hitted, missed)

            arrow1_group.update()
            arrow1_group.draw(screen)

            arrow2_group.update()
            arrow2_group.draw(screen)

            arrow3_group.update()
            arrow3_group.draw(screen)

            arrow4_group.update()
            arrow4_group.draw(screen)

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    sys.exit()

                elif ev.type == pygame.KEYDOWN:
                    if (ev.key == pygame.K_LEFT):
                        hit = pygame.sprite.spritecollide(leftA, arrow1_group, dokill = False)
                        if hit:
                            if hit[0].rect.centery < leftA.rect.midbottom[1] and hit[0].rect.y > 10:
                                arrow1_group.remove(hit[0])
                                hitted += 10
                    elif (ev.key == pygame.K_DOWN):
                        hit = pygame.sprite.spritecollide(downA, arrow2_group, dokill=False)
                        if hit:
                            if hit[0].rect.centery < downA.rect.midbottom[1] and hit[0].rect.y > 10:
                                arrow2_group.remove(hit[0])
                                hitted +=10
                    elif (ev.key == pygame.K_UP):
                        hit = pygame.sprite.spritecollide(upA, arrow3_group, dokill=False)
                        if hit:
                            if hit[0].rect.centery < upA.rect.midbottom[1] and hit[0].rect.y > 10:
                                arrow3_group.remove(hit[0])
                                hitted +=10
                    elif (ev.key == pygame.K_RIGHT):
                        hit = pygame.sprite.spritecollide(rightA, arrow4_group, dokill=False)
                        if hit:
                            if hit[0].rect.centery < rightA.rect.midbottom[1] and hit[0].rect.y > 10:
                                arrow4_group.remove(hit[0])
                                hitted +=10

            missed = len(arrow1_group) + len(arrow2_group) + len(arrow3_group) + len(arrow4_group)

            draw(screen, hitted)

            pygame.display.update()

    if level == "medium":
        map = ml.MapLoader("maps/medium.txt")

        pygame.display.set_caption("Dance Game")
        screen = pygame.display.set_mode((800, 600))


        leftA = Statarrow("images/arrowleft.bmp", 60, 75)
        downA = Statarrow("images/arrowdown.bmp", 225, 75)
        upA = Statarrow("images/arrowup.bmp",425, 75)
        rightA = Statarrow("images/arrowright.bmp",600, 75)

        gameBg = pygame.image.load("images/Gbg.png")
        gameBg = pygame.transform.scale(gameBg, (800, 600))

        pygame.init()

        gameClock = pygame.time.Clock()

        arrow1_group = pygame.sprite.LayeredUpdates()
        arrow2_group = pygame.sprite.LayeredUpdates()
        arrow3_group = pygame.sprite.LayeredUpdates()
        arrow4_group = pygame.sprite.LayeredUpdates()

        timer = 0
        musictimer = 0
        i = 1
        hitted = 0
        missed = 0

        music_play = False

        while True:

            screen.blit(gameBg, (0, 0))
            lefA = screen.blit(leftA.image, (60, 75))
            dowA = screen.blit(downA.image, (225, 75))
            uA = screen.blit(upA.image, (425, 75))
            rigA = screen.blit(rightA.image, (600, 75))

            if not music_play:
                try:
                    pygame.mixer.music.load("sound/BOOMBAYAH.mp3")
                    pygame.mixer.music.play()
                    music_play = True
                except IndexError:
                    pygame.mixer.music.stop()
                    music_play = False

            timer += 0.1
            if timer > 1:
                try:
                    keysattime = map.getKeys(i)
                    #if keysattime[0] == '0':
                    #    arrow0 = arw.Arrow(screen, 0, 0, 0, 150, 100, 8)
                    #    arrow1_group.add(arrow0)
                    if keysattime[0] == '1':
                        arrow1 = arw.Arrow(screen, 1, 60, 475, 150, 100, 8)
                        arrow1_group.add(arrow1)

                    #if keysattime[1] == '0':
                    #    arrow0 = arw.Arrow(screen, 0, 0, 0, 150, 100, 8)
                    #    arrow2_group.add(arrow0)
                    if keysattime[1] == '1':
                        arrow2 = arw.Arrow(screen, 2, 225, 475, 150, 100, 8)
                        arrow2_group.add(arrow2)

                    #if keysattime[2] == '0':
                    #    arrow0 = arw.Arrow(screen, 0, 0, 0, 150, 100, 8)
                    #    arrow3_group.add(arrow0)
                    if keysattime[2] == '1':
                        arrow3 = arw.Arrow(screen,3, 425, 475, 150, 100, 8)
                        arrow3_group.add(arrow3)

                    #if keysattime[3] == '0':
                    #    arrow0 = arw.Arrow(screen, 0, 0, 0, 150, 100, 8)
                    #    arrow4_group.add(arrow0)
                    if keysattime[3] == '1':
                        arrow4 = arw.Arrow(screen, 4, 600, 475, 150, 100, 8)
                        arrow4_group.add(arrow4)
                    i += 1
                    timer = 0
                except IndexError:
                    None

            arrow1_group.update()
            arrow1_group.draw(screen)

            arrow2_group.update()
            arrow2_group.draw(screen)

            arrow3_group.update()
            arrow3_group.draw(screen)

            arrow4_group.update()
            arrow4_group.draw(screen)

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    sys.exit()

                elif ev.type == pygame.KEYDOWN:
                    if (ev.key == pygame.K_LEFT):
                        hit = pygame.sprite.spritecollide(leftA, arrow1_group, dokill = False)
                        if hit:
                            if hit[0].rect.centery < leftA.rect.midbottom[1] and hit[0].rect.y > 10:
                                arrow1_group.remove(hit[0])
                                hitted += 10
                    elif (ev.key == pygame.K_DOWN):
                        hit = pygame.sprite.spritecollide(downA, arrow2_group, dokill=False)
                        if hit:
                            if hit[0].rect.centery < downA.rect.midbottom[1] and hit[0].rect.y > 10:
                                arrow2_group.remove(hit[0])
                                hitted +=10
                    elif (ev.key == pygame.K_UP):
                        hit = pygame.sprite.spritecollide(upA, arrow3_group, dokill=False)
                        if hit:
                            if hit[0].rect.centery < upA.rect.midbottom[1] and hit[0].rect.y > 10:
                                arrow3_group.remove(hit[0])
                                hitted +=10
                    elif (ev.key == pygame.K_RIGHT):
                        hit = pygame.sprite.spritecollide(rightA, arrow4_group, dokill=False)
                        if hit:
                            if hit[0].rect.centery < rightA.rect.midbottom[1] and hit[0].rect.y > 10:
                                arrow4_group.remove(hit[0])
                                hitted +=10

            missed = len(arrow1_group) + len(arrow2_group) + len(arrow3_group) + len(arrow4_group)

            draw(screen, hitted)

            musictimer += 0.1
            if musictimer > 115:
                pygame.mixer.music.stop()
                gameOver(Button, hitted, missed)

            pygame.display.update()

    if level == "hard":
        map = ml.MapLoader("maps/hard.txt")

        pygame.display.set_caption("Dance Game")
        screen = pygame.display.set_mode((800, 600))


        leftA = Statarrow("images/arrowleft.bmp", 60, 75)
        downA = Statarrow("images/arrowdown.bmp", 225, 75)
        upA = Statarrow("images/arrowup.bmp",425, 75)
        rightA = Statarrow("images/arrowright.bmp",600, 75)

        gameBg = pygame.image.load("images/Gbg.png")
        gameBg = pygame.transform.scale(gameBg, (800, 600))

        pygame.init()

        gameClock = pygame.time.Clock()

        arrow1_group = pygame.sprite.LayeredUpdates()
        arrow2_group = pygame.sprite.LayeredUpdates()
        arrow3_group = pygame.sprite.LayeredUpdates()
        arrow4_group = pygame.sprite.LayeredUpdates()

        timer = 0
        musictimer = 0
        i = 1
        hitted = 0
        missed = 0

        music_play = False

        while True:

            screen.blit(gameBg, (0, 0))
            lefA = screen.blit(leftA.image, (60, 75))
            dowA = screen.blit(downA.image, (225, 75))
            uA = screen.blit(upA.image, (425, 75))
            rigA = screen.blit(rightA.image, (600, 75))

            if not music_play:
                try:
                    pygame.mixer.music.load("sound/BOOMBAYAH.mp3")
                    pygame.mixer.music.play()
                    music_play = True
                except IndexError:
                    pygame.mixer.music.stop()
                    music_play = False

            timer += 0.12
            if timer > 1:
                try:
                    keysattime = map.getKeys(i)
                    #if keysattime[0] == '0':
                    #    arrow0 = arw.Arrow(screen, 0, 0, 0, 150, 100, 8)
                    #    arrow1_group.add(arrow0)
                    if keysattime[0] == '1':
                        arrow1 = arw.Arrow(screen, 1, 60, 475, 150, 100, 8)
                        arrow1_group.add(arrow1)

                    #if keysattime[1] == '0':
                    #    arrow0 = arw.Arrow(screen, 0, 0, 0, 150, 100, 8)
                    #    arrow2_group.add(arrow0)
                    if keysattime[1] == '1':
                        arrow2 = arw.Arrow(screen, 2, 225, 475, 150, 100, 8)
                        arrow2_group.add(arrow2)

                    #if keysattime[2] == '0':
                    #    arrow0 = arw.Arrow(screen, 0, 0, 0, 150, 100, 8)
                    #    arrow3_group.add(arrow0)
                    if keysattime[2] == '1':
                        arrow3 = arw.Arrow(screen,3, 425, 475, 150, 100, 8)
                        arrow3_group.add(arrow3)

                    #if keysattime[3] == '0':
                    #    arrow0 = arw.Arrow(screen, 0, 0, 0, 150, 100, 8)
                    #    arrow4_group.add(arrow0)
                    if keysattime[3] == '1':
                        arrow4 = arw.Arrow(screen, 4, 600, 475, 150, 100, 8)
                        arrow4_group.add(arrow4)
                    i += 1
                    timer = 0
                except IndexError:
                    None

            arrow1_group.update()
            arrow1_group.draw(screen)

            arrow2_group.update()
            arrow2_group.draw(screen)

            arrow3_group.update()
            arrow3_group.draw(screen)

            arrow4_group.update()
            arrow4_group.draw(screen)

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    sys.exit()

                elif ev.type == pygame.KEYDOWN:
                    if (ev.key == pygame.K_LEFT):
                        hit = pygame.sprite.spritecollide(leftA, arrow1_group, dokill = False)
                        if hit:
                            if hit[0].rect.centery < leftA.rect.midbottom[1] and hit[0].rect.y > 10:
                                arrow1_group.remove(hit[0])
                                hitted += 10
                    elif (ev.key == pygame.K_DOWN):
                        hit = pygame.sprite.spritecollide(downA, arrow2_group, dokill=False)
                        if hit:
                            if hit[0].rect.centery < downA.rect.midbottom[1] and hit[0].rect.y > 10:
                                arrow2_group.remove(hit[0])
                                hitted +=10
                    elif (ev.key == pygame.K_UP):
                        hit = pygame.sprite.spritecollide(upA, arrow3_group, dokill=False)
                        if hit:
                            if hit[0].rect.centery < upA.rect.midbottom[1] and hit[0].rect.y > 10:
                                arrow3_group.remove(hit[0])
                                hitted +=10
                    elif (ev.key == pygame.K_RIGHT):
                        hit = pygame.sprite.spritecollide(rightA, arrow4_group, dokill=False)
                        if hit:
                            if hit[0].rect.centery < rightA.rect.midbottom[1] and hit[0].rect.y > 10:
                                arrow4_group.remove(hit[0])
                                hitted +=10

            missed = len(arrow1_group) + len(arrow2_group) + len(arrow3_group) + len(arrow4_group)

            draw(screen)

            musictimer += 0.12
            if musictimer > 118:
                pygame.mixer.music.stop()
                gameOver(Button, hitted, missed)

            pygame.display.update()

