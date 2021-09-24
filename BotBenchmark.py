from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

test = 0
count = 0

while keyboard.is_pressed('q') == False:
    # The code that presses the left mouse button
    def click(x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


    # What test
    while test == 0:
        if pyautogui.locateOnScreen('aimtester.png') != None:
            test = 1
            count = 0
            time.sleep(0.001)
            click(971, 421)

        if pyautogui.locateOnScreen('reactiontest.png') != None:
            click(971, 421)
            test = 2
            count = 0

    # RGB: ( 43, 135, 209)
    # Aim Trainer
    while test == 1:
        flag = 0
        pic = pyautogui.screenshot(region=(600, 205, 850, 482))
        width, height = pic.size

        for x in range(0, width, 5):
            for y in range(0, height, 5):

                r, g, b = pic.getpixel((x, y))

                if b != 209:
                    flag = 1
                    count += 1
                    click(x + 600, y + 205)
                    time.sleep(0.05)
                    print(count)
                    break

            if flag == 1:
                break

            if count >= 31:
                time.sleep(0.5)
                test = 0
                count = 0
                time.sleep(0.5)

    # Reaction time
    while keyboard.is_pressed('q') == False and test == 2:

        if pyautogui.pixel(969, 404)[1] == 219:
            click(969, 404)
            time.sleep(0.01)
            click(969, 404)
            time.sleep(0.5)
            count += 1
            print(count)

        if count >= 5:
            test = 0
            count = 0
