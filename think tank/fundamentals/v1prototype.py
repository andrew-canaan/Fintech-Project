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
tickers = tickers[0:100] 
tickers = [item.replace(".", "-") for item in tickers]

index_used = '^IXIC' # index symbol for NASDAQ
index_data = web.get_data_yahoo(index_used, start_date, end_date)
index_data["% Change"] = index_data["Adj Close"].pct_change()

screenedList = pd.DataFrame(columns = ['Stock', 'Industry', 'Sector', 'Price', 'Volume (24h)', 'Market Cap', 'P/E Ratio', 
                                      'P/E/G Ratio', 'Beta', 'Earnings Date', 'EPS'])

for ticker in tickers:
    try:
        quote_table = si.get_quote_table(str(ticker), dict_result = False)

        earnings_date = str(quote_table["Earnings Date"])
        eps = quote_table["EPS (TTM)"]
        PE_ratio = quote_table["PE Ratio (TTM)"]
        
    except Exception as e:
        print(e)


    # industry = ticker.info['industry']
    # sector = ticker.info['sector']
    # price = ticker.info['price']
    # vol_24h = ticker.info['volume24Hr']
    # market_cap = ticker.info['marketCap']
    # PEG_ratio = ticker.info['pegRatio']
    # beta = ticker.info['beta']

    # screenedList.append({'Stock': ticker, 'Industry': industry, 'Sector': sector, 'Price': price, 'Volume (24h)': vol_24h, 
    #                     'Market Cap': market_cap, 'P/E Ratio': PE_ratio, 'P/E/G Ratio': PEG_ratio, 'Beta': beta, 
    #                     'Earnings Date': earnings_date, 'EPS': eps})