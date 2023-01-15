from finance_decision_service.bank_service import BankService
from finance_decision_service.decision_service import DecisionService
from finance_decision_service.file_and_parse_service import FileAndParseService
from finance_decision_service.finance_service import YFinanceService


class HandleStockService:

    def __init__(self):
        self.yfinance_service = YFinanceService()
        self.file_and_parse_service = FileAndParseService()
        self.decision_service = DecisionService()
        self.bank_service = BankService()

    def handle_already_bought_stocks(self):
        print("handle_already_bought_stocks start")

        bought_prices = self.file_and_parse_service.read_bought_stock_tickers()
        symbols = list(bought_prices.keys())

        # If there is only one stock left, it gives an error
        if len(symbols) < 2:
            return

        current_prices = self.yfinance_service.get_current_data(symbols, len(symbols))

        for stocks, bought_price in bought_prices.items():
            print("---------")
            current_price = current_prices[stocks]
            final_decision, percent = self.decision_service.decide_sell_or_not(bought_p=bought_price, current_p=current_price)
            if final_decision:
                print(f"SELL {stocks} because You bought {bought_price}, current price is {current_price}")
                print(f"There is a {percent}% increase")
                is_sold = self.bank_service.sell_stock(stocks, current_price)
                print(f"SOLD: {is_sold}")

            else:
                print(f"DO NOT SELL {stocks} because You bought {bought_price}, current price is {current_price}")

        print("handle_already_bought_stocks end")

    def try_to_buy_new_stock(self):
        print("try_to_buy_new_stock start")

        symbols = self.file_and_parse_service.get_buy_able_stock_symbols()
        average_prices = self.yfinance_service.get_last_3_day_average(symbols=symbols, number_of_symbol=len(symbols))

        current_prices = self.yfinance_service.get_current_data(symbols, len(symbols))

        for stocks, average_price in average_prices.items():
            print("---------")
            current_price = current_prices[stocks]
            final_decision, percent = self.decision_service.decide_buy_or_not(average_p=average_price, current_p=current_price)

            if final_decision:
                print(
                    f"BUY {stocks} because it's 3 day average price {average_price}, current price is {current_price}")
                print(f"There is a {percent}% decrease")
                is_bought = self.bank_service.buy_stock(stocks, price=current_price)
                print(f"BOUGHT: {is_bought}")

            else:
                print(
                    f"DO NOT BUY {stocks} because it's 3 day average price {average_price},"
                    f" current price is {current_price}")

        print("try_to_buy_new_stock end")

