#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2

# canvas : (height/rows, width/columns, channels)
width = 800
height = 600
canvas = np.zeros((height, width, 3), dtype='uint8')
gray = (128, 128, 128)
black = (0, 0, 0)
# Set canvas background
canvas[:, :] = gray

# generate random radius, color, center point
for i in range(0, 50):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high = width, size=(2,))
    # filling drawing: point (x, y)
    cv2.circle(canvas, tuple(pt), radius, color, -1)

    # draw text title
    cv2.putText(canvas, 
            "Draw Random Circles", 
            (int(width/2 - 300), int(height/2)), 
            cv2.FONT_HERSHEY_SIMPLEX,
            2, black, 2)
    cv2.imshow('circles', canvas)
    cv2.waitKey(100)


# wait for key press
# close the image display window
cv2.waitKey(0)
cv2.destroyAllWindows()
