import pygame

# Inicializando o Pygame
pygame.init()

# definindo o tamanho da janela
width, heighy = 800, 600
screen = pygame.display.set_mode((width, heighy))
pygame.display.set_caption("janela simples")


# Definindo a cor do fundo
BG_COLOR = (30, 30, 40) # cor de fundo (um tom escuro)

# Carregar a imagem 
image_file = "player.png" # coloque o nome da sua imagem 









# Loop principal do jogo 
running = True
while running:
    for evenent in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    # atualizar tela 
    pygame.display.flip()

# Finalizar o pygame 
pygame.quit()
