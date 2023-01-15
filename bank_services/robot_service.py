from time import sleep

import pyautogui as pt
from pynput.mouse import Controller


class RobotService:

    def __init__(self):
        pt.FAILSAFE = True
        self.mouse = Controller()

    def move_mouse(self, x, y):
        pt.moveTo(x, y, duration=0.3)
        pt.click()

    def move_to_image(self, image_path: str, second_image_path: str = ""):
        button_location = pt.locateCenterOnScreen(image_path, grayscale=False, confidence=0.8)
        if button_location:
            self.move_mouse(button_location.x / 2, button_location.y / 2)
        else:
            button_location = pt.locateCenterOnScreen(second_image_path, grayscale=False)
            self.move_mouse(button_location.x / 2, button_location.y / 2)

    def find_image_path_tab(self, image_path: str, second_image_path: str = "") -> bool:
        button_location = pt.locateCenterOnScreen(image_path, grayscale=False, confidence=0.8)
        if button_location:
            return True
        else:
            button_location = pt.locateCenterOnScreen(second_image_path, grayscale=False)
            if button_location:
                return True

        return False

    def write_text(self, text: str):
        pt.write(text)

    def press_tab(self, times: int = 1):
        for i in range(0, times):
            pt.hotkey('\t')

    def press_enter(self, times: int = 1):
        for i in range(0, times):
            pt.press('enter')
            sleep(1)

    def click(self, x, y):
        pt.click()

    def press_down(self, times: int = 1):
        for i in range(0, times):
            pt.press('down')

    def move_to_refresh(self, image_path: str):
        button_location = pt.locateCenterOnScreen(image_path, grayscale=False)
        sleep(1)
        self.move_mouse(button_location.x / 2 + 57, button_location.y / 2)
