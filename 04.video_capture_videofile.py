#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Realtime video capture from webcam

import numpy as np
import cv2 

cap = cv2.VideoCapture('/Users/nickjiang/Downloads/Breaking.Bad.S04E01.mp4')
while(True):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    # Convert BGR color to gray color
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame', frame)

    # Wait for 1 millisecond, press 'q' to exit
    ch = cv2.waitKey(50)
    if ch & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()