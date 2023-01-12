from time import sleep

import random
from bank_services.robot_service import RobotService


class LoginService:

    def __init__(self):
        self.tc = ''
        self.password = ''
        self.robot = RobotService()

    def go_and_click_lock(self):
        self.robot.move_to_image('images/lock.png')

    def go_and_click_account(self):
        self.robot.move_to_image('images/bireysel.png')

    def go_and_click_investment(self):
        self.robot.move_to_image('images/yatırımlar.png', 'images/yatırımlar_2.png')

    def go_and_click_buy_or_sell_request_follow(self):
        self.robot.move_to_image('images/buy_or_sell_request_follow.png')

    def go_and_click_empty_click(self):
        self.robot.move_to_image('images/empty_click.png')

    def go_and_click_balance(self):
        self.robot.move_to_image('images/balance.png')

    def go_and_click_jobs(self):
        self.robot.move_to_image('images/jobs.png')

    def go_and_click_refresh(self):
        self.robot.move_to_refresh('images/refresh.png')

    def go_and_click_next_button(self):
        self.robot.move_to_image('images/devam.png')

    def go_and_click_approve_button(self):
        self.robot.move_to_image('images/approve.png')

    def login_bank_account(self):
        sleep(2)
        self.go_and_click_lock()

        sleep(1)
        self.go_and_click_account()

        sleep(1)
        self.robot.write_text(self.tc)

        sleep(1)
        self.robot.press_tab()

        sleep(1)
        self.robot.write_text(self.password)

        sleep(1)
        self.robot.press_enter()

    def enter_buy_request(self, symbol: str, count: int):
        self.go_and_click_investment()
        sleep(1)

        self.go_and_click_buy_or_sell_request_follow()
        sleep(1)

        self.go_and_click_empty_click()
        sleep(1)

        # choose symbol
        self.robot.press_tab()
        sleep(2)

        self.robot.press_down()
        sleep(2)

        self.robot.write_text(symbol)
        sleep(2)

        self.robot.press_enter(1)
        sleep(2)

        self.robot.press_enter(1)
        sleep(2)

        # empty click
        self.go_and_click_empty_click()
        sleep(2)

        # choose buy
        self.robot.press_tab(2)
        sleep(2)

        self.robot.press_down(2)
        sleep(2)

        self.robot.press_enter(2)
        sleep(2)

        # empty click
        self.go_and_click_empty_click()
        sleep(2)

        # chose count
        self.robot.press_tab(4)
        sleep(2)

        self.robot.write_text(str(count))
        sleep(2)

        # empty click
        self.go_and_click_empty_click()
        sleep(2)

        # chose time
        self.robot.press_tab(7)
        sleep(2)

        self.robot.press_down(2)
        sleep(2)

        self.robot.press_enter(2)
        sleep(2)

        # empty click
        self.go_and_click_empty_click()
        sleep(2)

        # press next
        self.go_and_click_next_button()
        sleep(3)

        # press approve
        self.go_and_click_approve_button()
        sleep(3)

    def keep_alive(self):
        # empty click
        choice = random.randint(1, 4)
        if choice == 1:
            self.go_and_click_empty_click()
        elif choice == 2:
            self.go_and_click_refresh()
        elif choice == 3:
            self.go_and_click_jobs()
        elif choice == 4:
            self.go_and_click_balance()

        num_sec = random.randint(1, 10)
        sleep(num_sec)




