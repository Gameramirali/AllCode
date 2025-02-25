from constants import *
from pygame.locals import *
from game import Game
from player import Player


game=Game()
player=Player()

running=True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    game.draw(SCREEN)
    player.draw(SCREEN)
    pygame.display.update()
    CLOCK.tick(FPS)