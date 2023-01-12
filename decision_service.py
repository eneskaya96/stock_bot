from typing import Tuple, Any


def decide_sell_or_not(bought_p: float, current_p: float) -> Tuple[bool, Any]:
    diff = current_p - bought_p
    if diff <= 0:
        return False, None
    else:
        percent = diff * 100 / bought_p
        if percent > 2:
            return True, percent
        else:
            return False, None


def decide_buy_or_not(average_p: float, current_p: float) -> Tuple[bool, Any]:
    diff = average_p - current_p

    # more expensive than average
    if diff <= 0:
        return False, None
    else:
        percent = diff * 100 / average_p
        if percent > 1:
            return True, percent
        else:
            return False, None