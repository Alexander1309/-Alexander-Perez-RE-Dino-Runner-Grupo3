import random

from dino_runner.components.opstacles.opstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
  def __init__(self, image):
    self.image = image
    super().__init__(self.image, 0)