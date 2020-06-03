#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2

# canvas : (height/rows, width/columns, channels)
canvas = np.zeros((300, 500, 3), dtype='uint8')
green = (0, 255, 0)
red = (0, 0, 255)

# drawing: point (x, y)
cv2.line(canvas, (0,0), (500, 300), red)
cv2.rectangle(canvas,(0,0), (500, 300), green, 3 )
# fill the shape
cv2.rectangle(canvas,(30,50), (200, 100), green, -1 )
cv2.imshow('drawing', canvas)
 
# wait for key press
# close the image display window
cv2.waitKey(0)
cv2.destroyAllWindows()
