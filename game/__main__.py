# Built-In - Module
from sys import exit

# Downloaded - Module
import pygame

pygame.init()
# Window
WIDTH, HEIGHT = 1080, 720
win = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_icon("")
pygame.display.set_caption("Theme: The Red Planet!")

FPS = 60
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
