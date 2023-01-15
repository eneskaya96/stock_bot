from time import sleep

from finance_decision_service.handle_stocks import HandleStockService

def run_finance_app():
    handle_stock_service = HandleStockService()

    run_count = 0
    # infinite loop
    while 1:
        print("-----start----")
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
