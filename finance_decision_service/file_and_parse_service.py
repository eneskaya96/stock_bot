from typing import List, Dict

bought_stocks_filename = '../bought_stocks.txt'
follow_stocks_filename = '../follow_stocks.txt'


def read_lines(filenames: str) -> List[str]:
    bought_stocks_symbols = []
    with open(filenames) as f:
        for line in f.readlines():
            bought_stocks_symbols.append(line.strip())
    f.close()

    return bought_stocks_symbols


def read_bought_stock_tickers() -> Dict[str, float]:
    symbol_price_pair = {}
    lines = read_lines(bought_stocks_filename)
    for l in lines:
        symbol, price = l.split('|')
        symbol_price_pair[symbol] = float(price)

    return symbol_price_pair


def delete_line_from_file(symbol: str) -> None:
    with open(bought_stocks_filename, "r") as f:
        lines = f.readlines()
    with open(bought_stocks_filename, "w") as f:
        for line in lines:
            _line = line.strip()
            _symbol, _ = _line.split('|')
            if _symbol != symbol:
                f.write(line)
    f.close()


def get_follow_symbols():
    symbols = read_lines(follow_stocks_filename)
    return symbols


def get_buy_able_stock_symbols() -> List[str]:
    bought_stocks = read_bought_stock_tickers()

    symbols = get_follow_symbols()
    buy_able_stocks = []
    for symbol in symbols:
        if symbol in bought_stocks:
            print(f"The {symbol} already bought")
        else:
            buy_able_stocks.append(symbol)

    return buy_able_stocks
