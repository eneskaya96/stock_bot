from typing import List, Dict, Any, Union
from datetime import datetime, timedelta


class FileAndParseService:

    def __init__(self):
        self.bought_stocks_filename = '../bought_stocks.txt'
        self.follow_stocks_filename = 'follow_stocks.txt'
        self.balance_filename = '../balance.txt'
        self.buy_or_sell_requests = '../buy_or_sell_requests.txt'

    def read_lines(self, filenames: str) -> List[str]:
        bought_stocks_symbols = []
        with open(filenames) as f:
            for line in f.readlines():
                bought_stocks_symbols.append(line.strip())
        f.close()

        return bought_stocks_symbols

    def read_bought_stock_tickers(self) -> Dict[str, List[Union[float, int]]]:
        symbol_price_pair = {}
        lines = self.read_lines(self.bought_stocks_filename)
        for l in lines:
            symbol, price, count = l.split('|')
            symbol_price_pair[symbol] = [float(price), int(count)]

        return symbol_price_pair

    # used methods
    def get_requests(self) -> List:
        requests = []
        lines = self.read_lines(self.buy_or_sell_requests)

        # clean file
        with open(self.buy_or_sell_requests, "w") as f:
            f.write("\n")
        f.close()

        for l in lines:
            if len(l) > 1:
                request_type, symbol, price, count, date_str = l.split('|')
                _date = datetime.strptime(date_str, '%m/%d/%Y, %H:%M:%S')
                if _date + timedelta(minutes=20) < datetime.now():
                    pass
                else:
                    requests.append([request_type, symbol, float(price), count])

        return requests

    # used methods
    def delete_line_from_file(self, symbol: str) -> None:
        with open(self.bought_stocks_filename, "r") as f:
            lines = f.readlines()
        with open(self.bought_stocks_filename, "w") as f:
            for line in lines:
                _line = line.strip()
                _symbol, _ = _line.split('|')
                if _symbol != symbol:
                    f.write(line)
        f.close()

    # used methods
    def adding_line_to_bought_file(self, symbol: str, price: float) -> None:
        line = f"{symbol}.IS|{str(price)}\n"
        with open(self.bought_stocks_filename, "a") as f:
            f.write(line)
        f.close()

    def adding_line_to_buy_or_sell_requests_file(self, request_type: str, symbol: str, price: float = 0, count: int = 1) -> None:
        now = datetime.now()
        symbol = symbol.split(".")[0]
        line = f"{request_type}|{symbol}|{str(price)}|{str(count)}|{now.strftime('%m/%d/%Y, %H:%M:%S')}\n"
        with open(self.buy_or_sell_requests, "a") as f:
            f.write(line)
        f.close()

    def get_follow_symbols(self):
        symbols = self.read_lines(self.follow_stocks_filename)
        return symbols

    def get_buy_able_stock_symbols(self) -> List[str]:
        bought_stocks = self.read_bought_stock_tickers()

        symbols = self.get_follow_symbols()
        buy_able_stocks = []
        for symbol in symbols:
            if symbol in bought_stocks:
                #print(f"The {symbol} already bought")
                pass
            else:
                buy_able_stocks.append(symbol)

        return buy_able_stocks

    def read_balance(self) -> float:
        f = open(self.balance_filename, "r")
        balance = f.read()
        return float(balance)

    def update_balance(self, balance: float):
        f = open(self.balance_filename, "w")
        f.write(str(balance))
