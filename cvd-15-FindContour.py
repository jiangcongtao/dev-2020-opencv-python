#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import cv2
import imutils
import numpy as np

# fetch the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original Image', image)

grey =  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(grey, (15,15), 0)
cv2.imshow('Blurred', blurred)
cv2.waitKey(0)

cannyEdged = cv2.Canny(blurred, 30, 50)

(cnts,_) = cv2.findContours(cannyEdged.copy(),
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
print(' I count {} contours in this image'.format(len(cnts)))

imageCopied = image.copy()

cv2.drawContours(imageCopied, cnts, -1, (0, 255,0), 2)

cv2.imshow('Grey Scale and Edge', np.hstack([grey, cannyEdged])) 
cv2.imshow('Contours', imageCopied) 
cv2.waitKey(0)

# close the image display window.
cv2.destroyAllWindows()
