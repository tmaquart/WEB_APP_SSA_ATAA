#!/usr/bin/python3

import numpy as np
import cgi
import cgitb
cgitb.enable()

def evaluategeometry(alphas,leftvectors,numberofvertices3times):
    verticesevaluated=[]
    for i in range(0,numberofvertices3times):
        valuetemp=np.float(alphas[0])*np.float(leftvectors[i][0])
        valuetemp+=np.float(alphas[1])*np.float(leftvectors[i][1])
        valuetemp+=np.float(alphas[2])*np.float(leftvectors[i][2])
        valuetemp+=np.float(alphas[3])*np.float(leftvectors[i][3])
        valuetemp+=np.float(alphas[4])*np.float(leftvectors[i][4])
        valuetemp+=np.float(alphas[5])*np.float(leftvectors[i][5])
        valuetemp+=np.float(alphas[6])*np.float(leftvectors[i][6])
        valuetemp+=np.float(alphas[7])*np.float(leftvectors[i][7])
        valuetemp+=np.float(alphas[8])*np.float(leftvectors[i][8])
        valuetemp+=np.float(alphas[9])*np.float(leftvectors[i][9])
        verticesevaluated.append(valuetemp)		
    return verticesevaluated
