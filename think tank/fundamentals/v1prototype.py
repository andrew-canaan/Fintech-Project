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
#   Ex-Dividend Date

from pandas_datareader import data as web
from yahoo_fin import stock_info as si
from pandas import ExcelWriter
import yfinance as yf
import pandas as pd
import numpy as np
import datetime
import time
import os

from v1prototype_helpers import *

start_time = time.time()

yf.pdr_override()
pd.set_option('display.width', 160)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

start_date = datetime.datetime.now() - datetime.timedelta(days = 365)
end_date = datetime.date.today()

tickers = []
symbols = si.tickers_nasdaq()
symbols = symbols[0:20] 
 
for symbol in symbols:
    if len(symbol) <= 4:
        symbol.replace('.', '-')
        tickers.append(yf.Ticker(symbol))

index_used = '^IXIC' 
index_data = web.get_data_yahoo(index_used, start_date, end_date)
index_data["% Change"] = index_data["Adj Close"].pct_change()

screenedList = pd.DataFrame(columns = ['Stock', 'Industry', 'Sector', 'Price', 'Avg. Volume', 'Volume', 'Market Cap', 'Trailing P/E Ratio', 
                                      'P/EG Ratio', 'Beta', 'Trailing E/PS', '12 mo Trailing P/S'])
for ticker in tickers:
    screenedList = grab_fundamentals(ticker, screenedList)

    time.sleep(0.01)

writer = ExcelWriter("v1prototype.xlsx")
screenedList.to_excel(writer, "Output")
writer.save()

print("Execution time: %s seconds" % (time.time() - start_time))
# Graveyard:
# data = pd.DataFrame.from_dict(tickers[0].info, orient = 'index', columns = ['Value'])
# print(data)
# quote_table = si.get_quote_table(ticker.info['symbol'], dict_result = True) THIS SHIT BROKEN AF FUCK GET_QUOTE_TABLE