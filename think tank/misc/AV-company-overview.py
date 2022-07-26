# # My AlphaVantage API key! TJOCDKQ1PCX3BW7T
from yahoo_fin import stock_info as si
from pandas import ExcelWriter
import pandas as pd
import requests
import json

pd.set_option('display.width', 160)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=TJOCDKQ1PCX3BW7T'
response = requests.get(url)

data = json.loads(response.text)

overview_data = pd.DataFrame.from_dict(data, orient = 'index', columns = ['Value'])

writer = ExcelWriter("company-overview-demo.xlsx")
overview_data.to_excel(writer, "Output")
writer.save()