import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

#declara informação sobre sistema de pontuação do jogo
pontos = 0

#declarando informações da tela
altura_tela = int(500)
largura_tela = int(500)

#declarando tamanho da cobrinha e a maçã
altura_cobra = 15
largura_cobra = 15
altura_maca = 15
largura_maca = 15

#declara a posição dos objetos criados
posicao_x_cobra = posicao_y_cobra = 10
posicao_x_maca = 250
posicao_y_maca = 257
fator = 0.4

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobrinha')

while True:
    tela.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            exit()

    cobra = pygame.draw.rect(tela, (0, 255, 00), (posicao_x_cobra , posicao_y_cobra, altura_cobra, largura_cobra))
    maca = pygame.draw.rect(tela, (255, 0, 0), (posicao_x_maca, posicao_y_maca, altura_maca, largura_maca))

    if pygame.key.get_pressed()[K_a]:
        posicao_x_cobra -= fator
    elif pygame.key.get_pressed()[K_d]:
        posicao_x_cobra += fator
    elif pygame.key.get_pressed()[K_w]:
        posicao_y_cobra -= fator
    elif pygame.key.get_pressed()[K_s]:
        posicao_y_cobra += fator
    
    if cobra.colliderect(maca):
        posicao_x_maca = randint(0, largura_tela-largura_maca)
        posicao_y_maca = randint(0, altura_tela-altura_maca)
        pontos += 1
        largura_cobra += 15

    pygame.display.update()