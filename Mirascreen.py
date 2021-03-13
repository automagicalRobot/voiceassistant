import pygame
x=1960
y=1080
class Mira(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("strawberry2.png")
        self.image = pygame.transform.scale(self.image, (350, 500))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x / 2, self.y / 2)

class Miratalking(pygame.sprite.Sprite):
     def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("strawberrypixel.png")
        self.image = pygame.transform.scale(self.image, (500, 500))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x / 2, self.y / 2)

class Diamond(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("goldleafs.png")
        self.image = pygame.transform.scale(self.image, (1550, 850))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x / 2, self.y / 2)
class Frame(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("circle.png")
        self.image = pygame.transform.scale(self.image, (850, 850))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x / 2, self.y / 2)

def miratalk():
    sprites.kill(Mira())
    sprites.add(Miratalking(x, y))
    Miratalking = pygame.transform.scale(Miratalking, (1550, 850))
    pygame.display.update()
    Miratalking = pygame.transform.scale(Miratalking, (1565, 865))
    pygame.display.update()
    sprites.add(Mira(x,y))
