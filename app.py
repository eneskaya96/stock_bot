from time import sleep

from bank_service import sell_stock, buy_stock
from decision_service import decide_sell_or_not, decide_buy_or_not
from file_and_parse_service import read_bought_stock_tickers, get_buy_able_stock_symbols
from finance_service import get_current_data, get_last_3_day_average


def handle_already_bought_stocks():
    print("handle_already_bought_stocks start")

    bought_prices = read_bought_stock_tickers()
    symbols = list(bought_prices.keys())

    # If there is only one stock left, it gives an error
    if len(symbols) < 2:
        return

    current_prices = get_current_data(symbols, len(symbols))

    for stocks, bought_price in bought_prices.items():
        print("---------")
        current_price = current_prices[stocks]
        final_decision, percent = decide_sell_or_not(bought_p=bought_price, current_p=current_price)
        if final_decision:
            print(f"SELL {stocks} because You bought {bought_price}, current price is {current_price}")
            print(f"There is a {percent}% increase")
            is_sold = sell_stock(stocks)
            print(f"SOLD: {is_sold}")

        else:
            print(f"DO NOT SELL {stocks} because You bought {bought_price}, current price is {current_price}")

    print("handle_already_bought_stocks end")


def try_to_buy_new_stock():
    print("try_to_buy_new_stock start")

    symbols = get_buy_able_stock_symbols()
    average_prices = get_last_3_day_average(symbols=symbols, number_of_symbol=len(symbols))

    current_prices = get_current_data(symbols, len(symbols))

    for stocks, average_price in average_prices.items():
        print("---------")
        current_price = current_prices[stocks]
        final_decision, percent = decide_buy_or_not(average_p=average_price, current_p=current_price)

        if final_decision:
            print(f"BUY {stocks} because it's 3 day average price {average_price}, current price is {current_price}")
            print(f"There is a {percent}% decrease")
            is_bought = buy_stock(stocks)
            print(f"BOUGHT: {is_bought}")

        else:
            print(
                f"DO NOT BUY {stocks} because it's 3 day average price {average_price},"
                f" current price is {current_price}")

    print("try_to_buy_new_stock end")


print("Getting stock data is started ")

run_count = 0
# infinite loop
while 1:
    print("-----start----")
    try:
        handle_already_bought_stocks()
    except Exception as e:
        print(f"Exception occurs at handle_already_bought_stocks as e: {e}")

    try:
        try_to_buy_new_stock()
    except Exception as e:
        print(f"Exception occurs at try_to_buy_new_stock as e: {e}")

    run_count += 1
    print(f"-----end----{run_count}")
    sleep(600)  # 10 minutes
