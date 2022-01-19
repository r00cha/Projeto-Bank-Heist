import pygame

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




pygame.init()

maze = pygame.image.load("mapa_1_grande.png")
pygame.transform.scale(maze, (largura,altura))


lado_direita_img = pygame.image.load('lado_direita.png')
lado_esquerda_img = pygame.image.load('lado_esquerda.png')
frente_img = pygame.image.load('frente.png')
traseira_img = pygame.image.load('traseira.png')

walls = []

carro_x = 0
carro_y = 8*32

carro_vx = 0
carro_vy = 0




left_key = right_key = up_key = down_key = False
up_key = down_key
running = True
clock = pygame.time.Clock()






for row in range(0, len(level)):
    for col in range(0, len(level[row])):
        if level[row][col] == '1':
            walls.append((row*32,col*32))
            








while running:
    # 1. lidar com eventos (teclado)
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
            
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                running = False
                
            elif ev.key == pygame.K_LEFT:
                left_key = True
                
            elif ev.key == pygame.K_RIGHT:
                right_key = True
                
            elif ev.key == pygame.K_UP:
                up_key = True
            
            elif ev.key == pygame.K_DOWN:
                down_key = True
                
      #  elif ev.type == pygame.KEYUP:
       #       if ev.key == pygame.K_LEFT:
        #        left_key = False
                
         #     elif ev.key == pygame.K_RIGHT:
          #      right_key = False
           #   elif ev.key == pygame.K_UP:
            #    up_key = False
            #  elif ev.key == pygame.K_DOWN:
             #    down_key = False
        
    
    
    # 2. logica do jogo (fisica, etc)
    dt = clock.tick()
    
    if left_key:
        carro_vx = -0.2
        carro_vy = 0

    elif right_key:
        carro_vx = +0.2
        carro_vy = 0

        
    if up_key:
        carro_vy = -0.15
        carro_vx = 0
    elif down_key:
        carro_vy = +0.15
        carro_vx = 0

    
    carro_x += carro_vx*dt
    carro_y += carro_vy*dt
    

    if carro_x > largura-64 and ((carro_y > 7*32 and carro_y < 9*32) or (carro_y >= 11*32 and carro_y <= 13*32) ):
        carro_x = 0
        
    elif carro_x > largura-64:
        carro_x = largura-64
        
    if carro_x < 0 and ((carro_y > 7.*32 and carro_y < 9*32) or (carro_y >= 11*32 and carro_y <= 13*32) ):
        carro_x = largura-64
        
    elif carro_x < 0:
        carro_x = 0
   
    if carro_y > altura-32:
        carro_y = altura-32
  
    if carro_y < 0:
        carro_y = 0
        
    
    # 3. desenhar no ecra
    screen.fill("black")

    screen.blit(maze, (0,0))
    
    
    
    #desenhar o mapa com matrizes    
    for row in range(0, len(level)):
        for col in range(0, len(level[row])):
            if level[row][col] == '1':
                pygame.draw.rect(screen, pygame.Color(160,160,52,255), (col*BLOCK_SIZE, row*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    
    
    #linhas verticais
    for x in range(largura//32):
        pygame.draw.line(screen, "grey", (x*32,0),(x*32,altura))
    #linhas horizontais 
    for x in range(altura//32):
        pygame.draw.line(screen, "grey", (0,x*32),(largura,x*32))
    
    

    for y_ind, linha in enumerate(level):
        for x_ind, char in enumerate(level):
            if char == "1":
                print(char)
                walls.append(x_ind*32,y_ind*32)


    
    


    
    if right_key:
        screen.blit(lado_direita_img, (int(carro_x), int(carro_y)))
   
    if left_key:
       screen.blit(lado_esquerda_img, (int(carro_x), int(carro_y)))
     
    if down_key:
       screen.blit(frente_img, (int(carro_x), int(carro_y)))
    if up_key:
       screen.blit(traseira_img, (int(carro_x), int(carro_y)))

    pygame.display.flip()
    
     
     

pygame.quit()