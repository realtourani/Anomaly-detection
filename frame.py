# import necessary libraries
import cv2

cap = cv2.VideoCapture('videos/video1_with_anomalies.mp4') # read video

ret, frame = cap.read() # read each frame of vide
count = 0

while ret:
    cv2.imwrite("frames/frame%d.jpg" % count, frame) # store each frame to created folder
    ret, frame = cap.read() # read the next frame
    count += 1

cap.release()