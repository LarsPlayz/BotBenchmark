from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con


# Tile 1 Position: X:  608 Y:  746 RGB: (160, 164, 231)
# Tile 2 Position: X:  712 Y:  736 RGB: (253,  18,   1)
# Tile 3 Position: X:  794 Y:  736 RGB: (155, 161, 230)
# Tile 4 Position: X:  888 Y:  736 RGB: (169, 173, 232)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)  # This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
time.sleep(2)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(608, 746)[0] == 0:
        click(608, 746)
    if pyautogui.pixel(712, 746)[0] == 0:
        click(712, 746)
    if pyautogui.pixel(794, 746)[0] == 0:
        click(794, 746)
    if pyautogui.pixel(888, 746)[0] == 0:
        click(888, 746)
