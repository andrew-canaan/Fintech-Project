from v1_1prototypehelpers import *
import time

start_time = time.time()

pd.set_option('display.width', 160)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

excelOutput = False # Does user want to generate an excel sheet?

listings = FindActiveListings(excelOutput)

for ind in listings.index:
    quarterly_balance_sheets, annual_balance_sheets = GrabBalanceSheet(listings['Symbol'][ind], excelOutput)
    company_overview = GrabCompanyOverview(listings['Symbol'][ind], excelOutput)
    daily_price_history = GrabDailyPriceData(listings['Symbol'][ind], excelOutput)
    quarterly_company_earnings, annual_company_earnings = GrabCompanyEarnings(listings['Symbol'][ind], excelOutput)
    break # BREAK PREVENTS ME FROM OVER-QUERYING API

print("Execution time: %s seconds" % (time.time() - start_time))