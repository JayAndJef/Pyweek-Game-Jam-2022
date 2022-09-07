# -*- coding: utf_8 -*-

# player.py - General player code.
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
from .constants import IMAGE_BASE, SCREEN_WIDTH, SCREEN_HEIGHT
from .sprite import BaseSprite

import random 

import pygame

class BoostOrb(BaseSprite):
    def __init__(self, x, y):
        super().__init__(IMAGE_BASE / 'boost_orb.png', x, y)


    def random_location(self, x, y):
        self.x = random.randint(0, SCREEN_WIDTH-16)
        self.y = random.randint(SCREEN_HEIGHT/2, SCREEN_HEIGHT)
        self.rect.move_ip(x, y)
        
