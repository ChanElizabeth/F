from pygame import *

class DanceBg:
    #initializes baxkground setting
    def __init__(self, background):
        self.background = image.load(background)
        self.background = transform.scale(self.background, (800, 600))
        self.backgroundSize = self.background.get_size()
        self.backgroundRect = self.background.get_rect()
        self.width, self.height = self.backgroundSize

    #draws the background
    def draw(self, screen, x, y):
        screen.blit(self.background, (x, y))
