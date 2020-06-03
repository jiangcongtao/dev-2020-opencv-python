#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2

img = cv2.imread("./flower.jpg")
cv2.namedWindow("Flower", cv2.WINDOW_NORMAL)
cv2.imshow("Flower", img)

cv2.waitKey(0)
cv2.imwrite("output.jpg", img)

# Inspect image infomation
print(len(img)) # row length
print(len(img[0])) # column length per row
print(img.shape) 
print(img.dtype)
print(img.size) # image size. num of pixels in image x*h*channel
print(img[10,5])
img[10,5]