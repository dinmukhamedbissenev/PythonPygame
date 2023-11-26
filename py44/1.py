import pygame
import random

FPS = 60
screen = pygame.display.set_mode((1280, 720))
running = True
clock = pygame.time.Clock()
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("undertale-removebg-preview.png")
        self.image = pygame.transform.scale( self.image, (100, 100))
        self.rect = self.image.get_rect()
    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.rect.y -= 5
        if keystate[pygame.K_s]:
            self.rect.y += 5
        if keystate[pygame.K_a]:
            self.rect.x -= 5
        if keystate[pygame.K_d]:
            self.rect.x += 5
        
        if self.rect.bottom < 100:
            self.rect.y = 0
        if self.rect.top > 620:
            self.rect.y = 620
        if self.rect.left < 0:
            self.rect.x = 0
        if self.rect.right > 1280:
            self.rect.x = 1180
    
    def teleport(self,Bxod, Bixod):
        if (Bxod.x <= self.rect.x <= Bxod.x + 100 ) and (Bxod.y <= self.rect.y <= Bxod.y + 100):
            self.rect.center = (Bixod.x, Bixod.y)
        elif (Bxod.x <= self.rect.x + 100 <= Bxod.x + 100 ) and (Bxod.y <= self.rect.y + 100 <= Bxod.y + 100):
            self.rect.center = (Bixod.x, Bixod.y)
    
    

class Block():
    def __init__(self, width, height, x, y, colour):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.surf = pygame.surface.Surface((self.height, self.width))
        self.surf.fill(colour)
    def draw(self):
        pygame.surface.Surface.blit(screen, self.surf, (self.x, self.y))

class Stone(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("stone.png")
        self.image = pygame.transform.scale(self.image, (150,150))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, 1280), random.randint(0, 720))
    

b = Block(100,100, 500,500, 'red') # Bxod
c = Block(100,100, 1000,500, 'blue')# Bixod
p = Player()
s = Stone()
stoneGroup = pygame.sprite.Group()
def spawn():
    for i in range(10):
        s = Stone()
        stoneGroup.add(s)

spawn()


spriteGroup = pygame.sprite.Group()
spriteGroup.add(p)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('white')
    spriteGroup.draw(screen)
    stoneGroup.draw(screen)
    spriteGroup.update()
    if pygame.sprite.groupcollide(spriteGroup, stoneGroup, True, False):
        running = False
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()