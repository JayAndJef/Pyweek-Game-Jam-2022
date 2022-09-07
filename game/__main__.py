# -*- coding: utf_8 -*-

# __main__.py - Main Python file.
# Copyright (C) 2022  T.M.J
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


# Imports
import sys
from typing import NoReturn

from .constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BACKGROUND
from .boost_orb import BoostOrb
from .player import Player
from .platform import Platform

import pygame


# Main fuction
def main() -> NoReturn:
    # Initialize Pygame
    pygame.init()

    # Configure the game window
    win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # pygame.display.set_icon('')
    pygame.display.set_caption('Theme: The Red Planet!')

    clock = pygame.time.Clock()
    player = Player(500, 360)
    platforms = pygame.sprite.Group()
    for c in range(0, SCREEN_WIDTH, 24):
        platforms.add(Platform(c, SCREEN_HEIGHT-12))

    while True:
        # Update important game elements
        pygame.event.pump()
        win.fill(BACKGROUND)
        player.update(platforms)
        player.draw(win)
        platforms.draw(win)
        pygame.display.flip()

        # Kill the program when the window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(FPS)


if __name__ == '__main__':
    main()
