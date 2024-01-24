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
pygame.mixer.init()

#Som
som_perdeu = pygame.mixer.Sound('sound/perdeu.mp3')
# Aqui coloquei separado para ajustar as configurações do background
estrada = pygame.image.load('img/estrada.jpg')

# Determinei 800x600 mas vc pode aplicar a resolução que achar melhor (porém, vou fazer uma atividade em sala de upgrade)
largura_tela = 550
altura_tela = 950
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('IFMA Velozes e Estudiosos')

# Aqui coloquei separado para ajustar as configurações do carro
carro_largura = 100
carro_altura = 150
carro = pygame.image.load('img/carro.png')  
carro = pygame.transform.scale(carro, (carro_largura, carro_altura))

# Posição inicial do carro
x = (largura_tela * 0.45)
y = (altura_tela * 0.8)

# Obstáculo
obstaculo = pygame.image.load('img/obstaculo.png')
obstaculo_largura = 100
obstaculo_altura = 150
obstaculo = pygame.transform.scale(obstaculo, (obstaculo_largura, obstaculo_altura))
obstaculo_velocidade = 7 # Falarei disso na sala (Será também uma implementação como Atividade)
obstaculo_x = random.randrange(0, largura_tela - obstaculo_largura)
obstaculo_y = -800
contador_obstaculo = 0

# Coração
coracao_altura = 50
coracao_largura = 50
coracao = pygame.image.load('img/coracao.png')
coracao = pygame.transform.scale(coracao, (coracao_largura, coracao_altura))
coracao_x = random.randrange(0, largura_tela - coracao_largura)
coracao_y = -1200
coracao_velocidade = 6
qtd_coracao = 1
contador_rodadas_coracao = 0

# Exibindo a mensagens
def exibir_mensagem_perdeu():
    font = pygame.font.SysFont(None, 70)
    texto = font.render('Você perdeu!', True, (255, 0, 0))
    tela.blit(texto, [largura_tela/4, altura_tela/2])
    som_perdeu.play()
    pygame.time.wait(2500)
    pygame.display.update()
    pygame.time.wait(2000)

def exibir_mensagem_velocidade(nova_velocidade):
    font = pygame.font.SysFont(None, 50)
    texto = font.render('Velocidade Aumentada: ' + str(nova_velocidade),True, (255, 0, 0))
    tela.blit(texto, [largura_tela/6, altura_tela/2])
    pygame.display.update()
    pygame.time.wait(1000)

# Desenhando os obstáculos [leiam a documentação para implementar aqui fiz apenas alguns esboços]
def desenha_obstaculo(x, y):
    tela.blit(obstaculo, (x, y))

# Redesenhando a tela [leiam a documentação para implementar aqui fiz apenas alguns esboços]
y_estrada1 = 0
y_estrada2 = -altura_tela

def redesenhar_tela():
    global y_estrada1, y_estrada2

    tela.blit(estrada, (0, y_estrada1))
    tela.blit(estrada, (0, y_estrada2))

    y_estrada1 += obstaculo_velocidade
    y_estrada2 += obstaculo_velocidade

    # Movendo a imagem da estrada para o topo
    if y_estrada1 > altura_tela:
        y_estrada1 = -altura_tela

    if y_estrada2 > altura_tela:
        y_estrada2 = -altura_tela

    # print("Redesenrando a tela ", obstaculo_y)
    tela.blit(carro, (x, y))
    desenha_obstaculo(obstaculo_x, obstaculo_y)
    desenha_coracoes(qtd_coracao)
    tela.blit(coracao, (coracao_x, coracao_y))
    pygame.display.update()

def colisao_coracao(carro_x, carro_y, coracao_x, coracao_y, coracao_largura, coracao_altura, carro_largura, carro_altura):
    global qtd_coracao

    if carro_x < (coracao_x + coracao_largura) and  coracao_x < (carro_x + carro_largura):
        if carro_y < (coracao_y + coracao_altura) and coracao_y < (carro_y + carro_altura):
            return True
    return False

tempo_ultima_colisao = 0
tempo_entre_colisoes = 1000

def colisao_obstaculo(carro_x, carro_y, obstaculo_x, obstaculo_y, obstaculo_largura, obstaculo_altura, carro_largura, carro_altura):
    global qtd_coracao, tempo_ultima_colisao

    if pygame.time.get_ticks() - tempo_ultima_colisao < tempo_entre_colisoes:
        return False

    if carro_x < (obstaculo_x + obstaculo_largura) and  obstaculo_x < (carro_x + carro_largura):
        if carro_y < (obstaculo_y + obstaculo_altura) and obstaculo_y < (carro_y + carro_altura):
            if qtd_coracao > 0:
                qtd_coracao -= 1

                tempo_ultima_colisao = pygame.time.get_ticks()
                obstaculo_y = 0 - obstaculo_altura
                obstaculo_x = random.randrange(0, largura_tela - obstaculo_largura)
                return False
            return True
    return False

def desenha_coracoes(qtd_coracao):
    for i in range(qtd_coracao):
        tela.blit(coracao, (10 + i * 40, 10))

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

    obstaculo_y += obstaculo_velocidade
    coracao_y += coracao_velocidade
    # print("Vidas ", qtd_coracao)
    # print("Velocidade ",obstaculo_velocidade)
    # print("Contador ",contador_obstaculo)
    # print("Rodada ", contador_rodadas)

    if obstaculo_y > altura_tela:
        obstaculo_y = 0 - obstaculo_altura
        obstaculo_x = random.randrange(0, largura_tela - obstaculo_largura)
        contador_obstaculo += 1
        contador_rodadas_coracao += 1
    
        if contador_obstaculo == 3 and obstaculo_velocidade < 10:
            obstaculo_velocidade += 1
            contador_obstaculo = 0
            exibir_mensagem_velocidade(obstaculo_velocidade)
        
    if contador_rodadas_coracao % 5 == 0:
        coracao_y= -altura_tela
        coracao_x = random.randrange(0, largura_tela - coracao_largura)

    if coracao_y < altura_tela:
        tela.blit(coracao, (coracao_x, coracao_y))

        if colisao_coracao(x, y, coracao_x, coracao_y, coracao_largura, coracao_altura, carro_largura, carro_altura):
            coracao_y = altura_tela

            if qtd_coracao < 3:
                qtd_coracao += 1
            contador_rodadas_coracao += 0

    if colisao_obstaculo(x, y, obstaculo_x, obstaculo_y, obstaculo_largura, obstaculo_altura, carro_largura, carro_altura):
        
        if qtd_coracao == 0:
            print("Perdeu Sem Vidas")
            exibir_mensagem_perdeu()
            jogo_ativo = False

    redesenhar_tela()
    clock.tick(60)

pygame.quit()
