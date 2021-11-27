import pygame
import random



# Classe para criação do personagem principal
class Ninja(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = 603
        self.rect.y = 450
        self.speedx = 0

    def update(self):
        # Atualização da posição do Ninja
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

