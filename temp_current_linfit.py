# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 15:08:59 2022
Average chip temperature dependent on current

@author: Tamar
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


#T0 = np.array([55.25,56.75,58,59.5,61,62.25,63,63,65.5,67.25,67.25])
#T1 = np.array([60.75,61.5,63,64,65.75,67.25,68.5,69,71.25,72.75,74.75])
#T2 = np.array([46,45.75,46.75,47.75,49,49.5,50.25,50,52,53.25,54])
#T3 = np.array([43.25,43.75,44.5,45,46.25,46.75,47.5,46.75,49,49.75,50.25])

T0 = np.array([61.7,63,64.3,65.7,66.7,68.8,70.0,71.7,72.7,74.3,75.7])
T1 = np.array([50.7,51.7,52.3,53.3,54.7,55.3,56.0,58.0,58.7,59.7,61.0])
T2 = np.array([47.3,47.3,48.7,50.0,50.7,50.3,52.3,53.0,53.3,54.7,55.7])
T3 = np.array([57.0,57.7,59.0,60.3,61.7,62.7,63.7,65.0,66.3,68.3,69.0])
Stdv0 = np.array([4.9,4.6,5.7,5.1,5.9,5.3,6.2,5.9,6.8,6.7,7.8])/np.sqrt(3)
Stdv1 = np.array([5.5,5.1,6.0,5.0,6.1,6.7,6.0,7.2,7.1,6.1,7.2])/np.sqrt(3)
Stdv2 = np.array([5.0,3.8,4.5,5.6,5.1,5.0,4.7,5.0,6.0,6.1,5.9])/np.sqrt(3)
Stdv3 = np.array([3.0,2.5,3.0,2.5,3.1,3.1,3.5,3.0,3.5,3.5,4.0])/np.sqrt(3)



pt1000 = np.array([35.7,36.4,36.9,37.4,37.8,38.2,38.5,39.1,39.7,40.3,40.6])#R pt1000
I = np.array([5.5,5.6,5.7,5.8,5.9,6.0,6.1,6.2,6.3,6.4,6.5])
Ifit = np.array([5.5,6.5])
V = np.array([2.1,2.1,2.1,2.1,2.2,2.2,2.2,2.3,2.3,2.3,2.3])
W = I*V

fit0 = np.polyfit(I,T0,1)
fit1 = np.polyfit(I,T1,1)
fit2 = np.polyfit(I,T2,1)
fit3 = np.polyfit(I,T3,1)
fitp = np.polyfit(I,pt1000,1)
#fit0e = np.polyfit(I,np.log(T0),1)
#fit1e = np.polyfit(I,np.log(T1),1)
#fit2e = np.polyfit(I,np.log(T2),1)
#fit3e = np.polyfit(I,np.log(T3),1)
#fitpe = np.polyfit(I,np.log(pt1000),1)


print(fit0)
print(fit1)
print(fit2)
print(fit3)
print(fitp)

"""
print(fit0[0])
print(fit1[0])
print(fit2[0])
print(fit3[0])
print(fitp[0])
print(r2_score(T0,fit0[0]*I+fit0[1]))
print(r2_score(T1,fit1[0]*I+fit1[1]))
print(r2_score(T2,fit2[0]*I+fit2[1]))
print(r2_score(T3,fit3[0]*I+fit3[1]))
print(r2_score(pt1000,fitp[0]*I+fitp[1]))
"""

plt.figure(dpi=200)#200
#plt.plot(Ifit,np.exp(fit0e[1])*np.exp(fit0e[0]*Ifit))
#plt.plot(Ifit,np.exp(fit1e[1])*np.exp(fit1e[0]*Ifit))
#plt.plot(Ifit,np.exp(fit2e[1])*np.exp(fit2e[0]*Ifit))
#plt.plot(Ifit,np.exp(fit3e[1])*np.exp(fit3e[0]*Ifit))
#plt.plot(Ifit,np.exp(fitpe[1])*np.exp(fitpe[0]*Ifit))
plt.plot(Ifit,fit0[0]*Ifit+fit0[1],color='b')
plt.plot(Ifit,fit1[0]*Ifit+fit1[1],color='orange')
plt.plot(Ifit,fit2[0]*Ifit+fit2[1],color='g')
plt.plot(Ifit,fit3[0]*Ifit+fit3[1],color='r')
plt.plot(Ifit,fitp[0]*Ifit+fitp[1],color='m')
plt.errorbar(I,T0,Stdv0,fmt='b.',label="chip 0",markersize=5,mew=3)
plt.errorbar(I,T1,Stdv1,fmt='.',color='orange',label="chip 1",markersize=5,mew=3)
plt.errorbar(I,T2,Stdv2,fmt='g.',label="chip 2",markersize=5,mew=3)
plt.errorbar(I,T3,Stdv3,fmt='r.',label="chip 3",markersize=5,mew=3)
plt.errorbar(I,pt1000,0.3*np.ones(11),fmt='m.',label="pt1000",markersize=5,mew=3)

"""
#Day 3:
I3 = np.array([5.5,6,6.5])
plt.plot(I3,np.array([62.7,69.3,76.7]),'bx',ms=10)
plt.plot(I3,np.array([48.3,52.0,56.7]),'x',ms=10,color='orange')
plt.plot(I3,np.array([47.3,50.7,55.0]),'gx',ms=10)
plt.plot(I3,np.array([57.3,63.3,69.3]),'rx',ms=10)
plt.plot(I3,np.array([34.1,36.3,38.4]),'mx',ms=10)

plt.plot(I3,np.array([63.0,69.7,77.0]),'bx',ms=10)
plt.plot(I3,np.array([48.3,52.0,56.3]),'x',ms=10,color='orange')
plt.plot(I3,np.array([47.7,50.3,55.3]),'gx',ms=10)
plt.plot(I3,np.array([57.0,62.7,69.0]),'rx',ms=10)
plt.plot(I3,np.array([34.4,36.6,39.3]),'mx',ms=10)

#Other module
plt.plot(I3,np.array([67.3,74.0,81.3]),'bd',ms=7)
plt.plot(I3,np.array([54.3,57.3,62.3]),'d',ms=7,color='orange')
plt.plot(I3,np.array([53.7,59.0,64.3]),'gd',ms=7)
plt.plot(I3,np.array([63.0,68.0,73.7]),'rd',ms=7)
plt.plot(I3,np.array([37.5,40.0,42.6]),'md',ms=7)
"""

plt.xlabel("Current [A]")
plt.ylabel("Temperature [°C]")
plt.title("Module T06 temperature")
plt.legend()
plt.savefig("TempvsCurrent_lin.png")