#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Usage: 
#   ./00-fetch-display-save.py -i ./flower.jpg
#   ./00-fetch-display-save.py -h

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

# loading image into cv3 window
# wait for key press
# write image into another format
# close the image display window
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.imwrite(args['image']+'.png', image)
cv2.destroyAllWindows()
