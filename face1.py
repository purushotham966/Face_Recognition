#Firstly run face_train.py then run this

import pickle
import cv2
import smtplib
import numpy as np
face_cascade=cv2.CascadeClassifier("cascades/data/haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels={"person_name":1}
with open("labels.pickle","rb") as f:
    og_labels=pickle.load(f)
    labels={v:k for k,v in og_labels.items()}
    
cap=cv2.VideoCapture(0)

minW = 0.1*cap.get(3)
minH = 0.1*cap.get(4)
count=0
Num=0
flag=0
while(True):
    
    ret,frame =cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5,minSize=(int(minW),int(minH)))
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        Num=Num+1
        roi_gray=gray[y:y+h, x:x+w]
        roi_color=frame[y:y+h, x:x+w]
        cv2.rectangle(frame,(x,y),(x+h,y+h),(255,0,0),2)
    
        id_, conf = recognizer.predict(roi_gray)  
        front=cv2.FONT_HERSHEY_SIMPLEX
        
        color=(255,255,255)
        stroke=2
        print(conf)
        # Check if confidence is less them 100 ==> "0" is perfect match 
        if conf>=45 and conf<=70:       #confidence(conf) depends on the dataset you taken 
            print(id_)                  #you can adjest conf according to...
            print(labels[id_])
            name=labels[id_]
                
            confidence = "  {0}%".format(round(100 - conf))                                                                        
           

            cv2.putText(frame,name,(x,y),front,1,color,stroke,cv2.LINE_AA)
            cv2.putText(frame, str(confidence), (x+5,y+h-5), front, 1,color, 1)
        else:
            cv2.putText(frame,"unknown",(x,y),front,1,color,stroke,cv2.LINE_AA)
            count=count+1
        if count>20:
            print("unknown face is recognised many times")
            flag=1
            
            import mail           #please run any of these mail or sms by commenting other one
                                   #if you run mail and sms at a time then it will going to hang... because smtp will take time to send mail same as sms 
            #import sms
            break
            

       

    cv2.imshow("frame",frame)
    if cv2.waitKey(20)&0xFF==ord("q"):
        break
    elif Num>50:
        break
    elif flag==1:
        img_item="my_img.png"
        cv2.imwrite(img_item,roi_gray)
        break


cap.release()
cv2.destroyAllWindows()
