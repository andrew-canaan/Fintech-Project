from v1_1prototypehelpers import *

pd.set_option('display.width', 160)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

excelOutput = True

listings = list()
balance_sheets = list()
company_overview = pd.DataFrame()
daily_price_history = pd.DataFrame()
company_earnings = list()

listings = FindActiveListings(excelOutput)

for item in listings:
    print(item['Symbol'])
    # balance_sheets = GrabBalanceSheet(item['Symbol'], excelOutput)
    # company_overview = GrabCompanyOverview(item['Symbol'], excelOutput)
    # daily_price_history = GrabDailyPriceData(item['Symbol'], excelOutput)
    # company_earnings = GrabCompanyEarnings(item['Symbol'], excelOutput)