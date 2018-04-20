# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 03:02:28 2018

@author: asus
"""

from dominantColors import DominantColors

img = 'colors.jpg'
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

