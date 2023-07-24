import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

# Initialize the camera and grab a reference to the raw capture
camera = PiCamera()
camera.resolution = (4056, 3040)  # Set the resolution to full definition
camera.framerate = 10  # Adjust the frame rate as needed
raw_capture = PiRGBArray(camera, size=(4056, 3040))

# Allow the camera to warmup
time.sleep(2)

try:
    for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
        image = frame.array

        # Add your OpenCV processing here
        # For example, you can resize the image for display:
        # resized_image = cv2.resize(image, (640, 480))

        # Display the processed image (optional)
        # cv2.imshow("Processed Image", resized_image)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

        # Clear the stream for the next frame
        raw_capture.truncate(0)

except KeyboardInterrupt:
    pass

# Release the camera and close OpenCV windows (if any)
camera.close()
cv2.destroyAllWindows()
