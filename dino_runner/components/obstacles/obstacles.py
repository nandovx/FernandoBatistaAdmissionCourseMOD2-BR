import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):
    def __init__(self, image, type, bool):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.index_animated = 0
        self.is_animated = bool
        self.animation = self.image

    def update(self, game_speed, obstacles):
        self.animate()
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def animate(self):
        if self.index_animated >= 10:
            self.index_animated = 0

        image = self.image[0] if self.index_animated < 5 else self.image[1]
        self.animation = image

        self.index_animated  += 1
        


    def draw(self, screen):
        if self.is_animated:
            screen.blit(self.animation, (self.rect.x, self.rect.y))
        else:
            screen.blit(self.image[self.type], (self.rect.x, self.rect.y))