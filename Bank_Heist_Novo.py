import pygame
import os
import platform
pygame.init()
pygame.font.init()
#largura = 800
#altura = 600

largura = 1088
altura = 704
BLOCK_SIZE = 32

screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Bank Heist")

level = [
"0000000000000000000000000000000000",
"0000000000000000000000000000000000",
"0000000000000000000000000000000000",
"1111111111111111111111111111111111",
"1000000000000000000000000000000001",
"1001110010011111001111100100111001",
"1000000010000000000000000100000001",
"1110011110010011111100100111100111",
"0000000000010000000000100000000000",
"1110011001111100110011111001100111",
"1000011000000000110000000001100001",
"1001111001111100000011111001111001",
"0000000000000000110000000000000000",
"1001111111110011111100111111111001",
"1001000000000000000000000000001001",
"1000001100111111001111110011000001",
"1111001100100000000000010011001111",
"1000001100100111001110010011000001",
"1001111100100100000010010011111001",
"1000000000000000110000000000000001",
"1111111111111111111111111111111111",
"0000000000000000000000000000000000"
]

black = (0,0,0)
white = (255,255,255)
font = pygame.font.Font('freesansbold.ttf', 32)



bancos = [(14,10),(16,15)]


if platform.system() == "Windows":
    lado_direita_img = pygame.image.load('lado_direita.png')
    lado_esquerda_img = pygame.image.load('lado_esquerda.png')
    frente_img = pygame.image.load('frente.png')
    traseira_img = pygame.image.load('traseira.png')
    banco_img = pygame.image.load('banco.png')
    maze = pygame.image.load("mapa_1_grande.png")
else:
    pwd = os.path.dirname(os.path.abspath(__file__))
    lado_direita_img = pygame.image.load(pwd+'/lado_direita.png')
    lado_esquerda_img = pygame.image.load(pwd+'/lado_esquerda.png')
    frente_img = pygame.image.load(pwd+'/frente.png')
    traseira_img = pygame.image.load(pwd+'/traseira.png')
    banco_img = pygame.image.load(pwd+'/banco.png')
    maze = pygame.image.load(pwd+"/mapa_1_grande.png")


def drawLevel():
    
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == "1":
                pygame.draw.rect(screen, (160,160,52,255), (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            if level[y][x] == "0":
                pygame.draw.rect(screen, (0,0,0), (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    screen.blit(maze, (0,0))


def can_move(px, py, dx, dy):

    if px+dx >= 0 and px+dx < len(level[0]) and px+dx+1 >= 0 and px+dx+1 < len(level[0]) and py+dy >= 0 and py+dy < len(level):

        if level[py+dy][px+dx] == "0" and level[py+dy][px+dx+1] == "0":

            return True
    return False


def move(px, py, dx, dy):
    if can_move(px,py,dx,dy):
        return px+dx, py+dy
    
    if px <= 0 and (py == 12 or py == 8) and dx == -1:
        return 32, py

    if px >= 32 and (py == 12 or py == 8) and dx== 1:
        return 0, py


    return px, py

def drawPlayer(px, py, dx, dy):
    
    if dx == 0 and dy == 1:
        #sprite down
        screen.blit(frente_img, (px*BLOCK_SIZE, py*BLOCK_SIZE))
        
    elif dx == 0 and dy == -1:
        #sprite up
        screen.blit(traseira_img, (px*BLOCK_SIZE, py*BLOCK_SIZE))
    elif dx == -1 and dy == 0:
        #sprite left
        screen.blit(lado_esquerda_img, (px*BLOCK_SIZE, py*BLOCK_SIZE))
    elif dx == 1 and dy == 0:
        #sprite down
        screen.blit(lado_direita_img, (px*BLOCK_SIZE, py*BLOCK_SIZE))



def move_police(px, py, dx, dy):
    if px+dx >= 0 and px+dx < len(level[0]) and px+dx+1 >= 0 and px+dx+1 < len(level[0]) and py+dy >= 0 and py+dy < len(level):
        if level[py+dy][px+dx] == "0" and level[py+dy][px+dx+1] == "0":
            
            if px > positionX:
                return -1,py+dy

    return px, py

        
        
def drawPolice(px, py, dx, dy):
    if dx == 0 and dy == 1:
        #sprite down
        screen.blit(frente_img, (px*BLOCK_SIZE, py*BLOCK_SIZE))
    elif dx == 0 and dy == -1:
        #sprite up
        screen.blit(traseira_img, (px*BLOCK_SIZE, py*BLOCK_SIZE))
    elif dx == -1 and dy == 0:
        #sprite left
        screen.blit(lado_esquerda_img, (px*BLOCK_SIZE, py*BLOCK_SIZE))
    elif dx == 1 and dy == 0:
        #sprite down
        screen.blit(lado_direita_img, (px*BLOCK_SIZE, py*BLOCK_SIZE))
    

score = 0
def drawBancos(px,py,bancos):
    global score
    
    for value in bancos:
            
        screen.blit(banco_img, (value[0]*BLOCK_SIZE, value[1]*BLOCK_SIZE)) 
        if px == value[0] and py == value[1]:
            bancos.remove(value)
            score += 1






clock = pygame.time.Clock()
screen = pygame.display.set_mode((1088, 704), 0, 32)

surface = pygame.Surface(screen.get_size())
surface = surface.convert()

positionX=0
positionY=8

directionX=1
directionY=0


positionX_police = 23
positionY_police = 4
directionX_police = -1
directionY_police = 0


running = True
while (running):
        if directionX==0:
            clock.tick(10)
        else:
            clock.tick(15)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    running = False
                elif ev.key == pygame.K_UP and can_move(positionX,positionY,0,-1):
                    
                    directionX=0
                    directionY=-1
                elif ev.key == pygame.K_DOWN and can_move(positionX,positionY,0,1):
                    directionX=0
                    directionY=1
                elif ev.key == pygame.K_LEFT and can_move(positionX,positionY,-1,0):
                    directionX=-1
                    directionY=0
                elif ev.key == pygame.K_RIGHT and can_move(positionX,positionY,1,0):
                    directionX=1
                    directionY=0
        drawLevel()


        positionX, positionY = move(positionX, positionY, directionX, directionY)
        
        positionX_police, positionY_police = move_police(positionX_police, positionY_police, directionX_police, directionY_police)
        



        drawPlayer(positionX, positionY, directionX, directionY)

        #drawBancos(positionX, positionY, bancos)
        drawBancos(positionX, positionY, bancos)
        
        drawPolice(positionX_police, positionY_police, directionX_police, directionY_police)

        
        
        text = font.render(str(score), True, black)
        textRect = text.get_rect()
        textRect.center = (25*BLOCK_SIZE, 21.5*BLOCK_SIZE)
        screen.blit(text, textRect)

        pygame.display.update()

pygame.quit()