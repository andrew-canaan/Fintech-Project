# # My AlphaVantage API key! TJOCDKQ1PCX3BW7T
from yahoo_fin import stock_info as si
from pandas import ExcelWriter
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

try:
    response = requests.get(url)

    data = json.loads(response.text)
    df = pd.DataFrame(data["Time Series (Daily)"])

    stock_data = df.T

    writer = ExcelWriter("api-demo.xlsx")
    stock_data.to_excel(writer, "Output")
    writer.save()
except Exception as e:
    print("Error occurred: ", e)



# Notes
# Convert data to dict:
#   data = json.loads(response.text)

# Convert dict to string:
#   data = json.dumps(data)
