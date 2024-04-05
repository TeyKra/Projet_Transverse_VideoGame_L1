import pygame
import random
from Player1 import Oka
from Player1 import Ember
from Player1 import Tortue_Geniale
from Player1 import Mage
from Player2 import Oka2
from Player2 import Ember2
from Player2 import Tortue_Geniale_2
from Player2 import Mage_2
from Timer import Timer
#from projectile_ import Projectile_
from Sol import sol
from bonus_event import BonusEvent


#Representation du jeu
class Game:

    def __init__(self):
    #définir si le jeu a commencé
        self.is_playing = False


        self.bonus_event = BonusEvent(self)

    #timer
        self.timer = Timer(self)
    #Option
        self.option = False
        self.ChangeDroitePlayer1=False

    # Perso
        self.ChosePerso = False
        self.Player1=False
        self.Player2 = False
    #Player 1
        self.Oka_ = False
        self.Ember_ = False
        self.Tortue_Geniale_ = False
        self.Mage_=False
    #Player 2
        self.Oka2_ = False
        self.Ember2_ = False
        self.Tortue_Geniale_2_=False
        self.Mage2_=False

    #Sol
        self.sol = sol()

    #gravité joueur 1 + collision sol
        self.gravity_player_1=(0, 9.8)
        self.resistance_player_1=(0,0)
        self.collision_sol_player_1=False

    #gravité joueur 2 + collision sol
        self.gravity_player_2=(0,9.8)
        self.resistance_player_2=(0,0)
        self.collision_sol_player_2=False

    #gravité arrow
        self.gravity_arrow = (0, 9.8)
        self.resistance_arrow = (0,0)
        self.collision_sol_arrow = False

    #Map

        self.Map = False

    #fps
        self.clock=pygame.time.Clock()
        self.fps=260

        self.pressed = {}

        self.draw= False

    def Choose_Map(self):
        self.Map = True

#gravité
    def gravity_game(self):
        if self.Oka_==True:
            self.player1_Oka.rect.y += self.gravity_player_1[1] + self.resistance_player_1[1]
        if self.Ember_ == True:
            self.player1_Ember.rect.y += self.gravity_player_1[1] + self.resistance_player_1[1]
        if self.Tortue_Geniale_ == True:
            self.player1_Tortue_Geniale.rect.y += self.gravity_player_1[1] + self.resistance_player_1[1]
        if self.Mage_ == True:
            self.player1_Mage.rect.y += self.gravity_player_1[1] + self.resistance_player_1[1]
        if self.Oka2_==True:
            self.player2_Oka2.rect.y +=self.gravity_player_2[1] + self.resistance_player_2[1]
        if self.Ember2_==True:
            self.player2_Ember2.rect.y +=self.gravity_player_2[1] + self.resistance_player_2[1]
        if self.Tortue_Geniale_2_==True:
            self.player2_Tortue_Geniale_2.rect.y +=self.gravity_player_2[1] + self.resistance_player_2[1]
        if self.Mage2_==True:
            self.player2_Mage2.rect.y +=self.gravity_player_2[1] + self.resistance_player_2[1]

#Player 1
    def Oka(self):
        self.all_player1_Oka= pygame.sprite.Group()
        self.player1_Oka = Oka(self)
        self.all_player1_Oka.add(self.player1_Oka)
        self.Oka_=True
        self.Player2=True
        self.Player1 = True
    def Ember(self):
        self.all_player1_Ember= pygame.sprite.Group()
        self.player1_Ember = Ember(self)
        self.all_player1_Ember.add(self.player1_Ember)
        self.Ember_ =True
        self.Player2 = True
        self.Player1 = True
    def Tortue_Geniale(self):
        self.all_player1_Tortue_Geniale= pygame.sprite.Group()
        self.player1_Tortue_Geniale = Tortue_Geniale(self)
        self.all_player1_Tortue_Geniale.add(self.player1_Tortue_Geniale)
        self.Tortue_Geniale_ =True
        self.Player2 = True
        self.Player1 = True
    def Mage(self):
        self.all_player1_Mage= pygame.sprite.Group()
        self.player1_Mage = Mage(self)
        self.all_player1_Mage.add(self.player1_Mage)
        self.Mage_ =True
        self.Player1 = True
        self.Player2 = True
#Player 2
    def Oka2(self):
        self.all_player2_Oka2 = pygame.sprite.Group()
        self.player2_Oka2 = Oka2(self)
        self.all_player2_Oka2.add(self.player2_Oka2)
        self.Oka2_=True
        self.start()
    def Ember2(self):
        self.all_player2_Ember2 = pygame.sprite.Group()
        self.player2_Ember2 = Ember2(self)
        self.all_player2_Ember2.add(self.player2_Ember2)
        self.Ember2_=True
        self.start()
    def Tortue_Geniale_2(self):
        self.all_player2_Tortue_Geniale_2 = pygame.sprite.Group()
        self.player2_Tortue_Geniale_2 = Tortue_Geniale_2(self)
        self.all_player2_Tortue_Geniale_2.add(self.player2_Tortue_Geniale_2)
        self.Tortue_Geniale_2_=True
        self.start()
    def Mage2(self):
        self.all_player2_Mage2 = pygame.sprite.Group()
        self.player2_Mage2 = Mage_2(self)
        self.all_player2_Mage2.add(self.player2_Mage2)
        self.Mage2_=True
        self.start()

    def start(self):
        self.draw = False
        self.is_playing=True
    #Player 1
        if self.Oka_==True:
            self.player1_Oka.rect.x = 200
            self.player1_Oka.rect.y = 100
            self.player1_Oka.all_projectile_.remove()
        if self.Ember_==True:
            self.player1_Ember.rect.x = 200
            self.player1_Ember.rect.y = 100
            self.player1_Ember.all_projectile.remove()
        if self.Tortue_Geniale_==True:
            self.player1_Tortue_Geniale.rect.x = 200
            self.player1_Tortue_Geniale.rect.y = 100
            self.player1_Tortue_Geniale.all_poings.remove()
        if self.Mage_==True:
            self.player1_Mage.rect.x = 200
            self.player1_Mage.rect.y = 100
            self.player1_Mage.all_arrow.remove()

    #Player 2
        if self.Oka2_==True:
            self.player2_Oka2.rect.x = 1000
            self.player2_Oka2.rect.y = 100
            self.player2_Oka2.all_projectile_2.remove()
        if self.Ember2_==True:
            self.player2_Ember2.rect.x = 1000
            self.player2_Ember2.rect.y = 100
            self.player2_Ember2.all_projectile2.remove()
        if self.Tortue_Geniale_2_==True:
            self.player2_Tortue_Geniale_2.rect.x = 1000
            self.player2_Tortue_Geniale_2.rect.y = 100
            self.player2_Tortue_Geniale_2.all_poings_2.remove()
        if self.Mage2_==True:
            self.player2_Mage2.rect.x = 1000
            self.player2_Mage2.rect.y = 100
            self.player2_Mage2.all_arrow2.remove()

    def game_over(self):
        #remettre le jeu à neuf
    #Player1
        if self.Oka_ == True:
            self.player1_Oka.health=self.player1_Oka.max_health
            self.player1_Oka.all_projectile_.remove()
            self.player1_Oka.velocity = 10
            self.player1_Oka.attack = 7
            self.player1_Oka.health = 390

        if self.Ember_ == True:
            self.player1_Ember.health = self.player1_Ember.max_health
            self.player1_Ember.all_projectile.remove()
            self.player1_Ember.velocity = 10
            self.player1_Ember.attack = 45
            self.player1_Ember.health = 390

        if self.Tortue_Geniale_ == True:
            self.player1_Tortue_Geniale.health = self.player1_Tortue_Geniale.max_health
            self.player1_Tortue_Geniale.all_poings.remove()
            self.player1_Tortue_Geniale.velocity = 10
            self.player1_Tortue_Geniale.attack = 4
            self.player1_Tortue_Geniale.health = 390

        if self.Mage_ == True:
            self.player1_Mage.health = self.player1_Mage.max_health
            self.player1_Mage.all_arrow.remove()
            self.player1_Mage.velocity = 10
            self.player1_Mage.attack = 30
            self.player1_Mage.health = 390

    #Player2
        if self.Oka2_==True:
            self.player2_Oka2.health = self.player2_Oka2.max_health
            self.player2_Oka2.all_projectile_2.remove()
            self.player2_Oka2.velocity = 10
            self.player2_Oka2.attack = 7
            self.player2_Oka2.health = 390
        if self.Ember2_==True:
            self.player2_Ember2.health = self.player2_Ember2.max_health
            self.player2_Ember2.all_projectile2.remove()
            self.player2_Ember2.velocity = 10
            self.player2_Ember2.attack = 45
            self.player2_Ember2.health = 390
        if self.Tortue_Geniale_2_==True:
            self.player2_Tortue_Geniale_2.health = self.player2_Tortue_Geniale_2.max_health
            self.player2_Tortue_Geniale_2.all_poings_2.remove()
            self.player2_Tortue_Geniale_2.velocity = 10
            self.player2_Tortue_Geniale_2.attack = 4
            self.player2_Tortue_Geniale_2.health = 390
        if self.Mage2_==True:
            self.player2_Mage2.health = self.player2_Mage2.max_health
            self.player2_Mage2.all_arrow2.remove()
            self.player2_Mage2.velocity = 10
            self.player2_Mage2.attack = 30
            self.player2_Mage2.health = 390

        self.timer.percent_T = 100
        self.bonus_event.T1 = 10
        self.bonus_event.T2 = 95
        self.bonus_event.Random_Time = random.randint(self.bonus_event.T1, self.bonus_event.T2)
        self.bonus_event.Random_Bonus = random.randint(1, 3)
        self.bonus_event.reset_percent_b()
        self.bonus_event.bonus_vitesse.Bonus_True = False
        self.bonus_event.bonus_force.Bonus_True = False
        self.bonus_event.bonus_vie.Bonus_True = False
        self.bonus_event.bonus_vitesse.reset_percent_apparition_b()
        self.bonus_event.bonus_force.reset_percent_apparition_b()
        self.bonus_event.bonus_vie.reset_percent_apparition_b()
        self.draw = False

    #Player 1
        self.Oka_ = False
        self.Ember_ = False
        self.Tortue_Geniale_ = False
        self.Mage_ = False

    #Player 2
        self.Oka2_ = False
        self.Ember2_ = False
        self.Tortue_Geniale_2_ = False
        self.Mage2_ = False



        self.Player1=False
        self.Player2=False
        self.ChosePerso=False
        self.option=False
        self.is_playing = False
        self.Map = False



    def update(self, screen):

        self.clock.tick(self.fps)
    # Sol
        self.sol.afficher(screen)
        self.gravity_game()

        self.bonus_event.update_bar_b(screen)
        self.timer.update_bar_T(screen)

        if self.bonus_event.bonus_vitesse.Bonus_True == True:
            self.bonus_event.bonus_vitesse.update_bar_apparition_b(screen)
        if self.bonus_event.bonus_force.Bonus_True == True:
            self.bonus_event.bonus_force.update_bar_apparition_b(screen)
        if self.bonus_event.bonus_vie.Bonus_True == True:
            self.bonus_event.bonus_vie.update_bar_apparition_b(screen)

        self.bonus_event.all_bonus_vitesse.draw(screen)
        self.bonus_event.all_bonus_force.draw(screen)
        self.bonus_event.all_bonus_vie.draw(screen)

        for Bonus_Vie in self.bonus_event.all_bonus_vie:
            Bonus_Vie.fall()
        for Bonus_Force in self.bonus_event.all_bonus_force:
            Bonus_Force.fall()
        for Bonus_Vitesse in self.bonus_event.all_bonus_vitesse:
            Bonus_Vitesse.fall()

    #Player1
        if self.Oka_ == True:
            # image player
            screen.blit(self.player1_Oka.image, self.player1_Oka.rect)
            #fps

            #collision avec sol+saut
            if self.sol.rect.colliderect(self.player1_Oka.rect):
                self.resistance_player_1=(0,-9.8)
                self.collision_sol_player_1=True
                self.player1_Oka.Nombre_de_saut = 0
            else:
                self.resistance_player_1=(0,2)
            if self.collision_sol_player_1 and self.player1_Oka.a_sauter:
                if self.player1_Oka.Nombre_de_saut <2 :
                    self.player1_Oka.sauter()
            # recup projectiles
            #for projectile in self.player1_Oka.all_projectile:
            #    projectile.move()

            # actualiser barre du jeu
            self.player1_Oka.update_bar_2(screen)
            self.player1_Oka.update_bar(screen)


            # barresDevies
            for player1_Oka in self.all_player1_Oka:
                player1_Oka.update_health_bar(screen)
            # image projectile
            #self.player1_Oka.all_slash.draw(screen)

            for projectile_ in self.player1_Oka.all_projectile_:
                projectile_.move()

            self.player1_Oka.all_projectile_.draw(screen)

            # savoir si le joueur va à droite, gauche
            if self.pressed.get(pygame.K_d) and self.player1_Oka.rect.x + self.player1_Oka.rect.width < screen.get_width() and self.player1_Oka.cooldown:
                self.player1_Oka.move_right()
            elif self.pressed.get(pygame.K_q) and self.player1_Oka.rect.x > 0 and self.player1_Oka.cooldown:
                self.player1_Oka.move_left()


        if self.Ember_ == True:
            # image player
            screen.blit(self.player1_Ember.image, self.player1_Ember.rect)
            # collision avec sol+saut
            if self.sol.rect.colliderect(self.player1_Ember.rect):
                self.resistance_player_1 = (0, -9.8)
                self.collision_sol_player_1 = True
                self.player1_Ember.Nombre_de_saut = 0
            else:
                self.resistance_player_1 = (0, 2)
            if self.collision_sol_player_1 and self.player1_Ember.a_sauter:
                if self.player1_Ember.Nombre_de_saut < 2:
                    self.player1_Ember.sauter()
            # recup projectiles
            for projectile in self.player1_Ember.all_projectile:
                projectile.move()
            # barresDevies
            for player1_Ember in self.all_player1_Ember:
                player1_Ember.update_health_bar(screen)
            # image projectile
            self.player1_Ember.all_projectile.draw(screen)

            self.player1_Ember.update_bar_2(screen)
            self.player1_Ember.update_bar(screen)
            # savoir si le joueur va à droite, gauche
            if self.pressed.get(pygame.K_d) and self.player1_Ember.rect.x + self.player1_Ember.rect.width < screen.get_width() and self.player1_Ember.cooldown:
                self.player1_Ember.move_right()
            elif self.pressed.get(pygame.K_q) and self.player1_Ember.rect.x > 0 and self.player1_Ember.cooldown:
                self.player1_Ember.move_left()

        if self.Tortue_Geniale_ == True:
            # image player
            screen.blit(self.player1_Tortue_Geniale.image, self.player1_Tortue_Geniale.rect)
            # collision avec sol+saut
            if self.sol.rect.colliderect(self.player1_Tortue_Geniale.rect):
                self.resistance_player_1 = (0, -9.8)
                self.collision_sol_player_1 = True
                self.player1_Tortue_Geniale.Nombre_de_saut = 0
            else:
                self.resistance_player_1 = (0, 2)
            if self.collision_sol_player_1 and self.player1_Tortue_Geniale.a_sauter:
                if self.player1_Tortue_Geniale.Nombre_de_saut < 2:
                    self.player1_Tortue_Geniale.sauter()
            # recup projectiles
            #for projectile in self.player1_Tortue_Geniale.all_projectile:
            #    projectile.move()
            # barresDevies
            for player1_Tortue_Geniale in self.all_player1_Tortue_Geniale:
                player1_Tortue_Geniale.update_health_bar(screen)
            # image projectile
            for poing1 in self.player1_Tortue_Geniale.all_poings:
                poing1.move()

            self.player1_Tortue_Geniale.all_poings.draw(screen)

            self.player1_Tortue_Geniale.update_bar_2(screen)
            self.player1_Tortue_Geniale.update_bar(screen)
            # savoir si le joueur va à droite, gauche
            if self.pressed.get(pygame.K_d) and self.player1_Tortue_Geniale.rect.x + self.player1_Tortue_Geniale.rect.width < screen.get_width() and self.player1_Tortue_Geniale.cooldown:
                self.player1_Tortue_Geniale.move_right()
            elif self.pressed.get(pygame.K_q) and self.player1_Tortue_Geniale.rect.x > 0 and self.player1_Tortue_Geniale.cooldown:
                self.player1_Tortue_Geniale.move_left()

        if self.Mage_ == True:
            # image player
            screen.blit(self.player1_Mage.image, self.player1_Mage.rect)
            # collision avec sol+saut
            if self.sol.rect.colliderect(self.player1_Mage.rect):
                self.resistance_player_1 = (0, -9.8)
                self.collision_sol_player_1 = True
                self.player1_Mage.Nombre_de_saut = 0
            else:
                self.resistance_player_1 = (0, 2)
            if self.collision_sol_player_1 and self.player1_Mage.a_sauter:
                if self.player1_Mage.Nombre_de_saut < 2:
                    self.player1_Mage.sauter()
            # recup projectiles
            for Arrow in self.player1_Mage.all_arrow:
                Arrow.move()
            # barresDevies
            for player1_Mage in self.all_player1_Mage:
                player1_Mage.update_health_bar(screen)
            # image projectile
            self.player1_Mage.all_arrow.draw(screen)
            self.player1_Mage.update_bar_2(screen)
            self.player1_Mage.update_bar(screen)
            # savoir si le joueur va à droite, gauche
            if self.pressed.get(pygame.K_d) and self.player1_Mage.rect.x + self.player1_Mage.rect.width < 1280 and self.player1_Mage.cooldown_Mage:
                self.player1_Mage.move_right()
            elif self.pressed.get(pygame.K_q) and self.player1_Mage.rect.x > 0 and self.player1_Mage.cooldown_Mage:
                self.player1_Mage.move_left()
    #Player 2
        if self.Oka2_==True:
            # image player
            screen.blit(self.player2_Oka2.image, self.player2_Oka2.rect)
            # collision avec sol+saut
            if self.sol.rect.colliderect(self.player2_Oka2.rect):
                self.resistance_player_2 = (0, -9.8)
                self.collision_sol_player_2 = True
                self.player2_Oka2.Nombre_de_saut = 0
            else:
                self.resistance_player_2 = (0, 2)
            if self.collision_sol_player_2 and self.player2_Oka2.a_sauter:
                if self.player2_Oka2.Nombre_de_saut <2 :
                    self.player2_Oka2.sauter()


            # recup projectiles
            #for projectile2 in self.player2_Oka2.all_projectile2:
            #    projectile2.move()
            # barresDevies
            for player2_Oka2 in self.all_player2_Oka2:
                player2_Oka2.update_health_bar(screen)
            # image projectile
            for projectile_2 in self.player2_Oka2.all_projectile_2:
                projectile_2.move2()

            self.player2_Oka2.all_projectile_2.draw(screen)

            self.player2_Oka2.update_bar_22(screen)
            self.player2_Oka2.update_bar2(screen)

            # savoir si le joueur va à droite, gauche
            if self.pressed.get(pygame.K_RIGHT) and self.player2_Oka2.rect.x + self.player2_Oka2.rect.width < screen.get_width() and self.player2_Oka2.cooldown2:
                self.player2_Oka2.move_right()
            elif self.pressed.get(pygame.K_LEFT) and self.player2_Oka2.rect.x > 0 and self.player2_Oka2.cooldown2:
                self.player2_Oka2.move_left()

        if self.Ember2_==True:
            # image player
            screen.blit(self.player2_Ember2.image, self.player2_Ember2.rect)
            # collision avec sol+saut
            if self.sol.rect.colliderect(self.player2_Ember2.rect):
                self.resistance_player_2 = (0, -9.8)
                self.collision_sol_player_2 = True
                self.player2_Ember2.Nombre_de_saut = 0
            else:
                self.resistance_player_2 = (0, 2)
            if self.collision_sol_player_2 and self.player2_Ember2.a_sauter:
                if self.player2_Ember2.Nombre_de_saut < 2:
                    self.player2_Ember2.sauter()

            # recup projectiles
            for projectile2 in self.player2_Ember2.all_projectile2:
                projectile2.move()
            # barresDevies
            for player2_Ember2 in self.all_player2_Ember2:
                player2_Ember2.update_health_bar(screen)
            # image projectile
            self.player2_Ember2.all_projectile2.draw(screen)

            self.player2_Ember2.update_bar_22(screen)
            self.player2_Ember2.update_bar2(screen)
            # savoir si le joueur va à droite, gauche
            if self.pressed.get(pygame.K_RIGHT) and self.player2_Ember2.rect.x + self.player2_Ember2.rect.width < screen.get_width() and self.player2_Ember2.cooldown2:
                self.player2_Ember2.move_right()
            elif self.pressed.get(pygame.K_LEFT) and self.player2_Ember2.rect.x > 0 and self.player2_Ember2.cooldown2:
                self.player2_Ember2.move_left()

        if self.Tortue_Geniale_2_==True:
            # image player
            screen.blit(self.player2_Tortue_Geniale_2.image, self.player2_Tortue_Geniale_2.rect)
            # collision avec sol+saut
            if self.sol.rect.colliderect(self.player2_Tortue_Geniale_2.rect):
                self.resistance_player_2 = (0, -9.8)
                self.collision_sol_player_2 = True
                self.player2_Tortue_Geniale_2.Nombre_de_saut = 0
            else:
                self.resistance_player_2 = (0, 2)
            if self.collision_sol_player_2 and self.player2_Tortue_Geniale_2.a_sauter:
                if self.player2_Tortue_Geniale_2.Nombre_de_saut < 2:
                    self.player2_Tortue_Geniale_2.sauter()

            # recup projectiles
            for poing2 in self.player2_Tortue_Geniale_2.all_poings_2:
                poing2.move2()
            # barresDevies
            for player2_Tortue_Geniale_2 in self.all_player2_Tortue_Geniale_2:
                player2_Tortue_Geniale_2.update_health_bar(screen)
            # image projectile
            self.player2_Tortue_Geniale_2.all_poings_2.draw(screen)

            self.player2_Tortue_Geniale_2.update_bar_22(screen)
            self.player2_Tortue_Geniale_2.update_bar2(screen)
            # savoir si le joueur va à droite, gauche
            if self.pressed.get(pygame.K_RIGHT) and self.player2_Tortue_Geniale_2.rect.x + self.player2_Tortue_Geniale_2.rect.width < screen.get_width() and self.player2_Tortue_Geniale_2.cooldown2:
                self.player2_Tortue_Geniale_2.move_right()
            elif self.pressed.get(pygame.K_LEFT) and self.player2_Tortue_Geniale_2.rect.x > 0 and self.player2_Tortue_Geniale_2.cooldown2:
                self.player2_Tortue_Geniale_2.move_left()

        if self.Mage2_==True:
            # image player
            screen.blit(self.player2_Mage2.image, self.player2_Mage2.rect)
            # collision avec sol+saut
            if self.sol.rect.colliderect(self.player2_Mage2.rect):
                self.resistance_player_2 = (0, -9.8)
                self.collision_sol_player_2 = True
                self.player2_Mage2.Nombre_de_saut = 0
            else:
                self.resistance_player_2 = (0, 2)
            if self.collision_sol_player_2 and self.player2_Mage2.a_sauter:
                if self.player2_Mage2.Nombre_de_saut < 2:
                    self.player2_Mage2.sauter()
            # recup projectiles
            for Arrow2 in self.player2_Mage2.all_arrow2:
                Arrow2.move()
            # barresDevies
            for player2_Mage2 in self.all_player2_Mage2:
                player2_Mage2.update_health_bar(screen)
            # image projectile
            self.player2_Mage2.all_arrow2.draw(screen)
            self.player2_Mage2.update_bar_22(screen)
            self.player2_Mage2.update_bar2(screen)
            # savoir si le joueur va à droite, gauche
            if self.pressed.get(pygame.K_RIGHT) and self.player2_Mage2.rect.x + self.player2_Mage2.rect.width < screen.get_width() and self.player2_Mage2.cooldown2:
                self.player2_Mage2.move_right()
            elif self.pressed.get(pygame.K_LEFT) and self.player2_Mage2.rect.x > 0 and self.player2_Mage2.cooldown2:
                self.player2_Mage2.move_left()



    def check_collision(self, sprite,  group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


