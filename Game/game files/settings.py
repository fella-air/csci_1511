class Settings:

  def __init__(self):
    self.game_name = 'Alien Invasion'
    self.screen_width = 1000
    self.screen_height = 600
    self.resolution = (self.screen_width, self.screen_height)
    self.bg_color = (200, 200, 200)
    self.frame_rate = 60

    self.ship_speed = 5.0
    self.lives = 3

    self.bullet_speed = 10.0
    self.bullet_width = 5
    self.bullet_height = 25
    self.bullet_color = (240, 40, 60)
    self.bullets_allowed = 4

    self.alien_speed = 1.5
    self.fleet_advance_speed = 25
    self.fleet_direction = 1 # -1 = left, 1 = right
    self.advance_cooldown = 20 # Frames before the fleet can advance again. This prevents rapid advancing at alien speeds of over 1.
