# # My AlphaVantage API key! TJOCDKQ1PCX3BW7T
from yahoo_fin import stock_info as si
import pandas as pd
import requests
import json

pd.set_option('display.width', 160)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

tickers = si.tickers_nasdaq()

# JSON Version:
# for at home: https://stackoverflow.com/questions/67277838/convert-alphavantage-api-response-to-dataframe
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={tickers[0]}&apikey=TJOCDKQ1PCX3BW7T'
response = requests.get(url)
