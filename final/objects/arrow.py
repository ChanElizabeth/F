from pygame import *
from pygame.sprite import *

class Arrow(Sprite):
    def __init__(self, screen, type, x,y, width, height, speed):
        Sprite.__init__(self)
        self.screen = screen
        self.type = type
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        if self.type == 0:
            self.image = pygame.Surface((10, 10))
            self.rect = self.image.get_rect()
        elif self.type == 1:
            self.image = pygame.image.load("images/Leftarrow.bmp")
            self.rect = pygame.draw.rect(screen, (0, 0, 0), (60,475, 210, 575))
        elif self.type == 2:
            self.image = pygame.image.load("images/Downarrow.bmp")
            self.rect = pygame.draw.rect(screen, (0, 0, 0), (225,475, 375, 575))
        elif self.type == 3:
            self.image = pygame.image.load("images/Uparrow.bmp")
            self.rect = pygame.draw.rect(screen, (0, 0, 0), (425,475, 575, 575))
        elif self.type == 4:
            self.image = pygame.image.load("images/Rightarrow.bmp")
            self.rect = pygame.draw.rect(screen, (0, 0, 0), (600,475, 750, 575))
            #self.rect.bottom = startY

    def update(self):
        self.y -= self.speed
        # Update the rect position.
        self.rect.y = self.y

'''
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def collision(self):
        k = pygame.key.get_pressed()
        if k[pygame.K_UP]:
            del self.image
'''
