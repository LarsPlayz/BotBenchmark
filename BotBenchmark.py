import pyautogui
import time
import keyboard
import win32api, win32con
import pytesseract


test = 0
count = 0
locationx = []
locationy = []
pytesseract.pytesseract.tesseract_cmd = r'C:\users\elev\AppData\Local\Tesseract-OCR\tesseract.exe'

while keyboard.is_pressed('q') == False:
    # The code that presses the left mouse button
    def click(x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


    # What test
    while test == 0:
        if pyautogui.locateOnScreen(r'C:\Users\Elev\PycharmProjects\BotBenchmark\photos\aimtester.png') != None:
            test = 1
            count = 0
            time.sleep(0.01)
            click(971, 421)

        if pyautogui.locateOnScreen(r'C:\Users\Elev\PycharmProjects\BotBenchmark\photos\reactiontest.png') != None:
            click(971, 421)
            test = 2
            count = 0

        if pyautogui.locateOnScreen(r'C:\Users\Elev\PycharmProjects\BotBenchmark\photos\sequencememory.png') != None:
            test = 3
            count: int = 1
            state = 0
            click(972, 555)
            time.sleep(0.5)

        if pyautogui.locateOnScreen(r'C:\Users\Elev\PycharmProjects\BotBenchmark\photos\typingtest.png') != None:
            test = 4
            state = 0
            click(943, 190)


    # Aim Trainer
    while test == 1:
        state = 0
        pic = pyautogui.screenshot(region=(600, 205, 850, 482))
        width, height = pic.size

        for x in range(0, width, 5):
            for y in range(0, height, 5):

                r, g, b = pic.getpixel((x, y))

                if b != 209:
                    state = 1
                    count += 1
                    click(x + 600, y + 205)
                    time.sleep(0.05)
                    break

            if state == 1:
                break

            if count >= 31:
                test = 0
                count = 0
                time.sleep(0.5)


    # Reaction time
    while test == 2:

        if pyautogui.pixel(969, 404)[1] == 219:
            click(969, 404)
            time.sleep(0.01)
            click(969, 404)
            time.sleep(0.5)
            count += 1

        if count >= 5:
            test = 0
            count = 0




    #Sequence Memory
    # High Score: 200
    while test == 3:

        if pyautogui.locateOnScreen(r'C:\Users\Elev\PycharmProjects\BotBenchmark\photos\sequencedone.png') != None:
            test = 0
            break

        if state == 0:
            for z in range(0, count, 1):
                if pyautogui.pixel(838, 320)[2] == 255:
                    locationx.append(838)
                    locationy.append(320)
                    z += 1
                    time.sleep(0.4)
                if pyautogui.pixel(970, 320)[2] == 255:
                    locationx.append(970)
                    locationy.append(320)
                    z += 1
                    time.sleep(0.4)
                if pyautogui.pixel(1058, 320)[2] == 255:
                    locationx.append(1058)
                    locationy.append(320)
                    z += 1
                    time.sleep(0.4)
                if pyautogui.pixel(838, 450)[2] == 255:
                    locationx.append(838)
                    locationy.append(450)
                    z += 1
                    time.sleep(0.4)
                if pyautogui.pixel(970, 450)[2] == 255:
                    locationx.append(970)
                    locationy.append(450)
                    z += 1
                    time.sleep(0.4)
                if pyautogui.pixel(1058, 450)[2] == 255:
                    locationx.append(1058)
                    locationy.append(450)
                    z += 1
                    time.sleep(0.4)
                if pyautogui.pixel(838, 590)[2] == 255:
                    locationx.append(838)
                    locationy.append(590)
                    z += 1
                    time.sleep(0.4)
                if pyautogui.pixel(970, 590)[2] == 255:
                    locationx.append(970)
                    locationy.append(590)
                    z += 1
                    time.sleep(0.4)
                if pyautogui.pixel(1058, 590)[2] == 255:
                    locationx.append(1058)
                    locationy.append(590)
                    z += 1
                    time.sleep(0.4)
                if len(locationx) >= count:
                    state = 1


        # Clicks
        if state == 1:
            time.sleep(0.3)
            for n in range(0, count, 1):
                click(locationx[n], locationy[n])
                n += 1
                if n == count:
                    state = 2
                    break

        if state == 2:
            state = 0
            count += 1
            locationx.clear()
            locationy.clear()
            break


    #Typing Test
    while test == 4:

        if state == 0:
            pic = pyautogui.screenshot(region=(500, 380, 950, 200))
            txt = pytesseract.image_to_string(pic, config="--oem 3 --psm 6")
            txt = txt.replace("\n", " ")
            click(943, 480)
            state = 1

        if state == 1:
            pyautogui.typewrite(txt)
            time.sleep(0.1)
            keyboard.press(hotkey='home')
            test = 0
            state = 2
            break
