# -*- coding: utf-8 -*-
"""
Created on Sat May 15 19:11:27 2021

@author: Fetibek Aliev
"""

import matplotlib.pyplot as plt

from matplotlib.patches import Circle, Wedge, Polygon, Ellipse, Arc, Path, PathPatch

plt.xlim(0, 12)

plt.ylim(0, 12)

ax = plt.gca()

circle = Circle((6, 7),5)

ax.add_patch(circle)

ax.set_aspect(1)

plt.show()