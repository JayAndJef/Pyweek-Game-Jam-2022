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


# Built-In - Module
from sys import exit

# Constants
from .constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    BACKGROUND
)

from .player import Player

# Downloaded - Module
import pygame

# Main Function
def main():
    pygame.init()

    # Window

    win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #pygame.display.set_icon("")
    pygame.display.set_caption("Theme: The Red Planet!")

    clock = pygame.time.Clock()
    
    player = Player(500, 360)

    run = True
    while run:
        pygame.event.pump()
        
        win.fill(BACKGROUND)
        player.update(pygame.sprite.Group())
        player.draw(win)
        pygame.display.flip()
        # Ends Program when the X button is clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
        clock.tick(FPS)
        # Updates Window
        

    # Closes Program
    pygame.quit()
    exit()

if __name__ == '__main__':
    main()