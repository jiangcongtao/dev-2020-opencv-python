#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import cv2

# fetch the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

# loading and converting the image into numpy array
# printing the corresponding values
image = cv2.imread(args['image'])
print('width of the image in pixeles is : {}'.format(image.shape[1]))
print('height of the image in pixeles is : {}'.format(image.shape[0]))
print('channels present in the image is : {}'.format(image.shape[2]))

# Show original image
cv2.imshow('Orignial', image)

# Manipluate single pixel
(b, g, r) = image[0,0]
print('Pixel at (0,0) - Red: {} Green: {} Blue: {}'.format(r, g, b))
image[0,0] = (0,0,255)
(b, g, r) = image[0,0]
print('Pixel at (0,0) - Red: {} Green: {} Blue: {}'.format(r, g, b))

# Manipluate pixel region
corner = image[0:50, 0:500] # rows/y: 50 columns/x: 100
cv2.imshow("Corner", corner)

# Change the color of 50x100 pixels to green
image[0:50, 0:500] = (0, 255, 00)
cv2.imshow('Updated', image)
 
# wait for key press
# close the image display window
cv2.waitKey(0)
cv2.destroyAllWindows()
