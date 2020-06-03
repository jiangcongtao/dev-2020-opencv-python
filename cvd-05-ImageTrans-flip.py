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

flipped = cv2.flip(image, 1)
cv2.imshow('Horizontally Flip', flipped)

flipped = cv2.flip(image, 0)
cv2.imshow('Vertically Flip', flipped)

flipped = cv2.flip(image, -1)
cv2.imshow('Both Horizontally and Vertically Flip', flipped)

# wait for key press
# close the image display window.
cv2.waitKey(0)
cv2.destroyAllWindows()
