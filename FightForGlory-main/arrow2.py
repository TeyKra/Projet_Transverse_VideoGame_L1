import pygame

#classe pour projectile Player2

class Arrow2(pygame.sprite.Sprite):
    def __init__(self, player2, direction2):
        super().__init__()
        self.velocity = 10
        self.player2 = player2
        self.image = pygame.image.load('assets_2/Arrow.png')
        self.image = pygame.transform.scale(self.image, (180, 100))
        self.rect = self.image.get_rect()
        self.rect.x = player2.rect.x + 30
        self.rect.y = player2.rect.y + 18
        self.origin_image = self.image
        self.angle = 0
        self.direction2 = direction2





    def move(self):
        #self.rect.x += self.velocity * self.direction2
        if self.player2.direction2 == -1:
            #self.rect.x = self.player2.rect.x - 33
            self.rect.x += self.velocity * self.player2.direction2
            for i in range(1):
                    self.rect.y += 1

            self.image = pygame.image.load('assets_2/ArrowGauche.png')
            self.image = pygame.transform.scale(self.image, (180, 100))

        else:
            self.rect.x += self.velocity
            for i in range(1):
                    self.rect.y += 1

            self.image = pygame.image.load('assets_2/Arrow.png')
            self.image = pygame.transform.scale(self.image, (180, 100))

        if self.player2.game.Oka_==True:
            for player in self.player2.game.check_collision(self, self.player2.game.all_player1_Oka):
                #self.remove()
                self.player2.all_arrow2.remove(self)
                #dégats
                player.damage(self.player2.attack)
                if self.player2.direction2 == -1 and player.rect.x > 0:
                    player.rect.x -= 30
                elif self.player2.direction2 == 1 and player.rect.x + player.rect.width < 1280:
                    player.rect.x += 30
                self.player2.cooldown2 = True
        elif self.player2.game.Ember_ == True:
            for player in self.player2.game.check_collision(self, self.player2.game.all_player1_Ember):
                #self.remove()
                self.player2.all_arrow2.remove(self)
                #dégats
                player.damage(self.player2.attack)
                if self.player2.direction2 == -1 and player.rect.x > 0:
                    player.rect.x -= 30
                elif self.player2.direction2 == 1 and player.rect.x + player.rect.width < 1280:
                    player.rect.x += 30
                self.player2.cooldown2 = True
        elif self.player2.game.Tortue_Geniale_ == True:
            for player in self.player2.game.check_collision(self, self.player2.game.all_player1_Tortue_Geniale):
                #self.remove()
                self.player2.all_arrow2.remove(self)
                #dégats
                player.damage(self.player2.attack)
                if self.player2.direction2 == -1 and player.rect.x > 0:
                    player.rect.x -= 30
                elif self.player2.direction2 == 1 and player.rect.x + player.rect.width < 1280:
                    player.rect.x += 30
                self.player2.cooldown2 = True
        elif self.player2.game.Mage_ == True:
            for player in self.player2.game.check_collision(self, self.player2.game.all_player1_Mage):
                #self.remove()
                self.player2.all_arrow2.remove(self)
                #dégats
                player.damage(self.player2.attack)
                if self.player2.direction2 == -1 and player.rect.x > 0:
                    player.rect.x -= 30
                elif self.player2.direction2 == 1 and player.rect.x + player.rect.width < 1280:
                    player.rect.x += 30
                self.player2.cooldown2 = True

        if self.player2.is_full_load_22() or self.rect.x >= 1280:
            self.player2.all_arrow2.remove(self)
            self.player2.cooldown2 = True