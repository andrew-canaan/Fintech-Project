# # My AlphaVantage API key! TJOCDKQ1PCX3BW7T
from yahoo_fin import stock_info as si
from pandas import ExcelWriter
import pandas as pd
import requests
import csv

pd.set_option('display.width', 160)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# https://requests.readthedocs.io/en/latest/user/advanced/
# If no date is set, the API endpoint will return a list of active or delisted symbols as of the latest trading day
# By default, state=active and the API will return a list of actively traded stocks and ETFs. Set state=delisted to query a list of delisted assets
CSV_URL = 'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=demo'

exportList = pd.DataFrame(columns=['Symbol', 'Name', 'Exchange', 'Asset Type'])

with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)

    for row in my_list:
        if (len(row[0]) <= 4):
            exportList = exportList.append({'Symbol': row[0], 'Name': row[1], 'Exchange': row[2], 'Asset Type': row[3]}, ignore_index = True)

writer = ExcelWriter("AV-active-listings.xlsx")
exportList.to_excel(writer, "Output")
writer.save()