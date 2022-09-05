from itertools import count
from .base_sprite import baseSprite
from .constants import IMAGE_BASE
import pygame
import os

class Player(baseSprite):
    def __init__(self, x, y) -> None:
        try:
            super().__init__(IMAGE_BASE + "player_1.png", x, y)
        except FileNotFoundError:
            super().__init__("game/" + IMAGE_BASE + "player_1.png", x, y)
        self.vsp = 0
        self.hsp = 0
        self.boost_speed_left = 8
        self.boost_speed_right = 8
        self.boost_speed_up = 40 #This needs to counter gravity, would be great if someone fixed it
        self.gravity = 1 # For testing purposes
        self.press_delay = 20 #Delay button press for 5 updates
        self.counter = 20
        
    def update(self, platforms: pygame.sprite.Group):
        key = pygame.key.get_pressed()
        
        grounded = pygame.sprite.spritecollideany(self, platforms)
        #if self.rect.bottom >= 1000:
            #grounded = True
        
        if key[pygame.K_LEFT] and self.counter == self.press_delay and self.vsp < 10:
            self.hsp -= self.boost_speed_left
            self.vsp += self.boost_speed_up
            self.counter = 0
        if key[pygame.K_RIGHT] and self.counter == self.press_delay and self.vsp < 10:
            self.hsp += self.boost_speed_right
            self.vsp += self.boost_speed_up
            self.counter = 0
        
        if self.hsp < 0:
            self.hsp += 0.2
        elif self.hsp > 0:
            self.hsp -= 0.2
        
        if not grounded and self.vsp > -20:
            self.vsp -= self.gravity
        
        if grounded:
            self.vsp = 0
        
        self.move(self.hsp, -self.vsp)
        
        if self.counter < self.press_delay:
            self.counter += 1
        
        os.system("clear")
        print(self.vsp)
    
    def move(self, x, y):
        self.rect.move_ip(x, y)