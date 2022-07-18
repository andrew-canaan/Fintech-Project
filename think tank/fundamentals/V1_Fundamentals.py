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

# aapl = yf.Ticker("AAPL")

# aapl_quoteTable = si.get_quote_table("AAPL", dict_result = False)

# aapl_statsValuation = si.get_stats_valuation("AAPL")

# print('Sector: ' + aapl.info['sector'] + '\nIndustry: ' + aapl.info['industry'] + '\n')
# print(aapl_quoteTable)
# print("\n")
# print(aapl_statsValuation)

tickers = si.tickers_nasdaq()

tickers = [item.replace(".", "-") for item in tickers]
tickers = tickers[0:100] 