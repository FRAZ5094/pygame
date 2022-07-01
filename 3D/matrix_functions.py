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

class triangle:
    def __init__(self,verticies):
        self.verticies=verticies

class matrix:
    def __init__(self,array):
        self.m=np.array(array)


class vertex:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
