import pyautogui
import cv2
import time

time.sleep(1)

while True:
    location = pyautogui.locateOnScreen('ball.png', grayscale=True,  confidence=0.95)
    pyautogui.moveTo(location)
