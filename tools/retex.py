import cv2 
import numpy as np

cap = cv2.VideoCapture(0)

def apply_retinex(image, sigma=10):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a logarithmic transform
    log_image = np.log1p(gray_image.astype(np.float32))

    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(log_image, (0, 0), sigma)

    # Calculate the reflectance
    reflectance_image = log_image - blurred_image

    # Rescale the reflectance image
    reflectance_image = cv2.normalize(reflectance_image, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    return reflectance_image

while(1):

    _,frame = cap.read()
    frame = apply_retinex(image=frame)

    if _ == True:
        cv2.imshow("diaplay",frame)
    if cv2.waitKey(1) & 0xff ==("q"):
        break

cap.release()
cv2.destroyAllWindows()