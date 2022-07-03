import numpy as np
import pygame

def getTranslationMatrix(Tx,Ty,Tz):

    m = [
        [1,0,0,Tx],
        [0,1,0,Ty],
        [0,0,1,Tz],
        [0,0,0,1],
        ]
    return Matrix(m)

def getScaleMatrix(Sx,Sy,Sz,Ox,Oy,Oz):

    m = [
        [Sx,0,0,-Ox*Sx + Ox],
        [0,Sy,0,-Oy*Sy + Oy],
        [0,0,Sz,-Oz*Sz + Oz],
        [0,0,0,1],
        ]
    return Matrix(m)

def getRotationMatrix(angle,Ox,Oy,Oz,n):

    T=getTranslationMatrix(Ox,Oy,Oz)
    Tb=getTranslationMatrix(-Ox,-Oy,-Oz)

    angle=np.deg2rad(angle)

    c=np.cos(angle)
    s=np.sin(angle)

    n=np.array(n)
    n=n/np.sqrt(n.sum())
    

    x=n[0]
    y=n[1]
    z=n[2]

    # R = Matrix([
        # [c,0,0,0],
        # [0,1,0,0],
        # [-s,0,c,0],
        # [0,0,0,1],
        # ])

    R = Matrix([
        [((x**2) * (1-c)) + c,  ((x*y) * (1-c)) - z*s, ((x*z) * (1-c)) + y*s, 0],
        [((y*x) * (1-c)) + z*s,  ((y**2) * (1-c)) + c,  ((y*z) * (1-c)) - x*s, 0],
        [((x*z) * (1-c)) - y*s, ((y*z) * (1-c)) + x*s,     ((z**2) * (1-c)) + c, 0],
        [0,0,0,1]
        ])



    return T * R * Tb

class TriangleMesh:
    def __init__(self,verticies):
        if len(verticies) == 4:
            self.verticies=verticies
        else:
            transposedVerticies=np.array(verticies).T
            ncols=len(transposedVerticies[0])
            self.verticies=np.vstack([transposedVerticies, [1]*ncols])

    def draw(self,screen):
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        Colours=[RED,GREEN,BLUE]

        for i in range(int(len(self.verticies[0])/3)):
            verticies_tuple=[tuple(self.verticies[:,3*i][0:2]),tuple(self.verticies[:,(3*i)+1][0:2]),tuple(self.verticies[:,(3*i)+2][0:2])]
            pygame.draw.polygon(screen,Colours[int(i%3)],verticies_tuple)

class Matrix:
    def __init__(self,array):
        self.m=np.array(array)

    def __mul__(self,other):
        if isinstance(other,TriangleMesh):
            #TypeError: unsupported operand type(s) for *: 'int' and 'NoneType' ?????
            # print(self.m)
            # print(other.verticies)
            transformedVerticies=self.m.dot(other.verticies)
            return TriangleMesh(transformedVerticies)
        elif isinstance(other, Matrix):
            return Matrix(self.m.dot(other.m))
