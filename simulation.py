from time import sleep

from finance_decision_service.file_and_parse_service import FileAndParseService

file_service = FileAndParseService()
while 1:
    requests = file_service.get_requests()

    if len(requests) > 0:
        for request in requests:
            request_type, symbol, price, count = request
            is_sell = request_type == "SELL"
            #login_service.enter_buy_or_sell_request(symbol=symbol, count=int(count), is_sell=is_sell)

            if is_sell:
                symbol = f"{symbol}.IS"
                file_service.delete_line_from_file(symbol=symbol)
                # update balance
                current_balance = file_service.read_balance()
                current_balance = current_balance + price
                file_service.update_balance(current_balance)
            else:
                file_service.adding_line_to_bought_file(symbol, price=price)
                # update balance
                current_balance = file_service.read_balance()
                current_balance = current_balance - price
                file_service.update_balance(current_balance)

    print("heartbeat")
    sleep(3 * 60)