import pygame
import button

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu")

game_paused = False
menu_state = "main"

font = pygame.font.SysFont("JMH Laudanum CA", 40)

TEXT_COL = (255, 255, 255)

button_width = 220
button_height = 90

novojogo_img = pygame.image.load("button_novojogo.png").convert_alpha()
novojogo_img = pygame.transform.scale(novojogo_img, (button_width, button_height))

continuar_img = pygame.image.load("button_continuar.png").convert_alpha()
continuar_img = pygame.transform.scale(continuar_img, (button_width, button_height))

regras_img = pygame.image.load("button_regras.png").convert_alpha()
regras_img = pygame.transform.scale(regras_img, (button_width, button_height))

creditos_img = pygame.image.load("button_creditos.png").convert_alpha()
creditos_img = pygame.transform.scale(creditos_img, (button_width, button_height))

opcoes_img = pygame.image.load("button_opcoes.png").convert_alpha()
opcoes_img = pygame.transform.scale(opcoes_img, (button_width, button_height))

sair_img = pygame.image.load("button_sair.png").convert_alpha()
sair_img = pygame.transform.scale(sair_img, (button_width, button_height))

voltar_img = pygame.image.load("button_voltar.png").convert_alpha()
voltar_img = pygame.transform.scale(voltar_img, (button_width, button_height))

novojogo_button = button.Button(SCREEN_WIDTH/2 - button_width/2, 150, novojogo_img, 1)
continuar_button = button.Button(SCREEN_WIDTH/2 - button_width/2, 200, continuar_img, 1)
regras_button = button.Button(SCREEN_WIDTH/2 - button_width/2, 250, regras_img, 1)
creditos_button = button.Button(SCREEN_WIDTH/2 - button_width/2, 300, creditos_img, 1)
opcoes_button = button.Button(SCREEN_WIDTH/2 - button_width/2, 350, opcoes_img, 1)
sair_button = button.Button(SCREEN_WIDTH/2 - button_width/2, 400, sair_img, 1)
voltar_button = button.Button(SCREEN_WIDTH/2 - button_width/2, 450, voltar_img, 1)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

run = True
while run:
    screen.fill((184, 134, 11))

    if game_paused:
        if menu_state == "main":
            novojogo_button.draw(screen)
            continuar_button.draw(screen)
            opcoes_button.draw(screen)
            regras_button.draw(screen)
            sair_button.draw(screen)
            creditos_button.draw(screen)
        
            if continuar_button.clicked:
                game_paused = False

        if sair_button.clicked:
            run = False

    else:
        draw_text("Clique na barra de espaço para pausar", font, TEXT_COL, 160, 250)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
