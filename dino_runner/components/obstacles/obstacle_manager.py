from asyncio import constants
import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus_Small, Cactus_Large
from dino_runner.components.obstacles.bird import Bird_High, Bird_Low
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.leveldificult = 0
        self.birdrandom = 0

    def update(self, game):
        if len(self.obstacles) == 0:
            if self.leveldificult <= 3:
                self.obstacles.append(Cactus_Small(SMALL_CACTUS))
                self.leveldificult += 1
                                
            elif self.leveldificult >= 4:
                self.leveldificult = random.randint(5, 7)
                if self.leveldificult == 5:
                    self.obstacles.append(Cactus_Large(LARGE_CACTUS))            
                    
                elif self.leveldificult == 6:
                    self.obstacles.append(Cactus_Small(SMALL_CACTUS))
                
                elif self.leveldificult == 7:
                    self.birdrandom = random.randint(1, 2)
                    
                    if self.birdrandom == 1:
                        self.obstacles.append(Bird_Low(BIRD))
                    elif self.birdrandom == 2:
                        self.obstacles.append(Bird_High(BIRD))
                    
          
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = [] 
