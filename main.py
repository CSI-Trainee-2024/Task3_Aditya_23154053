import pygame


pygame.init()


screen = pygame.display.set_mode((800, 600))


pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)


playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
    screen.blit(playerImg, (x,y))



running = True
while running:


    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


<<<<<<< HEAD


    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

=======
    playerX += playerX_change
>>>>>>> 2ab43d53123c2a04a5ee5821a0f352559ba00dfe
    player(playerX, playerY)
    pygame.display.update()
