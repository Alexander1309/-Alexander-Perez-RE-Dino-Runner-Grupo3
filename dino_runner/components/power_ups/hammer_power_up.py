from dino_runner.components.power_ups.powerup import PowerUp
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE


class HammerPowerUp(PowerUp):
  def __init__(self):
    self.image = HAMMER
    self.type = HAMMER_TYPE
    super(HammerPowerUp, self).__init__(self.image, self.type)