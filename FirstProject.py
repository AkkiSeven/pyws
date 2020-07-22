import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")






while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
           pygame.quit()