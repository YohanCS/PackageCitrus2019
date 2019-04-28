import cv2
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('./trainner/trainner.yml')
cascadePath = "./preData/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)


cam = cv2.VideoCapture(0)
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1.0
fontColor = (255, 255, 255)
ret, im = cam.read()
locy = int(im.shape[0]/2) # the text location will be in the middle
locx = int(im.shape[1]/2) 
cv2.putText(im, "Success!", (locx, locy), fontFace, fontScale, fontColor) 
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(conf<50):
            if(Id==1):
                Id="Anthony"
            elif(Id==2):
                Id="Jesnine"
        else:
            Id="Unknown"
        #cv2.putText(cv2.fromarray(im),str(Id), (x,y+h),font, 255)
        cv2.putText(im, str(Id), (x, y+h), fontFace, fontScale, fontColor, lineType=cv2.LINE_AA) 
    cv2.imshow('im',im) 
    if (cv2.waitKey(1)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()