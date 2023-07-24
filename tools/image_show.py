import cv2 

cap = cv2.VideoCapture(0)
num =0 

while True:
  
    _,frame = cap.read()
    if _ == True:
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
       
        cv2.imshow("display",frame)
        print(frame.shape)

     
        if cv2.waitKey(1) & 0xff == ord("p"):
            cv2.imwrite("/home/ssg/Desktop/project/"+str(num)+".png",frame)
            num += 1
            print(" saved num "+ str(num))
        if cv2.waitKey(1) & 0xff == ord("q"):
            
            break
print(frame.shape)
cap.release()
cv2.destroyAllWindows()