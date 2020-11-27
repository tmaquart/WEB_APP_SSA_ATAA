#!/usr/bin/python3

import cgi
import cgitb
cgitb.enable()
from webevaluation import *
import numpy as np

form = cgi.FieldStorage()

minalpha1s=9964
maxalpha1s=15396
minalpha1d=9588
maxalpha1d=14800
minalpha2s=-1110
maxalpha2s=1251
minalpha2d=-1202
maxalpha2d=891
minalpha3s=-984
maxalpha3s=866
minalpha3d=-913
maxalpha3d=975
minalpha4s=-1360
maxalpha4s=895
minalpha4d=-871
maxalpha4d=1056
minalpha5s=-757
maxalpha5s=1037
minalpha5d=-950
maxalpha5d=726
minalpha6s=-1158
maxalpha6s=472
minalpha6d=-674
maxalpha6d=822
minalpha7s=-567
maxalpha7s=465
minalpha7d=-515
maxalpha7d=371
minalpha8s=-367
maxalpha8s=359
minalpha8d=-316
maxalpha8d=387
minalpha9s=-376
maxalpha9s=316
minalpha9d=-348
maxalpha9d=364
minalpha10s=-249
maxalpha10s=312
minalpha10d=-162
maxalpha10d=295

print ('Content-Type: text/html')
print ('')
print ('<html>')
print ('<style>')
print ('body{background-color: #BAB8B7;}')
print ('</style>')
print ('<head>')
print ('<title>Statistical Shape Analysis: Python process</title>')
print ('</head>')
print ('<center>')
print ('<h2>Chosen modes coefficients</h2>')
print ('<br>')
print ('They are:<br>')
print ('<br>')
print ('<b>Alpha_1:</b> ' + form['alpha1'].value + '<br>')
print ('<b>Alpha_2:</b> ' + form['alpha2'].value + '<br>')
print ('<b>Alpha_3:</b> ' + form['alpha3'].value + '<br>')
print ('<b>Alpha_4:</b> ' + form['alpha4'].value + '<br>')
print ('<b>Alpha_5:</b> ' + form['alpha5'].value + '<br>')
print ('<b>Alpha_6:</b> ' + form['alpha6'].value + '<br>')
print ('<b>Alpha_7:</b> ' + form['alpha7'].value + '<br>')
print ('<b>Alpha_8:</b> ' + form['alpha8'].value + '<br>')
print ('<b>Alpha_9:</b> ' + form['alpha9'].value + '<br>')
print ('<b>Alpha_10:</b> ' + form['alpha10'].value + '<br>')
print ('</p>')
print ('</center>')
print ('</html>')

systole=0.0
try:
  systole=form['systole'].value
  print ('<html>')
  print ('<center>')
  print ('<b>Systole study: </b>' + str(systole) + '<br>')
  print ('</center>')
  print ('</html>')
except:
  systole=0.0
  print ('<html>')
  print ('<center>')
  print ('<b>Diastole study: </b>' + str(systole) + '<br>')
  print ('</center>')
  print ('</html>')

if np.float(systole)==1.0:
    if np.float(form['alpha1'].value)<minalpha1s or np.float(form['alpha1'].value)>maxalpha1s:
      print ('<html>')
      print ('<center>')
      print ('<br>')
      print ('<b style="color:red;">Error: please check values for systole study!</b>')
      print ('<br>')
      print ('</center>')
      print ('</html>')
    elif np.float(form['alpha2'].value)<minalpha2s or np.float(form['alpha2'].value)>maxalpha2s:
      print ('<html>')
      print ('<center>')
      print ('<br>')
      print ('<b style="color:red;">Error: please check values for systole study!</b>')
      print ('<br>')
      print ('</center>')
      print ('</html>')
    elif np.float(form['alpha3'].value)<minalpha3s or np.float(form['alpha3'].value)>maxalpha3s:
      print ('<html>')
      print ('<center>')
      print ('<br>')
      print ('<b style="color:red;">Error: please check values for systole study!</b>')
      print ('<br>')
      print ('</center>')
      print ('</html>')
    elif np.float(form['alpha4'].value)<minalpha4s or np.float(form['alpha4'].value)>maxalpha4s:
      print ('<html>')
      print ('<center>')
      print ('<br>')
      print ('<b style="color:red;">Error: please check values for systole study!</b>')
      print ('<br>')
      print ('</center>')
      print ('</html>')
    elif np.float(form['alpha5'].value)<minalpha5s or np.float(form['alpha5'].value)>maxalpha5s:
      print ('<html>')
      print ('<center>')
      print ('<br>')
      print ('<b style="color:red;">Error: please check values for systole study!</b>')
      print ('<br>')
      print ('</center>')
      print ('</html>')
    elif np.float(form['alpha6'].value)<minalpha6s or np.float(form['alpha6'].value)>maxalpha6s:
      print ('<html>')
      print ('<center>')
      print ('<br>')
      print ('<b style="color:red;">Error: please check values for systole study!</b>')
      print ('<br>')
      print ('</center>')
      print ('</html>')
    elif np.float(form['alpha7'].value)<minalpha7s or np.float(form['alpha7'].value)>maxalpha7s:
      print ('<html>')
      print ('<center>')
      print ('<br>')
      print ('<b style="color:red;">Error: please check values for systole study!</b>')
      print ('<br>')
      print ('</center>')
      print ('</html>')
    elif np.float(form['alpha8'].value)<minalpha8s or np.float(form['alpha8'].value)>maxalpha8s:
      print ('<html>')
      print ('<center>')
      print ('<br>')
      print ('<b style="color:red;">Error: please check values for systole study!</b>')
      print ('<br>')
      print ('</center>')
      print ('</html>')
    elif np.float(form['alpha9'].value)<minalpha9s or np.float(form['alpha9'].value)>maxalpha9s:
      print ('<html>')
      print ('<center>')
      print ('<br>')
      print ('<b style="color:red;">Error: please check values for systole study!</b>')
      print ('<br>')
      print ('</center>')
      print ('</html>')
    elif np.float(form['alpha10'].value)<minalpha10s or np.float(form['alpha10'].value)>maxalpha10s:
      print ('<html>')
      print ('<center>')
      print ('<br>')
      print ('<b style="color:red;">Error: please check values for systole study!</b>')
      print ('<br>')
      print ('</center>')
      print ('</html>')
    else:
      try:
        alpha1=np.float(form['alpha1'].value)
        alpha2=np.float(form['alpha2'].value)
        alpha3=np.float(form['alpha3'].value)
        alpha4=np.float(form['alpha4'].value)
        alpha5=np.float(form['alpha5'].value)
        alpha6=np.float(form['alpha6'].value)
        alpha7=np.float(form['alpha7'].value)
        alpha8=np.float(form['alpha8'].value)
        alpha9=np.float(form['alpha9'].value)
        alpha10=np.float(form['alpha10'].value)
        result=webevaluationfunction(alpha1,alpha2,alpha3,alpha4,alpha5,alpha6,alpha7,alpha8,alpha9,alpha10,np.float(systole))
        print ('<html>')
        print ('<center>')
        print ('<br>')
        print ('<b>Result has been successfully written on the server!</b>')
        print ('<br>')
        print ('</center>')
        print ('</html>')
      except:
        print ('<html>')
        print ('<center>')
        print ('<br>')
        print ('<b style="color:red;">Error: undefined error!</b>')
        print ('<br>')
        print ('</center>')
        print ('</html>')
else:
    if np.float(form['alpha1'].value)<minalpha1d or np.float(form['alpha1'].value)>maxalpha1d:
      print ('<html>')
      print ('<center>')
      print ('<br>')
      print ('<b style="color:red;">Error: please check values for diastole study!</b>')
      print ('<br>')
      print ('</center>')
      print ('</html>')
    elif np.float(form['alpha2'].value)<minalpha2d or np.float(form['alpha2'].value)>maxalpha2d:
      print ('<html>')
      print ('<center>')
      print ('<br>')
      print ('<b style="color:red;">Error: please check values for diastole study!</b>')
      print ('<br>')
      print ('</center>')
      print ('</html>')
    elif np.float(form['alpha3'].value)<minalpha3d or np.float(form['alpha3'].value)>maxalpha3d:
      print ('<html>')
      print ('<center>')
      print ('<br>')
      print ('<b style="color:red;">Error: please check values for diastole study!</b>')
      print ('<br>')
      print ('</center>')
      print ('</html>')
    elif np.float(form['alpha4'].value)<minalpha4d or np.float(form['alpha4'].value)>maxalpha4d:
      print ('<html>')
      print ('<center>')
      print ('<br>')
      print ('<b style="color:red;">Error: please check values for diastole study!</b>')
      print ('<br>')
      print ('</center>')
      print ('</html>')
    elif np.float(form['alpha5'].value)<minalpha5d or np.float(form['alpha5'].value)>maxalpha5d:
      print ('<html>')
      print ('<center>')
      print ('<br>')
      print ('<b style="color:red;">Error: please check values for diastole study!</b>')
      print ('<br>')
      print ('</center>')
      print ('</html>')
    elif np.float(form['alpha6'].value)<minalpha6d or np.float(form['alpha6'].value)>maxalpha6d:
      print ('<html>')
      print ('<center>')
      print ('<br>')
      print ('<b style="color:red;">Error: please check values for diastole study!</b>')
      print ('<br>')
      print ('</center>')
      print ('</html>')
    elif np.float(form['alpha7'].value)<minalpha7d or np.float(form['alpha7'].value)>maxalpha7d:
      print ('<html>')
      print ('<center>')
      print ('<br>')
      print ('<b style="color:red;">Error: please check values for diastole study!</b>')
      print ('<br>')
      print ('</center>')
      print ('</html>')
    elif np.float(form['alpha8'].value)<minalpha8d or np.float(form['alpha8'].value)>maxalpha8d:
      print ('<html>')
      print ('<center>')
      print ('<br>')
      print ('<b style="color:red;">Error: please check values for diastole study!</b>')
      print ('<br>')
      print ('</center>')
      print ('</html>')
    elif np.float(form['alpha9'].value)<minalpha9d or np.float(form['alpha9'].value)>maxalpha9d:
      print ('<html>')
      print ('<center>')
      print ('<br>')
      print ('<b style="color:red;">Error: please check values for diastole study!</b>')
      print ('<br>')
      print ('</center>')
      print ('</html>')
    elif np.float(form['alpha10'].value)<minalpha10d or np.float(form['alpha10'].value)>maxalpha10d:
      print ('<html>')
      print ('<center>')
      print ('<br>')
      print ('<b style="color:red;">Error: please check values for diastole study!</b>')
      print ('<br>')
      print ('</center>')
      print ('</html>')
    else:
      try:
        alpha1=np.float(form['alpha1'].value)
        alpha2=np.float(form['alpha2'].value)
        alpha3=np.float(form['alpha3'].value)
        alpha4=np.float(form['alpha4'].value)
        alpha5=np.float(form['alpha5'].value)
        alpha6=np.float(form['alpha6'].value)
        alpha7=np.float(form['alpha7'].value)
        alpha8=np.float(form['alpha8'].value)
        alpha9=np.float(form['alpha9'].value)
        alpha10=np.float(form['alpha10'].value)
        result=webevaluationfunction(alpha1,alpha2,alpha3,alpha4,alpha5,alpha6,alpha7,alpha8,alpha9,alpha10,np.float(systole))
        print ('<html>')
        print ('<center>')
        print ('<br>')
        print ('<b>Result has been successfully written on the server!</b>')
        print ('<br>')
        print ('</center>')
        print ('</html>')
      except:
        print ('<html>')
        print ('<center>')
        print ('<br>')
        print ('<b style="color:red;">Error: undefined error!</b>')
        print ('<br>')
        print ('</center>')
        print ('</html>')

print ('<html>')
print ('<center>')
print ('<br>')
print ('<a href="javascript:history.back()">Previous page</a>')
print ('<br>')
print ('</center>')
print ('</html>')

print ('<html>')
print ('<center>')
print ('<h3>Designed and implemented by T.MAQUART using Python CGI and Three.js</h3>')
print ('</center>')
print ('</html>')

