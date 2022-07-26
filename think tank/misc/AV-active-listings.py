# # My AlphaVantage API key! TJOCDKQ1PCX3BW7T
from yahoo_fin import stock_info as si
from pandas import ExcelWriter
import pandas as pd
import requests
import json
import csv

pd.set_option('display.width', 160)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# If no date is set, the API endpoint will return a list of active or delisted symbols as of the latest trading day
# By default, state=active and the API will return a list of actively traded stocks and ETFs. Set state=delisted to query a list of delisted assets
CSV_URL = 'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=demo'

with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    read_file = pd.read_csv (r'Path where the CSV file is stored\File name.csv')
    read_file.to_excel (r'Path to store the Excel file\File name.xlsx', index = None, header=True)

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print(row)

