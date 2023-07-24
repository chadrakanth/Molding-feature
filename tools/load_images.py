
import cv2

cv2.namedWindow('display1',cv2.WINDOW_GUI_NORMAL)
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button down event
        pixel_value = img_gray[y, x]  # Retrieve pixel value at (x, y) coordinates
        print("Pixel value at ({}, {}): {}".format(x, y, pixel_value))

cv2.setMouseCallback('display1', mouse_callback)

def find_dark(image):
    img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("display1",img_gray)
    _,thres_img = cv2.threshold(img_gray,80,255,cv2.THRESH_BINARY)
    countours, hirearicy = cv2.findContours(image=thres_img,mode=cv2.RETR_TREE,method=cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(image, countours[0:], -1, (0, 255, 0), 3)
    cv2.imshow("display2",thres_img)
    cv2.imshow("display3",image)
   
    
#cap = cv2.VideoCapture(0)
#while True:
#    _,frame = cap.read()
#    find_dark(frame)
#    if cv2.waitKey(1) & 0xff == ord("q"):
#        break

# img = cv2.imread("/home/pc/workspace/SSG/black_teeth_algorithm/image_asset/1.png")
# cv2.imshow("diaplay",img)
    
img = cv2.imread("/home/ssg/Desktop/black_mark/sample_images/0.png")
find_dark(img)
cv2.waitKey(0)
    
    
cap.release()
cv2.destroyAllWindows()

