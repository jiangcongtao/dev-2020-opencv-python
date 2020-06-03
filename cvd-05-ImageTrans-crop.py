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

# Crop image (cat eyes) using numpy array slicing syntax
# X means X-axis (left to right), Y means Y-axis (up to down)
# image[Y_start:Y_end, X_start:X_end]
cropped = image[114:160, 191:340]
cv2.imshow('Crop', cropped)

# wait for key press
# close the image display window.
cv2.waitKey(0)
cv2.destroyAllWindows()
