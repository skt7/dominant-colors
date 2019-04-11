# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 03:02:28 2018

@author: asus
"""

from dominantColors import DominantColors
import cv2

#open image
img = 'colors.jpg'
img = cv2.imread(img)

#convert to RGB from BGR
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#no. of clusters
clusters = 5

#initialize using constructor
dc = DominantColors(img, clusters)

#print dominant colors
colors = dc.dominantColors()
print(colors)

#display clustered points
dc.plotClusters()

#display dominance order
dc.plotHistogram()

