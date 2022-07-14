# My AlphaVantage API key! TJOCDKQ1PCX3BW7T
from yahoo_fin import stock_info as si
import requests
import pandas as pd

# tickers = si.tickers_sp500()
# tickers = tickers[0:20]

# url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={tickers[1]}&apikey=TJOCDKQ1PCX3BW7T'
# response = requests.get(url)
# data = response.json()

# df = data.json_normalize()

# print(data.head(10))
