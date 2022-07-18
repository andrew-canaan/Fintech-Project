# # My AlphaVantage API key! TJOCDKQ1PCX3BW7T
# from yahoo_fin import stock_info as si
# import requests
# import pandas as pd

# tickers = si.tickers_sp500()
# tickers = tickers[0:20]

# url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={tickers[0]}&apikey=TJOCDKQ1PCX3BW7T'
# response = requests.get(url)
# data = response.json()

# df = pd.json_normalize(data)

# print(df.head(10))
from yahoo_fin import stock_info as si
import pandas as pd
import requests

tickers = si.tickers_sp500()

url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={tickers[0]}&apikey=TJOCDKQ1PCX3BW7T'
response = requests.get(url)

try:
    data = response.json()
except Exception as e:
    print(e)

df = pd.DataFrame.from_dict(data, orient = "index")

print(df.head(20))