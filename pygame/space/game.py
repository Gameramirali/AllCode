import pygame
from enemy import Enemy
from constants import *
from player import Player
from time import sleep

class Game:
    def __init__(self, player, enemy_group,player_bullet_group):
        self.score = 0
        self.round_number = 0
        self.player = player
        self.enemy_group = enemy_group
        self.font = pygame.font.Font("assets/Facon.ttf", 25)
        self.new_round_sound = pygame.mixer.Sound("assets/new_round.wav")
        self.player_bullet_group=player_bullet_group

    def draw(self, screen):
        score_text = self.font.render(f'Score:{self.score}', True, (255, 0, 0))
        score_rect=score_text.get_rect()
        score_rect.topleft = (0, 0)

        round_number_text=self.font.render(f'round_number:{self.round_number}',True,(255, 0, 0))
        round_number_rect=round_number_text.get_rect()
        round_number_rect.topleft=(0, 50)

        lives_text = self.font.render(f'lives:{self.player.lives}', True, (255, 0, 0))
        lives_rect = lives_text.get_rect()
        lives_rect.topleft = (0, 25)

        screen.blit(score_text,score_rect)
        screen.blit(round_number_text,round_number_rect)
        screen.blit(lives_text,lives_rect)

    def start_new_level(self):
        self.round_number += 1
        for i in range(7):
            for j in range(15):

                enemy = Enemy(j*64, i*64 + 100)
                self.enemy_group.add(enemy)

    def check_collisions(self):
        remained_sprite_enemy=self.enemy_group.sprites()
        if pygame.sprite.groupcollide(self.player_bullet_group,self.enemy_group,True,True):
            self.score+=1
        if len(remained_sprite_enemy)==0:
            self.start_new_level()
        
    def update(self):
        self.check_if_on_edge()
        self.check_collisions()

    def check_if_on_edge(self):
        on_edge = False
        for enemy in self.enemy_group:
            if enemy.rect.left < 0 or enemy.rect.right > SCREEN_WIDTH:
                on_edge = True
                break

        if on_edge:
            death = False
            for enemy in self.enemy_group:
                enemy.direction *= -1
                enemy.rect.y += self.round_number * 5
                if enemy.rect.bottom >= SCREEN_HEIGHT - 100:
                    death = True
                    break
            if death:
                self.reset()

    def reset(self):
        self.score=0
        self.round_number=0
        self.player.lives-=1
        self.enemy_group.empty()
    
    def gameover(self,screen):
        gameover_text=self.font.render('Gameover',True,(255, 0, 0))
        gameover_rect=gameover_text.get_rect()
        gameover_rect.topleft=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        screen.fill((0,0,0))
        screen.blit(gameover_text,gameover_rect)
        pygame.display.update()
        sleep(5)