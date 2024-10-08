# # My AlphaVantage API key! TJOCDKQ1PCX3BW7T
import pandas as pd
import requests
import json

pd.set_option('display.width', 160)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

url = f'https://www.alphavantage.co/query?function=EARNINGS&symbol=IBM&apikey=TJOCDKQ1PCX3BW7T'
response = requests.get(url)

data = json.loads(response.text)

try:
#annual_earnings_data = pd.DataFrame(data['annualEarnings'])
    quarterly_earnings_data = pd.DataFrame(data['quarterlyEarnings'])

# writer = pd.ExcelWriter("annual-earnings-demo.xlsx")
# annual_earnings_data.to_excel(writer, "Output")
# writer.save()

    writer = pd.ExcelWriter("quarterly-earnings-demo.xlsx")
    quarterly_earnings_data.to_excel(writer, "Output")
    writer.save()      
except Exception as e:
    print("Failed due to {e}")