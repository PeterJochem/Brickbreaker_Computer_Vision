
#####
import numpy as np
import math
import cv2 as cv
#####


# Start reading info from the video stream 
cap = cv.VideoCapture(0)


# Keep getting the next frame and processing it
while(True):
    
    # Capture frame-by-frame
    
    # Image is an individual image
    ret, image = cap.read()
    # Our operations on the frame come here

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    # Display the resulting frame
    cv.imshow('Video', image)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()






# Execution starts here








