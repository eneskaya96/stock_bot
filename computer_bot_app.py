from time import sleep

from bank_services.login_service import LoginService
from selenium_service.selenium_worker import SeleniumService


is_chrome_open = False
login_service = LoginService()
selenium_service = SeleniumService()

is_already_login = False

while 1:

    if not is_chrome_open:
        drive = selenium_service.open_yapi_kredi()
        is_chrome_open = True

    sleep(5)

    # if not login, sign in
    is_already_login = login_service.get_login_or_not()

    if not is_already_login:
        try:
            login_service.login_bank_account()
            print("SUCCESSFULLY LOGIN IN")
            sleep(45)
        except Exception as e:
            print(f"Exception {e}")
            is_chrome_open = False
            sleep(60)
    else:
        # if not in investment page  goto investment page
        is_at_investment_page = login_service.is_at_investment_page()
        if not is_at_investment_page:
            is_at_investment_page = login_service.goto_investments()

        # if in investment page, keep me alive
        if is_at_investment_page:
            try:
                login_service.keep_alive()
            except Exception as e:
                print(f"Exception {e}")

    print("heart_beat")
