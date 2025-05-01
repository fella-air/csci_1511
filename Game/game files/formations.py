# M. Overman, 4/24/2025
# lab 13, question 2

# Insert Sun Tzu quote here. I listen to too much Sabaton to be blanking on this one.
# 5/1/2025: Note to self: Invest in soundproofing and punching bag with James Corden's face on it.
from settings import Settings
from alien import Alien
from ship import Ship
import pygame
import random

class Formations():
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.resolution)
        self.ship = Ship(self)
        self.grid = []
        self.list = [self.full(), self.right_triangle(), self.checkerboard()]
        # grid is a dictionary that will contain a boolean for each possible alien placement.

        # Spacing between each alien is the width of one of their hitboxes.
        # Creates 30 aliens at the default resolution of 1000 x 600, with 5 columns and 6 rows.

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # Determine the number of aliens that fit in one row.
        available_space_x = self.settings.screen_width - (2 * alien_width)
        self.columns = available_space_x // (2 * alien_width)

        # Determine the number of rows that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        self.rows = available_space_y // (2 * alien_height)

        for col in range(self.columns + 1):
            # initialize the current column as a key, containing an empty list.
            self.grid.append([])
            for row in range(self.rows):
                # add position at the current row in the current column, will spawn an alien by default.
                self.grid[col].append(True)
    def full(self):
        # fills all tiles with aliens.
        for current_col in range(len(self.grid)):
            for current_row in range(len(self.grid[current_col])):
                self.grid[current_col][current_row] = True
    def right_triangle(self):
        for current_col in range(len(self.grid)):
            # iterate through each column after all rows have been edited.
            for current_row in range(len(self.grid[current_col])):
                if current_col + current_row <= (self.columns + self.rows) / 2:
                    # disables all tiles that are closer to the final tile than they are to the first.
                    self.grid[current_col][current_row] = False
    def checkerboard(self):
        for current_col in range(len(self.grid)):
            for current_row in range(len(self.grid[current_col])):
                # removes all aliens on even-numbered tiles.
                self.grid[current_col][current_row] = ((current_col + current_row) % 2 == 1)