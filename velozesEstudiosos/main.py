##### IFMA Velozes e Estudiosos #####
#Gênero: Corrida
#Subgênero: Corrida de esquiva ou obstáculos (Como queiram chamar!!)
#Faixa etaária: Livre
#Versão 0.1.0
#Direitos autorais: Jaelma Barbosa, Antonio Alécio, Kayo Vinícius, Narayane Chaves

#### Impletações - Parte 1 #### 
#1 - Nao permitir sair da Tela (Area Visivel);
#2 - Colisão com os obstáculos;
#3 - Implementar background (Deixo para alterações);

#Bonus# : Caso adicione 1(uma) funcionalidade fora da lista solicitada, que possua interatividade e dentro
# do escopo já estudado.  [ 1,5 pts ] 

import pygame
import random

# Aqui faço a inicialização da biblioteca Pygame
pygame.init()

# Determinei 800x600 mas vc pode aplicar a resolução que achar melhor (porém, vou fazer uma atividade em sala de upgrade)
largura_tela = 550
altura_tela = 950
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('IFMA Velozes e Estudiosos')

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)

# Aqui coloquei separado para ajustar as configurações do carro
carro_largura = 110
carro_altura = 200
dimensao_carro = (carro_largura, carro_altura)
carro = pygame.image.load('img/onibus2.png')  
carro = pygame.transform.scale(carro, (carro_largura, carro_altura))
# Aqui coloquei separado para ajustar as configurações do background
estrada = pygame.image.load('img/estrada.jpg')

# Posição inicial do carro
x = (largura_tela * 0.45)
y = (altura_tela * 0.8)

# Configurações dos obstáculos
obstaculo = pygame.image.load('img/carro2.jpg')
obstaculo_largura = 100
obstaculo_altura = 200
dimensao_obstaculo = (obstaculo_largura, obstaculo_altura)
obstaculo = pygame.transform.scale(obstaculo, (obstaculo_largura, obstaculo_altura))
# obstaculo_cor = (255, 0, 0)  # Veja que é usado o padrão RGB, não preciso entrar em detalhes, certo?
obstaculo_velocidade = 7 # Falarei disso na sala (Será também uma implementação como Atividade)
obstaculo_x = random.randrange(0, largura_tela - obstaculo_largura)
obstaculo_y = -800

# Configurações do Tomate
tomate = pygame.image.load('img/carro.png')
tomate_largura = 100
tomate_altura = 200
dimensao_tomate = (tomate_largura, tomate_altura)
tomate = pygame.transform.scale(tomate, (tomate_largura, tomate_altura))
tomate_x = random.randrange(0, largura_tela - tomate_largura)
tomate_y = -1200

# Desenhando os obstáculos [leiam a documentação para implementar aqui fiz apenas alguns esboços]
def desenha_obstaculo(x, y):
    tela.blit(obstaculo, (x, y))

# Redesenhando a tela [leiam a documentação para implementar aqui fiz apenas alguns esboços]
def redesenhar_tela():
    # tela.fill(branco)
    tela.blit(estrada, (0, 0))
    tela.blit(carro, (x, y))
    desenha_obstaculo(obstaculo_x, obstaculo_y)
    desenha_tomate(tomate_x, tomate_y)
    pygame.display.update()

def colisao(carro_x, carro_y, obstaculo_x, obstaculo_y, obstaculo_largura, obstaculo_altura, carro_largura, carro_altura):
    if carro_x < obstaculo_x + obstaculo_largura and carro_x + carro_largura > obstaculo_x and carro_y < obstaculo_y + obstaculo_altura and carro_y + carro_altura > obstaculo_y:
        return True
    return False


def exibir_mensagem():
    font = pygame.font.SysFont(None, 25)
    texto = font.render('Você perdeu!', True, (255, 0, 0))
    tela.blit(texto, [largura_tela/2, altura_tela/2])
    pygame.display.update()
    pygame.time.wait(2000)
    
def desenha_tomate(x, y):
    tela.blit(tomate, (x, y))
    
def colisao_tomate(carro_x, carro_y, tomate_x, tomate_y, tomate_largura, tomate_altura, carro_largura, carro_altura):
    if carro_x < tomate_x + tomate_largura and carro_x + carro_largura > tomate_x and carro_y < tomate_y + tomate_altura and carro_y + carro_altura > tomate_y:
        return True
    return False

def tela_vermelha():
    font = pygame.font.SysFont(None, 245)
    texto = font.render('TOMATE', True, (255, 0, 0))
    tela.blit(texto, [largura_tela/2, altura_tela/2])
    pygame.display.update()
    pygame.time.wait(2000)
    
    

# Parte principal do jogo (aqui executo a criação do loop)
jogo_ativo = True
clock = pygame.time.Clock()

while jogo_ativo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_ativo = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= 5
        if x < 0:
            x = 0
    if keys[pygame.K_RIGHT]:
        x += 5
        if x > largura_tela - carro_largura:  
            x = largura_tela - carro_largura

     #Colisão do obstaculo
    obstaculo_y += obstaculo_velocidade
    if obstaculo_y > altura_tela:
        obstaculo_y = 0 - obstaculo_altura
        obstaculo_x = random.randrange(0, largura_tela - obstaculo_largura)

    if colisao(x, y, obstaculo_x, obstaculo_y, obstaculo_largura, obstaculo_altura, carro_largura, carro_altura):
        exibir_mensagem()
        jogo_ativo = False
    
    
    #Colisão do tomate
    tomate_y += obstaculo_velocidade
    if tomate_y > altura_tela:
        tomate_y = 0 - tomate_altura
        tomate_x = random.randrange(0, largura_tela - tomate_largura)

    # if colisao_tomate(x, y, tomate_x, tomate_y, tomate_largura, tomate_altura, carro_largura, carro_altura):
        # cor_fundo = (255, 255, 255) #Cor vermelho
        # tela_vermelha()
        # pygame.time.set_timer(pygame.USEREVENT, 5000)

    redesenhar_tela()
    clock.tick(60)

pygame.quit()
