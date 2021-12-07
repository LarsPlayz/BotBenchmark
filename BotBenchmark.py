import pyautogui
import time
import keyboard
import win32api, win32con
import pytesseract

#Change this to your location
pytesseract.pytesseract.tesseract_cmd = r'C:\users\elev\AppData\Local\Tesseract-OCR\tesseract.exe'



# The code that presses the left mouse button
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# Aim Trainer
def aimTrainer():
    global state, count
    print("Aim Trainer Test")
    while count <= 33:
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
    if count >= 33:
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
    global state, count, work
    locationx = []
    locationy = []
    delay = 0.45

    while work == True:
        if pyautogui.locateOnScreen(r'photos\sequencedone.png', grayscale=True, confidence=0.6) != None:
            reset()


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


# Number Memory not working
def numberTest():
    global state, work

    while work == True:
        if pyautogui.locateOnScreen(r'photos\numberfailed.png', grayscale=True, confidence=0.6) != None:
            reset()

        if state == 0:
            time.sleep(0.5)
            pic = pyautogui.screenshot(region=(650, 370, 600, 90))
            pic.save(r"C:\Users\Elev\PycharmProjects\BotBenchmark\photos\savedimage.png")
            num = pytesseract.image_to_string(pic, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
            time.sleep(0.5)
            state = 1

        if state == 1:
            if pyautogui.pixel(930, 514)[0] == 255:
                time.sleep(0.5)
                print(num)
                pyautogui.write(num)
                if pyautogui.pixel(977, 543)[0] == 255:
                    print('test')
                    state = 0


#Verbal Memory test    High Score: 100000
def verbalTest():
    global state, count, work
    words = []
    print("Verbal Memory")

    while work == True:
        if state == 0:
            pic = pyautogui.screenshot(region=(650, 370, 600, 90))
            pic.save(r"C:\Users\Elev\PycharmProjects\BotBenchmark\photos\savedimage.png")
            txt = pytesseract.image_to_string(pic, config="--oem 3 --psm 6")
            state = 1

        if state == 1:
            if txt in words:
                click(905, 500)
                state = 0
                count += 1
            else:
                words.append(txt)
                click(1044, 501)
                state = 0
                count += 1

        if count >= 300:
            click(905, 500)
        if pyautogui.locateOnScreen(r'photos\verbalfailed.png', grayscale=True, confidence=0.6) != None:
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
        #Number Memory
        elif pyautogui.locateOnScreen(r'photos\numbermemory.png', grayscale=True, confidence=0.6) != None:
            click(970, 570)
            numberTest()
        #Verbal Memory
        elif pyautogui.locateOnScreen(r'photos\verbalmemory.png', grayscale=True, confidence=0.6) != None:
            time.sleep(0.5)
            click(971, 582)
            time.sleep(0.5)
            verbalTest()



def reset():
    global count, state, looking, work
    print("reset")
    looking = True
    work = True
    count = 0
    state = 0
    whatTest()

reset()
