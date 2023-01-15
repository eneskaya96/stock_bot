from finance_decision_service.file_and_parse_service import FileAndParseService


class BankService:

    def __init__(self):
        self.file_and_parse_service = FileAndParseService()
        self.balance = 0
        self.read_balance()

    def read_balance(self):
        self.balance = self.file_and_parse_service.read_balance()

    def send_sell_request(self, symbol) -> bool:
        self.file_and_parse_service.adding_line_to_buy_or_sell_requests_file(request_type="SELL", symbol=symbol)
        return True

    def send_buy_request(self, symbol) -> bool:
        self.file_and_parse_service.adding_line_to_buy_or_sell_requests_file(request_type="BUY", symbol=symbol)
        return True

    def check_balance(self, price: float):
        if self.balance - price < 0:
            return False
        else:
            self.balance = self.balance - price
            self.file_and_parse_service.update_balance(self.balance)
            return True

    def sell_stock(self, symbol: str) -> bool:
        print(f"Try to sell {symbol} started")
        is_sold = self.send_sell_request(symbol)
        if is_sold:
            # remove from bought.txt
            try:
                self.file_and_parse_service.delete_line_from_file(symbol)
            except Exception as e:
                print(f"Error at delete_line_from_file ")
        return is_sold

    def buy_stock(self, symbol: str, price: float) -> bool:

        is_balance_enough = self.check_balance(price)
        if not is_balance_enough:
            print(f"Balance is not enough balance : {self.balance}, price : {price}")
            return False



        print(f"Try to buy {symbol} started")
        is_bought = self.send_buy_request(symbol)
        if is_bought:
            # add to bought.txt
            try:
                self.file_and_parse_service.adding_line_to_bought_file(symbol, price=price)
            except Exception as e:
                print(f"Error at adding_line_from_file ")
        return is_bought
