import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2


camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet) #for the piCam
#cam =cv2.VideoCapture(0)for the logitech
dispW=int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
dispH=int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
xPos=100
yPos=270
boxW=int(.15*dispW)
boxH=int(.15*dispH)

dX=5
dY=5
while True:
    ret,frame= cam.read()
    #parameters-the object,top corner of rec,bottom corner,GBR,linewidth
    frame=cv2.rectangle(frame,(xPos,yPos),(xPos+boxW,yPos+boxH),(0,255,0),-1) 

    cv2.imshow('Gunshow',frame)
    cv2.moveWindow('Gunshow',0,0)
    xPos=xPos+dX
    yPos=yPos+dY

    if(xPos+boxW > dispW or xPos < 0):
      dX=dX*-1
    if(yPos+boxH>dispH or yPos < 0):
      dY=dY*-1
 
    if cv2.waitKey(1)==ord('q'):
      break
        
cam.release() 
cv2.destroyAllWindows()

#direction should always be its own variable