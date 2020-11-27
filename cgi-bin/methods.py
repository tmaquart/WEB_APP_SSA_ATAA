#!/usr/bin/python3

import numpy as np
import cgi
import cgitb
cgitb.enable()

def readleftvectors(totalnumberofsnapshots,path):
    leftvectors = np.loadtxt(path + 'left.txt', usecols=range(totalnumberofsnapshots))
    return leftvectors
	
def readconnectivity(connectivitycols,path):
    connectivity = np.loadtxt(path + 'CONNECTIVITY.cnc', usecols=range(connectivitycols))
    return connectivity
