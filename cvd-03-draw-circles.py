#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2

# canvas : (height/rows, width/columns, channels)
canvas = np.zeros((300, 500, 3), dtype='uint8')
green = (0, 255, 0)
red = (0, 0, 255)
gray = (128, 128, 128)

# Set canvas background
canvas[:, :] = gray

# filling drawing: point (x, y)
cv2.circle(canvas, (250,150), 60, red, -1)
# no filling drawing: point (x, y)
cv2.circle(canvas, (250,150), 100, green, 4)

# draw concentric circles
for r in range(120, 500, 10):
    cv2.circle(canvas, (250,150), r, red, 1)

# draw text title
cv2.putText(canvas, 
        "Draw Concentric Circles", 
        (150, 20), 
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6, green,1)
cv2.imshow('circles', canvas)


# wait for key press
# close the image display window
cv2.waitKey(0)
cv2.destroyAllWindows()
