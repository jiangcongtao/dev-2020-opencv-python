#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2

black = np.zeros([200, 300, 1], 'uint8')
cv2.imshow('Black', black)
print(black[0, 0, :])

ones = np.ones([200, 300, 3], 'uint8')
cv2.imshow('Ones', ones)
print(ones[0, 0, :])

white = np.ones([200, 300, 3], 'uint16')
white *= 2**16 - 1
cv2.imshow('White', white)
print(white[0, 0, :])

color = ones.copy()
color[:,:] = (255,0,0)
cv2.imshow('Color', color)
print(color[0, 0, :])

cv2.waitKey(0)
cv2.destroyAllWindows()
