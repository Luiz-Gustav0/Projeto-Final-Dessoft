# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from classes import init_screen, perdeu_screen,velha,Moto,Carro1,Carro2
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
font_principal2 = pygame.font.SysFont('Bodoni', 33)
assets = {}
background = pygame.image.load('imagens/background.png').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
velha_img = pygame.image.load('imagens/velinha.png').convert_alpha()
velha_img = pygame.transform.scale(velha_img, (75, 75))
moto_img = pygame.image.load('imagens/imgem_moto.png').convert_alpha()
moto_img = pygame.transform.scale(moto_img, (75, 75))
carro1_img = pygame.image.load('imagens/Imagem_Carro_2.png').convert_alpha()
carro1_img = pygame.transform.scale(carro1_img, (125, 125))
carro2_img = pygame.image.load('imagens/imagem_carro.png').convert_alpha()
carro2_img = pygame.transform.scale(carro2_img, (115, 115))
pygame.mixer.music.load('sons/musicadefundo.mp3')
pygame.mixer.music.set_volume(0.4)
assets['velhaatropelada'] = pygame.mixer.Sound('sons/velhaatropelada.wav')

#  Estruturas inicias do jogo
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
    #Mostrando tela inicial
    while estado == 'inicial':
        estado = init_screen(window)
    #Mostrando a tela do jogo
    while estado == 'game':
        window = pygame.display.set_mode((1280,720))
        pygame.display.set_caption('Crazy Drivers!')
        todos_sprites.update()
        hits = pygame.sprite.spritecollide(velha1, todos_carros_e_motos, True, collided=pygame.sprite.collide_mask)
        # Verifica se a Velha bateu em algum carro ou moto
        if len(hits) > 0:
            #reinicia todo jogo após uma colisão
            for elemento in todos_sprites.sprites():
                elemento.kill()
            velha1 = velha(velha_img)
            carro1 = Carro1(carro1_img)
            carro3 = Carro1(carro1_img)
            carro2 = Carro2(carro2_img)
            todos_carros_e_motos.add(carro1)
            todos_carros_e_motos.add(carro2)
            todos_carros_e_motos.add(carro3)
            todos_sprites.add(carro1)
            todos_sprites.add(carro2)
            todos_sprites.add(carro3)
            todos_sprites.add(velha1)
            dificuldade = 0
            contador = 0
            assets['velhaatropelada'].play()
            estado = perdeu_screen(window)
        #criando um jeito de mudar a dificuldade a cada 5 segundos (150FPS)
        if contador % 150 == 0:
            dificuldade += 1
            moto1 = Moto(moto_img)
            todos_sprites.add(moto1)
            todos_carros_e_motos.add(moto1)
        window.fill((0, 0, 0)) 
        #Colocando um limite máximo na dificuldade
        if contador > 4500:
            contador = 4501
        #Printando a dificuldade na tela
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