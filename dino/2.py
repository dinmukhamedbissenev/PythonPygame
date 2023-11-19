from typing import Any
import pygame

RES = (1280, 720)
WHITE = (255, 255, 255)
FPS = 30

pygame.init()
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
running = True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dino-removebg-preview.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        self.speed = 10

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.rect.y -= self.speed
        if keystate[pygame.K_s]:
            self.rect.y += self.speed
        if keystate[pygame.K_a]:
            self.rect.x -= self.speed
        if keystate[pygame.K_d]:
            self.rect.x += self.speed

class Cactus():
    pass
cactus_sprites = pygame.sprite.Group()

def spawn():
    for i in range(20):
        c = Cactus()
        cactus_sprites.add(c)
    
    

p = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(p)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)

    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()