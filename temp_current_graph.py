# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 10:52:45 2022

Comparison of temperatures of 2 uncoated and one coated module

@author: Tamar
"""
import matplotlib.pyplot as plt
import numpy as np

I3 = np.array([5.5,6,6.5])


plt.figure(dpi=200,figsize=(2,5))

#plt.plot(I3,np.array([53.9,58.8,64.4]),'bo',ms=5,label='T06 edge (uncoated)')
#plt.plot(I3,np.array([54.0,58.7,64.4]),'bo',ms=5)
plt.errorbar(I3,np.array([53.95,58.75,64.4]),np.array([0.05,0.05,0.1]),fmt='bo',ms=5,label='T06 edge (uncoated)')
#plt.plot(I3,np.array([55.8,60.3,64.5]),'rx',ms=5,label='T07 edge (uncoated)')
#plt.plot(I3,np.array([55.8,60.8,64.5]),'rx',ms=5)
#plt.plot(I3,np.array([55.8,59.5,64.3]),'rx',ms=5)
plt.errorbar(I3,np.array([55.8,60.2,64.4]),np.array([0,0.4,0.1]),fmt='rx',ms=5,label='T07 edge (uncoated)')
#plt.plot(I3,np.array([59.6,64.6,70.4]),'gd',ms=5,label='T09 edge (coated)')
#plt.plot(I3,np.array([58.5,64.2,70.4]),'gd',ms=5)
plt.errorbar(I3,np.array([59.05,64.4,70.4]),np.array([0.55,0.2,0]),fmt='gd',ms=5,label='T09 edge (coated)')
#plt.plot(I3,np.array([54.0,58.7,63.8]),'v',color='orange',ms=5,label='T14 edge (coated)')
#plt.plot(I3,np.array([52.5,57.1,61.7]),'v',color='orange',ms=5)
#plt.plot(I3,np.array([52.5,57.0,62.3]),'v',color='orange',ms=5)
plt.errorbar(I3,np.array([53.0,57.6,62.6]),np.array([0.5,0.6,0.6]),fmt='v',color='orange',ms=5,label='T14 edge (coated)')

plt.xlabel('Current [A]')
plt.ylabel('Temperature [°C]')
plt.title('Temperature of coated vs uncoated modules')
plt.legend(loc='upper center',bbox_to_anchor=(0.5,-0.1 ))
plt.savefig('CoatedvsUncoated1.png',bbox_inches='tight')

plt.figure(dpi=200,figsize=(2,5))

#plt.plot(I3,np.array([33.6,35.7,37.8]),'bo',ms=5,label='T06 top pt1000s (uncoated)')
#plt.plot(I3,np.array([33.9,36.0,38.4]),'bo',ms=5)
plt.errorbar(I3,np.array([33.75,35.85,38.1]),np.array([0.15,0.15,0.3]),fmt='bo',ms=5,label='T06 top pt1000s (uncoated)')
#plt.plot(I3,np.array([34.0,35.8,37.8]),'rx',ms=5,label='T07 top pt1000s (uncoated)')
#plt.plot(I3,np.array([33.6,35.7,37.6]),'rx',ms=5)
#plt.plot(I3,np.array([33.8,35.7,37.6]),'rx',ms=5)
plt.errorbar(I3,np.array([33.8,35.7,37.7]),np.array([0.1,0.0,0.1]),fmt='rx',ms=5,label='T07 top pt1000s (uncoated)')
#plt.plot(I3,np.array([36.4,38.7,41.3]),'gd',ms=5,label='T09 top pt1000s (coated)')
#plt.plot(I3,np.array([36.4,38.8,41.2]),'gd',ms=5)
plt.errorbar(I3,np.array([36.4,38.75,41.25]),np.array([0,0.05,0.05]),fmt='gd',ms=5,label='T09 top pt1000s (coated)')
#plt.plot(I3,np.array([36.4,38.9,41.6]),'v',color='orange',ms=5,label='T14 top pt1000s (coated)')#Subtracted 0.4 for hat
#plt.plot(I3,np.array([36.7,38.7,41.2]),'v',color='orange',ms=5)
#plt.plot(I3,np.array([36.6,38.8,41.0]),'v',color='orange',ms=5)
plt.errorbar(I3,np.array([36.6,38.8,41.3]),np.array([0.1,0.1,0.2]),fmt='v',color='orange',ms=5,label='T14 top pt1000s (coated)')

plt.xlabel('Current [A]')
plt.ylabel('Temperature [°C]')
plt.title('Temperature of coated vs uncoated modules')
plt.legend(loc='upper center',bbox_to_anchor=(0.5,-0.1 ))
plt.savefig('CoatedvsUncoated2.png',bbox_inches='tight')

plt.figure(dpi=200,figsize=(2,5))

#plt.plot(I3,np.array([31.5,33.3,35.1]),'bo',ms=5,label='T06 block pt1000 (uncoated)')
#plt.plot(I3,np.array([31.7,33.4,35.0]),'bo',ms=5)
plt.errorbar(I3,np.array([31.6,33.35,35.05]),np.array([0.1,0.05,0.05]),fmt='bo',ms=5,label='T06 block pt1000 (uncoated)')
#plt.plot(I3,np.array([32.2,33.8,35.5]),'rx',ms=5,label='T07 block pt1000 (uncoated)')
#plt.plot(I3,np.array([31.9,33.5,35.3]),'rx',ms=5)
plt.errorbar(I3,np.array([32.05,33.65,35.4]),np.array([0.15,0.15,0.1]),fmt='rx',ms=5,label='T07 block pt1000 (uncoated)')
#plt.plot(I3,np.array([31.6,33.3,35.0]),'gd',ms=5,label='T09 block pt1000 (coated)')
#plt.plot(I3,np.array([31.6,33.4,35.1]),'gd',ms=5)
plt.errorbar(I3,np.array([31.6,33.35,35.05]),np.array([0,0.05,0.05]),fmt='gd',ms=5,label='T09 block pt1000 (coated)')
#plt.plot(I3,np.array([31.9,33.7,35.6]),'v',color='orange',ms=5,label='T14 block pt1000 (coated)')
#plt.plot(I3,np.array([31.9,33.4,35.3]),'v',color='orange',ms=5)
#plt.plot(I3,np.array([32.1,33.8,35.5]),'v',color='orange',ms=5)
plt.errorbar(I3,np.array([32.0,33.6,35.5]),np.array([0.1,0.1,0.1]),fmt='v',color='orange',ms=5,label='T14 block pt1000 (coated)')

plt.xlabel('Current [A]')
plt.ylabel('Temperature [°C]')
plt.title('Temperature of coated vs uncoated modules')
plt.legend(loc='upper center',bbox_to_anchor=(0.5,-0.1 ))
plt.savefig('CoatedvsUncoated3.png',bbox_inches='tight')

plt.figure(dpi=200,figsize=(2,5))

#plt.plot(I3,np.array([45.0,48.3,51.3]),'bo',ms=5,label='T06 middle (uncoated)')
#plt.plot(I3,np.array([45.3,48.3,51.3]),'bo',ms=5)
plt.errorbar(I3,np.array([45.15,48.3,51.3]),np.array([0.15,0,0]),fmt='bo',ms=5,label='T06 middle (uncoated)')
#plt.plot(I3,np.array([45.3,47.5,50.8]),'rx',ms=5,label='T07 middle (uncoated)')
#plt.plot(I3,np.array([45.5,48.3,50.8]),'rx',ms=5)
#plt.plot(I3,np.array([45.3,47.0,50.0]),'rx',ms=5)
plt.errorbar(I3,np.array([45.4,47.6,50]),np.array([0.1,0.4,0.3]),fmt='rx',ms=5,label='T07 middle (uncoated)')
#plt.plot(I3,np.array([48.3,51.5,55.0]),'gd',ms=5,label='T09 middle (coated)')
#plt.plot(I3,np.array([48.3,51.8,55.3]),'gd',ms=5)
plt.errorbar(I3,np.array([48.3,51.65,55.15]),np.array([0,0.15,0.15]),fmt='gd',ms=5,label='T09 middle (coated)')
#plt.plot(I3,np.array([46.8,49.8,52.5]),'v',color='orange',ms=5,label='T14 middle (coated)')
#plt.plot(I3,np.array([44.5,47.5,50.5]),'v',color='orange',ms=5)
#plt.plot(I3,np.array([44.8,47.3,50.3]),'v',color='orange',ms=5)
plt.errorbar(I3,np.array([45.4,48.2,51.1]),np.array([0.7,0.8,0.7]),fmt='v',color='orange',ms=5,label='T14 middle (coated)')

plt.xlabel('Current [A]')
plt.ylabel('Temperature [°C]')
plt.title('Temperature of coated vs uncoated modules')
plt.legend(loc='upper center',bbox_to_anchor=(0.5,-0.1 ))
plt.savefig('CoatedvsUncoated4.png',bbox_inches='tight')