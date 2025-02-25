import pygame
from pygame.sprite import Sprite

from constants import *

class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.left_image=pygame.image.load('asstes/dog.png')
        self.left_image_rect=self.left_image.get_rect(center=(WIDTH/2,HEIGHT-35))
        self.right_image=pygame.transform.flip(self.left_image,True,False)

    def draw(self,screen):
        screen.blit(self.left_image,self.left_image_rect)

    def move(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_w]and :
            self.left_image_rect.y