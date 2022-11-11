import random

from dino_runner.components.meteors.meteor import Meteor
from dino_runner.utils.constants import LARGE_METEORS, SMALL_METEORS


class MeteorManager:
  def __init__(self):
    self.meteors = []
    self.meteors_count = 0
  
  def update(self):
    if self.meteors_count % 50 == 0 and len(self.meteors) < 6:
      select_meteor = random.randint(0, 1)
      if select_meteor == 0:
        self.meteors.append(Meteor(SMALL_METEORS))
      else:
        self.meteors.append(Meteor(LARGE_METEORS))

    for meteor in self.meteors:
      meteor.update(self)

    self.meteors_count += 1
  
  def draw(self, screen):
    for meteor in self.meteors:
      meteor.draw(screen)

  def reset_meteors(self):
    self.meteors_count = 0
    self.meteors = []