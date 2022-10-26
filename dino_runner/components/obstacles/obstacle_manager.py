from asyncio import constants
import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus_Small, Cactus_Large
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.leveldificult = 0

    def update(self, game):
        if len(self.obstacles) == 0:
            if self.leveldificult <= 3:
                self.obstacles.append(Cactus_Small(SMALL_CACTUS))
                self.leveldificult += 1
                print(self.leveldificult)
                print ("small")
            elif self.leveldificult >= 4:
                self.leveldificult = random.randint(5, 6)
                if self.leveldificult == 5:
                    self.obstacles.append(Cactus_Large(LARGE_CACTUS))            
                    print ("large")
                elif self.leveldificult == 6:
                    self.obstacles.append(Cactus_Small(SMALL_CACTUS))
                    print ("small")
          
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
