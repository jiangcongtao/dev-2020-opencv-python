#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt

# fetch the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('BGR Color Space', image)
# Convert to gray, hsv, lab color space
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Gray Scale Image', gray)

# calculate histogram
hist = cv2.calcHist([gray],[0], None, [256], [0, 256])
# Plot histogram
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

# wait for key press
# close the image display window.
cv2.waitKey(0)
cv2.destroyAllWindows()
