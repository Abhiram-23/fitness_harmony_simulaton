import cv2
import numpy as np
import PoseModule as pm
import pyttsx3
from beeply import notes

pyobj = pyttsx3.init()
pyobj.setProperty("rate", 100)
pyobj.say("Welcome to fitness harmony simulator Please watch the video before beginning the workout")
pyobj.runAndWait()
mybeep = notes.beeps(1000)
mybeep.hear('C_')
# Sample workout
vid = cv2.VideoCapture('trimbicep.mp4')
detector = pm.poseDetector()
count = 0
dir = 0
while True:
    abc, img2 = vid.read()
    img2 = cv2.resize(img2, (1280, 720))
    img2 = detector.findPose(img2, False)
    lmList = detector.findPosition(img2, False)
    if len(lmList) != 0:
        # left Arm
        angle = detector.findAngle(img2, 12, 14, 16)
        # Left Arm
        per = np.interp(angle, (185, 50), (0, 100))
        bar = np.interp(angle, (185, 50), (650, 100))
        color = (255, 0, 255)
        if per == 100:
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            color = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0
        print(count)
        cv2.rectangle(img2, (0, 550), (180, 720), (214, 245, 162), cv2.FILLED)
        cv2.putText(img2, str(int(count)), (45, 670), cv2.FONT_HERSHEY_COMPLEX, 3,
                    (166, 108, 94), 10)
    cv2.imshow("Image", img2)
    if (count == 3):
        break
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
vid.release()
cv2.destroyAllWindows()
# left audio
pyobj = pyttsx3.init()
pyobj.setProperty("rate", 100)
pyobj.say("Do the workout as shown in video")
pyobj.runAndWait()
cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
# For left arm
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    img = cv2.flip(img, 1)
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    if len(lmList) != 0:
        # left Arm
        angle = detector.findAngle(img, 12, 14, 16)
        # Left Arm
        per = np.interp(angle, (50, 160), (0, 100))
        bar = np.interp(angle, (50, 160), (650, 100))
        color = (255, 0, 255)
        if per == 100:
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            color = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0
        print(count)
        cv2.rectangle(img, (0, 550), (180, 720), (214, 245, 162), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_COMPLEX, 3,
                    (166, 108, 94), 10)

    cv2.imshow("Image", img)
    if (count == 10):
        break
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
# for right hand
pyobj.setProperty("rate", 100)
pyobj.say("You have completed left hand now do with the right hand after listening to the beep")
pyobj.runAndWait()
mybeep = notes.beeps(1000)
mybeep.hear('C_')
count = 0
dir = 0
pTime = 0
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    img = cv2.flip(img, 1)
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    if len(lmList) != 0:
        angle = detector.findAngle(img, 11, 13, 15)
        per = np.interp(angle, (300, 210), (0, 100))
        bar = np.interp(angle, (300, 210), (650, 100))
        color = (255, 0, 255)
        if per == 100:
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            color = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0
        print(count)
        cv2.rectangle(img, (0, 550), (180, 720), (214, 245, 162), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_COMPLEX, 3,
                    (166, 108, 94), 10)

    cv2.imshow("Image", img)
    if (count == 10):
        break
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
cv2.destroyAllWindows()
cap.release()
pyobj.setProperty("rate", 100)
pyobj.say("Congratulations You Have Completed Your Traning")
pyobj.runAndWait()