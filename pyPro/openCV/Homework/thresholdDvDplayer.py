import cv2
print(cv2.__version__)
dispW=320
dispH=240
flip=2
boxW=70
boxH=50
dx=1
dy=1
xpos=0
ypos=0

#making the orginal logo
pyLogo=cv2.imread('pl.jpg')
pyLogo=cv2.resize(pyLogo,(boxW,boxH)) 
cv2.imshow('pylogo',pyLogo)
cv2.moveWindow('pylogo',350,0)

#gray scaling the logo
pygLogo=cv2.cvtColor(pyLogo,cv2.COLOR_BGR2GRAY)
#pygLogo=cv2.cvtColor(pyLogo,cv2.COLOR_GRAY2BGR)
cv2.imshow('PYG',pygLogo)
cv2.moveWindow('PYG',350,250)


camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet) #for the piCam
#cam =cv2.VideoCapture(0)for the logitech

#creating threshold for bg mask
_,BGMask=cv2.threshold(pygLogo,240,255,cv2.THRESH_BINARY)
cv2.imshow('BGMask',BGMask)
cv2.moveWindow('BGMask',350,500)

#Fg mask is not of bg mask
FGMask = cv2.bitwise_not(BGMask)
cv2.imshow('FGMask',FGMask)
cv2.moveWindow('FGMask',350,770)

#making the fg by using and bitwise operator with FG mask
#FG=cv2.bitwise_and(pyLogo,pyLogo,mask=FGMask)
#cv2.imshow('FG',FG)
#cv2.moveWindow('FG',710,260)
FG=cv2.bitwise_and(pyLogo,pyLogo,mask=FGMask)
cv2.imshow('FG',FG)
cv2.moveWindow('FG',710,260)

while True:
    ret,frame= cam.read()
    #frame=cv2.rectangle(frame,(xpos,ypos),(xpos+boxW,ypos+boxH),(255,255,255),0)
    
    frameCopy=frame[ypos:ypos+boxH,xpos:xpos+boxW]
    BG=cv2.bitwise_and(frameCopy,frameCopy,mask=BGMask)
    cv2.imshow('BG',BG)
    cv2.moveWindow('BG',710,0)
    frame[ypos:ypos+boxH,xpos:xpos+boxW]=BG


    FG2=cv2.add(FG,frame[ypos:ypos+boxH,xpos:xpos+boxW])
    cv2.imshow('FG2',FG2)
    cv2.moveWindow('FG2',1010,0)
    frame[ypos:ypos+boxH,xpos:xpos+boxW]=FG2


    cv2.imshow('OGFrame',frame)
    cv2.moveWindow('OGFrame',0,0)

    xpos=xpos+dx
    ypos=ypos+dy
    if xpos <=0 or xpos+boxW>=dispW:
        dx=dx*-1
    if ypos <=0 or ypos+boxH>=dispH:
        dy=dy*-1

   # compImg=cv2.add(BG,FG)
   # cv2.imshow('compImg',compImg)
   # cv2.moveWindow('compImg',710,540)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release() 
cv2.destroyAllWindows()