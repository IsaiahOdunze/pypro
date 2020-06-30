import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2
boxW=200
boxH=180
xpos=50
ypos=70
dx=5
dy=5
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet) #for the piCam
#cam =cv2.VideoCapture(0)for the logitech
while True:
    ret,frame= cam.read()
    roi=frame[ypos:ypos+boxH,xpos:xpos+boxW].copy()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame=cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    frame[ypos:ypos+boxH,xpos:xpos+boxW]=roi


    cv2.rectangle(frame,(xpos,ypos),(xpos+boxW,ypos+boxH),(0,0,255),5)
    xpos=xpos+dx
    ypos=ypos+dy
    if xpos<=0 or xpos+boxW>=dispW:
        dx=dx*-1
    if ypos<=0 or ypos+boxH>=dispH:
        dy=dy*-1

    cv2.imshow('Gunshow',frame)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release() 
cv2.destroyAllWindows()

#when you turn something gray, u lose its BGR value, so to put it back you have to 
 #go back from gray to BGR which will make it still gray but give it a BGR value