from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#(region=(785,265,380,380))

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


        pic = pyautogui.screenshot(region=(785,265,380,380))
        width, height = pic.size


        for x in range(0, width, 20):
            for y in range(0, height, 20):
                r, g, b = pic.getpixel((x, y))

                #Finds where to click
                if flag == 0 and b == 255:
                    for z in range (0, count, 1):
                        time.sleep(0.5)
                        locationx.append(x+780)
                        locationy.append(y+265)
                        if locationx.count(int) == count:
                            flag = 1

                #Clicks
                if flag == 1:
                    print('X:', locationx)
                    print('Y:', locationy)
                    for n in range(0, count, 1):
                        time.sleep(3)
                        print('N:', n)
                        print('Count:', count)
                        click(locationx[n], locationy[n])
                        print('clicked')
                        n += 1
                        if n == count:
                            flag = 2
                            break

                #Resets
                if flag == 2:
                    time.sleep(1)
                    flag = 0
                    count += 1
                    locationx.clear()
                    locationy.clear()
                    print('Last')
                    break




