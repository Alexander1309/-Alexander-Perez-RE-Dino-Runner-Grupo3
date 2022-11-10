import random

from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH


class Cloud(Sprite):
  def __init__(self, image):
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.x = SCREEN_WIDTH
    self.cordenate_y = [100, 180, 250]
    self.rect.y = self.cordenate_y[random.randint(0, 2)]
  
  def update(self, self1):
    self.rect.x -= 10

    if self1.clouds_count == 270:
      self1.reset_clouds()
        
  def draw(self, screen):
    screen.blit(self.image, self.rect)

