import pyautogui
import time
import keyboard
import win32api, win32con
import pytesseract
import cv2
from PIL import Image


if pyautogui.locateOnScreen(r'C:\Users\Elev\PycharmProjects\BotBenchmark\photos\numbermemory.png') != None:
    test = 5
    state = 0
    click(970, 570)




# Number Memory
while test == 5:
    if state == 0:
        time.sleep(0.2)
        pic = pyautogui.screenshot(region=(500, 380, 950, 100), grayscale=True)
        pic.save(r"C:\Users\Elev\PycharmProjects\BotBenchmark\photos\savedimage.png")
        num = pytesseract.image_to_string(pic, config="--psm 7 digits -c tessedit_char_whitelist=0123456789")
        state = 1

    if state == 1:
        if pyautogui.pixel(930, 514)[0] == 255:
            print(num)
            pyautogui.write(num)
            pyautogui.press('enter')
            pyautogui.press('enter')
            state = 2
