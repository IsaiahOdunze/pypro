import cv2
print(cv2.__version__)
dispW=960
dispH=720
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet) #for the piCam
#cam =cv2.VideoCapture(0)for the logitech
while True:
    ret,frame= cam.read()
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',700,0)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    frameSmall=cv2.resize(frame,(320,240))
    graySmall=cv2.resize(gray,(320,240))
    cv2.moveWindow('BW',0,265)
    cv2.moveWindow('piSmall',0,0)
    cv2.imshow('BW',graySmall)
    cv2.imshow('piSmall',frameSmall)

    cv2.moveWindow('BW2',385,265)
    cv2.moveWindow('piSmall2',385,0)
    cv2.imshow('BW2',graySmall)
    cv2.imshow('piSmall2',frameSmall)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release() 
cv2.destroyAllWindows()