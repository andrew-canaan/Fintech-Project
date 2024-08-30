from pandas_datareader import data as web
from yahoo_fin import stock_info as si
from pandas import ExcelWriter
import yfinance as yf
import pandas as pd
import numpy as np
import datetime
import time
import os

yf.pdr_override()
pd.options.display.width = 0

start_date = datetime.datetime.now() - datetime.timedelta(days = 365)
end_date = datetime.date.today()

# tickers_nasdaq = si.tickers_nasdaq()
# tickers_nasdaq = [item.replace(".", "-") for item in tickers_nasdaq] # yahoo finance prefers dashes in the tickers, not periods
# index_name = '^IXIC'  # S&P 500: ^GSPC  Dow Jones: ^DJI   Nasdaq: ^IXIC

# # for item in tickers_nasdaq:
# #     # Set a time delay between each stock
# #     time.sleep(0.01)

# #     df = web.get_data_yahoo(item, start_date, end_date) # https://pandas-datareader.readthedocs.io/en/latest/remote_data.html

# #     print(df.head())

df = web.get_data_yahoo('IBM', start_date, end_date)

print(df.tail(100))
