from pygame import *
from pygame.sprite import *

class Statarrow(Sprite):
    def __init__(self, image):
        Sprite.__init__(self)
        self.statarrow = pygame.image.load(image)
        self.statarrow = pygame.transform.scale(self.statarrow, (150, 100))
