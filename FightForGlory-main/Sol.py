import pygame

class sol(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.rect = pygame.Rect(0,490,1280,270)

    def afficher(self,surface):

        pygame.draw.rect(surface, [255, 0, 0], [50, 50, 90, 180], 1)