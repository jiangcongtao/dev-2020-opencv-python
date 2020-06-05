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
cv2.imshow('Original', image)

# Split image to B G R channels
(b, g, r) = cv2.split(image)
cv2.imshow("Red", r)
cv2.imshow("Green", g)
cv2.imshow("Blue", b)

# Merge B G R channels 
merged = cv2.merge([b, g, r])
cv2.imshow('Merged', merged)

# Show b, r, g image
zeros = np.zeros(image.shape[:2], dtype='uint8')
cv2.imshow('Red Image', cv2.merge([zeros, zeros, r]))
cv2.imshow('Green Image', cv2.merge([zeros, g, zeros]))
cv2.imshow('Blue Image', cv2.merge([b, zeros, zeros]))
# wait for key press
# close the image display window.
cv2.waitKey(0)
cv2.destroyAllWindows()
