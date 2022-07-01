from sympy import *

Sx,Sy,Sz,Ox,Oy,Oz,x,y,z = symbols("Sx,Sy,Sz,Ox,Oy,Oz,x,y,z")

T = Matrix([[1,0,0,Ox],[0,1,0,Oy],[0,0,1,Oz],[0,0,0,1]])
Tb = Matrix([[1,0,0,-Ox],[0,1,0,-Oy],[0,0,1,-Oz],[0,0,0,1]])
S = Matrix([[Sx,0,0,0],[0,Sy,0,0],[0,0,Sz,0],[0,0,0,1]])
P = Matrix([x,y,z,1])


pprint(T*S*Tb)
