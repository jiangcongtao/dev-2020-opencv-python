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

shifted = imutils.translate(image, 0, 100)
cv2.imshow('Shifted Down', shifted)


shifted = imutils.translate(image, 0, -100)
cv2.imshow('Shifted Up', shifted)

shifted = imutils.translate(image, 100, 0)
cv2.imshow('Shifted Right', shifted)

shifted = imutils.translate(image, -100, 0)
cv2.imshow('Shifted Left', shifted)

# wait for key press
# close the image display window.
cv2.waitKey(0)
cv2.destroyAllWindows()
