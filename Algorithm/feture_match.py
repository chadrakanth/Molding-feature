import cv2

cv2.namedWindow("Result",cv2.WINDOW_GUI_NORMAL)

def find_template(image_gray, template_gray, threshold=0.7):
    # Convert the images to grayscale (necessary for template matching)
  

    # Perform template matching
    result = cv2.matchTemplate(image_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Get the location of the best match (top-left corner of the rectangle)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        # Get the width and height of the template image
        template_width, template_height = template_gray.shape[::-1]

        # Calculate the bottom-right corner of the rectangle
        bottom_right = (max_loc[0] + template_width, max_loc[1] + template_height)

        return max_loc, bottom_right
    else:
        return None

# Load the main image and the template image
template_image = '/home/ssg/project/0.png'

template_image = cv2.imread(template_image,0)

# Find the template in the main image
cap = cv2.VideoCapture(0)
while (1):
    _,main_image = cap.read()  
    main_image = cv2.cvtColor(main_image,cv2.COLOR_BGR2GRAY)
    main_image= main_image[190:250,270:380]
    result = find_template(main_image, template_image)

    # Draw a rectangle around the matched region on the main image

        

    if result is not None:
        top_left, bottom_right = result

        # Draw a rectangle around the matched region on the main image
        cv2.rectangle(main_image, result[0], result[1], (0, 255, 0), 2)
    else:
        print("Template not found.")

    # Display the result
    cv2.imshow('Result', main_image)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

