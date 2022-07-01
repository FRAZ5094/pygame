import pygame
import os
import numpy as np
from matrix_functions import *


WIDTH = 800
HEIGHT = 800
FPS = 30
scaleFactor=1
theta=0
x=0
y=0
z=0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



screen_x = 1500
screen_y = 300
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screen_x,screen_y)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("<Your game>")
clock = pygame.time.Clock()   



## Game loop
running = True
while running:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    verticies=np.array([
    np.array([400,100,0,1]),
    np.array([100,700,0,1]),
    np.array([700,700,0,1]),
    ])

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_t]:
        scaleFactor+=0.01
    if pressed[pygame.K_r]:
        scaleFactor-=0.01
    if pressed[pygame.K_e]:
        theta+=1
    if pressed[pygame.K_q]:
        theta-=1
    if pressed[pygame.K_s]:
        y+=10
    if pressed[pygame.K_w]:
        y-=10
    if pressed[pygame.K_d]:
        x+=10
    if pressed[pygame.K_a]:
        x-=10
    if pressed[pygame.K_u]:
        x=0
        y=0
        z=0
        theta=0


    for i in range(len(verticies)):
        translationMatrix = getTranslationMatrix(x,y,0)
        scaleMatrix = getScaleMatrix(scaleFactor,scaleFactor,scaleFactor,400,400,0)
        rotationYMatrix = getRotationYMatrix(np.deg2rad(theta))
        verticies[i]=translationMatrix.dot(scaleMatrix.dot(rotationYMatrix.dot(verticies[i])))

    verticies_tuples=[]
    for vertex in verticies:
        verticies_tuples.append((vertex[0],vertex[1]))

    pygame.draw.polygon(screen,RED,verticies_tuples)

    # for i in range(len(verticies)):
        # if i==len(verticies)-1:
            # pygame.draw.line(screen, BLACK, (verticies[i][0],verticies[i][1]), (verticies[0][0],verticies[0][1]))
        # else:
            # pygame.draw.line(screen, BLACK, (verticies[i][0],verticies[i][1]), (verticies[i+1][0],verticies[i+1][1]))

    # pygame.draw.line(screen, RED,(400,400),(400,400))

    

    pygame.display.flip()

pygame.quit()
