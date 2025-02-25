import pygame
import pygame.locals

pygame.init()
WIDTH=600
HEIGHT=600

main_surface=pygame.display.set_mode((WIDTH,HEIGHT))


running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()