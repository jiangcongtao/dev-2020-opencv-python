#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Usage: 
#   ./00-fetch-display-save.py -i ./flower.jpg
#   ./00-fetch-display-save.py -h

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

rotated = imutils.rotate(image, 45)
cv2.imshow('Rotate by 45 degree', rotated)

rotated = imutils.rotate(image, -45)
cv2.imshow('Rotate by -45 degree', rotated)


rotated = imutils.rotate(image, 90)
cv2.imshow('Rotate by 90 degree', rotated)

rotated = imutils.rotate(image, -90)
cv2.imshow('Rotate by -90 degree', rotated)

rotated = imutils.rotate(image, -90, scale= 1.5)
cv2.imshow('Rotate by -90 degree and scaled 1.5', rotated)

rotated = imutils.rotate(image, -45, center= (0, 0))
cv2.imshow('Rotate by -90 degree, center= (30, 30)', rotated)


# wait for key press
# close the image display window.
cv2.waitKey(0)
cv2.destroyAllWindows()
