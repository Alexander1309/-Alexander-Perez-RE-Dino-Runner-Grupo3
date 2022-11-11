import random

import pygame

from dino_runner.components.opstacles.birds import Bird
from dino_runner.components.opstacles.cactus import Cactus
from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:
  def __init__(self):
    self.obstacles = []
    self.select_enemy = 0
  
  def update(self, game):
    if len(self.obstacles) == 0:
      self.select_enemy = random.randint(0, 4)
      if self.select_enemy == 0:
        self.obstacles.append(Cactus(LARGE_CACTUS))
      elif self.select_enemy == 1:
        self.obstacles.append(Cactus(SMALL_CACTUS))
      else:
        self.obstacles.append(Bird(BIRD))
    
    for obstacle in self.obstacles:
      obstacle.update(game.game_speed, self.obstacles, self.select_enemy)

      if game.player.hammer is not None and game.player.hammer.rect.colliderect(obstacle.rect):
        game.player.hammer.kill()
        self.obstacles.pop()
      else:
        obstacle.update(game.game_speed, self.obstacles, self.select_enemy)

      if game.player.dino_rect.colliderect(obstacle.rect):
        if not game.player.shield:
          game.player.sounds[1].play()
          self.obstacles = []
          game.player_heart_manager.reduce_heart()
          if game.player_heart_manager.heart_count > 0:
            game.player.shield = True
            game.player.show_text = False
            start_time = pygame.time.get_ticks()
            game.player.shield_time_up = start_time + 1000
          else:
            pygame.time.delay(500)
            game.playing = False
            game.death_count += 1
            break
        else:
          self.obstacles.remove(obstacle)
          


  def draw(self, screen):
    for obstacle in self.obstacles:
      obstacle.draw(screen)

  def reset_obstacles(self, self1):
    self.obstacles = []
