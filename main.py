import pygame
import sys
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 600
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pokemon battle')
white = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0,0,0)
vida_maxima = 394

hpAlak = 394
ataqueAlak = 105
defesaAlak = 126
spaataqueAlak = 369
spdefenseAlak = 226
velocidadeAlak = 339 
habilidadeAlak = "Syncronize"

hpArc = 394
ataqueArc = 319
defesaArc = 196
spataqueArc = 236
spdefenseArc = 196
velocidadeArc = 219
habilidadeArc = "Intimidate"

imagem_fundo = pygame.image.load('fotos/battlescene.png').convert_alpha()
imagem_fundo = pygame.transform.scale(imagem_fundo, (WIDTH, HEIGHT))

class Pokemon(pygame.sprite.Sprite):
    def __init__(self, image_path, max_health, position, ataque, defesa, spataque, spdefense):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.image = pygame.transform.scale(self.image, (self.rect.width * 3, self.rect.height * 3))
        self.max_health = max_health
        self.health = max_health
        self.ataque = ataque
        self.defesa = defesa
        self.spataque = spataque
        self.spdefense = spdefense

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

def draw_health_bar(surface, x, y, health, max_health):
    bar_width = 200
    bar_height = 20
    font = pygame.font.Font(None, 24)
    text_surface = font.render(f"{health}/{max_health}", True, BLACK)
    text_rect = text_surface.get_rect(center=(x + 30 , y + 10))  # Posição acima da barra de vida
    
       
    fill = (health / max_health) * bar_width
    border_rect = pygame.Rect(x, y, bar_width, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(surface, RED, border_rect)
    pygame.draw.rect(surface, GREEN, fill_rect)
    surface.blit(text_surface, text_rect)
def execute_attack(atacante, atacado, ataque):
    damage1 = 0
    hpAlak = 394
    ataqueAlak = 105
    defesaAlak = 126
    spaataqueAlak = 369
    spdefenseAlak = 226
    velocidadeAlak = 339 
    habilidadeAlak = "Syncronize"
     
    hpArc = 394
    ataqueArc = 319
    defesaArc = 196
    spataqueArc = 236
    spdefenseArc = 196
    velocidadeArc = 219
    habilidadeArc = "Intimidate"
    
    if ataque == "Shadow Ball":
        damage = int((((2 * 100 / 5 + 2) * atacante.spataque * 80 / atacado.spdefense) / 50) + 2) * 1 * 1
    elif ataque == "Psychic":
        damage = int((((2 * 100 / 5 + 2) * atacante.spataque * 90 / atacado.spdefense) / 50) + 2) * 1 * 1
    elif ataque == "Energy Ball":
        damage = int((((2 * 100 / 5 + 2) * atacante.spataque * 90 / atacado.spdefense) / 50) + 2) * 1 * 0.5 * 1
    elif ataque == "Calm Mind" or ataque == "Agility":
        damage = 0
    elif ataque == "Crunch":
        damage = int((((2 * 100 / 5 + 2) * atacante.ataque * 80 / atacado.defesa) / 50) + 2) * 1 * 2 * 1
        print(f"Super Efetivo")

    elif ataque == "Outrage":
        damage = int((((2 * 100 / 5 + 2) * atacante.ataque * 120 / atacado.defesa) / 50) + 2) * 1 * 1


    elif ataque == "Flare Blitz": 
        damage = int((((2 * 100 / 5 + 2) * atacante.ataque * 120 / atacado.defesa) / 50) + 2) * 1 * 1
        damage1 = atacante.max_health * (33/100)
    
    
    
    atacado.take_damage(damage) #ARC DANO
    atacante.take_damage(damage1)#Alak DANO
    print(f"{atacante.__class__.__name__} causou {damage} de dano a {atacado.__class__.__name__} com {ataque}.")
    print(f"{damage} {damage1}")
fonte = pygame.font.Font(None, 40)
fonte_button = pygame.font.Font(None, 24)

def draw_buttons(surface, buttons):
    for button in buttons:
        pygame.draw.rect(surface, button.color, button.rect)
        text_surface = fonte_button.render(button.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=button.rect.center)
        surface.blit(text_surface, text_rect)

class Button:
    def __init__(self, x, y, width, height, color, text, ataque):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.ataque = ataque

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = fonte_button.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event, atacante, atacado):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                execute_attack(atacante, atacado, self.ataque)

buttons_alakazam = [
    Button(400, 450, 98, 30, (128, 128, 128), "Shadow Ball", "Shadow Ball"),
    Button(520, 450, 98, 30, (128, 128, 128), "Calm Mind", "Calm Mind"),
    Button(400, 500, 98, 30, (128, 128, 128), "Energy Ball", "Energy Ball"),
    Button(520, 500, 98, 30, (128, 128, 128), "Psychic", "Psychic")
]

buttons_arcanine = [
    Button(465, 50, 98, 30, (128, 128, 128), "Agility", "Agility"),
    Button(465, 90, 98, 30, (128, 128, 128), "Crunch", "Crunch"),
    Button(580, 50, 98, 30, (128, 128, 128), "Flare Blitz", "Flare Blitz"),
    Button(580, 90, 98, 30, (128, 128, 128), "Outrage", "Outrage")
]

arcanine = Pokemon('fotos/arcanine.png', max_health=394, position=(450, 150), ataque=319, defesa=196, spataque=236, spdefense=196)
alakazam = Pokemon('fotos/alakazam.png', max_health=394, position=(100, 320), ataque=105, defesa=126, spataque=369, spdefense=226)
ataques = ["Shadow Ball", "Calm Mind", "Energy Ball", "Psychic", "Agility", "Crunch", "Flare Blitz", "Outrage"]

round_inicial = 1
rounds = 1
mensagem = f"Round {rounds}"
text_font = pygame.font.SysFont('Arial', 24, True, True)
text_format = text_font.render(mensagem, True, BLACK)
text_rect = text_format.get_rect()
alakazam_atacou = False
arcanine_atacou = False



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botão esquerdo do mouse
                for button in buttons_alakazam + buttons_arcanine:
                    if button.rect.collidepoint(event.pos):
                        if button.ataque in ataques:
                            if button in buttons_alakazam:
                                execute_attack(alakazam, arcanine, button.ataque)
                                atacando = alakazam
                                alakazam_atacou = True
                            elif button in buttons_arcanine:
                                execute_attack(arcanine, alakazam, button.ataque)
                                atacando = arcanine
                                arcanine_atacou = True
                                if alakazam_atacou == True and arcanine_atacou == True:
                                  round_inicial += 1
                                  rounds = round_inicial  # Incrementando o número do round aqui
                                  print(f"Round :{rounds}")

    if alakazam.health <= 0 or arcanine.health <= 0:
        running = False

    tela.fill(white)
    tela.blit(imagem_fundo, (0, 0))
    tela.blit(alakazam.image, alakazam.rect)
    tela.blit(arcanine.image, arcanine.rect)
    draw_health_bar(tela, 150, 320, alakazam.health, vida_maxima,)
    draw_health_bar(tela, 475, 160, arcanine.health, vida_maxima,)

    draw_buttons(tela, buttons_alakazam)
    draw_buttons(tela, buttons_arcanine)
    text_format = text_font.render(f'Round: {rounds}', True, BLACK)
    tela.blit(text_format, (20, 15))

    pygame.display.flip()

pygame.quit()
sys.exit()