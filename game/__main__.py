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