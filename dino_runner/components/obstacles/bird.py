import random

from dino_runner.components.obstacles.obstacles import Obstacle

class Bird_High(Obstacle):
    def __init__(self, image):
        self.type = 0
        self.is_animated = True
        super().__init__(image, self.type, self.is_animated)
        self.rect.y = 240

class Bird_Low(Obstacle):
    def __init__(self, image):
        self.type = 0
        self.is_animated = True
        super().__init__(image, self.type, self.is_animated)
        self.rect.y = 287