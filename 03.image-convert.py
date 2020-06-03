#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2

color = cv2.imread('flower.jpg',1)

gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
cv2.imwrite('flower-gray.jpg', gray)

b = color[:,:, 0]
g = color[:,:, 1]
r = color[:,:, 2]

rgba = cv2.merge((b,g,r,g))
cv2.imwrite('flower-rbga.png', rgba)
