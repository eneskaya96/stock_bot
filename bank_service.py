from file_and_parse_service import delete_line_from_file


def send_sell_request(symbol) -> bool:
    return False


def sell_stock(symbol: str) -> bool:
    print(f"Try to sell {symbol} started")
    is_sold = send_sell_request(symbol)
    if is_sold:
        # remove from bought.txt
        try:
            delete_line_from_file(symbol)
        except Exception as e:
            print(f"Error at delete_line_from_file ")
    return is_sold


def buy_stock(symbol: str) -> bool:
    return True
