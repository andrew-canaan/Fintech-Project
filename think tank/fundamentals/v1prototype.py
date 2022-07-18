# This program is a v1.0 version of the stock screener.
# It reads a menu to the user, then reads in user selection to generate a screened stock list.
# The screens that it makes available include:
#   Mark Cap >, =, <
#   Price (current)
#   EPS
#   P/E Ratio
#   PEG Ratio
#   Beta
#   Sector
#   Industry
#   Volume (24h)
#   Earnings Date

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

start_date = datetime.datetime.now() - datetime.timedelta(days = 365)
end_date = datetime.date.today()

tickers = si.tickers_nasdaq()
tickers = [item.replace(".", "-") for item in tickers]
tickers = tickers[0:100] 

index_used = '^IXIC' # index symbol for NASDAQ
index_data = web.get_data_yahoo(index_used, start_date, end_date)
index_data["% Change"] = index_data["Adj Close"].pct_change()

screenedList = pd.DataFrame(columns = 'Stock', 'Industry', 'Sector', 'Price', 'Volume (24h)', 'Market Cap', 'P/E Ratio', 
                                      'P/E/G Ratio', 'Beta', 'Earnings Date', 'EPS')

