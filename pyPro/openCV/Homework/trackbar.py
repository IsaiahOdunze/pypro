import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2
def nothing(x):
    pass
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet) #for the piCam
cv2.namedWindow('Gunshow')
cv2.createTrackbar('xVal','Gunshow',0,dispW,nothing)
cv2.createTrackbar('yVal','Gunshow',0,dispH,nothing)
cv2.createTrackbar('width','Gunshow',10,dispW,nothing)
cv2.createTrackbar('height','Gunshow',10,dispH,nothing)
#cam =cv2.VideoCapture(0)for the logitech
while True:
    ret,frame= cam.read()
    xVal=cv2.getTrackbarPos('xVal','Gunshow')
    yVal=cv2.getTrackbarPos('yVal','Gunshow')
    width=cv2.getTrackbarPos('width','Gunshow')
    height=cv2.getTrackbarPos('height','Gunshow')
    cv2.rectangle(frame,(xVal,yVal),(xVal+width,yVal+height),(255,0,0),5)


    cv2.imshow('Gunshow',frame)
    cv2.moveWindow('Gunshow',0,0)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release() 
cv2.destroyAllWindows()