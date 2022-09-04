import pygame

class baseSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y) -> None:
        super().__init__()
        
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        
    def update(self):
        pass
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        