# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 15:08:59 2022
Average chip temperature dependent on current

@author: Tamar
"""
import numpy as np
import matplotlib.pyplot as plt


#T0 = np.array([55.25,56.75,58,59.5,61,62.25,63,63,65.5,67.25,67.25])
#T1 = np.array([60.75,61.5,63,64,65.75,67.25,68.5,69,71.25,72.75,74.75])
#T2 = np.array([46,45.75,46.75,47.75,49,49.5,50.25,50,52,53.25,54])
#T3 = np.array([43.25,43.75,44.5,45,46.25,46.75,47.5,46.75,49,49.75,50.25])

T0 = np.array([59.3,61.3,62.3,64.0,65.7,67.0,68.0,68.3,71.0,73.0,73.7])
T1 = np.array([62.7,63.7,65.3,66.3,68.3,70.0,71.3,72.0,74.7,76.3,78.7])
T2 = np.array([48.7,48.7,49.7,51.0,52.3,52.7,53.7,53.3,55.3,56.7,57.7])
T3 = np.array([43.7,44.0,45.0,45.7,47.3,47.7,48.3,47.7,50.0,50.7,51.3])
Stdv0 = np.array([3.8,2.9,3.8,3.6,4.2,4.4,4.4,4.7,4.4,5.3,5.8])/np.sqrt(3)
Stdv1 = np.array([4.2,4.2,4.7,4.7,4.7,5.3,4.7,5.3,5.9,5.5,5.9])/np.sqrt(3)
Stdv2 = np.array([5.1,5.9,5.9,6.1,6.4,5.9,5.9,6.7,6.4,6.7,6.8])/np.sqrt(3)
Stdv3 = np.array([1.2,1.7,2.6,2.1,2.5,2.5,2.5,3.1,3.0,3.1,3.5])/np.sqrt(3)



pt1000 = np.array([32,32.3,32.7,33.1,33.4,33.8,34.2,34.5,34.9,35.2,35.7])
I = np.array([5.5,5.6,5.7,5.8,5.9,6.0,6.1,6.2,6.3,6.4,6.5])



plt.figure(dpi=200)
plt.errorbar(I,T0,Stdv0,fmt='.',label="chip 0",markersize=5,mew=3)
plt.errorbar(I,T1,Stdv1,fmt='.',label="chip 1",markersize=5,mew=3)
plt.errorbar(I,T2,Stdv2,fmt='.',label="chip 2",markersize=5,mew=3)
plt.errorbar(I,T3,Stdv3,fmt='.',label="chip 3",markersize=5,mew=3)
plt.errorbar(I,pt1000,0.2*np.ones(11),fmt='.',label="pt1000",markersize=5,mew=3)
plt.xlabel("Current [A]")
plt.ylabel("Temperature [°C]")
plt.title("Chip temperature dependent on current")
plt.legend()
#plt.savefig("TempvsCurrent.png")