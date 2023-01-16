from time import sleep
from datetime import datetime
from finance_decision_service.handle_stocks import HandleStockService


def is_market_off():

    # if market is not open
    if datetime.today().weekday() > 5:
        print("OUTSIDE WEEKDAY")
        return True

    now = datetime.now()
    if now.hour >= 18 or now.hour < 10:
        print("SLEEPING")
        return True


def run_finance_app():
    handle_stock_service = HandleStockService()

    run_count = 0
    # infinite loop
    while 1:
        print("-----start----")

        if is_market_off():
            print("SLEEPING")
            sleep(60 * 5)
            continue

        try:
            handle_stock_service.handle_already_bought_stocks()
        except Exception as e:
            print(f"Exception occurs at handle_already_bought_stocks as e: {e}")

        try:
            handle_stock_service.try_to_buy_new_stock()
        except Exception as e:
            print(f"Exception occurs at try_to_buy_new_stock as e: {e}")

        run_count += 1
        print(f"-----end----{run_count}")
        sleep(600)  # 10 minutes


print("Getting stock data is started ")
run_finance_app()
