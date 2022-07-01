import pygame
import os
import numpy as np
from matrix_functions import *


WIDTH = 800
HEIGHT = 800
FPS = 30
scaleFactor=100
theta=0
startx=400
x=startx
starty=400
y=starty

z=0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



screen_x = 500
screen_y = 200
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
    np.array([-1,-1,0,1]),
    np.array([-1,1,0,1]),
    np.array([1,-1,0,1]),
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
        x=startx
        y=starty
        z=0
        theta=0

    translationMatrix = getTranslationMatrix(x,y,z)
    scaleMatrix = getScaleMatrix(scaleFactor,scaleFactor,scaleFactor,x,y,0)
    rotationYMatrix = getRotationYMatrix(np.deg2rad(theta),x,y,z)

    for i in range(len(verticies)):
        verticies[i]=rotationYMatrix.dot(scaleMatrix.dot(translationMatrix.dot(verticies[i])))

    verticies_tuples=[]
    for vertex in verticies:
        verticies_tuples.append((vertex[0],vertex[1]))

    pygame.draw.polygon(screen,RED,verticies_tuples, width=1)

    pygame.draw.circle(screen,BLUE,(x,y),2)

    pygame.display.flip()

pygame.quit()
