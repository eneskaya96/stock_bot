from time import sleep

import pyautogui as pt
from pyautogui import Point
from datetime import datetime


import pyperclip as pc

from pynput.mouse import Button, Controller

from bank_services.login_service import LoginService

pt.FAILSAFE = True

mouse = Controller()


login_service = LoginService()
login_service.login_bank_account()
print("FINISH")

sleep(5)
#login_service.enter_buy_request("ASELS", 1)

"""
now = datetime.utcnow()
while 1:
    try:
        login_service.keep_alive()
        sleep(2)
    except Exception as e:
        print('Exception')
        print(datetime.utcnow() - now )
        now = datetime.utcnow()
        exit()
"""

print("XXXXXXXX")
sleep(1)
print(pt.position())


#move_who_to_talk()
#position = pt.locateCenterOnScreen("images/huysuz.png", confidence=.8)
#print(position)
#move_who_to_talk(position)


sleep(2)
#move_edit_text()
#print(pt.size())


def move_mouse_to_position(position):
    pt.moveTo(position, duration=0.3)
    # pt.click()
    # pt.click()


def send_message():
    pt.write('Selam Ben bir robotum')
    pt.press('enter')


