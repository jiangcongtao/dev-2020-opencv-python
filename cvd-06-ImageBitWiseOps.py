#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import cv2
import imutils
import numpy as np

# create 300x300 numpy array and 250x250 white rectangle inside it
rectangle = np.zeros((300,300), dtype='uint8')
cv2.rectangle(rectangle, (25,25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

# create 300x300 numpy array and radius circle white rectangle inside it
circle = np.zeros((300,300), dtype='uint8')
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow('NOT', bitwiseNot)


# wait for key press
# close the image display window.
cv2.waitKey(0)
cv2.destroyAllWindows()
