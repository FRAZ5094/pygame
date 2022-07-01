import numpy as np

def getTranslationMatrix(Tx,Ty,Tz):

    m = np.array([
        [1,0,0,Tx],
        [0,1,0,Ty],
        [0,0,1,Tz],
        [0,0,0,1],
        ])
    return m

def getScaleMatrix(Sx,Sy,Sz,Ox,Oy,Oz):

    m = np.array([
        [Sx,0,0,-Ox*Sx + Ox],
        [0,Sy,0,-Oy*Sy + Oy],
        [0,0,Sz,-Oz*Sz + Oz],
        [0,0,0,1],
        ])
    return m

def getRotationYMatrix(theta,Ox,Oy,Oz):

    T=getTranslationMatrix(Ox,Oy,Oz)
    Tb=getTranslationMatrix(-Ox,-Oy,-Oz)

    R = np.array([
        [np.cos(theta),0,0,0],
        [0,1,0,0],
        [-np.sin(theta),0,np.cos(theta),0],
        [0,0,0,1],
        ])

    return T.dot(R.dot(Tb))

class Triangle:
    def __init__(self,verticies):
        self.verticies=np.array(verticies)

    def __len__(self):
        return len(self.verticies)
class Mesh:
    def __init__(self,triangles):
        self.triangles=triangles

    def draw(self):
        for triangle in self.triangles:
            verticies_tuples=[]
            for vertex in triangle.verticies:
                verticies_tuples.append(vertex[0],vertex[1])
            pygame.draw.polygon(screen,RED,verticies_tuples, width=1)

    def __mul__(self,other):
        new_triangles = []
        for i in range(len(self.triangles)):
            print(self.triangles)
            new_triangles.append(self.triangles[i].verticies.dot(other))

        return Mesh(np.array(new_triangles))


class Matrix:
    def __init__(self,array):
        self.m=np.array(array)

    def __mult__(self,b):
        pass
    def __rmult__(self,b):
        pass
