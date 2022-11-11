from dino_runner.components.clouds.cloud import Cloud
from dino_runner.utils.constants import CLOUD


class CloudManager:
  def __init__(self):
    self.clouds = []
    self.clouds_count = 0
  
  def update(self):
    if self.clouds_count % 50 == 0 and len(self.clouds) < 6:
      self.clouds.append(Cloud(CLOUD))

    for cloud in self.clouds:
      cloud.update(self)

    self.clouds_count += 1
  
  def draw(self, screen):
    for cloud in self.clouds:
      cloud.draw(screen)

  def reset_clouds(self):
    self.clouds_count = 0
    self.clouds = []