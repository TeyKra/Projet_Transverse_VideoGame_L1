import pygame
from Projectiles2 import Projectile2
from projectile_2 import Projectile_2
from Poing2 import poing2
from arrow2 import Arrow2
#Joueur 2

#Oka2
class Oka2(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 390
        self.max_health = 390
        self.attack = 7
        self.velocity = 10
        #self.all_projectile2 = pygame.sprite.Group()
        self.all_projectile_2 = pygame.sprite.Group()
        self.image = pygame.image.load('assets_2/SamuraiGauche.png')
        self.image = pygame.transform.scale(self.image, (100, 120))
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 570
        self.rect_x_barre_de_vie = 671
        self.rect_y_barre_de_vie = 21
        self.direction2 = -1
        self.saut = 0
        self.saut_montee = 0
        self.saut_descente = 5
        self.Nombre_de_saut = 0
        self.a_sauter = False
        self.EnVie=True
        self.percent2 = 0
        self.percent_22 = 0
        self.cooldown2 = True

    def add_percent_22(self):

        self.percent_22 += 5

    def reset_percent_22(self):
        self.percent_22 = 0

    def is_full_load_22(self):
        return self.percent_22 >= 100

    def update_bar_22(self, surface):
        self.add_percent_22()

        #pygame.draw.rect(surface, (0, 0, 0), [
        #    0,
        #    surface.get_height() - 300,
        #    surface.get_width(),
        #    10
        # ])
        #pygame.draw.rect(surface, (187, 11, 11), [
        #    0, surface.get_height() - 300, (surface.get_width() / 100) * self.percent_22, 10
        # ])

    def launch_projectile_2(self):
        self.all_projectile_2.add(Projectile_2(self))

    def add_percent2(self):
        self.percent2 += 2

    def is_full_load2(self):
        return self.percent2 >= 100

    def reset_percent2(self):
        self.percent2 = 0

    def update_bar2(self, surface):
        # ajouter pourcentage
        self.add_percent2()
        #pygame.draw.rect(surface, (0,0,0), [
        #    0,
        #    surface.get_height() - 100,
        #    surface.get_width(),
        #    10
        # ])
        #pygame.draw.rect(surface, (187, 11, 11), [
        #    0, surface.get_height() - 100, (surface.get_width()/100)*self.percent2, 10
        # ])

    def sauter(self):

        if self.a_sauter:

            if self.saut_montee >= 15:
                self.saut_descente -= 1
                self.saut = self.saut_descente

            else:
                self.saut_montee += 3
                self.saut = self.saut_montee

            if self.saut_descente < 0:
                self.saut_descente = 5
                self.saut_montee = 0
                self.a_sauter = False

        self.rect.y = self.rect.y - (10 * (self.saut / 2))

    def Recul(self):
        self.rect.x -= 5

    def damage(self, amount):
        #infliger les degats

        #mort
        if self.health-amount>amount:
            self.health-=amount
        else:
            #si hp=0
            self.all_projectile_2.remove()
            self.EnVie=False

    def update_health_bar(self,surface):
        #pygame.draw.rect(surface, (80, 80, 80), [self.rect.x, self.rect.y, self.max_health, 5])
        pygame.draw.rect(surface, (233, 52, 13), [self.rect_x_barre_de_vie, self.rect_y_barre_de_vie, self.health, 15])

    #def launch_projectile2(self,direction2):
    #    self.all_projectile2.add(Projectile2(self, direction2))

    def move_right(self):
        self.image = pygame.image.load("assets_2/SamuraiDroite.png")
        self.image = pygame.transform.scale(self.image, (100, 120))
        self.rect.x += self.velocity

    def move_left(self):
        self.image = pygame.image.load("assets_2/SamuraiGauche.png")
        self.image = pygame.transform.scale(self.image, (100, 120))
        self.rect.x -= self.velocity

#Ember2
class Ember2(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 390
        self.max_health = 100
        self.attack = 45
        self.velocity = 10
        self.all_projectile2 = pygame.sprite.Group()
        self.image = pygame.image.load('assets_2/Mage_Gauche.png')
        self.image = pygame.transform.scale(self.image, (95,120))
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 570
        self.rect_x_barre_de_vie = 671
        self.rect_y_barre_de_vie = 21
        self.direction2 = -1
        self.saut = 0
        self.saut_montee = 0
        self.saut_descente = 5
        self.Nombre_de_saut = 0
        self.a_sauter = False
        self.EnVie = True
        self.percent2 = 0
        self.percent_22 = 0
        self.cooldown2 = True

    def add_percent_22(self):

        self.percent_22 += 2

    def reset_percent_22(self):
        self.percent_22 = 0

    def is_full_load_22(self):
        return self.percent_22 >= 100

    def update_bar_22(self, surface):
        self.add_percent_22()

        # pygame.draw.rect(surface, (0, 0, 0), [
        #    0,
        #    surface.get_height() - 300,
        #    surface.get_width(),
        #    10
        # ])
        # pygame.draw.rect(surface, (187, 11, 11), [
        #    0, surface.get_height() - 300, (surface.get_width() / 100) * self.percent_22, 10
        # ])

    def add_percent2(self):
        self.percent2 += 3

    def is_full_load2(self):
        return self.percent2 >= 100

    def reset_percent2(self):
        self.percent2 = 0

    def update_bar2(self, surface):
        # ajouter pourcentage
        self.add_percent2()
        # pygame.draw.rect(surface, (0,0,0), [
        #    0,
        #    surface.get_height() - 100,
        #    surface.get_width(),
        #    10
        # ])
        # pygame.draw.rect(surface, (187, 11, 11), [
        #    0, surface.get_height() - 100, (surface.get_width()/100)*self.percent2, 10
        # ])

    def sauter(self):

        if self.a_sauter:

            if self.saut_montee >= 15:
                self.saut_descente -= 1
                self.saut = self.saut_descente

            else:
                self.saut_montee += 3
                self.saut = self.saut_montee

            if self.saut_descente < 0:
                self.saut_montee = 0
                self.saut_descente = 5
                self.a_sauter = False

        self.rect.y = self.rect.y - (10 * (self.saut / 2))

    def Recul(self):
        self.rect.x -= 5

    def damage(self, amount):
        #infliger les degats

        #mort
        if self.health-amount>amount:
            self.health-=amount
        else:
            # si hp=0
            self.all_projectile2.remove()
            self.EnVie = False

    def update_health_bar(self,surface):
        #pygame.draw.rect(surface, (80, 80, 80), [self.rect.x, self.rect.y, self.max_health, 5])
        pygame.draw.rect(surface, (233, 52, 13), [self.rect_x_barre_de_vie, self.rect_y_barre_de_vie, self.health, 15])

    def launch_projectile2(self):
        self.all_projectile2.add(Projectile2(self))

    def move_right(self):
        self.image = pygame.image.load("assets_2/Mage_fini.png")
        self.image = pygame.transform.scale(self.image, (95, 120))
        self.rect.x += self.velocity

    def move_left(self):
        self.image = pygame.image.load("assets_2/Mage_Gauche.png")
        self.image = pygame.transform.scale(self.image, (95, 120))
        self.rect.x -= self.velocity

#Tortue Geniale 2
class Tortue_Geniale_2(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 390
        self.max_health = 100
        self.attack = 4
        self.velocity = 10
        self.all_poings_2 = pygame.sprite.Group()
        self.image = pygame.image.load('assets_2/KaratekaGauche.png')
        self.image = pygame.transform.scale(self.image, (100, 120))
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 570
        self.rect_x_barre_de_vie = 671
        self.rect_y_barre_de_vie = 21
        self.direction2 = -1
        self.saut = 0
        self.saut_montee = 0
        self.saut_descente = 5
        self.Nombre_de_saut = 0
        self.a_sauter = False
        self.EnVie = True
        self.percent2 = 0
        self.percent_22 = 0
        self.cooldown2 = True

    def add_percent_22(self):

        self.percent_22 += 10

    def reset_percent_22(self):
        self.percent_22 = 0

    def is_full_load_22(self):
        return self.percent_22 >= 100

    def update_bar_22(self, surface):
        self.add_percent_22()

        # pygame.draw.rect(surface, (0, 0, 0), [
        #    0,
        #    surface.get_height() - 300,
        #    surface.get_width(),
        #    10
        # ])
        # pygame.draw.rect(surface, (187, 11, 11), [
        #    0, surface.get_height() - 300, (surface.get_width() / 100) * self.percent_22, 10
        # ])

    def launch_poing2(self):
        self.all_poings_2.add(poing2(self))

    def add_percent2(self):
        self.percent2 += 8

    def is_full_load2(self):
        return self.percent2 >= 100

    def reset_percent2(self):
        self.percent2 = 0

    def update_bar2(self, surface):
        # ajouter pourcentage
        self.add_percent2()
        # pygame.draw.rect(surface, (0,0,0), [
        #    0,
        #    surface.get_height() - 100,
        #    surface.get_width(),
        #    10
        # ])
        # pygame.draw.rect(surface, (187, 11, 11), [
        #    0, surface.get_height() - 100, (surface.get_width()/100)*self.percent2, 10
        # ])


    def sauter(self):

        if self.a_sauter:

            if self.saut_montee >= 15:
                self.saut_descente -= 1
                self.saut = self.saut_descente

            else:
                self.saut_montee += 3
                self.saut = self.saut_montee

            if self.saut_descente < 0:
                self.saut_montee = 0
                self.saut_descente = 5
                self.a_sauter = False

        self.rect.y = self.rect.y - (10 * (self.saut / 2))

    def Recul(self):
        self.rect.x -= 5

    def damage(self, amount):
        #infliger les degats

        #mort
        if self.health-amount>amount:
            self.health-=amount
        else:
            # si hp=0
            self.all_poings_2.remove()
            self.EnVie = False

    def update_health_bar(self,surface):
        #pygame.draw.rect(surface, (80, 80, 80), [self.rect.x, self.rect.y, self.max_health, 5])
        pygame.draw.rect(surface, (233, 52, 13), [self.rect_x_barre_de_vie, self.rect_y_barre_de_vie, self.health, 15])

    #def launch_projectile2(self,direction2):
    #    self.all_projectile2.add(Projectile2(self, direction2))

    def move_right(self):
        self.image = pygame.image.load("assets_2/Karateka.png")
        self.image = pygame.transform.scale(self.image, (100, 120))
        self.rect.x += self.velocity

    def move_left(self):
        self.image = pygame.image.load("assets_2/KaratekaGauche.png")
        self.image = pygame.transform.scale(self.image, (100, 120))
        self.rect.x -= self.velocity

#Mage 2

class Mage_2(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 390
        self.max_health = 100
        self.attack = 30
        self.velocity = 10
        self.all_arrow2 = pygame.sprite.Group()
        self.image = pygame.image.load('assets_2/archer_arc.png')
        self.image = pygame.transform.scale(self.image, (100, 120))
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 570
        self.rect_x_barre_de_vie = 671
        self.rect_y_barre_de_vie = 21
        self.direction2 = -1
        self.saut = 0
        self.saut_montee = 0
        self.saut_descente = 5
        self.Nombre_de_saut = 0
        self.a_sauter = False
        self.EnVie = True
        self.percent2 = 0
        self.percent_22 = 0
        self.cooldown2 = True

    def add_percent_22(self):

        self.percent_22 += 2

    def reset_percent_22(self):
        self.percent_22 = 0

    def is_full_load_22(self):
        return self.percent_22 >= 100

    def update_bar_22(self, surface):
        self.add_percent_22()

        # pygame.draw.rect(surface, (0, 0, 0), [
        #    0,
        #    surface.get_height() - 300,
        #    surface.get_width(),
        #    10
        # ])
        # pygame.draw.rect(surface, (187, 11, 11), [
        #    0, surface.get_height() - 300, (surface.get_width() / 100) * self.percent_22, 10
        # ])

    def add_percent2(self):
        self.percent2 += 3

    def is_full_load2(self):
        return self.percent2 >= 100

    def reset_percent2(self):
        self.percent2 = 0

    def update_bar2(self, surface):
        # ajouter pourcentage
        self.add_percent2()
        # pygame.draw.rect(surface, (0,0,0), [
        #    0,
        #    surface.get_height() - 100,
        #    surface.get_width(),
        #    10
        # ])
        # pygame.draw.rect(surface, (187, 11, 11), [
        #    0, surface.get_height() - 100, (surface.get_width()/100)*self.percent2, 10
        # ])

    def sauter(self):

        if self.a_sauter:

            if self.saut_montee >= 15:
                self.saut_descente -= 1
                self.saut = self.saut_descente

            else:
                self.saut_montee += 3
                self.saut = self.saut_montee

            if self.saut_descente < 0:
                self.saut_montee = 0
                self.saut_descente = 5
                self.a_sauter = False

        self.rect.y = self.rect.y - (10 * (self.saut / 2))

    def damage(self, amount):
        #infliger les degats

        #mort
        if self.health-amount>amount:
            self.health-=amount
        else:
            # si hp=0
            self.all_arrow2.remove()
            self.EnVie = False

    def update_health_bar(self,surface):
        #pygame.draw.rect(surface, (80, 80, 80), [self.rect.x, self.rect.y, self.max_health, 5])
        pygame.draw.rect(surface, (233, 52, 13), [self.rect_x_barre_de_vie, self.rect_y_barre_de_vie, self.health, 15])

    def launch_projectile2(self,direction2):
        self.all_arrow2.add(Arrow2(self, direction2))

    def Recul(self):
        self.rect.x -= 5

    def move_right(self):
        self.image = pygame.image.load("assets_2/archer_arc_Droite.png")
        self.image = pygame.transform.scale(self.image, (100, 120))
        self.rect.x += self.velocity

    def move_left(self):
        self.image = pygame.image.load("assets_2/archer_arc.png")
        self.image = pygame.transform.scale(self.image, (100, 120))
        self.rect.x -= self.velocity


