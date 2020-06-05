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

# Using rectangle mask
# create numpy array with zeros with exact width and height of image
mask = np.zeros(image.shape[:2], dtype='uint8')
(cX, cY) = (image.shape[1] // 2, image.shape[0]//2)
cv2.rectangle(mask, (cX-75, cY-75), (cX+75, cY+75), 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Rectangle Mask", mask)
cv2.imshow("Rectangle Mask Applied to Image", masked)
cv2.waitKey(0)

# Using circle mask
mask = np.zeros(image.shape[:2], dtype='uint8')
cv2.circle(mask, (cX, cY), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Circle Mask", mask)
cv2.imshow("Cricle Mask Applied to Image", masked)

# wait for key press
# close the image display window.
cv2.waitKey(0)
cv2.destroyAllWindows()
