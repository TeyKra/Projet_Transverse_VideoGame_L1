import pygame
from projectiles import Projectile
from projectile_ import Projectile_
from Poing1 import  poing1
from arrow import Arrow
#from Slash import Epee
import math
from Projectiles2 import Projectile2


#Oka
class Oka(pygame.sprite.Sprite):

            def __init__(self,game):
                super().__init__()
                self.game = game
                self.health = 390
                self.max_health = 390
                self.attack = 7
                self.velocity = 10
                #self.all_projectile = pygame.sprite.Group()
                #self.all_slash = pygame.sprite.Group()
                self.all_projectile_ = pygame.sprite.Group()
                self.image = pygame.image.load('assets_2/SamuraiDroite.png')
                self.image = pygame.transform.scale(self.image, (100, 120))
                self.image_attaque_gauche = pygame.image.load('assets_2/SamuraiAttaqueGauche.png')
                self.image_attaque_gauche = pygame.transform.scale(self.image_attaque_gauche, (140, 150))
                self.rect = self.image.get_rect()
                self.rect.x = 400
                self.rect.y = 570
                self.rect_x_barre_de_vie = 220
                self.rect_y_barre_de_vie = 21
                self.direction = 1
                self.saut=0
                self.saut_montee=0
                self.saut_descente=5
                self.Nombre_de_saut=0
                self.a_sauter=False
                self.EnVie=True
                self.percent = 0
                self.percent_2 = 0
                self.cooldown = True

            def add_percent_2(self):

                self.percent_2 += 5

            def reset_percent_2(self):
                self.percent_2 = 0

            def is_full_load_2(self):
                return self.percent_2 >= 100

            def update_bar_2(self, surface):
                self.add_percent_2()

                #pygame.draw.rect(surface, (0, 0, 0), [
                #    0,
                #    surface.get_height() - 300,
                #    surface.get_width(),
                #    10
                #])
                #pygame.draw.rect(surface, (187, 11, 11), [
                #    0, surface.get_height() - 300, (surface.get_width() / 100) * self.percent_2, 10
                #])

            def launch_projectile_(self):
                self.all_projectile_.add(Projectile_(self))

            def add_percent(self):
                self.percent += 2

            def is_full_load(self):
                return self.percent >= 100

            def reset_percent(self):
                self.percent = 0

            def update_bar(self, surface):
                #ajouter pourcentage
                self.add_percent()

                #pygame.draw.rect(surface, (0,0,0), [
                #    0,
                #    surface.get_height() - 100,
                #    surface.get_width(),
                #    10
                #])
                #pygame.draw.rect(surface, (187, 11, 11), [
                #    0, surface.get_height() - 100, (surface.get_width()/100)*self.percent, 10
                #])


            #def launch_slash(self, direction):
                #self.image = pygame.image.load('assets_2/SamuraiAttaqueDroite.png')
                #self.image = pygame.transform.scale(self.image, (120, 150))
             #   self.all_slash.add(Epee(self, direction))


            def sauter(self):


                if self.a_sauter:

                    if self.saut_montee>=15:
                        self.saut_descente-=1
                        self.saut=self.saut_descente

                    else:
                        self.saut_montee+=3
                        self.saut=self.saut_montee

                    if self.saut_descente<0:
                        self.saut_descente=5
                        self.saut_montee = 0
                        self.a_sauter=False

                self.rect.y = self.rect.y -(10*(self.saut/2))

            def Recul(self):
                self.rect.x -= 5

            def damage(self, amount):
                if self.health - amount > amount:
                    self.health -= amount
                else:
                    # si hp=0
                    self.all_projectile_.remove()
                    self.EnVie=False


            def update_health_bar(self,surface):
                #couleur barre vie
                #arrière jauge
                #position jauge de vie + épaisseur et largeur
                #position back_bar
                #dessin jauge
                #pygame.draw.rect(surface, (80, 80, 80), [self.rect_x_barre_de_vie, self.rect_y_barre_de_vie, self.max_health, 15])
                pygame.draw.rect(surface, (233, 52, 13), [self.rect_x_barre_de_vie, self.rect_y_barre_de_vie, self.health, 15])

            #def launch_projectile(self, direction):
            #    self.all_projectile.add(Projectile(self, direction))

            def move_right(self):

                self.image = pygame.image.load("assets_2/SamuraiDroite.png")
                self.image = pygame.transform.scale(self.image, (100, 120))

                self.rect.x += self.velocity

            def move_left(self):
                self.image = pygame.image.load("assets_2/SamuraiGauche.png")
                self.image = pygame.transform.scale(self.image, (100, 120))

                self.rect.x -= self.velocity

#Ember
class Ember(pygame.sprite.Sprite):

            def __init__(self, game):
                super().__init__()
                self.game = game
                self.health = 390
                self.max_health = 100
                self.attack = 45
                self.velocity = 10
                self.all_projectile = pygame.sprite.Group()
                self.image = pygame.image.load('assets_2/Mage_fini.png')
                self.image = pygame.transform.scale(self.image, (95, 120))
                self.rect = self.image.get_rect()
                self.rect.x = 400
                self.rect.y = 570
                self.rect_x_barre_de_vie = 220
                self.rect_y_barre_de_vie = 21
                self.direction = 1
                self.saut = 0
                self.saut_montee = 0
                self.saut_descente = 5
                self.Nombre_de_saut = 0
                self.a_sauter = False
                self.EnVie = True
                self.percent = 0
                self.percent_2 = 0
                self.cooldown = True

            def add_percent_2(self):

                self.percent_2 += 2

            def reset_percent_2(self):
                self.percent_2 = 0

            def is_full_load_2(self):
                return self.percent_2 >= 100

            def update_bar_2(self, surface):
                self.add_percent_2()

                # pygame.draw.rect(surface, (0, 0, 0), [
                #    0,
                #    surface.get_height() - 300,
                #    surface.get_width(),
                #    10
                # ])
                # pygame.draw.rect(surface, (187, 11, 11), [
                #    0, surface.get_height() - 300, (surface.get_width() / 100) * self.percent_2, 10
                # ])



            def add_percent(self):
                self.percent += 3

            def is_full_load(self):
                return self.percent >= 100

            def reset_percent(self):
                self.percent = 0

            def update_bar(self, surface):
                # ajouter pourcentage
                self.add_percent()

                # pygame.draw.rect(surface, (0,0,0), [
                #    0,
                #    surface.get_height() - 100,
                #    surface.get_width(),
                #    10
                # ])
                # pygame.draw.rect(surface, (187, 11, 11), [
                #    0, surface.get_height() - 100, (surface.get_width()/100)*self.percent, 10
                # ])

            # def launch_slash(self, direction):
            # self.image = pygame.image.load('assets_2/SamuraiAttaqueDroite.png')
            # self.image = pygame.transform.scale(self.image, (120, 150))
            #   self.all_slash.add(Epee(self, direction))




            def sauter(self):


                if self.a_sauter:

                    if self.saut_montee>=15:
                        self.saut_descente-=1
                        self.saut=self.saut_descente

                    else:
                        self.saut_montee+=3
                        self.saut=self.saut_montee

                    if self.saut_descente<0:
                        self.saut_descente=5
                        self.saut_montee=0
                        self.a_sauter=False

                self.rect.y=self.rect.y-(10*(self.saut/2))

            def Recul(self):
                self.rect.x -= 5

            def damage(self, amount):
                # infliger les degats

                # mort
                if self.health - amount > amount:
                    self.health -= amount
                else:
                    # si hp=0
                    self.all_projectile.remove()
                    self.EnVie = False

            def update_health_bar(self, surface):
                #pygame.draw.rect(surface, (80, 80, 80), [self.rect.x, self.rect.y, self.max_health, 5])
                pygame.draw.rect(surface, (233, 52, 13), [self.rect_x_barre_de_vie, self.rect_y_barre_de_vie, self.health, 15])

            def launch_projectile(self, direction):
                self.all_projectile.add(Projectile(self, direction))

            def move_right(self):
                self.image = pygame.image.load("assets_2/Mage_fini.png")
                self.image = pygame.transform.scale(self.image, (95, 120))
                self.rect.x += self.velocity

            def move_left(self):
                self.image = pygame.image.load("assets_2/Mage_Gauche.png")
                self.image = pygame.transform.scale(self.image, (95, 120))
                self.rect.x -= self.velocity

#TortueGeniale

class Tortue_Geniale(pygame.sprite.Sprite):

            def __init__(self, game):
                super().__init__()
                self.game = game
                self.health = 390
                self.max_health = 100
                self.attack = 4
                self.velocity = 10
                self.all_poings = pygame.sprite.Group()
                self.image = pygame.image.load('assets_2/Karateka.png')
                self.image = pygame.transform.scale(self.image, (100, 120))
                self.image_attaque_droite = pygame.image.load('assets_2/KaratekaCoup.png')
                self.image_attaque_droite = pygame.transform.scale(self.image_attaque_droite, (120, 120))
                self.image_attaque_gauche = pygame.image.load('assets_2/KaratekaCoupGauche.png')
                self.image_attaque_gauche = pygame.transform.scale(self.image_attaque_gauche, (120, 120))
                self.rect = self.image.get_rect()
                self.rect.x = 400
                self.rect.y = 570
                self.rect_x_barre_de_vie = 220
                self.rect_y_barre_de_vie = 21
                self.direction = 1
                self.saut = 0
                self.saut_montee = 0
                self.saut_descente = 5
                self.Nombre_de_saut = 0
                self.a_sauter = False
                self.EnVie = True
                self.percent = 0
                self.percent_2 = 0
                self.cooldown = True

            def add_percent_2(self):

                self.percent_2 += 10

            def reset_percent_2(self):
                self.percent_2 = 0

            def is_full_load_2(self):
                return self.percent_2 >= 100

            def update_bar_2(self, surface):
                self.add_percent_2()

                # pygame.draw.rect(surface, (0, 0, 0), [
                #    0,
                #    surface.get_height() - 300,
                #    surface.get_width(),
                #    10
                # ])
                # pygame.draw.rect(surface, (187, 11, 11), [
                #    0, surface.get_height() - 300, (surface.get_width() / 100) * self.percent_2, 10
                # ])

            def launch_poing(self):
                self.all_poings.add(poing1(self))

            def add_percent(self):
                self.percent += 8

            def is_full_load(self):
                return self.percent >= 100

            def reset_percent(self):
                self.percent = 0

            def update_bar(self, surface):
                # ajouter pourcentage
                self.add_percent()

                # pygame.draw.rect(surface, (0,0,0), [
                #    0,
                #    surface.get_height() - 100,
                #    surface.get_width(),
                #    10
                # ])
                # pygame.draw.rect(surface, (187, 11, 11), [
                #    0, surface.get_height() - 100, (surface.get_width()/100)*self.percent, 10
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
                # infliger les degats

                # mort
                if self.health - amount > amount:
                    self.health -= amount
                else:
                    # si hp=0
                    self.all_poings.remove()
                    self.EnVie = False

            def update_health_bar(self, surface):
                #pygame.draw.rect(surface, (80, 80, 80), [self.rect.x, self.rect.y, self.max_health, 5])
                pygame.draw.rect(surface, (233, 52, 13), [self.rect_x_barre_de_vie, self.rect_y_barre_de_vie, self.health, 15])

            #def launch_projectile(self, direction):
            #    self.all_projectile.add(Projectile(self, direction))

            def move_right(self):
                self.image = pygame.image.load("assets_2/Karateka.png")
                self.image = pygame.transform.scale(self.image, (100, 120))
                self.rect.x += self.velocity

            def move_left(self):
                self.image = pygame.image.load("assets_2/KaratekaGauche.png")
                self.image = pygame.transform.scale(self.image, (100, 120))
                self.rect.x -= self.velocity

#Mage
class Mage(pygame.sprite.Sprite):

            def __init__(self, game):
                super().__init__()
                self.game = game
                self.health = 390
                self.max_health = 100
                self.attack = 30
                self.velocity = 10
                self.all_arrow = pygame.sprite.Group()
                self.image = pygame.image.load('assets_2/archer_arc_Droite.png')
                self.image = pygame.transform.scale(self.image, (100, 120))
                self.rect = self.image.get_rect()
                self.rect.x = 400
                self.rect.y = 570
                self.rect_x_barre_de_vie = 220
                self.rect_y_barre_de_vie = 21
                self.direction = 1
                self.arrow = Arrow(self, self.direction)
                self.saut = 0
                self.saut_montee = 0
                self.saut_descente = 5
                self.Nombre_de_saut = 0
                self.a_sauter = False
                self.EnVie = True
                self.percent = 0
                self.percent_2 = 0
                self.cooldown_Mage = True

            def add_percent_2(self):

                self.percent_2 += 2

            def reset_percent_2(self):
                self.percent_2 = 0

            def is_full_load_2(self):
                return self.percent_2 >= 100

            def update_bar_2(self, surface):
                self.add_percent_2()

                # pygame.draw.rect(surface, (0, 0, 0), [
                #    0,
                #    surface.get_height() - 300,
                #    surface.get_width(),
                #    10
                # ])
                # pygame.draw.rect(surface, (187, 11, 11), [
                #    0, surface.get_height() - 300, (surface.get_width() / 100) * self.percent_2, 10
                # ])

            def add_percent(self):
                self.percent += 3

            def is_full_load(self):
                return self.percent >= 100

            def reset_percent(self):
                self.percent = 0

            def update_bar(self, surface):
                # ajouter pourcentage
                self.add_percent()

                # pygame.draw.rect(surface, (0,0,0), [
                #    0,
                #    surface.get_height() - 100,
                #    surface.get_width(),
                #    10
                # ])
                # pygame.draw.rect(surface, (187, 11, 11), [
                #    0, surface.get_height() - 100, (surface.get_width()/100)*self.percent, 10
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

            def damage(self, amount):
                # infliger les degats

                # mort
                if self.health - amount > amount:
                    self.health -= amount
                else:
                    # si hp=0
                    self.all_arrow.remove()
                    self.EnVie = False

            def update_health_bar(self, surface):
                #pygame.draw.rect(surface, (80, 80, 80), [self.rect.x, self.rect.y, self.max_health, 5])
                pygame.draw.rect(surface, (233, 52, 13), [self.rect_x_barre_de_vie, self.rect_y_barre_de_vie, self.health, 15])

            def launch_projectile(self, direction):
                self.all_arrow.add(Arrow(self, direction))

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
