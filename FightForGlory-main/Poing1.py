import pygame

class poing1(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = 0
        self.image = pygame.image.load('assets_2/SlashPoingDroite.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (100, 80))
        self.rect.x = player.rect.x+50
        self.rect.y = player.rect.y+30


    def move(self):
        #self.rect.x += self.velocity
        if self.player.direction == -1:
            self.rect.x = self.player.rect.x - 33
            self.player.image = self.player.image_attaque_gauche

            self.image = pygame.image.load('assets_2/SlashPoingGauche.png')
            self.image = pygame.transform.scale(self.image, (100, 80))

        else:
            self.rect.x += self.velocity
            self.player.image = self.player.image_attaque_droite
            self.image = pygame.image.load('assets_2/SlashPoingDroite.png')
            self.image = pygame.transform.scale(self.image, (100, 80))

        if self.player.game.Oka2_==True:
            for player2 in self.player.game.check_collision(self, self.player.game.all_player2_Oka2):
                #self.player.all_projectile_.remove(self)
                player2.damage(self.player.attack)
                if self.player.direction == -1 and player2.rect.x > 0:
                    player2.rect.x -= 10
                elif self.player.direction == 1 and player2.rect.x + player2.rect.width < 1280:
                    player2.rect.x += 10
                #self.player.cooldown = True
        elif self.player.game.Ember2_==True:
            for player2 in self.player.game.check_collision(self, self.player.game.all_player2_Ember2):
                #self.player.all_projectile_.remove(self)
                player2.damage(self.player.attack)
                if self.player.direction == -1 and player2.rect.x > 0:
                    player2.rect.x -= 10
                elif self.player.direction == 1 and player2.rect.x + player2.rect.width < 1280:
                    player2.rect.x += 10
                #self.player.cooldown = True
        elif self.player.game.Tortue_Geniale_2_==True:
            for player2 in self.player.game.check_collision(self, self.player.game.all_player2_Tortue_Geniale_2):
                #self.player.all_projectile_.remove(self)
                player2.damage(self.player.attack)
                if self.player.direction == -1 and player2.rect.x > 0:
                    player2.rect.x -= 10
                elif self.player.direction == 1 and player2.rect.x + player2.rect.width < 1280:
                    player2.rect.x += 10
                #self.player.cooldown = True
        elif self.player.game.Mage2_==True:
            for player2 in self.player.game.check_collision(self, self.player.game.all_player2_Mage2):
                #self.player.all_projectile_.remove(self)
                player2.damage(self.player.attack)
                if self.player.direction == -1 and player2.rect.x > 0:
                    player2.rect.x -= 10
                elif self.player.direction == 1 and player2.rect.x + player2.rect.width < 1280:
                    player2.rect.x += 10
                #self.player.cooldown = True

        if self.player.is_full_load_2():
            if self.player.direction == -1:
                self.player.image = pygame.image.load('assets_2/KaratekaGauche.png')
                self.player.image = pygame.transform.scale(self.player.image, (100, 120))
            else:
                self.player.image = pygame.image.load('assets_2/Karateka.png')
                self.player.image = pygame.transform.scale(self.player.image, (100, 120))
            self.player.all_poings.remove(self)
            self.player.cooldown = True