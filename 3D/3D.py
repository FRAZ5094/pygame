import pygame
import os
import numpy as np
from matrix_functions import *


WIDTH = 800
HEIGHT = 800
FPS = 60
scaleFactor=400

camerax=0
cameray=0
cameraz=0
theta=0
psi=0


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

verticies=np.array([
np.array([-1,-1,0,1]),
np.array([-1,1,0,1]),
np.array([1,-1,0,1]),
])

mesh = TriangleMesh([
    [0,0,0],[0,1,0],[1,1,0],
    [0,0,0],[1,1,0],[1,0,0],

    [1,0,0],[1,1,0],[1,1,1],
    [1,0,0],[1,1,1],[1,0,1],

    [1,0,1],[1,1,1],[0,1,1],
    [1,0,1],[0,1,1],[0,0,1],

    [0,0,1],[0,1,1],[0,1,0],
    [0,0,1],[0,1,0],[0,0,0],

    [0,1,0],[0,1,1],[1,1,1],
    [0,1,0],[1,1,1],[1,1,0],

    [1,0,1],[0,0,1],[0,0,0],
    [1,0,1],[0,0,0],[1,0,0],
    ]
)

w,h = pygame.display.get_surface().get_size()
a=0

## Game loop
running = True
while running:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)


    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_t]:
        scaleFactor*=1.1
    if pressed[pygame.K_r]:
        scaleFactor/=1.1
    if pressed[pygame.K_w]:
        cameraz-=10
    if pressed[pygame.K_s]:
        cameraz+=10
    if pressed[pygame.K_d]:
        camerax+=10
    if pressed[pygame.K_a]:
        camerax-=10
    if pressed[pygame.K_SPACE]:
        cameray-=10
    if pressed[pygame.K_LSHIFT]:
        cameray+=10
    if pressed[pygame.K_UP]:
        theta+=1
    if pressed[pygame.K_DOWN]:
        theta-=1
    if pressed[pygame.K_LEFT]:
        psi+=1
    if pressed[pygame.K_RIGHT]:
        psi-=1
    if pressed[pygame.K_u]:
        camerax=0
        cameray=0
        cameraz=0
        theta=0
        psi=0

    #Position Mesh in world at (400,400,0)
    x=400
    initialScaleFactor=50
    a+=1
    modelToWorldMatrix = getRotationMatrix(a,x,0,0,[0,1,0]) * getTranslationMatrix(0,0,0) * getTranslationMatrix(h/2,w/2,0) * getScaleMatrix(initialScaleFactor,initialScaleFactor,initialScaleFactor,0,0,0) * getTranslationMatrix(-0.5,-0.5,0)
    worldToViewMatrix = getRotationMatrix(psi,w/2,h/2,0,[0,1,0])
    viewToProjectionMatrix = getProjectionMatrix()
    translatedMesh = modelToWorldMatrix * mesh

    translatedMesh.draw(screen)

    pygame.draw.line(screen,(255,0,0),(x,0),(x,h))
    pygame.draw.line(screen,(255,0,0),(x+25,0),(x+25,h))

    getProjectionMatrix()

    # for triangle in mesh:
        # transformedMesh=rotationYMatrix.dot(scaleMatrix.dot(translationMatrix.dot(verticies[i])))



    pygame.display.flip()

pygame.quit()
