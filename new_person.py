import numpy as np
import cv2
import os

def addNewPerson(name):
    cap = cv2.VideoCapture(0)
    
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    DIR = 'images'
    nextid = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    #cv2.imshow('frame', frame)
    cv2.imwrite('images/{}_{}.jpg'.format(nextid + 1, name), frame)
    print(" " + str(nextid + 1))
    cap.release()
    cv2.destroyAllWindows()


addNewPerson(input("Set name of new person: "))