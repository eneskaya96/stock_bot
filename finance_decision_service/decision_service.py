from typing import Tuple, Any


class DecisionService:

    def __init__(self):
        pass

    def decide_sell_or_not(self, bought_p: float, current_p: float) -> Tuple[bool, Any]:
        diff = current_p - bought_p
        if diff <= 0:
            return False, None
        else:
            percent = diff * 100 / bought_p
            if 4 < percent < 10:
                return True, percent
            else:
                return False, None

    def decide_buy_or_not(self, average_p: float, current_p: float) -> Tuple[bool, Any]:
        diff = average_p - current_p

        # more expensive than average
        percent = diff * 100 / average_p
        # print(f"percent {percent}")
        if -1 < percent < 40:
            return True, percent
        else:
            return False, None
