import cv2
print(cv2.__version__)
dispW=320
dispH=240
flip=2
def nothing(x):
    pass
cv2.namedWindow('blended')
cv2.createTrackbar('BlendValue','blended',50,100,nothing)
#images must be the same size for masking
cvLogo=cv2.imread('pl.jpg')#read an image
cvLogo=cv2.resize(cvLogo,(320,240))
cvLogoGray=cv2.cvtColor(cvLogo,cv2.COLOR_BGR2GRAY)
cv2.imshow('CVLOGOGRAY',cvLogoGray) 
cv2.moveWindow('CVLOGOGRAY',0,350)


camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet) #for the piCam
#cam =cv2.VideoCapture(0)for the logitech
#creating the threshold variables, one is not necessary (_)
_,BGMask=cv2.threshold(cvLogoGray,225,255,cv2.THRESH_BINARY)
cv2.imshow('BGMASK',BGMask)
cv2.moveWindow('BGMASK',385,100)

FGMask=cv2.bitwise_not(BGMask)
cv2.imshow('FGMASK',FGMask)
cv2.moveWindow('FGMASK',385,350)

FG=cv2.bitwise_and(cvLogo,cvLogo,mask=FGMask)
cv2.imshow('FG',FG)
cv2.moveWindow('FG',703,350)

while True:
    ret,frame= cam.read()
    BG=cv2.bitwise_and(frame,frame,mask=BGMask)

    cv2.imshow('BG',BG)
    cv2.moveWindow('BG',703,100)
    cv2.imshow('Gunshow',frame)
    cv2.moveWindow('Gunshow',0,100)

    compImage=cv2.add(BG,FG)
    cv2.imshow('CompImg',compImage)
    cv2.moveWindow('CompImg',1017,100)

    bv=cv2.getTrackbarPos('BlendValue','blended')/100
    bv2=1-bv
    blended=cv2.addWeighted(frame,bv,cvLogo,bv2,0)
    cv2.imshow('blended',blended)
    cv2.moveWindow('blended',1017,350)

    FG2=cv2.bitwise_and(blended,blended,mask=FGMask)
    cv2.imshow('fg2',FG2)
    cv2.moveWindow('fg2',1324,100)

    compFinal=cv2.add(BG,FG2)
    cv2.imshow('compFinal',compFinal)
    cv2.moveWindow('compFinal',1324,350)


    if cv2.waitKey(1)==ord('q'):
        break

cam.release() 
cv2.destroyAllWindows()