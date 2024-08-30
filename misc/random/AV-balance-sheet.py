# # My AlphaVantage API key! TJOCDKQ1PCX3BW7T
import pandas as pd
import requests
import json

pd.set_option('display.width', 160)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=IBM&apikey=TJOCDKQ1PCX3BW7T'
response = requests.get(url)

data = json.loads(response.text)

annual_balance_sheet_data = pd.DataFrame(data['annualReports'])
quarterly_balance_sheet_data = pd.DataFrame(data['quarterlyReports'])

writer = pd.ExcelWriter("annual-balance-sheet-demo.xlsx")
annual_balance_sheet_data.to_excel(writer, "Output")
writer.save()

writer = pd.ExcelWriter("quarterly-balance-sheet-demo.xlsx")
quarterly_balance_sheet_data.to_excel(writer, "Output")
writer.save()