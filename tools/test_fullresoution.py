import cv2
import time

import timeit
# Open the camera capture
cap = cv2.VideoCapture(1)

cv2.namedWindow("Frame",cv2.WINDOW_GUI_NORMAL)

# Set the desired resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
#cap.set(cv2.CAP_PROP_FRAME_COUNT,30)

# Read and display frames
while True:
    val = timeit.timeit()
    ret, frame = cap.read()
    print(cap.get(cv2.CAP_PROP_FPS))
   
    if ret == True:
        cv2.imshow("Frame", frame)
        #print((timeit.timeit()-  val)/60)

        # Break the loop on 'q' key press
        #print((cv2.getTickCount()-val)/cv2.getTickFrequency())
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
