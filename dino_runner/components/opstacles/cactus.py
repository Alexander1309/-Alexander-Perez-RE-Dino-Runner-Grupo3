import random

from dino_runner.components.opstacles.opstacle import Obstacle


class Cactus(Obstacle):
  def __init__(self, image):
    self.type = random.randint(0, 2)
    super().__init__(image, self.type)
