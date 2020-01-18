import pygame
import sys

RED = 255,0,0
GREEN = 0,255,0
BLUE = 0,0,255
WHITE = 255,255,255
BLACK = 0,0,0
PURPLE = 128,0,128
GOLD	=	(255,215,0)
KHAKI	=	(240,230,140)
OLIVE	=	(128,128,0)
YELLOW	=	(255,255,0)
SILVER	=	(192,192,192)

canvas = pygame.display.set_mode([1080,720])



done = False

while not done:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        if event.type is not pygame.KEYDOWN:
            continue
        
        if event.key == pygame.K_r:
            canvas.fill(RED)

        if event.key == pygame.K_g:
            canvas.fill(GREEN)

        if event.key == pygame.K_b:
            canvas.fill(BLUE)

        if event.key == pygame.K_w:
            canvas.fill(WHITE)

        if event.key == pygame.K_p:
            canvas.fill(PURPLE)

        if event.key == pygame.K_g:
            canvas.fill(GOLD)

        if event.key == pygame.K_k:
            canvas.fill(KHAKI)

        if event.key == pygame.K_s:
            canvas.fill(SILVER)

        if event.key == pygame.K_y:
            canvas.fill(YELLOW)

  

    pygame.display.flip()