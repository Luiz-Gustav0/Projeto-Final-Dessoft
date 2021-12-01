# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

from pygame.constants import DOUBLEBUF

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Hello World!')

# ----- Inicia estruturas de dados
WIDTH = 1280
HEIGHT = 720
BLACK = (0, 0, 0)
game = True
dificuldade = 1
assets = {}
background = pygame.image.load('Projeto-Final-Dessoft/imagens/background.png').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
velha_img = pygame.image.load('Projeto-Final-Dessoft/imagens/velinha.png').convert_alpha()
velha_img = pygame.transform.scale(velha_img, (75, 75))
moto_img = pygame.image.load('Projeto-Final-Dessoft/imagens/imgem_moto.png').convert_alpha()
moto_img = pygame.transform.scale(moto_img, (100, 100))
carro1_img = pygame.image.load('Projeto-Final-Dessoft/imagens/Imagem_Carro_2.png').convert_alpha()
carro1_img = pygame.transform.scale(carro1_img, (150, 150))
carro2_img = pygame.image.load('Projeto-Final-Dessoft/imagens/imagem_carro.png').convert_alpha()
carro2_img = pygame.transform.scale(carro2_img, (115, 115))

# Classe para criação do personagem principal
class velha(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = velha_img
        self.rect = self.image.get_rect()
        self.rect.x = 603
        self.rect.y = 450
        self.speedx = 0
        self.speedy = 0

    def update(self):
        # Atualização da posição do Velha
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.y > 610:
            self.rect.y = 610
        if self.rect.y < 0:
            self.rect.y = 0

class Moto(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = moto_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-100)
        self.rect.y = -100
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 6)

    def update(self):
        # Atualizando a posição da moto
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se a moto passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-100)
            self.rect.y = -100
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 6)

# Classe para criação do carro 1
class Carro1(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = carro1_img
        self.rect = self.image.get_rect()
        posicoes = [-150, 1280]
        self.rect.x = random.choice(posicoes)
        if self.rect.x == -150:
            self.speedx = random.randint(2,4)
        if self.rect.x == 1280:
            self.speedx = random.randint(-3,-2)
        self.rect.y = random.randint(250,525)
        self.speedy = 0

    def update(self):
        # Atualizando a posição do carro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o carro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.right < 0 or self.rect.left > WIDTH:
            posicoes = [-150, 1280]
            self.rect.x = random.choice(posicoes)
            if self.rect.x == -150:
                self.speedx = random.randint(1,3)
            if self.rect.x == 1280:
                self.speedx = random.randint(-3,-1)
            self.rect.y = random.randint(250,525)
            self.speedy = 0

# Classe para criação do carro 2
class Carro2(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = carro2_img
        self.rect = self.image.get_rect()
        posicoes = [0, 1280]
        self.rect.y = random.choice(posicoes)
        if self.rect.y == -150:
            self.speedy = random.randint(3,4)
        if self.rect.y == 1280:
            self.speedy = random.randint(-4,-3)
        self.rect.x = random.randint(250,525)
        self.speedx = 0

    def update(self):
        # Atualizando a posição do carro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o carro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.bottom < 0 or self.rect.top > WIDTH:
            posicoes = [0, 720]
            self.rect.y = random.choice(posicoes)
            if self.rect.y == -150:
                self.speedy = random.randint(3,5)
            if self.rect.y == 1280:
                self.speedy = random.randint(-5,-3)
            self.rect.x = random.randint(250,525)
            self.speedx = 0

clock = pygame.time.Clock()
FPS = 30
todos_sprites = pygame.sprite.Group()
todos_carros_e_motos = pygame.sprite.Group()
velha1 = velha(velha_img)
moto1 = Moto(moto_img)
carro1 = Carro1(carro1_img)
carro2 = Carro2(carro2_img)
carro3 = Carro1(carro1_img)
for i in range(dificuldade):
    moto1 = Moto(moto_img)
    todos_carros_e_motos.add(moto1)
todos_carros_e_motos.add(carro1)
todos_carros_e_motos.add(carro2)
todos_carros_e_motos.add(carro3)
todos_sprites.add(carro1)
todos_sprites.add(carro2)
todos_sprites.add(carro3)
todos_sprites.add(moto1)
todos_sprites.add(velha1)

# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
    # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                velha1.speedx -= 8
            if event.key == pygame.K_RIGHT:
                velha1.speedx += 8
            if event.key == pygame.K_UP:
                velha1.speedy -= 8
            if event.key == pygame.K_DOWN:
                velha1.speedy += 8
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
        # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                velha1.speedx += 8
            if event.key == pygame.K_RIGHT:
                velha1.speedx -= 8
            if event.key == pygame.K_UP:
                velha1.speedy += 8
            if event.key == pygame.K_DOWN:
                velha1.speedy -= 8

    # ----- Gera saídas
    todos_sprites.update()
    hits = pygame.sprite.spritecollide(velha1, todos_carros_e_motos, True, collided=pygame.sprite.collide_mask)
    if len(hits) > 0:
        game = False
    if pygame.time.get_ticks() > 5000:
        dificuldade += 1
    window.fill((0, 0, 0))  # Preenche com a cor azul
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    todos_sprites.draw(window)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados