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
from .constants import IMAGE_BASE
from .sprite import BaseSprite

import pygame


# Player class
class Player(BaseSprite):
    def __init__(self, x, y) -> None:
        super().__init__(IMAGE_BASE / 'player_1.png', x, y)

        self.v_spd = 0
        self.h_spd = 0
        self.boost_speed_left = 8
        self.boost_speed_right = 8
        self.boost_speed_up = 40  # FIXME (gravity)
        self.gravity = 1  # TODO
        self.press_delay = 20
        self.counter = 20

    def update(self, platforms: pygame.sprite.Group) -> None:
        key = pygame.key.get_pressed()
        grounded = pygame.sprite.spritecollideany(self, platforms)

        if self.counter == self.press_delay and self.v_spd < 10:
            if key[pygame.K_LEFT]:
                self.h_spd -= self.boost_speed_left
            if key[pygame.K_RIGHT]:
                self.h_spd += self.boost_speed_right

            self.v_spd += self.boost_speed_up
            self.counter = 0

        if self.h_spd < 0:
            self.h_spd += 0.2
        elif self.h_spd > 0:
            self.h_spd -= 0.2

        if not grounded and self.v_spd > -20:
            self.v_spd -= self.gravity

        if grounded:
            self.v_spd = 0

        self.move(self.h_spd, -self.v_spd)

        if self.counter < self.press_delay:
            self.counter += 1

    def move(self, x, y) -> None:
        self.rect.move_ip(x, y)
