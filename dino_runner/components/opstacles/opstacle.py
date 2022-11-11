from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):
  def __init__(self, image, type):
    self.image = image
    self.type = type
    self.rect = self.image[self.type].get_rect()
    self.rect.x = SCREEN_WIDTH
    self.rect.y = 410 - self.rect.height
    self.step_index = 0

  def update(self, game_speed, obstacles, type):
    self.rect.x -= 15

    if self.step_index >= 10:
      self.step_index = 0
      
    if type in [2, 3, 4]: 
      rest_y = [325, 335, 390]
      self.rect.y = rest_y[(type - 2)] - self.rect.height
      self.run()

    if self.rect.x < -game_speed and obstacles:
      obstacles.pop()
    
    
  def draw(self, screen):
    screen.blit(self.image[self.type], self.rect)
    
  def run(self):
    self.type = 0 if self.step_index < 5 else 1
    self.step_index += 1