import pygame
from config import *
from player import Player
from game import Game


pygame.init()


display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

player_group = pygame.sprite.Group()
my_player = Player()

player_group.add(my_player)

monster_group = pygame.sprite.Group()


game = Game(my_player, monster_group)
game.start_new_round()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.espect() 
    display_surface.fill((0, 0, 0))
    player_group.draw(display_surface)
    my_player.move()
    monster_group.draw(display_surface)
    monster_group.update()
    game.draw(display_surface)
    game.update()
    game.Gameover(display_surface,running)
    pygame.display.update()
    clock.tick(FPS)