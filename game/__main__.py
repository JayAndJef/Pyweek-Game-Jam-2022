from sys import exit

import pygame

pygame.init()

WIDTH, HEIGHT = 1080, 720
win = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_icon("")
pygame.display.set_caption("Theme: The Red Planet!")

FPS = 60
clock = pygame.time.Clock()

def main():

    run = True
    while run:
        clock.tick(FPS)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    


        pygame.display.update()

    pygame.quit()
    exit()

if __name__ == '__main__':
    main()
