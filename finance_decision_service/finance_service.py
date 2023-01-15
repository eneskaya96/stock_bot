from typing import List, Dict
import pandas as pd

import yfinance as yf

def get_symbol_data(symbols: List[str], period: str, interval: str) -> pd.DataFrame:
    data = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers=symbols,

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period=period,

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval=interval,

        # Whether to ignore timezone when aligning ticker data from
        # different timezones. Default is True. False may be useful for
        # minute/hourly data.
        ignore_tz=False,

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by='ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust=True,

        # attempt repair of missing data or currency mixups e.g. $/cents
        repair=False,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost=True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads=True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy=None
    )
    return data


def get_current_data(symbols: List[str], number_of_symbol: int) -> Dict[str, float]:
    all_data = get_symbol_data(symbols=symbols, period="1d", interval="15m")
    list_of_data = parse_data(data=all_data, number_of_symbol=number_of_symbol)

    current_prices = {}
    for l in list_of_data:
        symbol, _ = l.columns[0]
        l.columns = ["OPEN", "HIGH", "LOW", "CLOSE", "VOLUME"]
        current_prices[symbol] = l.iloc[-1]["OPEN"]

    return current_prices


def parse_data(data: pd.DataFrame, number_of_symbol: int) -> List[pd.DataFrame]:
    columns = data.columns
    list_of_data = []
    for i in range(0, number_of_symbol):
        symbol_data = data.loc[:, columns[i * 5:(i + 1) * 5]]
        list_of_data.append(symbol_data)

    return list_of_data


def get_last_3_day_average(symbols: List[str], number_of_symbol: int) -> Dict[str, float]:
    all_data = get_symbol_data(symbols=symbols, period="3d", interval="1d")
    list_of_data = parse_data(data=all_data, number_of_symbol=number_of_symbol)

    threed_average_prices = {}
    for l in list_of_data:
        symbol, _ = l.columns[0]
        l.columns = ["OPEN", "HIGH", "LOW", "CLOSE", "VOLUME"]
        average_of_high_and_low = l[["HIGH", "LOW"]].mean()
        threed_average_prices[symbol] = average_of_high_and_low.mean()

    return threed_average_prices
