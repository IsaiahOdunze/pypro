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
    #parameters-the object,top corner of rec,bottom corner,BGR,linewidth
    frame=cv2.rectangle(frame,(340,100),(400,170),(0,255,0),7) 
    #parameters-the center of circ,radius,BGR,linewidth(-1 makes colored in)
    frame=cv2.circle(frame,(320,240),50,(255,130,255),-1)
    fnt = cv2.FONT_HERSHEY_DUPLEX  #font for the Text in cv2 
    #parameters- object,'actual Text',(coordinates),font,size,BGR, line widt
    frame=cv2.putText(frame,'First Text',(300,300),fnt,1.5,(255,0,150),3)
    #parameters-object,first coords, second coords, BGR, thickness
    frame=cv2.line(frame,(10,10),(630,470),(0,0,0),4)
    #parameters-object,first coords, second coords, BGR, thickness
    cv2.arrowedLine(frame,(10,470),(630,10),(255,255,255),1)
    cv2.imshow('Gunshow',frame)
    cv2.moveWindow('Gunshow',0,0)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release() 
cv2.destroyAllWindows()