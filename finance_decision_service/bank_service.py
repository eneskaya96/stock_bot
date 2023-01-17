from finance_decision_service.file_and_parse_service import FileAndParseService


class BankService:

    def __init__(self):
        self.file_and_parse_service = FileAndParseService()
        self.balance = 0
        self.read_balance()

    def read_balance(self):
        self.balance = self.file_and_parse_service.read_balance()
        print(f"Balance is {self.balance}")

    def send_sell_request(self, symbol, price) -> bool:
        self.file_and_parse_service.adding_line_to_buy_or_sell_requests_file(request_type="SELL", symbol=symbol,
                                                                             price=price)
        return True

    def send_buy_request(self, symbol, price) -> bool:
        self.file_and_parse_service.adding_line_to_buy_or_sell_requests_file(request_type="BUY", symbol=symbol,
                                                                             price=price)
        return True

    def check_balance(self, price: float):
        self.balance = self.file_and_parse_service.read_balance()
        if self.balance - price < 0:
            return False
        else:
            self.balance = self.balance - price
            self.file_and_parse_service.update_balance(self.balance)
            return True

    def sell_stock(self, symbol: str, price: float) -> bool:

        print(f"Try to sell {symbol} started")
        is_sold = self.send_sell_request(symbol, price)

        self.balance = self.file_and_parse_service.read_balance()
        self.balance = self.balance + price
        self.file_and_parse_service.update_balance(self.balance)

        return is_sold

    def buy_stock(self, symbol: str, price: float) -> bool:

        is_balance_enough = self.check_balance(price)
        if not is_balance_enough:
            print(f"Balance is not enough balance : {self.balance}, price : {price}")
            return False

        print(f"Try to buy {symbol} started")
        is_bought = self.send_buy_request(symbol, price=price)

        return is_bought
