# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Hello World!')

# ----- Inicia estruturas de dados
WIDTH = 1280
HEIGHT = 720
BLACK = (0, 0, 0)
game = True
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

clock = pygame.time.Clock()
FPS = 30
all_sprites = pygame.sprite.Group()
velha1 = velha(velha_img)
all_sprites.add(velha1)

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
    # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                velha1.speedx -= 1
            if event.key == pygame.K_RIGHT:
                velha1.speedx += 1
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
        # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                velha1.speedx += 1
            if event.key == pygame.K_RIGHT:
                velha1.speedx -= 1

    # ----- Gera saídas
    all_sprites.update()
    window.fill((0, 0, 0))  # Preenche com a cor azul
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    window.blit(moto_img, (0, 0))
    window.blit(carro1_img, (150, 0))
    window.blit(carro2_img, (300, 0))
    all_sprites.draw(window)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados