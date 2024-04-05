import random
#import math
import pygame
from bonus_vitesse import Bonus_Vitesse
from bonus_force import Bonus_Force
from bonus_vie import Bonus_Vie

class BonusEvent:

    def __init__(self, game):
        self.game = game
        self.percent_b = 0
        self.percent_speed_b = 5

        self.bonus_vie = Bonus_Vie(self)
        self.all_bonus_vie = pygame.sprite.Group()

        self.bonus_force = Bonus_Force(self)
        self.all_bonus_force = pygame.sprite.Group()

        self.bonus_vitesse = Bonus_Vitesse(self)
        self.all_bonus_vitesse = pygame.sprite.Group()


        self.T1 = 10
        self.T2 = 95
        self.Random_Time = random.randint(self.T1, self.T2)
        self.Random_Bonus = random.randint(1, 3)


    def add_percent_b(self):
        self.percent_b += self.percent_speed_b / 200

    def is_full_loaded_b(self):
        return self.percent_b >= 100

    def reset_percent_b(self):
        self.percent_b = 0

    def bonus_fall(self):
        if self.Random_Bonus == 1:
            self.all_bonus_vitesse.add(self.bonus_vitesse)
        if self.Random_Bonus == 2:
            self.all_bonus_force.add(self.bonus_force)
        if self.Random_Bonus == 3:
            self.all_bonus_vie.add(self.bonus_vie)

    def attempt_fall_b(self):
        #print("RT =", self.Random_Time)
        #print("RB =", self.Random_Bonus)
        if self.Random_Time == round(self.percent_b, 2):

            #print("Apparition bonus")
            if self.Random_Bonus == 1:
                self.bonus_vitesse.Bonus_True = True
            if self.Random_Bonus == 2:
                self.bonus_force.Bonus_True = True
                if self.game.Oka_ == True:
                    self.game.player1_Oka.velocity = 10
                if self.game.Ember_ == True:
                    self.game.player1_Ember.velocity = 10
                if self.game.Tortue_Geniale_ == True:
                    self.game.player1_Tortue_Geniale.velocity = 10
                if self.game.Mage_ == True:
                    self.game.player1_Mage.velocity = 10
                if self.game.Oka2_ == True:
                    self.game.player2_Oka2.velocity = 10
                if self.game.Ember2_ == True:
                    self.game.player2_Ember2.velocity = 10
                if self.game.Tortue_Geniale_2_ == True:
                    self.game.player2_Tortue_Geniale_2.velocity = 10
                if self.game.Mage2_ == True:
                    self.game.player2_Mage2.velocity = 10
            if self.Random_Bonus == 3:
                self.bonus_vie.Bonus_True = True
                if self.game.Oka_ == True:
                    self.game.player1_Oka.velocity = 10
                if self.game.Ember_ == True:
                    self.game.player1_Ember.velocity = 10
                if self.game.Tortue_Geniale_ == True:
                    self.game.player1_Tortue_Geniale.velocity = 10
                if self.game.Mage_ == True:
                    self.game.player1_Mage.velocity = 10
                if self.game.Oka2_ == True:
                    self.game.player2_Oka2.velocity = 10
                if self.game.Ember2_ == True:
                    self.game.player2_Ember2.velocity = 10
                if self.game.Tortue_Geniale_2_ == True:
                    self.game.player2_Tortue_Geniale_2.velocity = 10
                if self.game.Mage2_ == True:
                    self.game.player2_Mage2.velocity = 10
            self.bonus_fall()
            #self.reset_percent_b()

    def update_bar_b(self, surface):
        self.add_percent_b()

        self.attempt_fall_b()

        #pygame.draw.rect(surface, (0,0,0),[
        #    0,
        #    surface.get_height() - 300,
        #    surface.get_width(),
        #    10
        #])
        #pygame.draw.rect(surface, (187, 11, 11), [
        #    0,
        #    surface.get_height() - 300,
        #    (surface.get_width()/100) * self.percent_b,
        #    10
        #])