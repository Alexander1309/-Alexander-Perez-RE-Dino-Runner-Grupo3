import random

from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH


class Meteor(Sprite):
  def __init__(self, image):
    self.image = image
    self.type = 0
    self.rect = self.image[self.type].get_rect()
    self.rect.x = SCREEN_WIDTH - random.randint(10, 600)
    self.rect.y = 10
    self.step_count = 0
  
  def update(self, self1):
    self.rect.y += 10
    self.rect.x -= 20
    self.run()

    if self1.meteors_count == 400:
      self1.reset_meteors()

    if self.step_count > 4:
      self.step_count = 0
        
  def draw(self, screen):
    screen.blit(self.image[self.type], self.rect)

  def run(self):
      self.type = self.step_count // 1
