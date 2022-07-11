# My AlphaVantage API key! TJOCDKQ1PCX3BW7T
# Requires 'pip install requests'

import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=TJOCDKQ1PCX3BW7T'
r = requests.get(url)
data = r.json()

# Prints data. Data is a JSON formatted list of intraday (5 minutes) price data. Price data includes: open, high, low, close, volume for the asset IBM.
# To view a different asset, different time series, or different api key user must modify the requested url from above.
print(data)
