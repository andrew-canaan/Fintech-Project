# # My AlphaVantage API key! TJOCDKQ1PCX3BW7T
import pandas as pd
import requests
import json

pd.set_option('display.width', 160)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol=A&apikey=TJOCDKQ1PCX3BW7T'
response = requests.get(url)

data = json.loads(response.text)

try:
    overview_data = pd.DataFrame.from_dict(data, orient = 'index', columns = ['Value'])
    writer = pd.ExcelWriter("company-overview-demo.xlsx")
    overview_data.to_excel(writer, "Output")
    writer.save()
except Exception as e:
    print(f"Failed due to {e}")