import pygame

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_STYLE = "freesansbold.ttf"

def get_scrore_element(points, color=(255, 255, 255)):
  font = pygame.font.Font(FONT_STYLE, 22)
  text = font.render(f"Points: {points}", True, color)
  text_rect = text.get_rect()
  text_rect.center = (1000, 50)
  return text, text_rect

def get_center_message(msg, color=(255, 255, 255), width=SCREEN_WIDTH // 2, height=SCREEN_HEIGHT // 2):
  font = pygame.font.Font(FONT_STYLE, 30)
  text = font.render(msg, True, color)
  text_rect = text.get_rect()
  text_rect.center = (width, height)

  return text, text_rect
