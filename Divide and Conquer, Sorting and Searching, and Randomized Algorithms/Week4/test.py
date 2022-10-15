import pygame
import random as r
import copy
import randContraction as rc

from pygame.locals import (

    K_UP,

    K_DOWN,

    K_LEFT,

    K_RIGHT,

    K_ESCAPE,

    KEYDOWN,

    QUIT,

)




pygame.init()

width, height = 1000, 800
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption("Random Contraction Algorithm")


def drawNode(node,radius):
    font = pygame.font.SysFont("monospace",15)
    label = font.render(str(node),True,(0,0,0))
    
    color = [r.randint(50,255),r.randint(50,255),r.randint(50,255)]
    position = (r.randint(15,985),r.randint(15,785))

    pygame.draw.circle(screen,color,position,radius)
    screen.blit(label,[position[0]-5,position[1]-5])



def main():
    open = True
    screen.fill((255,255,255))
    while open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                open = False
            if event.type == KEYDOWN:
                drawNode("12",20)
                pygame.display.flip()

        

    pygame.display.quit()

main()