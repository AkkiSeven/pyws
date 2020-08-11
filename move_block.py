import pygame
import sys

GREEN = 0,255,0
BLACK = 0,0,0

def flip() :
    pygame.display.flip()

canvas = pygame.display.set_mode((1080, 720))


x = 160
y = 120
block = pygame.Surface((20, 20))
block.fill(GREEN)




done = False

while not done:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        if event.type is not pygame.KEYDOWN:
            continue

        if event.key == pygame.K_LEFT:
            x  -= 10
        elif event.key ==  pygame.K_RIGHT:
            x  += 10
        elif event.key ==  pygame.K_UP: 
            y  -= 10
        elif event.key ==  pygame.K_DOWN: 
            y  += 10

    canvas.fill(BLACK)
    canvas.blit(block, [x,y])
    flip()