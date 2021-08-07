import cv2 as cv
import imutils
import numpy as np
from pygame import mixer
import time

def play_drums(x,y):
    if x >= 44 and x <= 270:
        if y >= 320 and y <= 540:
            mixer.init()
            mixer.Sound('C:\\Users\\Mohamed\\PycharmProjects\\VirtualDrums\\DrumsSounds\\Floor-Tom-Drum-Hit-Level-5B.mp3').play()
            time.sleep(0.2)
            mixer.Sound('C:\\Users\\Mohamed\\PycharmProjects\\VirtualDrums\\DrumsSounds\\Floor-Tom-Drum-Hit-Level-5B.mp3').stop()

    elif x >= 320 and x <= 546:
        if y >= 320 and y <= 540:
            mixer.init()
            mixer.Sound(
                'C:\\Users\\Mohamed\\PycharmProjects\\VirtualDrums\\DrumsSounds\\Bass-Drum-Hit-Level-4a.mp3').play()
            time.sleep(0.2)
            mixer.Sound(
                'C:\\Users\\Mohamed\\PycharmProjects\\VirtualDrums\\DrumsSounds\\Bass-Drum-Hit-Level-4a.mp3').stop()

    elif x >= 596 and x <= 812:
        if y >= 320 and y <= 540:
            mixer.init()
            mixer.Sound(
                'C:\\Users\\Mohamed\\PycharmProjects\\VirtualDrums\\DrumsSounds\\Hi-Hat-Open-Hit-A1.mp3').play()
            time.sleep(0.2)
            mixer.Sound(
                'C:\\Users\\Mohamed\\PycharmProjects\\VirtualDrums\\DrumsSounds\\Hi-Hat-Open-Hit-A1.mp3').stop()

    elif x >= 842 and x <= 1085:
        if y >= 320 and y <= 540:
            mixer.init()
            mixer.Sound(
                'C:\\Users\\Mohamed\\PycharmProjects\\VirtualDrums\\DrumsSounds\\Snare-Drum-Hit-Level-3a.mp3').play()
            time.sleep(0.07)
            mixer.Sound(
                'C:\\Users\\Mohamed\\PycharmProjects\\VirtualDrums\\DrumsSounds\\Snare-Drum-Hit-Level-3a.mp3').stop()


capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    frame = imutils.resize(frame, width=1220)
    frame = cv.flip(frame, 1) # to make the frame displayed properly

    hsv_frame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    low_green = np.array([42, 129, 33])
    high_green = np.array([80, 255, 255])
    mask = cv.inRange(hsv_frame, low_green, high_green)
    contours,_ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    # print(contours)

    x, y = 0, 0
    f_center, f_radius = 0, 0

    try:
        for i in range(10):
            f_center, f_radius = cv.minEnclosingCircle(contours[i])
            x, y = int(f_center[0]), int(f_center[1])

            if cv.contourArea(contours[i]) > 2100:
                cv.circle(frame, (x, y), 10, (0, 250, 250), 3)
                break
    except:
        pass

    play_drums(x,y)

    cv.imshow("Mask", mask)

    cv.rectangle(frame, (44, 320), (270, 540), (255, 0, 0), 3)
    cv.rectangle(frame, (320, 320), (546, 540), (0, 255, 0), 3)
    cv.rectangle(frame, (596, 320), (812, 540), (0, 0, 255), 3)
    cv.rectangle(frame, (842, 320), (1085, 540), (0, 255, 255), 3)

    cv.imshow("Video",frame)
    if cv.waitKey(6) & 0xFF == ord("q"):
        break

capture.release()
cv.destroyAllWindows()
