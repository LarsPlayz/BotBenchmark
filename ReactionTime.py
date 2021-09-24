from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#The code that presses the left mouse button
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#The code looks at one pixel on the screen, and when that turns green it clicks
while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(969, 404)[1] == 219:
        click(969, 404)
        time.sleep(0.01)
        click(969, 404)
        time.sleep(0.5)







