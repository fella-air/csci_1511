import sys
from time import sleep
import pygame
import random
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from formations import Formations

class AlienInvasion:

  def __init__(self):
    pygame.init()
    self.settings = Settings()
    self.screen = pygame.display.set_mode(self.settings.resolution)
    self.stats = GameStats(self)
    self.clock = pygame.time.Clock()
    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()
    self.aliens = pygame.sprite.Group()
    self.formations = Formations()
    pygame.display.set_caption(self.settings.game_name)

    self._create_fleet()

  def _create_fleet(self):
    # Creates the fleet of aliens.
    # Chooses any one of the formations in the list.
    result = random.randint(0, len(self.formations.list) - 1)
    # Alright, fucking finally. Do you have any idea how much time I spent trying to figure
    # out how to do this? Initially the formations file was responsible for this randomizer function,
    # but it didn't let me call the formation functions from it. Now my only solution that I can think of
    # is this Yandere Simulator-esque "if result == 0, 1, or 2" bullshit. I'm already a few weeks behind
    # on my assignments, so this will have to do for now. I swear, if I ever have the displeasure of
    # reading the phrase "module object is not callable" again, I will slam my forehead so hard into a
    # wall that everything within a mile radius will be reduced to a fine powder.
    # Fat Man, meet "Fucking Malding."
    if result == 0:
      self.formations.full()
    elif result == 1:
      self.formations.right_triangle()
    elif result == 2:
      self.formations.checkerboard()

    # Create the first row.
    for col_number in range (self.formations.rows):
      for row_number in range (self.formations.columns):
        # Place one alien on all grid tiles marked "True".
        if self.formations.grid[row_number][col_number]:
          self._create_alien(col_number, row_number)

  def _create_alien(self, alien_number, row_number):
    alien = Alien(self)
    alien_width, alien_height = alien.rect.size
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2 * alien.rect.height * row_number
    self.aliens.add(alien)

  def _check_keydown_events(self, event):
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = True
    elif event.key == pygame.K_q:
      sys.exit()
    elif event.key == pygame.K_SPACE:
      self._fire_bullet()
  
  def _check_keyup_events(self, event):
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = False

  def _check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        self._check_keydown_events(event)
      elif event.type ==  pygame.KEYUP:
        self._check_keyup_events(event)
      
  def _fire_bullet(self):
    if len(self.bullets) < self.settings.bullets_allowed:
      new_bullet = Bullet(self)
      self.bullets.add(new_bullet)

  def _update_aliens(self):
    self._check_fleet_edges()
    self.aliens.update()

    # Check if alien collides with player
    if pygame.sprite.spritecollideany(self.ship, self.aliens):
      print("Ship hit!")
      self._ship_hit()

  def _ship_hit(self):
    if self.stats.ships_left > 0:
      self.stats.lives -= 1
      self.aliens.empty()
      self.bullets.empty()
      self._create_fleet()
      self.ship.center_ship()
      sleep(0.5)
    else:
      self.stats.game_active = False

  def _check_fleet_edges(self):
    if (self.stats.last_advance <= self.settings.advance_cooldown):
      self.stats.last_advance += 1
    for alien in self.aliens.sprites():
      if alien.check_edges() and (self.stats.last_advance > self.settings.advance_cooldown):
        self.stats.last_advance = 0
        self._change_fleet_direction()
        break

  def _change_fleet_direction(self):
    for alien in self.aliens.sprites():
      alien.rect.y += self.settings.fleet_advance_speed
    self.settings.fleet_direction *= -1

  def _update_bullets(self):
    # Updates bullet positions.
    self.bullets.update()
    # Get rid of offscreen bullets
    for bullet in self.bullets.copy():
      if bullet.rect.bottom <= 0:
        self.bullets.remove(bullet)
    self._check_bullet_collision()

  def _check_bullet_collision(self):
    # Check for bullet collision with aliens
    collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
    # Reset bullets and aliens once all aliens dead.
    if not self.aliens:
      self.bullets.empty()
      self._create_fleet()

  def _update_screen(self):
    self.screen.fill(self.settings.bg_color)
    self.ship.blit_me()
    for bullet in self.bullets.sprites():
      bullet.draw_bullet()
    self.aliens.draw(self.screen)

    pygame.display.flip()

  def run_game(self):
    while True:
      self._check_events()
      if self.stats.game_active:
        self.ship.update()
        self._update_bullets()
        self._update_aliens()
      self._update_screen()
      self.clock.tick(self.settings.frame_rate)

if __name__ == '__main__':
  # Make a game instance, and run the game.
  ai = AlienInvasion()
  ai.run_game()
