import cv2
import numpy as np 
print(cv2.__version__)
evt=-1
coord=[]
img=np.zeros((250,250,3),np.uint8)
def click(event,x,y,flags,params):
    global pnt 
    global evt
    if event==cv2.EVENT_LBUTTONDOWN:
        print("Mouse event was: ",event)
        print(x,',',y)
        pnt=(x,y)
        coord.append(pnt)
      #  print(coord)
        evt=event
    if event==cv2.EVENT_RBUTTONDOWN:
        print(x,y)
        blue=frame[y,x,0]
        green=frame[y,x,1]
        red=frame[y,x,2]
        print(blue,green,red)
        colorString=str(blue)+','+str(green)+','+str(red)
        img[:]=[blue,green,red]
        fnt=cv2.FONT_HERSHEY_PLAIN
        r=255-int(red)
        g=255-int(green)
        b=255-int(blue)
        tp=(b,g,r)
        cv2.putText(img,colorString,(10,25),fnt,1,tp,2)
        cv2.imshow('myColor',img)
dispW=640
dispH=480
flip=2
cv2.namedWindow('Gunshow')
cv2.setMouseCallback('Gunshow',click)
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet) #for the piCam
#cam =cv2.VideoCapture(0)for the logitech
while True:
    ret,frame= cam.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame=cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    for pnts in coord:
        cv2.circle(frame,pnts,5,(0,255,0),-1)
        font=cv2.FONT_HERSHEY_PLAIN
        myStr=str(pnts)
        cv2.putText(frame,myStr,pnts,font,1.2,(0,0,255),2)
    cv2.imshow('Gunshow',frame)
    cv2.moveWindow('Gunshow',0,0)
    keyEvent=cv2.waitKey(1)
    if keyEvent==ord('q'):
        break
    if keyEvent==ord('c'):
        coord = []
cam.release() 
cv2.destroyAllWindows()