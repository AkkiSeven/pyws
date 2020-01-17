import pygame
import os
import sys

def __main__():
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



BLACK = (0, 0, 0)
WHITE = (255, 255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255) 

canvas = pygame.display.set_mode([500,600])
canvas.fill(GREEN)
pygame.display.flip()


red_block = pygame.Surface([50,20])

red_block.fill(RED)

canvas.blit(red_block, [10,10])

pygame.display.flip()













__main__()



