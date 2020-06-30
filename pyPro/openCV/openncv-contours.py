import cv2
import numpy as np  
print(cv2.__version__)
stored=-1

def nothing(x):
    pass
cv2.namedWindow('trackbars')
cv2.moveWindow('trackbars',1320,0)


cv2.createTrackbar('hueLow','trackbars',50,179,nothing)
cv2.createTrackbar('hueHigh','trackbars',100,179,nothing)
cv2.createTrackbar('hueLow2','trackbars',50,179,nothing)
cv2.createTrackbar('hueHigh2','trackbars',100,179,nothing)
cv2.createTrackbar('satLow','trackbars',100,255,nothing)
cv2.createTrackbar('satHigh','trackbars',255,255,nothing)
cv2.createTrackbar('valLow','trackbars',100,255,nothing)
cv2.createTrackbar('valHigh','trackbars',255,255,nothing)


dispW=640
dispH=480
flip=2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet) #for the piCam
#cam =cv2.VideoCapture(0)for the logitech
while True:
    ret,frame= cam.read()
    #frame=cv2.imread('smarties.png')
    

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    hueLow=cv2.getTrackbarPos('hueLow','trackbars')
    hueHigh=cv2.getTrackbarPos('hueHigh','trackbars')

    hueLow2=cv2.getTrackbarPos('hueLow2','trackbars')
    hueHigh2=cv2.getTrackbarPos('hueHigh2','trackbars')


    satLow=cv2.getTrackbarPos('satLow','trackbars')
    satHigh=cv2.getTrackbarPos('satHigh','trackbars')

    valLow=cv2.getTrackbarPos('valLow','trackbars')
    valHigh=cv2.getTrackbarPos('valHigh','trackbars')

    lb=np.array([hueLow,satLow,valLow])
    ub=np.array([hueHigh,satHigh,valHigh])

    lb2=np.array([hueLow2,satLow,valLow])
    ub2=np.array([hueHigh2,satHigh,valHigh])
    #print('lb',lb)
    #print('ub',ub)

    FGMask=cv2.inRange(hsv,lb,ub)
    FGMask2=cv2.inRange(hsv,lb2,ub2)
    FGMaskComp=cv2.add(FGMask,FGMask2)
    cv2.imshow('FGMaskcomp',FGMaskComp)
    cv2.moveWindow('FGMaskcomp',0,530)


   # _,contours,_=cv2.findContours(FGMaskComp,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
   # cv2.drawCountours(frame,contours,-1,(255,0,0),3)

    cv2.imshow('smarties',frame)
    cv2.moveWindow('smarties',0,0)


 #   cv2.imshow('Gunshow',frame)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release() 
cv2.destroyAllWindows()