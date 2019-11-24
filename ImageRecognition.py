
#####
import numpy as np
import math
import cv2
#####


# Start reading info from the video stream 
cap = cv2.VideoCapture(0)


# Keep getting the next frame and processing it
while(True):
    
    # Capture frame-by-frame
    
    # Image is an individual image
    ret, image = cap.read()
    # Our operations on the frame come here

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Display the resulting frame
    cv2.imshow('Video', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()






# Execution starts here








