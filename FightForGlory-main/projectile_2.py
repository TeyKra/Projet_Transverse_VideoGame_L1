import pygame

class Projectile_2(pygame.sprite.Sprite):

    def __init__(self, player2):
        super().__init__()
        self.player2 = player2
        self.velocity = 0
        self.image = pygame.image.load('assets_2/Slash.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (70, 130))
        self.rect.x = player2.rect.x+60
        self.rect.y = player2.rect.y



    def move2(self):
        #self.rect.x += self.velocity
        if self.player2.direction2 == -1:
            self.rect.x = self.player2.rect.x - 10
            self.player2.image = pygame.image.load('assets_2/SamuraiAttaqueGauche.png')
            self.player2.image = pygame.transform.scale(self.player2.image, (140, 150))
            self.image = pygame.image.load('assets_2/SlashGauche.png')
            self.image = pygame.transform.scale(self.image, (70, 130))

        else:
            self.rect.x += self.velocity
            self.player2.image = pygame.image.load('assets_2/SamuraiAttaqueDroite.png')
            self.player2.image = pygame.transform.scale(self.player2.image, (140, 150))
            self.image = pygame.image.load('assets_2/Slash.png')
            self.image = pygame.transform.scale(self.image, (70, 130))

        if self.player2.game.Oka_==True:
            for player in self.player2.game.check_collision(self, self.player2.game.all_player1_Oka):
                #self.remove()
                #dégats
                player.damage(self.player2.attack)
                if self.player2.direction2 == -1 and player.rect.x > 0:
                    player.rect.x -= 10
                elif self.player2.direction2 == 1 and player.rect.x + player.rect.width < 1280:
                    player.rect.x += 10
        elif self.player2.game.Ember_ == True:
            for player in self.player2.game.check_collision(self, self.player2.game.all_player1_Ember):
                #self.remove()
                #dégats
                player.damage(self.player2.attack)
                if self.player2.direction2 == -1 and player.rect.x > 0:
                    player.rect.x -= 10
                elif self.player2.direction2 == 1 and player.rect.x + player.rect.width < 1280:
                    player.rect.x += 10
        elif self.player2.game.Tortue_Geniale_ == True:
            for player in self.player2.game.check_collision(self, self.player2.game.all_player1_Tortue_Geniale):
                #self.remove()
                #dégats
                player.damage(self.player2.attack)
                if self.player2.direction2 == -1 and player.rect.x > 0:
                    player.rect.x -= 10
                elif self.player2.direction2 == 1 and player.rect.x + player.rect.width < 1280:
                    player.rect.x += 10
        elif self.player2.game.Mage_ == True:
            for player in self.player2.game.check_collision(self, self.player2.game.all_player1_Mage):
                #self.remove()
                #dégats
                player.damage(self.player2.attack)
                if self.player2.direction2 == -1 and player.rect.x > 0:
                    player.rect.x -= 10
                elif self.player2.direction2 == 1 and player.rect.x + player.rect.width < 1280:
                    player.rect.x += 10


        if self.player2.is_full_load_22():
            if self.player2.direction2 == -1:
                self.player2.image = pygame.image.load('assets_2/SamuraiGauche.png')
                self.player2.image = pygame.transform.scale(self.player2.image, (100, 120))
            else:
                self.player2.image = pygame.image.load('assets_2/SamuraiDroite.png')
                self.player2.image = pygame.transform.scale(self.player2.image, (100, 120))
            self.player2.all_projectile_2.remove(self)
            self.player2.cooldown2 = True