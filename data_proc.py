import cv2 as cv
import mediapipe as mp
import time
import math

vcap = cv.VideoCapture('http://192.168.43.41:5000/video_feed')
mphands=mp.solutions.hands
hands=mphands.Hands()
mpDraw= mp.solutions.drawing_utils


while True:
    success,img = vcap.read()

    imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results= hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handlmks in results.multi_hand_landmarks:
            for id,lm in enumerate(handlmks.landmark):
                # print(id,lm)
                h,w,c = img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)
            mpDraw.draw_landmarks(img, handlmks, mphands.HAND_CONNECTIONS)

    cv.imshow('image',img)
    cv.waitKey(1)
cv.destroyAllWindows()