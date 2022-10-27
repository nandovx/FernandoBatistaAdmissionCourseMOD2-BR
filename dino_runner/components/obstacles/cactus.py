import random

from dino_runner.components.obstacles.obstacles import Obstacle

class Cactus_Small(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        self.is_animated = False
        super().__init__(image, self.type, self.is_animated)
        self.rect.y = 325
        
class Cactus_Large(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        self.is_animated = False
        super().__init__(image, self.type, self.is_animated)
        self.rect.y = 300