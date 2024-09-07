import mouse
import pyautogui
import random
import time

def randomm():
    return random.randint(1, 6)
        

def random_mouse():
    if randomm == 1:
        print("click")
        mouse.click()
    else:
        print("no click")

def random_enter():

    if randomm == 1:
        print("enter")
        pyautogui.press('enter')
    else:
        print("no enter")

def random_enter_keep(bullet):
    rand = random.randint(1, bullet)
    if rand == 1:
        print("enter")
        pyautogui.press('enter')
    else:
        print("no enter")
        a = input(f"Bullet left : {bullet - 1}\nPress Enter to continue...")
        if a == "":
            random_enter_keep(bullet - 1)

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

countdown(5)
#random_enter()
random_enter_keep(6)

    