from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#(region=(785,265,380,380))
#High Score: 85

test = 0
locationx = []
locationy = []

while keyboard.is_pressed('q') == False:
    def click(x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    while test == 0:
        if pyautogui.locateOnScreen('sequencememory.png') != None:
            test = 1
            count: int = 1
            flag = 0
            click(972, 555)
            time.sleep(0.5)



    while test == 1:

        if pyautogui.locateOnScreen('sequencedone.png') != None:
            test = 0
            print('Done with sequence')
            break



        if flag == 0:

            print('Looking...')
            for z in range(0, count, 1):
                if pyautogui.pixel(838, 320)[0] == 255:
                    locationx.append(838)
                    locationy.append(320)
                    z += 1
                    time.sleep(0.4)
                if pyautogui.pixel(970, 320)[0] == 255:
                    locationx.append(970)
                    locationy.append(320)
                    z += 1
                    time.sleep(0.4)
                if pyautogui.pixel(1058, 320)[0] == 255:
                    locationx.append(1058)
                    locationy.append(320)
                    z += 1
                    time.sleep(0.4)
                if pyautogui.pixel(838, 450)[0] == 255:
                    locationx.append(838)
                    locationy.append(450)
                    z += 1
                    time.sleep(0.4)
                if pyautogui.pixel(970, 450)[0] == 255:
                    locationx.append(970)
                    locationy.append(450)
                    z += 1
                    time.sleep(0.4)
                if pyautogui.pixel(1058, 450)[0] == 255:
                    locationx.append(1058)
                    locationy.append(450)
                    z += 1
                    time.sleep(0.4)
                if pyautogui.pixel(838, 590)[0] == 255:
                    locationx.append(838)
                    locationy.append(590)
                    z += 1
                    time.sleep(0.4)
                if pyautogui.pixel(970, 590)[0] == 255:
                    locationx.append(970)
                    locationy.append(590)
                    z += 1
                    time.sleep(0.4)
                if pyautogui.pixel(1058, 590)[0] == 255:
                    locationx.append(1058)
                    locationy.append(590)
                    z += 1
                    time.sleep(0.4)
                if len(locationx) >= count:
                    flag = 1
                    print('Done looking')


        # Clicks
        if flag == 1:
            print('Clicking')
            time.sleep(0.3)
            for n in range(0, count, 1):
                click(locationx[n], locationy[n])
                n += 1
                if n == count:
                    flag = 2
                    break

        if flag == 2:
            flag = 0
            count += 1
            locationx.clear()
            locationy.clear()
            print('Last')
            break
















