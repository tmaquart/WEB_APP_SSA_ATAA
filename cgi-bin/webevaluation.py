#!/usr/bin/python3

#web version 1.0
#created by T.MAQUART
#thanks to S.AVRIL and M.DI GIUSEPPE

########## IMPORTS ##########

from methods import *
from writemeshes import *
from buildingevaluation import *
import shutil
import numpy as np
import cgi
import cgitb
cgitb.enable()

########## NOTES ##########

#1- Alpha_Mesh_i.txt files must contain only string + value per line
#2- CONNECTIVITY.cnc must contain only integers
#3- please read README.txt

def webevaluationfunction(alpha1, alpha2, alpha3, alpha4, alpha5, alpha6, alpha7, alpha8, alpha9, alpha10, studytype):

    ########## INPUT ##########

    #--- fixed parameters of SSA ---

    totalnumberofsnapshots=24

    #--- connectivity parameters ---

    connectivitycols=5

    ########## PROGRAM ##########

    #--- study path ---

    path="systole/"
    if np.float(studytype)==0:
        path="diastole/"

    #--- reading from text files ---

    leftvectors = readleftvectors(totalnumberofsnapshots,path)
    numberofvertices3times=len(leftvectors)

    connectivity = readconnectivity(connectivitycols,path)
    numberofelements=len(connectivity)
	
    #--- evaluation parameters ---

    alphas=[np.float(alpha1),np.float(alpha2),np.float(alpha3),np.float(alpha4),np.float(alpha5),np.float(alpha6),np.float(alpha7),np.float(alpha8),np.float(alpha9),np.float(alpha10)]

    #--- compute evaluation ---

    vertices=evaluategeometry(alphas,leftvectors,numberofvertices3times)

    #--- write evaluated mesh as OBJ ---

    writeobj(connectivity,numberofvertices3times,numberofelements,vertices,path)

    #--- write STL file ---

    writestl(connectivity,vertices,numberofvertices3times,numberofelements,path)

    #--- work on generated files --

    if np.float(studytype)==0:
        print("<br>")
        print("<center>")
        print("Requested Python study type: " + str(studytype))
        print("<center>")
        shutil.copy2("/var/www/cgi-bin/diastole/iso.obj", "/var/www/html/meshes/generated.obj")
        shutil.copy2("/var/www/cgi-bin/diastole/iso.stl", "/var/www/html/meshes/generated.stl")
    else:
        print("<br>")
        print("<center>")
        print("Requested Python study type: " + str(studytype))
        print("</center>")
        shutil.copy2("/var/www/cgi-bin/systole/iso.obj", "/var/www/html/meshes/generated.obj")
        shutil.copy2("/var/www/cgi-bin/systole/iso.stl", "/var/www/html/meshes/generated.stl")

    return 1.0

