from functools import partial
import yfinance as yf


def get_stock_price(ticker, start_date, end):
    return yf.download(ticker, start=start_date, end=end)

#data = get_stock_price("AAPL", "2018-01-01", "2019-03-01")

get_data_from_2018_2019 = partial(get_stock_price, start_date="2018-01-01",end="2019-03-01")

print(get_data_from_2018_2019("AAPL"))
