# -*- coding: utf_8 -*-

# base_sprite.py - Base game sprite class.
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
import pygame


# Base sprite class
class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y) -> None:
        super().__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self) -> None:
        pass

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)
