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
cv2.imshow('BGR Color Space', image)
cv2.waitKey(0)

# Convert to gray, hsv, lab color space
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', hsv)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow('lab', lab)
# wait for key press
# close the image display window.
cv2.waitKey(0)
cv2.destroyAllWindows()
