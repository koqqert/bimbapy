import cv2
import os
import numpy as np
from keras.models import load_model
from pygame import mixer
import time

#чтобы был звук
mixer.init()
sound = mixer.Sound('alarm.mp3')

#каскады Хаара чтобы обнаружить глаза и лицо
face = cv2.CascadeClassifier('haar cascade files\haarcascade_frontalface_alt.xml')
leye = cv2.CascadeClassifier('haar cascade files\haarcascade_lefteye_2splits.xml')
reye = cv2.CascadeClassifier('haar cascade files\haarcascade_righteye_2splits.xml')

#метки состояния
lbl = ['Открыты', 'Закрыты']

model = load_model('models\opcl_eyes.h5')

path = os.getcwd() #получаем текущую рабочую директорию
cap = cv2.VideoCapture(0) #видеозахват с веб-камеры по умолчанию
font = cv2.FONT_HERSHEY_COMPLEX_SMALL #шрифт
count=0 #счётчик
score=0 #очки
thicc=2 
rpred=[99]
lpred=[99]

while(True):
    ret, frame = cap.read()
    if ret:
        height,width = frame.shape[:2]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #обнаруживаем лица и глаз в кадре
        faces = face.detectMultiScale(gray,minNeighbors=5,scaleFactor=1.1,minSize=(25,25))
        left_eye = leye.detectMultiScale(gray)
        right_eye =  reye.detectMultiScale(gray) 

        cv2.rectangle(frame, (0,height-50) , (250,height) , (0,0,0) , thickness=cv2.FILLED ) #рисуем черный прямоугольник внизу

        for (x,y,w,h) in faces: #рисуем прямоугольник вокруг обнаруженных лиц
            cv2.rectangle(frame, (x,y) , (x+w,y+h) , (100,100,100) , 1 )
        
        for (x,y,w,h) in right_eye: #код для правого глаза
            r_eye=frame[y:y+h,x:x+w]

            r_eye = cv2.cvtColor(r_eye,cv2.COLOR_BGR2GRAY)
            r_eye = cv2.resize(r_eye,(24,24))

            r_eye= r_eye/255
            r_eye=  r_eye.reshape(24,24,-1)
            r_eye = np.expand_dims(r_eye,axis=0)

            rpred = np.argmax(model.predict(r_eye), axis=-1)

            if(rpred[0]==1):
                lbl='Открыты'
            if(rpred[0]==0):
                lbl='Закрыты'
            break

        for (x,y,w,h) in left_eye: #код для левого глаза
            l_eye=frame[y:y+h,x:x+w]
            
            l_eye = cv2.cvtColor(l_eye,cv2.COLOR_BGR2GRAY)
            l_eye = cv2.resize(l_eye,(24,24))

            l_eye= l_eye/255
            l_eye=  l_eye.reshape(24,24,-1)
            l_eye = np.expand_dims(l_eye,axis=0)

            lpred = np.argmax(model.predict(l_eye), axis=-1)

            if(lpred[0]==1):
                lbl='Открыты'
            if(lpred[0]==0):
                lbl='Закрыты'
            break
        
        #рисуем текстовую метку состояния глаз
        if(rpred[0]==1 or lpred[0]==1):
            score=score-1.5
            cv2.putText(frame,"open",(10,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
        if(rpred[0]==0 and lpred[0]==0):
            score=score+0.5
            cv2.putText(frame,"closed",(10,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
        if(score<0): #сбрасываем баллы сонливости если они отриц.
            score=0

        #рисуем баллы сонливости
        cv2.putText(frame,'score:'+str(score),(100,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
        
        #если баллы сонливости превышают 15, то сохраняем кадр и включаем звук
        if(score>30):
            try:
                sound.play()
            except:  
                pass
            if(thicc<16):
                thicc= thicc+2
            else:
                thicc=thicc-2
                if(thicc<2):
                    thicc=2
            cv2.rectangle(frame,(0,0),(width,height),(0,0,255),thicc) 

        # Отображаем обработанный кадр
        cv2.imshow('frame',frame)

        #выход клавишей "q"
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

#завершаем захват камеры и закрываем окна
cap.release()
cv2.destroyAllWindows()

