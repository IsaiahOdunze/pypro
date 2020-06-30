import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet) #for the piCam
#cam =cv2.VideoCapture(0)for the logitech
while True:
    ret,frame= cam.read()
    #frame is matrix (y,x)
    roi=frame[50:250,200:400].copy()
    roiGray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    roiGray=cv2.cvtColor(roiGray,cv2.COLOR_GRAY2BGR)
    frame[50:250,200:400]= roiGray
    cv2.imshow('ROI',roi)
    cv2.moveWindow('ROI',705,0)

    cv2.imshow('Gray',roiGray)
    cv2.moveWindow('Gray',705,250)
    cv2.imshow('Gunshow',frame)
    cv2.moveWindow('Gunshow',0,0)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release() 
cv2.destroyAllWindows()