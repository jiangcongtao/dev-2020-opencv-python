#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Resize operation needs to take consideration of image
# aspect ratio

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

resized = imutils.resize(image, 300)
cv2.imshow('Resize to width to 300 pixels', resized)

resized = imutils.resize(image, 800, inter=cv2.INTER_CUBIC)
cv2.imshow('Resize to width to 800 pixels', resized)

resized = imutils.resize(image, 1440, inter=cv2.INTER_CUBIC)
cv2.imshow('Resize to width to 1440 pixels', resized)

# wait for key press
# close the image display window.
cv2.waitKey(0)
cv2.destroyAllWindows()
