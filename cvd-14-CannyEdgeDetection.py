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

image =  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow('Blurred', image)
cv2.waitKey(0)

canny50 = cv2.Canny(image, 30, 50)
canny150 = cv2.Canny(image, 30, 150)
cv2.imshow('Canny Edge Detection', np.hstack([canny50, canny150])) 
cv2.waitKey(0)

# close the image display window.
cv2.destroyAllWindows()
