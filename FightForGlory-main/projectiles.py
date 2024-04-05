import pygame
import time

#classe pour projectile Player1

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player, direction):
        super().__init__()
        self.velocity = 7
        self.player = player
        self.image = pygame.image.load('assets_2/boule_de_feu.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 10
        self.rect.y = player.rect.y + 40
        self.direction = direction




    #def remove(self):
    #    self.player.all_projectile.remove(self)


    def move(self):
        if self.player.direction == -1:
            #self.rect.x = self.player.rect.x - 33
            self.rect.x += self.velocity * self.direction
            self.image = pygame.image.load('assets_2/boule_de_feu.png')
            self.image = pygame.transform.scale(self.image, (50, 50))

        else:
            self.rect.x += self.velocity

            self.image = pygame.image.load('assets_2/boule_de_feu.png')
            self.image = pygame.transform.scale(self.image, (50, 50))


        if self.player.game.Oka2_==True:
            for player2 in self.player.game.check_collision(self, self.player.game.all_player2_Oka2):
                #self.remove()
                self.player.all_projectile.remove(self)
                player2.damage(self.player.attack)
                if self.player.direction == -1 and player2.rect.x > 0:
                    player2.rect.x -= 30
                elif self.player.direction == 1 and player2.rect.x + player2.rect.width < 1280:
                    player2.rect.x += 30
                self.player.cooldown = True

        elif self.player.game.Ember2_==True:
            for player2 in self.player.game.check_collision(self, self.player.game.all_player2_Ember2):
                #self.remove()
                self.player.all_projectile.remove(self)
                player2.damage(self.player.attack)
                if self.player.direction == -1 and player2.rect.x > 0:
                    player2.rect.x -= 30
                elif self.player.direction == 1 and player2.rect.x + player2.rect.width < 1280:
                    player2.rect.x += 30
                self.player.cooldown = True
        elif self.player.game.Tortue_Geniale_2_==True:
            for player2 in self.player.game.check_collision(self, self.player.game.all_player2_Tortue_Geniale_2):
                #self.remove()
                self.player.all_projectile.remove(self)
                player2.damage(self.player.attack)
                if self.player.direction == -1 and player2.rect.x > 0:
                    player2.rect.x -= 30
                elif self.player.direction == 1 and player2.rect.x + player2.rect.width < 1280:
                    player2.rect.x += 30
                self.player.cooldown = True
        elif self.player.game.Mage2_==True:
            for player2 in self.player.game.check_collision(self, self.player.game.all_player2_Mage2):
                #self.remove()
                self.player.all_projectile.remove(self)
                player2.damage(self.player.attack)
                if self.player.direction == -1 and player2.rect.x > 0:
                    player2.rect.x -= 30
                elif self.player.direction == 1 and player2.rect.x + player2.rect.width < 1280:
                    player2.rect.x += 30
                self.player.cooldown = True

        if self.player.is_full_load_2() or self.rect.x > 1280:
            self.player.all_projectile.remove(self)
            self.player.cooldown = True






