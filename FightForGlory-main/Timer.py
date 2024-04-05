import pygame

class Timer(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.percent_T = 100
        self.percent_speed_T = 5

    def add_percent_T(self):
        self.percent_T -= self.percent_speed_T/200

    def is_full_load_T(self):
        return self.percent_T <=0

    def reset_percent_T(self):
        self.percent_T = 100

    def update_bar_T(self, surface):
        # ajouter pourcentage
        self.add_percent_T()

        pygame.draw.rect(surface, (0,0,0), [
            0,
            surface.get_height() - 20,
            surface.get_width(),
            10
         ])
        pygame.draw.rect(surface, (30, 144, 255), [
            0, surface.get_height() - 20, (surface.get_width()/100)*self.percent_T, 10
         ])

