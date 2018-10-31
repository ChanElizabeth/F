from pygame import *
from pygame.sprite import *

class Button(Sprite):
    def __init__(self, image):
        Sprite.__init__(self)
        self.button = pygame.image.load(image)
        self.button = pygame.transform.scale(self.button, (150, 100))
