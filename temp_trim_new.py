# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 14:02:44 2022

@author: Tamar
Temperature dependent on trimbits
"""
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb


#T09=3D
#Digital
"""
VDDD = np.array([1.08,1.11,1.16,1.21,1.27])
Tint = np.array([60.6,60.8,60.5,60.3,60.3])
Text = np.array([38.05,38.00,38.05,37.90,37.90])
"""
#Analog

VDDA = np.array([1.17,1.22,1.27,1.33])
Tint = np.array([60.3,58.6,56.6,54.8])
Text = np.array([37.9,37.9,37.9,37.75])


#T06=20-3
#Digital
"""
VDDD = np.array([1.02,1.06,1.09,1.13,1.18,1.23,1.30,1.34])
Tint = np.array([52.0,51.75,51.69,51.88,51.63,51.63,51.13,50.69])
Text = np.array([35.8,35.85,35.75,35.75,35.75,35.7,35.55,35.5])
"""
#Analog
"""
VDDA = np.array([1.18,1.20,1.22,1.24,1.27,1.30,1.33,1.34])
Tint = np.array([51.50,50.69,50.38,49.19,48.63,48.00,47.13,46.00])
Text = np.array([35.70,35.75,35.70,35.65,35.60,35.45,35.30,35.00])
"""

Terr = 0.05/np.sqrt(16)*Tint

plt.figure(dpi=200)
plt.errorbar(VDDA,Tint,Terr,fmt='x',markersize=15,mew=5,label="internal temperature")
#plt.plot(VDDD,Text,'x',markersize=15,mew=5,label="external temperature")
plt.xlabel("Analog voltage [V]")
plt.ylabel("avg. module temperature [°C]")
plt.title("Module T09 temperature")
#plt.xticks([6,8,10,12,14,16,18,20,22,24,26])
plt.legend()
plt.savefig("TempvsTrimAnaT09.png")
