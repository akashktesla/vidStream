import numpy as np
import cv2


vcap = cv2.VideoCapture('http://192.168.43.41:5000/video_feed')

while(True):

    ret, frame = vcap.read()

    if frame is not None:
        cv2.imshow('frame',frame)
        if cv2.waitKey(22) & 0xFF == ord('q'):
            break
    else:
        print("Frame is None")
        break

vcap.release()
cv2.destroyAllWindows()
print("Video stop")