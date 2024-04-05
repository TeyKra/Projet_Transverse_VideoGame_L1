import pygame
import random

class Bonus_Vie(pygame.sprite.Sprite):

    def __init__(self, bonus_event):
        super().__init__()
        self.Bonus_True = False
        self.image = pygame.image.load('assets_2/coeur_bonus_pour_la_vie.png')
        self.image = pygame.transform.scale(self.image, (100, 75))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(80, 1200)
        self.rect.y = 429
        self.percent_apparition_b = 0
        self.percent_speed_apparition_b = 1
        self.bonus_event = bonus_event

    def add_percent_apparition_b(self):
        self.percent_apparition_b += self.percent_speed_apparition_b /2

    def is_full_loaded_apparition_b(self):
        return self.percent_apparition_b >= 100

    def reset_percent_apparition_b(self):
        self.percent_apparition_b = 0

    def attempt_fin(self):
        if self.is_full_loaded_apparition_b():
            #print("FIN apparition")
            self.bonus_event.T1 = self.bonus_event.Random_Time
            self.bonus_event.Random_Time = random.randint(self.bonus_event.T1, self.bonus_event.T2)
            self.bonus_event.Random_Bonus = random.randint(1, 3)
            self.bonus_event.all_bonus_vie.remove(self)
            #self.bonus_event.reset_percent_b()
            self.Bonus_True = False
            self.reset_percent_apparition_b()
        if self.bonus_event.game.Oka_ == True:
            #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            if self.bonus_event.game.check_collision(self, self.bonus_event.game.all_player1_Oka):
                self.bonus_event.all_bonus_vie.remove(self)
                if self.bonus_event.game.player1_Oka.health <= 380:
                    self.bonus_event.game.player1_Oka.health += 10
                else:
                    self.bonus_event.game.player1_Oka.health += 0
        if self.bonus_event.game.Ember_ == True:
            #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            if self.bonus_event.game.check_collision(self, self.bonus_event.game.all_player1_Ember):
                #self.bonus_event.all_bonus_vie.remove(self)
                if self.bonus_event.game.player1_Ember.health <= 380:
                    self.bonus_event.game.player1_Ember.health += 10
                else:
                    self.bonus_event.game.player1_Ember.health += 0
        if self.bonus_event.game.Tortue_Geniale_ == True:
            #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            if self.bonus_event.game.check_collision(self, self.bonus_event.game.all_player1_Tortue_Geniale):
                self.bonus_event.all_bonus_vie.remove(self)
                if self.bonus_event.game.player1_Tortue_Geniale.health <= 380:
                    self.bonus_event.game.player1_Tortue_Geniale.health += 10
                else:
                    self.bonus_event.game.player1_Tortue_Geniale.health += 0
        if self.bonus_event.game.Mage_ == True:
            #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            if self.bonus_event.game.check_collision(self, self.bonus_event.game.all_player1_Mage):
                self.bonus_event.all_bonus_vie.remove(self)
                if self.bonus_event.game.player1_Mage.health <= 380:
                    self.bonus_event.game.player1_Mage.health += 10
                else:
                    self.bonus_event.game.player1_Mage.health += 0
        if self.bonus_event.game.Oka2_ == True:
            #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            if self.bonus_event.game.check_collision(self, self.bonus_event.game.all_player2_Oka2):
                self.bonus_event.all_bonus_vie.remove(self)
                if self.bonus_event.game.player2_Oka2.health <= 380:
                    self.bonus_event.game.player2_Oka2.health += 10
                else:
                    self.bonus_event.game.player2_Oka2.health += 0
        if self.bonus_event.game.Ember2_ == True:
            #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            if self.bonus_event.game.check_collision(self, self.bonus_event.game.all_player2_Ember2):
                self.bonus_event.all_bonus_vie.remove(self)
                if self.bonus_event.game.player2_Ember2.health <= 380:
                    self.bonus_event.game.player2_Ember2.health += 10
                else:
                    self.bonus_event.game.player2_Ember2.health += 0

        if self.bonus_event.game.Tortue_Geniale_2_ == True:
            #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            if self.bonus_event.game.check_collision(self, self.bonus_event.game.all_player2_Tortue_Geniale_2):
                self.bonus_event.all_bonus_vie.remove(self)
                if self.bonus_event.game.player2_Tortue_Geniale_2.health <= 380:
                    self.bonus_event.game.player2_Tortue_Geniale_2.health += 10
                else:
                    self.bonus_event.game.player2_Tortue_Geniale_2.health += 0
        if self.bonus_event.game.Mage2_ == True:
            #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            if self.bonus_event.game.check_collision(self, self.bonus_event.game.all_player2_Mage2):
                self.bonus_event.all_bonus_vie.remove(self)
                if self.bonus_event.game.player2_Mage2.health <= 380:
                    self.bonus_event.game.player2_Mage2.health += 10
                else:
                    self.bonus_event.game.player2_Mage2.health += 0

    def update_bar_apparition_b(self, surface):
        self.add_percent_apparition_b()
        self.attempt_fin()
        #pygame.draw.rect(surface, (0, 0, 0), [
        #    0,
        #    surface.get_height() - 400,
        #    surface.get_width(),
        #    10
        #])
        #pygame.draw.rect(surface, (187, 11, 11), [
        #    0,
        #    surface.get_height() - 400,
        #    (surface.get_width() / 100) * self.percent_apparition_b,
        #    10
        #])

    def fall(self):
        self.rect.y = 425