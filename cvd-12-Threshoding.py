#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import cv2
import imutils
import numpy as np

# fetch the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
ap.add_argument('-s', '--size', required=False, default=3, help='Kernel size of gaussian blur')
args = vars(ap.parse_args())

kernelSize = int(args['size'])

image = cv2.imread(args['image'])
cv2.imshow('Original BGR Color Space', image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Gaussian blurring
blurred  = cv2.GaussianBlur(gray, (kernelSize,kernelSize), 0)
cv2.imshow('Gray and Gaussian Blurring', np.hstack([gray,blurred]))
cv2.waitKey(0)

# Thresholding
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold Binary', thresh)
cv2.waitKey(0)

(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Threshold Binary Inverse', threshInv)
cv2.waitKey(0)

cv2.imshow('Coins', cv2.bitwise_and(image, image, mask=threshInv))
cv2.waitKey(0)

thresh = cv2.adaptiveThreshold(blurred, 255, 
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow('Mean Thresh', thresh)
cv2.waitKey(0)

thresh = cv2.adaptiveThreshold(blurred, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow('Gaussian Thresh', thresh)
cv2.waitKey(0)

# close the image display window.
cv2.destroyAllWindows()
