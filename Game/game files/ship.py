import pygame

class Ship:
  def __init__(self, ai_game):
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()

    self.image = pygame.image.load('Game/game files/resources/ship.bmp')
    self.rotated_image = pygame.transform.rotate(self.image, -90)
    self.rect = self.image.get_rect()

    self.rect.midbottom = self.screen_rect.midbottom

    self.moving_right = False
    self.moving_left = False

    self.settings = ai_game.settings

    self.x = float(self.rect.x)

  def center_ship(self):
    self.rect.midbottom = self.screen_rect.midbottom
    self.x = float(self.rect.x)

  def update(self):
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.x += self.settings.ship_speed
    elif self.moving_left and self.rect.left > self.screen_rect.left:
      self.x -= self.settings.ship_speed

    self.rect.x = self.x

  def blit_me(self):
    self.screen.blit(self.image, self.rect)
