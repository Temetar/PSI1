# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 09:30:50 2022

@author: Tamar
Goal: Create a 2D-Heatmap from discrete temperature points
"""

import numpy as np
import seaborn as sb
import scipy
import matplotlib.pyplot as plt


lenx = 400//10
leny = 232//10
measurement_x_0 = 200-np.array([1,1,62,33])
measurement_y_0 = 232-np.array([113,7,3,3])
measurement_values_0 = np.array([45,51,48,53])
measurement_x_1 = 400-np.array([1,1,62,33])
measurement_y_1 = 232-np.array([113,7,3,3])
measurement_values_1 = np.array([55,58,60,60])
measurement_x_2 = 200+np.array([1,1,62,33])
measurement_y_2 = np.array([113,7,3,3])
measurement_values_2 = np.array([46,60,56,60])
measurement_x_3 = np.array([1,1,62,33])
measurement_y_3 = np.array([113,7,3,3])
measurement_values_3 = np.array([0,0,0,0])

measurement_x = np.concatenate((measurement_x_0,measurement_x_1,measurement_x_2,measurement_x_3))//10
measurement_y = np.concatenate((measurement_y_0,measurement_y_1,measurement_y_2,measurement_y_3))//10
measurement_values = np.concatenate((measurement_values_0,measurement_values_1,measurement_values_2,measurement_values_3))


#print(np.array((measurement_x_3,measurement_y_3)).transpose())
def draw_heatmap(measurement_values, tmin=None, tmax=None, title="TITLE", cmap=None):
    sb.set(font_scale=2.5)
    measurement_x = np.array([19,19,13,16,39,39,33,36,20,20,26,23,0,0,6,3])
    measurement_y = np.array([11,22,22,22,11,22,22,22,11,0,0,0,11,0,0,0])
    heatmap = np.zeros((lenx,leny))
    for x in range(lenx):
        for y in range(leny):
            distances = np.linalg.norm(np.array((measurement_x,measurement_y)).transpose()-(x,y),axis=1)
            distance_factors = 1/distances**2
            total_distance = sum(distance_factors)
            temperature = np.dot(distance_factors, measurement_values)/total_distance
            heatmap[x,y] = temperature
    fig, ax = plt.subplots(figsize=(13,13))
    plt.title(title,size=40)
    sb.heatmap(heatmap,square=True,vmin=tmin,vmax=tmax,cmap=cmap,xticklabels=False,yticklabels=False)

#draw_heatmap(measurement_values)

#for i, point in enumerate(np.array((measurement_x,measurement_y)).transpose()):
#    heatmap[point[0]][point[1]] = 1000

"""
x_values = np.concatenate((measurement_x,np.array([-10,-10,410,410])))
y_values = np.concatenate((measurement_y,np.array([-10,242,-10,242])))
z_values = np.concatenate((measurement_values,np.array([20,20,20,20])))

f = scipy.interpolate.interp2d(x_values,y_values,z_values)
for x in range (lenx):
    for y in range(leny):
        heatmap[x,y] = f(x,y)
"""


#for i, x in enumerate(measurement_x):
#    print(x,measurement_y[i],measurement_values[i],f(x,measurement_y[i]))

