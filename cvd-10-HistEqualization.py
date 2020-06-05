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
cv2.imshow('Original BGR Color Space', image)

# Histogram equalization can only work on gray scaled image
# Histogram equalization is a technique for enhancing image to be more readable
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalized = cv2.equalizeHist(gray)

cv2.imshow('Histogram Equalization', np.hstack([gray, equalized]))

# wait for key press
# close the image display window.
cv2.waitKey(0)
cv2.destroyAllWindows()
