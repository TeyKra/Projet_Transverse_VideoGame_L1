import pygame

class poing2(pygame.sprite.Sprite):

    def __init__(self, player2):
        super().__init__()
        self.player2 = player2
        self.velocity = 0
        self.image = pygame.image.load('assets_2/SlashPoingDroite.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (100, 80))
        self.rect.x = player2.rect.x+50
        self.rect.y = player2.rect.y+30

    def move2(self):
        #self.rect.x += self.velocity
        if self.player2.direction2 == -1:
            self.rect.x = self.player2.rect.x - 33
            self.player2.image = pygame.image.load('assets_2/KaratekaCoupGauche.png')
            self.player2.image = pygame.transform.scale(self.player2.image, (120, 120))
            self.image = pygame.image.load('assets_2/SlashPoingGauche.png')
            self.image = pygame.transform.scale(self.image, (100, 80))

        else:
            self.rect.x += self.velocity
            self.player2.image = pygame.image.load('assets_2/KaratekaCoup.png')
            self.player2.image = pygame.transform.scale(self.player2.image, (120, 120))
            self.image = pygame.image.load('assets_2/SlashPoingDroite.png')
            self.image = pygame.transform.scale(self.image, (100, 80))

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
                self.player2.image = pygame.image.load('assets_2/KaratekaGauche.png')
                self.player2.image = pygame.transform.scale(self.player2.image, (100, 120))
            else:
                self.player2.image = pygame.image.load('assets_2/Karateka.png')
                self.player2.image = pygame.transform.scale(self.player2.image, (100, 120))
            self.player2.all_poings_2.remove(self)
            self.player2.cooldown2 = True