from typing import List, Dict


class FileAndParseService:

    def __init__(self):
        self.bought_stocks_filename = '../bought_stocks.txt'
        self.follow_stocks_filename = '../follow_stocks.txt'

    def read_lines(self, filenames: str) -> List[str]:
        bought_stocks_symbols = []
        with open(filenames) as f:
            for line in f.readlines():
                bought_stocks_symbols.append(line.strip())
        f.close()

        return bought_stocks_symbols

    def read_bought_stock_tickers(self) -> Dict[str, float]:
        symbol_price_pair = {}
        lines = self.read_lines(self.bought_stocks_filename)
        for l in lines:
            symbol, price = l.split('|')
            symbol_price_pair[symbol] = float(price)

        return symbol_price_pair

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

    def get_follow_symbols(self):
        symbols = self.read_lines(self.follow_stocks_filename)
        return symbols

    def get_buy_able_stock_symbols(self) -> List[str]:
        bought_stocks = self.read_bought_stock_tickers()

        symbols = self.get_follow_symbols()
        buy_able_stocks = []
        for symbol in symbols:
            if symbol in bought_stocks:
                print(f"The {symbol} already bought")
            else:
                buy_able_stocks.append(symbol)

        return buy_able_stocks
