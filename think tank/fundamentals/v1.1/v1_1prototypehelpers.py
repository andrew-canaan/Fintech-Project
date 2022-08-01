import pandas as pd
import requests
import json
import csv

# Returns a dataframe containing active ETF/stocks that have symbols less than or equal to 4 characters 
def FindActiveListings(excelFlag):
    # If no date is set, the API endpoint will return a list of active or delisted symbols as of the latest trading day
    # By default, state=active and the API will return a list of actively traded stocks and ETFs. Set state=delisted to query a list of delisted assets
    CSV_URL = 'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=TJOCDKQ1PCX3BW7T'

    exportList = pd.DataFrame(columns=['Symbol', 'Name', 'Exchange', 'Asset Type'])

    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)

        for row in my_list:
            if (len(row[0]) <= 4):
                try:
                    exportList = exportList.append({'Symbol': row[0], 'Name': row[1], 'Exchange': row[2], 'Asset Type': row[3]}, ignore_index = True)
                except Exception as e:
                    print("\n", e)

    if excelFlag: 
        writer = pd.ExcelWriter("active-listings.xlsx")
        exportList.to_excel(writer, "Output")
        writer.save()

    return exportList

def GrabBalanceSheet(symbol, excelFlag):
    # balance_sheets = list()

    url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey=TJOCDKQ1PCX3BW7T'
    response = requests.get(url)

    data = json.loads(response.text)

    annual_balance_sheet_data = pd.DataFrame(data['annualReports'])
    quarterly_balance_sheet_data = pd.DataFrame(data['quarterlyReports'])

    # balance_sheets.append(annual_balance_sheet_data)
    # balance_sheets.append(quarterly_balance_sheet_data)

    if excelFlag:
        writer = pd.ExcelWriter("annual-balance-sheet-demo.xlsx")
        annual_balance_sheet_data.to_excel(writer, "Output")
        writer.save()

        writer = pd.ExcelWriter("quarterly-balance-sheet-demo.xlsx")
        quarterly_balance_sheet_data.to_excel(writer, "Output")
        writer.save()

    return quarterly_balance_sheet_data, annual_balance_sheet_data

def  GrabCompanyOverview(symbol, excelFlag):
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey=TJOCDKQ1PCX3BW7T'
    response = requests.get(url)

    data = json.loads(response.text)

    overview_data = pd.DataFrame.from_dict(data, orient = 'index', columns = ['Value'])

    if excelFlag:
        writer = pd.ExcelWriter("company-overview-demo.xlsx")
        overview_data.to_excel(writer, "Output")
        writer.save()

    return overview_data

def GrabDailyPriceData(symbol, excelFlag):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=TJOCDKQ1PCX3BW7T'
    response = requests.get(url)

    data = json.loads(response.text)
    df = pd.DataFrame(data["Time Series (Daily)"])

    # Transpose the data frame such that rows are dates, and columns are 'open', 'low', 'high', 'close'
    stock_data = df.T

    if excelFlag:
        writer = pd.ExcelWriter("daily-price-demo.xlsx")
        stock_data.to_excel(writer, "Output")
        writer.save()

    return stock_data

def GrabCompanyEarnings(symbol, excelFlag):
    # earnings = list()

    url = f'https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol}&apikey=TJOCDKQ1PCX3BW7T'
    response = requests.get(url)

    data = json.loads(response.text)

    annual_earnings_data = pd.DataFrame(data['annualEarnings'])
    quarterly_earnings_data = pd.DataFrame(data['quarterlyEarnings'])

    # earnings.append(annual_earnings_data)
    # earnings.append(quarterly_earnings_data)

    if excelFlag:
        writer = pd.ExcelWriter("annual-earnings-demo.xlsx")
        annual_earnings_data.to_excel(writer, "Output")
        writer.save()

        writer = pd.ExcelWriter("quarterly-earnings-demo.xlsx")
        quarterly_earnings_data.to_excel(writer, "Output")
        writer.save()

    return quarterly_earnings_data, annual_earnings_data