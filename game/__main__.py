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

import pygame

from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
)

# Initialize Pygame
pygame.init()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_icon('')
pygame.display.set_caption('Theme: The Red Planet!')

clock = pygame.time.Clock()

# Main function
def main():
    while True:
        clock.tick(FPS)
    
        # End the program when the window is closed
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    sys.exit()
    
        # Update the window
        pygame.display.update()


if __name__ == '__main__':
    main()
