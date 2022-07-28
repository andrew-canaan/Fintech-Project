# # My AlphaVantage API key! TJOCDKQ1PCX3BW7T
import pandas as pd
import requests
import json

pd.set_option('display.width', 160)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# JSON Version:
# for at home: https://stackoverflow.com/questions/67277838/convert-alphavantage-api-response-to-dataframe
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=TJOCDKQ1PCX3BW7T'
response = requests.get(url)

data = json.loads(response.text)
df = pd.DataFrame(data["Time Series (Daily)"])

# Transpose the data frame such that rows are dates, and columns are 'open', 'low', 'high', 'close'
stock_data = df.T

writer = pd.ExcelWriter("daily-price-demo.xlsx")
stock_data.to_excel(writer, "Output")
writer.save()

# Notes
# Convert data to dict:
#   data = json.loads(response.text)

# Convert dict to string:
#   data = json.dumps(data)
