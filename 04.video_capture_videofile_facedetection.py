#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Realtime video capture from webcam

import numpy as np
import cv2 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture('/Users/nickjiang/Downloads/test.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

time_ms_wait = int(1000 / fps)
print("time_ms_wait = {0}".format(time_ms_wait))

while(True):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    # Convert BGR color to gray color
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # face detection causes computing power. which slowing video playing speed!!!
    faces = face_cascade.detectMultiScale(grey_frame, 
                    scaleFactor=1.03,
                    minNeighbors = 5)
    # print(faces)

    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)

    # show grey image
    cv2.imshow('Frame', frame)

    # Wait for 1 millisecond, press 'q' to exit
    ch = cv2.waitKey(time_ms_wait)
    if ch & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()