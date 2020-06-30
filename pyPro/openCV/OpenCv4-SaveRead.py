import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2
#actually getting frames from camera(for piCam)
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam=cv2.VideoCapture(camSet) #for the piCam parameters live feed
cam=cv2.VideoCapture('videos/myCam.avi')#playing back a saved video from given directory
#outVid=cv2.VideoWriter('videos/myCam.avi',cv2.VideoWriter_fourcc(*'XVID'),21,(dispW,dispH))
#cam =cv2.VideoCapture(0)for the logitech
while True:
    ret,frame= cam.read()
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
   # outVid.write(frame)
    if cv2.waitKey(50)==ord('q'):
        break

cam.release() 
#outVid.release()
cv2.destroyAllWindows()