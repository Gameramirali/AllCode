from pygame.sprite import Sprite
import pygame

class EnemyBullet(Sprite):
    def __init__(self, x,y , EnemyBullet):
        super().__init__()
        self.image = pygame.image.load("assets/red_laser.png")
        self.rect = self.image.get_rect(centerx = x, bottom =y)
        EnemyBullet.add(self)

    def update(self):
        self.rect.y += 5
        if self.rect.bottom <= 0:
            self.kill()