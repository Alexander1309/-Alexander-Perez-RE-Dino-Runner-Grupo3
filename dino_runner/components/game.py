import pygame

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.opstacles.obstacle_manager import ObstacleManager
from dino_runner.components.player_hearts.player_heart_manager import \
    PlayerHeartManager
from dino_runner.components.text_utils import *
from dino_runner.utils.constants import (BG, FPS, GAME_SPEED, ICON, RUNNING,
                                         SCREEN_HEIGHT, SCREEN_WIDTH, TITLE)


class Game:
  def __init__(self):
    pygame.init()
    pygame.display.set_caption(TITLE)
    pygame.display.set_icon(ICON)
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    self.clock = pygame.time.Clock()
    self.playing = False
    self.game_speed = GAME_SPEED
    self.x_pos_bg = 0  
    self.y_pos_bg = 380
    self.player = Dinosaur()
    self.obstacle_manager = ObstacleManager()
    self.player_heart_manager = PlayerHeartManager()

    self.poitn_ant = 0
    self.points = 0
    self.running = True
    self.death_count = 0

  def reset(self):
    self.poitn_ant = self.points
    self.points = 0
    self.game_speed = GAME_SPEED

  def run(self):
    self.obstacle_manager.reset_obstacles(self)
    self.player_heart_manager.reset_hearts()
    self.playing = True
    while self.playing:
      self.events()
      self.update()
      self.draw()

  def execute(self):
    while self.running:
      if not self.playing:
        self.show_menu()

  def events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.playing = False
        self.running = False
    self.screen.fill((255, 255, 255))

  def update(self):
    user_input = pygame.key.get_pressed()
    self.player.update(user_input)
    self.obstacle_manager.update(self)

  def draw(self):
    self.score()
    self.clock.tick(FPS)
    self.draw_background()
    self.player.draw(self.screen)
    self.obstacle_manager.draw(self.screen)
    self.player_heart_manager.draw(self.screen)

    pygame.display.update()
    pygame.display.flip()

  def draw_background(self):
    image_width = BG.get_width()
    self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
    self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
    if self.x_pos_bg <= -image_width:
      self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
      self.x_pos_bg = 0
    self.x_pos_bg -= self.game_speed
  
  def score(self):
    self.points += 1
    if self.points % 100 == 0:
      self.game_speed += 1
    text, text_rect = get_scrore_element(self.points)
    self.screen.blit(text, text_rect)

  def handle_key_event_menu(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
        self.playing = False
        pygame.display.quit()
        pygame.quit()
        exit()

      if event.type == pygame.KEYDOWN:
        self.run()
    
  def print_menu_elements(self):
    half_screen_height = SCREEN_HEIGHT // 2
    half_screen_width = SCREEN_WIDTH // 2

    if self.death_count == 0:
      text, text_rect = get_center_message("Press any Key Start")
      self.screen.blit(text, text_rect)
    elif self.death_count > 0:
      text, text_rect = get_center_message("Press any Key to Restart")
      score, score_rect = get_center_message(f"Your Score: {self.poitn_ant}", height=half_screen_height + 50)
      death, death_rect = get_center_message(f"Death Count: {self.death_count}", height=half_screen_height + 100)
      self.screen.blit(text, text_rect)
      self.screen.blit(score, score_rect)
      self.screen.blit(death, death_rect)

    self.screen.blit(RUNNING[0], (half_screen_width-20, half_screen_height-140))

  def show_menu(self):
    self.running = True
    white_color = (155, 255, 255)
    self.screen.fill(white_color)
    self.print_menu_elements()
    pygame.display.update()
    self.handle_key_event_menu()
