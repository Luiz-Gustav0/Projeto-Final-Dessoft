# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

from pygame.constants import DOUBLEBUF

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Crazy Drivers!')

# ----- Inicia estruturas de dados
WIDTH = 1280
HEIGHT = 720
BLACK = (0, 0, 0)
game = True
dificuldade = 0
font = pygame.font.SysFont('impact', 48)
font_principal = pygame.font.SysFont('Bodoni', 48)
assets = {}
background = pygame.image.load('Projeto-Final-Dessoft/imagens/background.png').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
velha_img = pygame.image.load('Projeto-Final-Dessoft/imagens/velinha.png').convert_alpha()
velha_img = pygame.transform.scale(velha_img, (75, 75))
moto_img = pygame.image.load('Projeto-Final-Dessoft/imagens/imgem_moto.png').convert_alpha()
moto_img = pygame.transform.scale(moto_img, (75, 75))
carro1_img = pygame.image.load('Projeto-Final-Dessoft/imagens/Imagem_Carro_2.png').convert_alpha()
carro1_img = pygame.transform.scale(carro1_img, (125, 125))
carro2_img = pygame.image.load('Projeto-Final-Dessoft/imagens/imagem_carro.png').convert_alpha()
carro2_img = pygame.transform.scale(carro2_img, (115, 115))
pygame.mixer.music.load('Projeto-Final-Dessoft/sons/musicadefundo.mp3')
pygame.mixer.music.set_volume(0.4)
assets['velhaatropelada'] = pygame.mixer.Sound('Projeto-Final-Dessoft/sons/velhaatropelada.mp3')

def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    window.fill((0, 0, 0))
    welcome = font_principal.render('Welcome to Crazy Drivers!', True, (255, 0, 0))
    desejajogar = font_principal.render('Aperte ENTER para iniciar!', True, (255, 0, 0))
    window.blit(velha_img,(640, 500))
    window.blit(welcome,(100, 300))
    window.blit(desejajogar, (100, 400))
    
    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                estado = 'sair'
                running = False

            if event.type == pygame.KEYUP:
                estado = 'game'
                if event.key == pygame.K_RETURN:
                    estado = 'game'
                    running = False


        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return estado

def perdeu_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    textoperdeu = font_principal.render('Voce perdeu!', True, (255, 0, 0))
    querjogardnv = font_principal.render('Aperte qualquer tecla para jogar novamente!', True, (255, 0, 0))
    window.blit(background, (0, 0))
    window.blit(textoperdeu, (100, 300))
    window.blit(querjogardnv, (100, 400))

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    estado = init_screen(window)
                    running = False


        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    return estado

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
        if self.rect.right > 860:
            self.rect.right = 860
        if self.rect.left < 360:
            self.rect.left = 360
        if self.rect.y > 630:
            self.rect.y = 630
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
        posicoes = [0, 1280]
        self.rect.x = random.choice(posicoes)
        if self.rect.x == 0:
            self.speedx = random.randint(5,6)
        if self.rect.x == 1280:
            self.speedx = random.randint(-6,-5)
        self.rect.y = random.randint(50,100)
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
                self.speedx = random.randint(5,6)
            if self.rect.x == 1280:
                self.speedx = random.randint(-6,-5)
            self.rect.y = random.randint(250,525)
            self.speedy = 0

# Classe para criação do carro 2
class Carro2(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = carro2_img
        self.rect = self.image.get_rect()
        posicao = random.choice([[0, random.randint(3,4)],[HEIGHT, random.randint(-4,-3)]])
        self.rect.y = posicao[0]
        self.speedy = posicao[1]
        self.rect.x = random.randint(400,700)
        self.speedx = 0

    def update(self):
        # Atualizando a posição do carro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o carro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.bottom < 0 or self.rect.top > HEIGHT:
            posicao = random.choice([[0, random.randint(3,4)],[HEIGHT, random.randint(-4,-3)]])
            self.rect.y = posicao[0]
            self.speedy = posicao[1]
            self.rect.x = random.randint(400,700)
            self.speedx = 0

clock = pygame.time.Clock()
FPS = 30
todos_sprites = pygame.sprite.Group()
todos_carros_e_motos = pygame.sprite.Group()
velha1 = velha(velha_img)
moto1 = Moto(moto_img)
carro1 = Carro1(carro1_img)
carro3 = Carro1(carro1_img)
carro2 = Carro2(carro2_img)
todos_carros_e_motos.add(carro1)
todos_carros_e_motos.add(carro2)
todos_carros_e_motos.add(carro3)
todos_carros_e_motos.add(moto1)
todos_sprites.add(moto1)
todos_sprites.add(carro1)
todos_sprites.add(carro2)
todos_sprites.add(carro3)
todos_sprites.add(velha1)

# ===== Loop principal =====
contador = 0
estado = 'inicial'
while estado != 'sair':
    while estado == 'inicial':
        estado = init_screen(window)
    while estado == 'game':
        window = pygame.display.set_mode((1280,720))
        pygame.display.set_caption('Crazy Drivers!')
        todos_sprites.update()
        hits = pygame.sprite.spritecollide(velha1, todos_carros_e_motos, True, collided=pygame.sprite.collide_mask)
        if len(hits) > 0:
            assets['velhaatropelada'].play()
            estado = perdeu_screen(window)
        if contador % 300 == 0:
            dificuldade += 1
            moto1 = Moto(moto_img)
            todos_sprites.add(moto1)
            todos_carros_e_motos.add(moto1)
        window.fill((0, 0, 0)) 
        if contador > 3000:
            contador = 3001
        window.blit(background, (0, 0))
        dificuldades = 'Dificuldade: {}'.format(dificuldade)
        texto = font.render(dificuldades, True, (255, 0, 0))
        window.blit(texto, (100, 100))
        todos_sprites.draw(window)

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
        contador += 1
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                pygame.quit()
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
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados