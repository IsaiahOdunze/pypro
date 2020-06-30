import cv2
print(cv2.__version__)
goFlag = 0
def click(event,x,y,flags,params):
    global x1,y1,x2,y2
    global goFlag
    if event==cv2.EVENT_LBUTTONDOWN:
     x1=x
     y1=y
     goFlag=0
    if event==cv2.EVENT_LBUTTONUP:
     x2=x
     y2=y
     goFlag=1 
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
    if goFlag==1 and x2-x1 > 10 and y2-y1 > 10:
      frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),5)
      roi = frame[y1:y2,x1:x2]
      cv2.imshow('Winner',roi)
    cv2.imshow('Gunshow',frame)
    cv2.moveWindow('Gunshow',0,0)
    keyEvent=cv2.waitKey(1)
    if keyEvent==ord('q'):
        break
    if keyEvent==ord('c'):
        coord = []
cam.release() 
cv2.destroyAllWindows()

#if you want tsomething that only becomes relevant after a certain event, consider using some type of flag