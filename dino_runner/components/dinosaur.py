import pygame
from pygame.sprite import Sprite

from dino_runner.components.hammer import Hammer
from dino_runner.utils.constants import (DEFAULT_TYPE, DUCKING, DUCKING_HAMMER,
                                         DUCKING_SHIELD, HAMMER_TYPE, JUMPING,
                                         JUMPING_HAMMER, JUMPING_SHIELD,
                                         PATH_DEATH_SOUND, PATH_JUMP_SOUND,
                                         PATH_SHOOT_SOUND, RUNNING,
                                         RUNNING_HAMMER, RUNNING_SHIELD,
                                         SHIELD_TYPE)


class Dinosaur(Sprite):
  X_POS = 80
  Y_POS = 310

  Y_POS_DUCK = 340
  JUMP_SPEED = 8.5

  def __init__(self):
    self.duck_img = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
    self.run_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}
    self.jum_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
    self.type = DEFAULT_TYPE
    self.image = self.run_img[self.type][0]
    self.dino_rect = self.image.get_rect()

    self.sounds = [
      pygame.mixer.Sound(PATH_JUMP_SOUND),
      pygame.mixer.Sound(PATH_DEATH_SOUND),
      pygame.mixer.Sound(PATH_SHOOT_SOUND),
    ]

    self.dino_rect.x = self.X_POS
    self.dino_rect.y = self.Y_POS

    self.step_index = 0

    self.dino_run = True
    self.dino_duck = False
    self.dino_jump = False
    self.jump_speed = self.JUMP_SPEED
    self.setup_state_boolean()

  def setup_state_boolean(self):
    self.has_powerup = False
    self.shield = False
    self.show_text = False
    self.shield_time_up = 0
    self.hammer = None
    self.hammer_enabled = 0

  def update(self, user_input):
    if self.dino_jump:
      self.jump()
    if self.dino_duck:
      self.duck()
    if self.dino_run:
      self.run()

    if user_input[pygame.K_DOWN] and not self.dino_jump:
      self.dino_run = False
      self.dino_duck = True
      self.dino_jump = False
    elif user_input[pygame.K_UP] and not self.dino_jump:
      self.sounds[0].play()
      self.dino_run = False
      self.dino_duck = False
      self.dino_jump = True
    elif not self.dino_jump:
      self.dino_run = True
      self.dino_duck = False
      self.dino_jump = False
    
    if self.step_index >= 10:
      self.step_index = 0

    if self.hammer_enabled > 0 and user_input[pygame.K_SPACE]:
      self.sounds[2].play()
      self.hammer = Hammer(self.dino_rect.x + 100, self.dino_rect.y + 50)
      self.hammer_enabled = max(self.hammer_enabled - 1, 0)
      if self.hammer_enabled == 0:
        self.update_to_default(HAMMER_TYPE)

    if self.hammer:
      self.hammer.update()

  def duck(self):
    self.image = self.duck_img[self.type][self.step_index // 5]
    self.dino_rect = self.image.get_rect()
    self.dino_rect.x = self.X_POS
    self.dino_rect.y = self.Y_POS_DUCK
    self.step_index += 1

  def jump(self):
    self.image = self.jum_img[self.type]
    if self.dino_jump:
      self.dino_rect.y -= self.jump_speed * 4
      self.jump_speed -= 0.8
    if self.jump_speed < -self.jump_speed:
      self.dino_rect.y = self.Y_POS
      self.dino_jump  = False
      self.jump_speed = self.JUMP_SPEED

  def draw(self, screen):
    screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
    if self.hammer:
      self.hammer.draw(screen)

  def check_invisibility(self, screen):
    if self.shield:
      time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) / 1000, 2)
      if time_to_show >= 0:
        if self.show_text:
          found = pygame.font.Font("freesansbold.ttf", 18)
          text = found.render(f"Shield enable for {time_to_show}", True, (255, 255, 255))
          text_rect = text.get_rect()
          text_rect.center = (500, 450)
          screen.blit(text, text_rect)
      else:
        self.shield = False
        self.update_to_default(SHIELD_TYPE)

  def update_to_default(self, current_type):
    if self.type == current_type:
      self.type  = DEFAULT_TYPE

  def run(self):
    self.image = self.run_img[self.type][self.step_index // 5]
    self.dino_rect = self.image.get_rect()
    self.dino_rect.x = self.X_POS
    self.dino_rect.y = self.Y_POS

    self.step_index += 1