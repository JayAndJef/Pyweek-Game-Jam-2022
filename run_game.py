# -*- coding: utf_8 -*-

# run_game.py - Simple game launcher.
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


# Required Python version
MIN_VER = (3, 10)

if sys.version_info[:2] < MIN_VER:
    sys.exit('This game requires Python {}.{}.'.format(*MIN_VER))

# Start the game
from game.__main__ import main

main()
