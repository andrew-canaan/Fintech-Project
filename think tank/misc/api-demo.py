# # My AlphaVantage API key! TJOCDKQ1PCX3BW7T
from yahoo_fin import stock_info as si
import pandas as pd
import requests

pd.set_option('display.width', 160)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

tickers = si.tickers_sp500()

# JSON Version:
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={tickers[0]}&apikey=TJOCDKQ1PCX3BW7T'
response = requests.get(url)

try:
    data = response.json()
    df = pd.DataFrame.from_dict(data, orient = "index")
    df.to_csv(f'{tickers[0]}.csv')
except Exception as e:
    print(e)