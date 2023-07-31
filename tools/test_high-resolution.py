import cv2
import threading

# Function to capture frames from the camera
def capture_frames():
    global frame

    # Open the camera capture
    cap = cv2.VideoCapture(1)

    # Set the desired resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)

    while True:
        # Read the frame
        ret, frame = cap.read()

        # Break the loop if there's an issue reading the frame
        if not ret:
            break

    # Release the capture
    cap.release()

# Function to process and display frames
def process_frames():
    while True:
        global frame

        # Perform image processing operations on the frame
        # Here, you can apply any desired image processing algorithms

        # Display the frame
        if frame !=0:
            cv2.imshow("Frame", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Global variable to share the frame between threads
frame = None

# Start the capture thread
capture_thread = threading.Thread(target=capture_frames)
capture_thread.start()

# Start the processing thread
process_thread = threading.Thread(target=process_frames)
process_thread.start()

# Wait for both threads to finish
#capture_thread.join()
#process_thread.join()

# Close all windows
cv2.destroyAllWindows()
