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

# split image to channels B, G, R
channels = cv2.split(image)
colors = ('b', 'g', 'r')
plt.figure()
plt.title('Flattened Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.xlim([0, 256])

for (chan, color) in zip(channels, colors):
    # calculate histogram
    hist = cv2.calcHist([chan],[0], None, [256], [0, 256])
    # Plot histogram
    plt.plot(hist, color = color)

plt.show()

# wait for key press
# close the image display window.
cv2.waitKey(0)
cv2.destroyAllWindows()
