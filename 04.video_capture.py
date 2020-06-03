#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Realtime video capture from webcam

import numpy as np
import cv2 

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    cv2.imshow('Frame', frame)

    # Wait for 1 millisecond, press 'q' to exit
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()