# import necessary libraries
import cv2
import os

if not os.path.exists("frames"): # A condition that if the directory is not exist create it
    os.makedirs("frames")

cap = cv2.VideoCapture('videos/video1_with_anomalies.mp4') # read video

ret, frame = cap.read() # read each frame of vide
count = 0

while ret:
    cv2.imwrite("frames/frame%d.jpg" % count, frame) # store each frame to created folder
    ret, frame = cap.read() # read the next frame
    count += 1

cap.release()