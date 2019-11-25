import threading
import cv2
import numpy as np
import sys
import time



class ImageRecognizer:
    
    def __init__(self):
        pass 


    def recognize(self):
        cap = cv2.VideoCapture(0)

        windowCenterX = -1
        windowCenterY = -1

        # Define the codec and create VideoWriter object
        # fourcc = cv2.VideoWriter_fourcc(*'XVID')

        # cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

        i = 0
    
        while(cap.isOpened()):
    
            i = i + 1

            time0 = time.time()
            ret, frame = cap.read()
    
            height = int( np.size(frame, 0) )
            width = int (np.size(frame, 1) )
    
            windowCenterX = int( float(width) / 2.0)
            windowCenterY = int( float(height) / 2.0)

            if ret==True:
                # frame = cv2.flip(frame,0)
    
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

                # define range of yellow color in HSV
                lower_yellow = np.array([23,41,133])
                upper_yellow = np.array([40,150,255])

                lower_orange = np.array([18, 40, 90])
                upper_orange = np.array([27, 255, 255])

                # Threshold the HSV image to get only yellow colors
                mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

                im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                # Bitwise-AND mask and original image
                res = cv2.bitwise_and(frame,frame, mask= mask)
                # cv2.imshow('frame',frame)
                # cv2.imshow('res', res)

                cv2.drawContours(res, contours, -1, (0,255,0), 3)
                # print("The number of countours is " + str(len(contours) ) )
        
                indexOfLargest = -1
                largestContour = -1
                for i in range( len(contours) ):
                    if ( (cv2.contourArea(contours[i], False) ) > largestContour):
                        largestContour = cv2.contourArea(contours[i], False)
                        indexOfLargest = i
     
                #print(indexOfLargest)
        
                cy = -1
                cx = -1 
                # Check that we really found a contour in the image
                if ( indexOfLargest != -1):
                    M = cv2.moments( contours[indexOfLargest] )
            
                    # FIX ME - Zero division error
                    try:
                        cx = int(M['m10']/M['m00'])
                        cy = int(M['m01']/M['m00'])
                    except:
                        cx = -1
                        cy = -1

                    cv2.drawContours( frame, [contours[indexOfLargest] ],  0, (0,255,0), 3 )
                    #print("The center of the circle is " + str(cx) + ", " + str(cy) )
              
                    # Draw a line to the center 
                    cv2.line(frame, (cx,cy), (windowCenterX * 2, cy), (255,255,255), 5)
                    cv2.line(frame, (cx,cy), (cx, windowCenterY * 2), (255,255,255), 5)
                    
                    # Update the threads data structures

                    # if ( (i % 5) == 0):
                    # correctY()



                # cv2.imshow('Title!!', frame)
         
                # write the flipped frame
                #cv2.out.write(frame)
    
                # cv2.imshow('frame',frame)
        
                #out.write(frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

            time1 = time.time()
            loopDuration = time1 - time0



        # Release everything if job is finished
        #cv2.cap.release()
        #cv2.out.release()
        cv2.destroyAllWindows()


