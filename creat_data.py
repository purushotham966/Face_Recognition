
#***make sure that name you are entering in the input should be already created in the images folder.


import cv2
import numpy as np
cam=cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('cascades\data\haarcascade_frontalface_default.xml')


Id=input('enter your id: ')
name=input("enter name yhat was already created in directery:")
sampleNum=0



while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
    
        
#incrementing sample number
        sampleNum=sampleNum+1
#saving the captured face in the dataset folder
        cv2.imwrite("images/"+name+"/"+"User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w]) // name should already be created in images folder.
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('frame',img)
#wait for 100 miliseconds
    if cv2.waitKey(100) & 0xFF == ord('q'):
    
        break
# break if the sample number is morethan 20
    elif sampleNum>20:
        break
cam.release()
cv2.destroyAllWindows()
