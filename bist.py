from tradingview_ta import TA_Handler, Interval, TradingView

coin = TA_Handler(
    symbol="ASELS",
    screener="stock",
    exchange="Turkey",
    interval=Interval.INTERVAL_5_MINUTES
)


xx = coin.get_analysis()
print(xx)
print(type(xx))

"""

tv = TradingView()
tv.search("QNBFB")
"""
