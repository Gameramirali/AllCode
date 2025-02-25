import pygame
from constants import *

class Game:
    def __init__(self):
        self.bg_image=pygame.image.load('asstes/background.png')
        self.bg_image=pygame.transform.scale(self.bg_image, (WIDTH,HEIGHT))
        self.bg_image_rect=self.bg_image.get_rect(topleft=(0,0))
    def draw(self,screen):
        screen.blit(self.bg_image,self.bg_image_rect)