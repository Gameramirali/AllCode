import pygame
from random import choice
from pygame.locals import *
pygame.init()
WINDOW_WIDTH = 967
WINDOW_HEIGHT = 655


main_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Clown")

clown_image = pygame.image.load("catch_the_clown\\assets\images\\clown.png")
pygame.display.set_icon(clown_image)


background_image = pygame.image.load(
    "catch_the_clown\\assets\images\\background.png")
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)


font = pygame.font.Font(
    "catch_the_clown\\assets\\fonts\Franxurter.ttf", 64)
title_text = font.render("MyGame", True, (1, 175, 209))
title_rect = title_text.get_rect()
title_rect.topleft = (0, 0)


score = 0
lives = 3

score_text = font.render(f"Score:{score}", True, (248, 231, 28))
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH, 0)

lives_text = font.render(f"Lives:{lives}", True, (248, 231, 28))
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH, 60)

gameover_text = font.render(f"game over for contnue press enter", True, (248, 231, 28))
gameover_rect= gameover_text.get_rect()
gameover_rect.topright = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2)

player = clown_image
player_rect = player.get_rect()
player_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

player_velocity = 5
dx = choice((-1, 1))
dy = choice((-1, 1))


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                score+=1
                # print(score)
                
            else:
                lives-=1
                # print(lives)
    player_rect.x += dx * player_velocity
    player_rect.y += dy * player_velocity

    if player_rect.top <= 0 or player_rect.bottom >= WINDOW_HEIGHT:
        dy *= -1

    if player_rect.left <= 0 or player_rect.right >= WINDOW_WIDTH:
        dx *= -1
    score_text = font.render(f"Score:{score}", True, (248, 231, 28))
    lives_text = font.render(f"Lives:{lives}", True, (248, 231, 28))
    main_surface.blit(background_image, background_rect)
    main_surface.blit(title_text, title_rect)
    main_surface.blit(score_text, score_rect)
    main_surface.blit(lives_text, lives_rect)
    main_surface.blit(player, player_rect)
    if lives==0:
        main_surface.blit(gameover_text,gameover_rect)
        score=0
        lives=3
        pygame.display.update()
        is_paused=True
        while is_paused:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        is_paused=False
                if event.type==pygame.QUIT:
                    is_paused=False
                    running=False
    pygame.display.update()


pygame.quit()