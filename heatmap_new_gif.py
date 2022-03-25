# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 11:52:37 2022
Temperature dependent on current

@author: Tamar
"""

from heatmap import draw_heatmap
import imageio
import matplotlib.pyplot as plt
import numpy as np

Amps = np.array([5.5,5.6,5.7,5.8,5.9,6.0,6.1,6.2,6.3,6.4,6.5])
Volts = np.array([2.1,2.1,2.1,2.1,2.2,2.2,2.2,2.3,2.3,2.3,2.3])
Watts = np.round(Amps*Volts,1)
print(Watts)
VDDD_0 = (30,30,30,29,29,29,29,29,29,28,28)
VDDA_0 = (14,14,13,13,13,13,13,13,13,13,13)
VDDD_1 = (28,28,28,27,27,27,27,27,27,27,27)
VDDA_1 = (17,17,16,16,16,16,16,16,16,16,16)
VDDD_2 = (31,31,30,30,29,29,29,29,29,29,28)
VDDA_2 = (17,17,17,17,17,17,16,16,16,16,16)
VDDD_3 = (30,29,29,29,28,28,28,28,28,28,28)
VDDA_3 = (17,18,17,17,17,17,17,16,16,16,16)
temps_55 = (45,56,64,65,47,45,51,56,37,42,52,48,50,54,60,57)
temps_56 = (44,58,64,67,46,46,53,56,37,43,50,49,51,55,60,58)
temps_57 = (45,58,66,69,47,46,53,58,38,44,53,49,53,56,62,59)
temps_58 = (46,60,67,70,47,48,54,58,38,44,55,51,53,58,63,60)
temps_59 = (47,60,69,71,48,48,56,60,38,45,55,52,54,59,65,61)
temps_60 = (46,62,70,72,48,48,57,61,39,45,55,51,54,60,66,62)
temps_61 = (48,63,72,75,49,50,56,62,40,47,56,54,55,60,67,64)
temps_62 = (48,65,74,76,49,50,60,64,40,48,58,53,55,62,68,65)
temps_63 = (49,65,75,78,50,51,60,65,40,47,59,54,57,63,70,66)
temps_64 = (51,67,76,80,50,53,61,65,42,48,60,56,57,65,72,68)
temps_65 = (50,67,78,82,51,53,63,67,41,49,60,58,58,65,73,69)
temps = (temps_55,temps_56,temps_57,temps_58,temps_59,temps_60,temps_61,temps_62,temps_63,temps_64,temps_65)


filenames = []
for i, temp in enumerate(temps):
    draw_heatmap(temp, 43, 83, "Module T06 - "+str(5.5+0.1*i)+"A / "+str(Watts[i])+"W", "inferno")
    filename = "./heatmap2_day2/"+str(5.5+0.1*i)+"A.png"
    filenames.append(filename)
    plt.savefig(filename)
"""

"""
images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave("./heatmap2_day2/A.gif", images, duration = [0.8*x for x in [1,1,1,1,1,1,1,1,1,1,5]])


"""
plt.figure()
plt.plot(Amps, VDDD_0, 'x')
plt.plot(Amps, VDDD_1, 'x')
plt.plot(Amps, VDDD_2, 'x')
plt.plot(Amps, VDDD_3, 'x')
"""