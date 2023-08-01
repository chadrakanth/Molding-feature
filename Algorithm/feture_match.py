import cv2
import numpy as np

cv2.namedWindow("Result",cv2.WINDOW_GUI_NORMAL)

def find_template(image_gray, template_gray, threshold=0.7):
    # Convert the images to grayscale (necessary for template matching)
  

    # Perform template matching
    result = cv2.matchTemplate(image_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Get the location of the best match (top-left corner of the rectangle)
   
    loc = np.where(result >= threshold)
    locations = list(zip(*loc[::-1]))

    return locations

# Load the main image and the template image
template_image = '/home/ssg/Desktop/img_temp/left_top.png'

template_image = cv2.imread(template_image,0)

# Find the template in the main image
cap = cv2.VideoCapture(0)
while (1):
    _,main_image = cap.read()  
    main_image = cv2.cvtColor(main_image,cv2.COLOR_BGR2GRAY)
    result = find_template(main_image, template_image)

    # Draw a rectangle around the matched region on the main image
    for location in result:
        top_left = location
        bottom_right = (top_left[0] + template_image.shape[1], top_left[1] + template_image.shape[0])
        cv2.rectangle(main_image, top_left, bottom_right, (0, 255, 0), 2)

        


    # Display the result
    cv2.imshow('Result', main_image)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

