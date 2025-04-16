import pygame

class Ship:
  def __init__(self, ai_game):
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()

    self.image = pygame.image.load('Week 11/game files/resources/ship.bmp')
    self.rotated_image = pygame.transform.rotate(self.image, -90)
    self.rect = self.image.get_rect()

    self.rect.midleft = self.screen_rect.midleft

    self.moving_right = False
    self.moving_left = False

    self.settings = ai_game.settings

    self.y = float(self.rect.y)

  def update(self):
    if self.moving_right and self.rect.bottom < self.screen_rect.bottom:
      self.y += self.settings.ship_speed
    elif self.moving_left and self.rect.top > self.screen_rect.top:
      self.y -= self.settings.ship_speed

    self.rect.y = self.y

  def blit_me(self):
    self.screen.blit(self.rotated_image, self.rect)
