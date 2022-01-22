from signal import valid_signals
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

font = pygame.font.Font('freesansbold.ttf', 32)



bancos = [(14,10),(16,15),(18,19)]


if platform.system() == "Windows":
    lado_direita_img = pygame.image.load('lado_direita.png')
    lado_esquerda_img = pygame.image.load('lado_esquerda.png')
    frente_img = pygame.image.load('frente.png')
    traseira_img = pygame.image.load('traseira.png')
    lado_direita_policia_img = pygame.image.load('lado_direita_policia.png')
    lado_esquerda_policia_img = pygame.image.load('lado_esquerda_policia.png')
    frente_policia_img = pygame.image.load('frente_policia.png')
    traseira_policia_img = pygame.image.load('traseira_policia.png')
    banco_img = pygame.image.load('banco.png')
    maze = pygame.image.load("mapa_1_grande.png")
else:
    pwd = os.path.dirname(os.path.abspath(__file__))
    lado_direita_img = pygame.image.load(pwd+'/lado_direita.png')
    lado_esquerda_img = pygame.image.load(pwd+'/lado_esquerda.png')
    frente_img = pygame.image.load(pwd+'/frente.png')
    traseira_img = pygame.image.load(pwd+'/traseira.png')
    lado_direita_policia_img = pygame.image.load(pwd+'/lado_direita_policia.png')
    lado_esquerda_policia_img = pygame.image.load(pwd+'/lado_esquerda_policia.png')
    frente_policia_img = pygame.image.load(pwd+'/frente_policia.png')
    traseira_policia_img = pygame.image.load(pwd+'/traseira_policia.png')
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


def movePolice(px_police,py_police,dx_police,dy_police,px_carro, py_carro):
    #direita
    if px_police < px_carro and can_move(px_police,py_police,1, 0):
        dx_police = 1
        dy_police = 0
        return px_police+1,py_police,dx_police,dy_police

    #esquerda
    if px_police > px_carro and can_move(px_police,py_police,-1, 0):
        dx_police = -1
        dy_police = 0
        return px_police-1,py_police,dx_police,dy_police

    #baixo
    if py_police < py_carro and can_move(px_police,py_police,0, 1):
        dx_police = 0
        dy_police = 1
        return px_police,py_police+1,dx_police,dy_police

    #cima
    if py_police > py_carro and can_move(px_police,py_police,0, -1):
        dx_police = 0
        dy_police = -1
        return px_police,py_police-1,dx_police,dy_police

    # #x = x
    # elif px_carro == px_police:
    #     #vai cima
    #     if can_move(px_police,py_police,0, -1):
    #         dx_police = 0
    #         dy_police = -1
    #         return px_police,py_police-1,dx_police,dy_police
    
    #     #vai baixo
    #     if can_move(px_police,py_police,0, 1):
    #         dx_police = 0
    #         dy_police = 1
    #         return px_police,py_police+1,dx_police,dy_police


    #     #agora ve se vale a pena ir pela esquerda ou pela direita
    #     #tenta ver depois tipo ves o dx do carro normal,se for 1 fazes pela direita 

    #     else:
    #         return px_police,py_police, dx_police, dy_police

    # elif py_carro == py_police:
    #     #vai direita
    #     if px_police < px_carro and can_move(px_police,py_police,1, 0):
    #         dx_police = 1
    #         dy_police = 0
    #         return px_police+1,py_police,dx_police,dy_police

    #     #vai esquerda
    #     if px_police > px_carro and can_move(px_police,py_police,-1, 0):
    #         dx_police = -1
    #         dy_police = 0
    #         return px_police-1,py_police,dx_police,dy_police

    #     else:
    #         return px_police,py_police,dx_police,dy_police


    
    else:
    
        #ficar parado
        #return px_police,py_police,dx_police,dy_police

        #andar mas por cima das cenas
        return px_police+dx_police,py_police+dy_police, dx_police, dy_police

def drawPolice(px,py,dx,dy):
      
    if dx == 0 and dy == 1:
        #sprite down
        screen.blit(frente_policia_img, (px*BLOCK_SIZE, py*BLOCK_SIZE))
        
    elif dx == 0 and dy == -1:
        #sprite up
        screen.blit(traseira_policia_img, (px*BLOCK_SIZE, py*BLOCK_SIZE))
    elif dx == -1 and dy == 0:
        #sprite left
        screen.blit(lado_esquerda_policia_img, (px*BLOCK_SIZE, py*BLOCK_SIZE))
    elif dx == 1 and dy == 0:
        #sprite down
        screen.blit(lado_direita_policia_img, (px*BLOCK_SIZE, py*BLOCK_SIZE))
    else:
        screen.blit(lado_direita_policia_img, (px*BLOCK_SIZE, py*BLOCK_SIZE))


def collideX(px_carro,py_carro, px_police, py_police):

    if px_carro == px_police or px_carro == px_police + 1 or px_carro+1 == px_police or px_carro == px_police+1:
        return True

def collideY(px_carro,py_carro, px_police, py_police):

    if py_carro == py_police:
        return True
vidas = 4
def collide(px_carro,py_carro,dx_carro, dy_carro,px_police, py_police, dx_police, dy_police):
    global vidas
    global running
    
    if collideX(px_carro,py_carro, px_police, py_police) and collideY(px_carro,py_carro, px_police, py_police):


        px_carro=0
        py_carro=8

        dx_carro=1
        dy_carro=0

        px_police = 31
        py_police = 4

        dx_police = -1
        dy_police = 0
        nascer_policia = True
        vidas -= 1
        if vidas == 0:
            running = False
    return px_carro,py_carro,dx_carro,dy_carro, px_police, py_police, dx_police, dy_police

 

score = 0
def drawBancos(px,py,bancos):
    global score
    
    for value in bancos:
            
        screen.blit(banco_img, (value[0]*BLOCK_SIZE, value[1]*BLOCK_SIZE)) 
        if px == value[0] and py == value[1]:
            valores.append(value)
            global nascer_policia
            nascer_policia = True
            bancos.remove(value)
            score += 10



def drawScore():
    text = font.render(str(score), True, black)
    textRect = text.get_rect()
    textRect.center = (25*BLOCK_SIZE, 21.5*BLOCK_SIZE)
    screen.blit(text, textRect)


clock = pygame.time.Clock()
screen = pygame.display.set_mode((1088, 704), 0, 32)

surface = pygame.Surface(screen.get_size())
surface = surface.convert()

positionX=0
positionY=8

directionX=1
directionY=0

px_police = 31
py_police = 4

dx_police = -1
dy_police = 0

valores = []

nascer_policia = False
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
        drawBancos(positionX, positionY, bancos)
        
        px_police, py_police, dx_police, dy_police = movePolice(px_police, py_police, dx_police, dx_police,positionX,positionY)

        positionX,positionY,directionX,directionY, px_police, py_police, dx_police, dy_police = collide(positionX, positionY, directionX, directionY, px_police, py_police, dx_police, dy_police)

        drawPlayer(positionX, positionY, directionX, directionY)

        drawPolice(px_police, py_police, dx_police, dy_police)
        print(valores)
        if nascer_policia:
            for i in range(len(valores)):
                drawPolice(valores[i][0],valores[i][1],0,-1)

        
        drawScore()

        pygame.display.update()

pygame.quit()