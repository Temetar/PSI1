# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 14:02:44 2022

@author: Tamar
Temperature dependent on trimbits
"""
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

VDDD = np.array([16,31,31,31,0,0,0])
VDDA = np.array([16,16,20,25,25,15,6])
#T = np.array([56.5,55.7,54.5,52.2,53.4,57.6,60.3])
#T = np.array([59.5,58.6,57.3,54.8,56.3,60.8,63.7])
T = np.array([47.5,47,46,44.8,44.5,48,50])

plt.plot(VDDA[0],T[0],'x',label="VDDD = 16",markersize=15,mew=5)
plt.plot(VDDA[1:4],T[1:4],'x',label="VDDD = 31",markersize=15,mew=5)
plt.plot(VDDA[4:7],T[4:7],'x',label="VDDD = 0",markersize=15,mew=5)
plt.xlabel("VDDA (Analog voltage trimming)")
#plt.xlabel("VDDD (Digital voltage trimming)")
#plt.plot(VDDD,T,'x',markersize=15,mew=5)
plt.ylabel("avg. module temperature [°C]")
plt.title("Module T06 temperature dependent on voltage trimmings")
plt.xticks([6,8,10,12,14,16,18,20,22,24,26])
plt.legend()
#plt.savefig("TempvsTrimDig.png")
