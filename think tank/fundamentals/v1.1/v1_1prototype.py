from v1_1prototypehelpers import *

pd.set_option('display.width', 160)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

excelOutput = False # Does user want to generate an excel sheet?

listings = list() # All 9,000+ valid listings (stock, etf) that are active
balance_sheets = list() # Holds annual and quarterly balance sheets for a given company
company_overview = pd.DataFrame() # Dataframe with fundamentals and other useful info
daily_price_history = pd.DataFrame() # Dataframe with daily price info going back 100 days, or until inception date
company_earnings = list() # Holds annual and quarterly earnings for a given company

listings = FindActiveListings(excelOutput)

for ind in listings.index:
    balance_sheets = GrabBalanceSheet(listings['Symbol'][ind], excelOutput)
    company_overview = GrabCompanyOverview(listings['Symbol'][ind], excelOutput)
    daily_price_history = GrabDailyPriceData(listings['Symbol'][ind], excelOutput)
    company_earnings = GrabCompanyEarnings(listings['Symbol'][ind], excelOutput)
    break
