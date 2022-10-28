from asyncio import shield
import random
import pygame
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE

class PowerUpManager:
    def __init__(self):
        self.key_power_up = 0
        self.power_ups = []
        self.when_appears = 0
    
    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.key_power_up = random.randint(1,2)
            if self.key_power_up == 1:
                self.power_ups.append(Shield())
            if self.key_power_up == 2:
                self.power_ups.append(Hammer())
            self.when_appears += random.randint(200, 300)
            
           
                        
    def update(self, game):
        self.generate_power_up (game.score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                if self.key_power_up == 1:
                    game.player.shield = True
                elif self.key_power_up == 2:
                    game.player.hammer = True
                game.player.type = power_up.type
                game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)
        
        
        