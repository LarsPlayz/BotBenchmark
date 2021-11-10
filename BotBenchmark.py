import pyautogui
import time
import keyboard
import win32api, win32con
import pytesseract

locationx = []
locationy = []
pytesseract.pytesseract.tesseract_cmd = r'C:\users\elev\AppData\Local\Tesseract-OCR\tesseract.exe'

# The code that presses the left mouse button
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while 1:

    # Aim Trainer
    def aimTrainer():
        global state, count
        print("Aim Trainer Test")
        while count <= 31:
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
            reset()


    # Reaction time
    def reactionTest():
        global count
        print("Reaction Time Test")
        while count <= 5:
            if pyautogui.pixel(969, 404)[1] == 219:
                click(969, 404)
                time.sleep(0.01)
                click(969, 404)
                time.sleep(0.5)
                count += 1
            if count >= 5:
                reset()




    #Sequence Memory    High Score: 200
    def sequenceTest():
        global state, count
        state = 0
        delay = 0.45

        while True:
            if state == 0:
                print(len(locationx))
                for z in range(0, count, 1):
                    if pyautogui.pixel(838, 320)[2] == 255:
                        locationx.append(838)
                        locationy.append(320)
                        z += 1
                        time.sleep(delay)
                    if pyautogui.pixel(970, 320)[2] == 255:
                        locationx.append(970)
                        locationy.append(320)
                        z += 1
                        time.sleep(delay)
                    if pyautogui.pixel(1058, 320)[2] == 255:
                        locationx.append(1058)
                        locationy.append(320)
                        z += 1
                        time.sleep(delay)
                    if pyautogui.pixel(838, 450)[2] == 255:
                        locationx.append(838)
                        locationy.append(450)
                        z += 1
                        time.sleep(delay)
                    if pyautogui.pixel(970, 450)[2] == 255:
                        locationx.append(970)
                        locationy.append(450)
                        z += 1
                        time.sleep(delay)
                    if pyautogui.pixel(1058, 450)[2] == 255:
                        locationx.append(1058)
                        locationy.append(450)
                        z += 1
                        time.sleep(delay)
                    if pyautogui.pixel(838, 590)[2] == 255:
                        locationx.append(838)
                        locationy.append(590)
                        z += 1
                        time.sleep(delay)
                    if pyautogui.pixel(970, 590)[2] == 255:
                        locationx.append(970)
                        locationy.append(590)
                        z += 1
                        time.sleep(delay)
                    if pyautogui.pixel(1058, 590)[2] == 255:
                        locationx.append(1058)
                        locationy.append(590)
                        z += 1
                        time.sleep(delay)
                    if len(locationx) >= count:
                        state = 1


            # Clicks
            if state == 1:
                time.sleep(0.3)
                for n in range(0, count, 1):
                    click(locationx[n], locationy[n])
                    time.sleep(0.1)
                    n += 1
                    if n == count:
                        state = 2
                        break

            if state == 2:
                state = 0
                count += 1
                locationx.clear()
                locationy.clear()




    #Typing Test
    def typingTest():
        global state
        print("Typing Test")

        if state == 0:
            time.sleep(0.5)
            pic = pyautogui.screenshot(region=(500, 380, 950, 200))
            txt = pytesseract.image_to_string(pic, config="--oem 3 --psm 6")
            txt = txt.replace("\n", " ")
            click(943, 480)
            state = 1

        if state == 1:
            pyautogui.typewrite(txt)
            time.sleep(0.1)
            keyboard.press(hotkey='home')
            reset()

    #Figures out what test
    def whatTest():
        global count, state, looking

        print("What test")
        while looking == True:

            #Aim Trainer
            if pyautogui.locateOnScreen(r'photos\aimtester.png', grayscale=True, confidence=0.6) != None:
                click(971, 421)
                aimTrainer()
                looking = False

            #Reaction Test
            elif pyautogui.locateOnScreen(r'photos\reactiontest.png', grayscale=True, confidence=0.6) != None:
                click(971, 421)
                reactionTest()
                looking = False

            #Sequence Memory
            elif pyautogui.locateOnScreen(r'photos\sequencememory.png', grayscale=True, confidence=0.6) != None:
                count = 1
                click(972, 555)
                sequenceTest()
                looking = False

            #Typing Test
            elif pyautogui.locateOnScreen(r'photos\typingtest.png',grayscale=True, confidence=0.6) != None:
                typingTest()
                click(943, 190)
                looking = False

    def reset():
        global count, state, looking
        print("reset")
        looking = True
        count = 0
        state = 0
        whatTest()

    reset()
