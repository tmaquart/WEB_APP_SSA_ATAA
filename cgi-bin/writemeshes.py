#!/usr/bin/python3

import numpy as np
from stl import mesh
import cgi
import cgitb
cgitb.enable()
    
def writeobj(connectivity,numberofvertices3times,numberofelements,vertices,path):
    f = open(path + "iso.obj", "w")
    for i in range(0,numberofvertices3times,3):
        stringtowrite='v ' + str(vertices[i]) + ' ' + str(vertices[i+1]) + ' ' + str(vertices[i+2])
        f.write(stringtowrite)
        f.write("\n")
    for i in range(0,numberofelements):
        stringtowrite='f ' + str(int(connectivity[i][1]+1)) + ' ' + str(int(connectivity[i][2]+1)) + ' ' + str(int(connectivity[i][3]+1)) + ' ' + str(int(connectivity[i][4]+1))
        f.write(stringtowrite)
        f.write("\n")
    f.close()

def writestl(connectivity,vertices,numberofvertices3times,numberofelements,path):	
    stlmesh = mesh.Mesh(np.zeros(connectivity.shape[0]*2, dtype=mesh.Mesh.dtype))
    verticesstl=np.array([[vertices[0],vertices[0+1],vertices[0+2]]])
    for i in range(3,numberofvertices3times,3):
        verticesstl=np.append(verticesstl,[[vertices[i],vertices[i+1],vertices[i+2]]],axis=0)
        connectivitystl=np.array([[int(connectivity[0][2]),int(connectivity[0][3]),int(connectivity[0][4])]])
        connectivitystl=np.append(connectivitystl,[[int(connectivity[0][1]),int(connectivity[0][2]),int(connectivity[0][4])]],axis=0)
    for i in range(1,numberofelements):
        connectivitystl=np.append(connectivitystl,[[int(connectivity[i][2]),int(connectivity[i][3]),int(connectivity[i][4])]],axis=0)
    for i in range(1,numberofelements):
        connectivitystl=np.append(connectivitystl,[[int(connectivity[i][1]),int(connectivity[i][2]),int(connectivity[i][4])]],axis=0)
    for i,f in enumerate(connectivitystl):
        for j in range(3):
            stlmesh.vectors[i][j] = verticesstl[f[j],:]
    stlmesh.save(path + 'iso.stl')
