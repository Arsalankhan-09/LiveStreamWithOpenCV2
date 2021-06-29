
import cv2

cap = cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    if ret == False:
        print("Frame is empty")
        break
    else:
        cv2.imshow('VIDEO', frame)
       
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
