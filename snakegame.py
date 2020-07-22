import pygame
import time
import random
#pygame window initialisation
pygame.init()
#Declare the colours using their RGB codes
orangecolour = (255, 123, 7)
blackcolour = (0, 0 , 0)
redcolour = (213, 50, 80)
greencolour = (0, 255, 0)
bluecolour = (50, 153, 213)

#Display window's width and height
display_width = 600
display_height = 400
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')  # fix the caption
snake_block = 10
snake_list = []
# Defines the snake's structure and position
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, orangecolour, [x[0], x[1], snake_block, snake_block])
#main function
def snakegame():        
    game_over = False
    game_end = False
    #co-ordinates of the snake
    x1 = display_width / 2
    y1 = display_height / 2
    # when the  snake moves
    x1_change = 0
    y1_change = 0
    while not game_over:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                if event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                if event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_end = True
        x1 += x1_change
        y1 += y1_change
        pygame.display.update()
    pygame.quit()
    quit()