from finance_decision_service.file_and_parse_service import get_buy_able_stock_symbols

"""
bought_prices = read_bought_stock_tickers()

symbols = list(bought_prices.keys())
print(f"bought_prices {bought_prices}")
print("---------------")
current_prices = get_current_data(symbols, len(symbols))

print(f"current_prices {current_prices}")

print("------------------")


# should I sell it
for stocks, bought_price in bought_prices.items():
    print(f"stocks {stocks} , bought_price {bought_price}")
    current_price = current_prices[stocks]
    print(f"current_price {current_price}")

    print(current_price - bought_price)
    final_decision = decide_sell_or_not(bought_p=bought_price, current_p=current_price)
    print(final_decision)
print("test finished")
"""

"""
delete_line_from_file("aaa")
"""


"""
symbols = get_follow_symbols()
average_prices = get_last_3_day_average(symbols=symbols, number_of_symbol=len(symbols))
print(f"average_prices {average_prices}")

current_prices = get_current_data(symbols, len(symbols))
print(f"current_prices {current_prices}")


for stocks, average_price in average_prices.items():
    print("---------")
    print(f"stocks {stocks} , average_price {average_price}")
    current_price = current_prices[stocks]
    final_decision, percent = decide_buy_or_not(average_p=average_price, current_p=current_price)

    if final_decision:
        print(f"BUY {stocks} because it's 3 day average price {average_price}, current price is {current_price}")
        print(f"There is a {percent}% decrease")
        is_bought = buy_stock(stocks)
        print(f"BOUGHT: {is_bought}")

    else:
        print(f"DO NOT BUY {stocks} because it's 3 day average price {average_price}, current price is {current_price}")


"""
ss = get_buy_able_stock_symbols()


