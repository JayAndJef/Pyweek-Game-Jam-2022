# Built-In - Module
from sys import exit

# Constants
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
)

# Downloaded - Module
import pygame

pygame.init()
# Window
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#pygame.display.set_icon("")
pygame.display.set_caption("Theme: The Red Planet!")

clock = pygame.time.Clock()

# Main Function
def main():

    run = True
    while run:
        clock.tick(FPS)
    
        # Ends Program when the X button is clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    

        # Updates Window
        pygame.display.update()

    # Closes Program
    pygame.quit()
    exit()

if __name__ == '__main__':
    main()
