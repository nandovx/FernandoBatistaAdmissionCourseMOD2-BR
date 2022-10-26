import random

from dino_runner.components.obstacles.obstacles import Obstacle

class Bird(Obstacle):
    def __init__(self, image):
        self.type = image[0] 
        super().__init__(image, self.type)
        self.rect.y = 200
