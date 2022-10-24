import sys
import mouse
import keyboard
import time
import uuid
##################################
import atexit
from time import time, strftime, localtime, sleep
from datetime import timedelta
####################################
def control():
    global IsWork
    if IsWork:
        IsWork = False
        print("завершил")
##########################################
        atexit.register(endlog)
        log("Start Program")
   ###################################################33
    else:
        IsWork = True


def kb_actions():
    s = str(uuid.uuid4())
    print(s)

    keyboard.press("ctrl+s")
    keyboard.release("ctrl+s")

    sleep(0.5)

    keyboard.write(s)

    sleep(0.5)

    keyboard.send("Enter")


#########################################
def secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))

def log(s, elapsed=None):
    line = "="*40
    print(line)
    print(secondsToStr(), '-', s)
    if elapsed:
        print("Elapsed time:", elapsed)
    print(line)
    print()

def endlog():
    end = time()
    elapsed = end-start
    log("End Program", secondsToStr(elapsed))

start = time()

#######################################33

mouse_events1 = []
mouse_events2 = []


keyboard.wait("CapsLock")

mouse.hook(mouse_events1.append)

keyboard.wait("CapsLock")

mouse.unhook(mouse_events1.append)

keyboard.wait("CapsLock")

mouse.hook(mouse_events2.append)

keyboard.wait("CapsLock")

mouse.unhook(mouse_events2.append)



keyboard.add_hotkey("/", control)


IsWork = False
while True:
    if keyboard.is_pressed("/"):
        while IsWork:
            print("работаю")
            sleep(1)
            kb_actions()
            sleep(1)
            mouse.play(mouse_events1)
            sleep(1)
            kb_actions()
            sleep(1)
            mouse.play(mouse_events2)
            sleep(1)

