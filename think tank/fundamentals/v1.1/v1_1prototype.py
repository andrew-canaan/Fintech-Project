from v1_1prototypehelpers import *
from v1_1prototypemenu import *
import time

start_time = time.time()

screens = list() # Used to hold user input for which screens they wish to apply

menu_options = {
    "Market Cap":    {"active": False, "greater": False, "less": False, "equalto": False, "value": 0},
    "Current Price": {"active": False, "greater": False, "less": False, "equalto": False, "value": 0}, # Is screen greater than, less than, or equal to value 
    "Volume":        {"active": False, "greater": False, "less": False, "equalto": False, "value": 0},
    "Dividends Y/N": {"active": False, "value": False},
    "EPS":           {"active": False, "greater": False, "less": False, "equalto": False, "value": 0},
    "P/E":           {"active": False, "greater": False, "less": False, "equalto": False, "value": 0},
    "P/E/G":         {"active": False, "greater": False, "less": False, "equalto": False, "value": 0},  
    "Beta":          {"active": False, "greater": False, "less": False, "equalto": False, "value": 0}
}

pd.set_option('display.width', 160)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

excelOutput = False # Does user want to generate an excel sheet?

listings = FindActiveListings(excelOutput)

for ind in listings.index:
    
    company_overview = GrabCompanyOverview(listings['Symbol'][ind], excelOutput)
    quarterly_balance_sheets, annual_balance_sheets = GrabBalanceSheet(listings['Symbol'][ind], excelOutput)
    daily_price_history = GrabDailyPriceData(listings['Symbol'][ind], excelOutput)
    quarterly_company_earnings, annual_company_earnings = GrabCompanyEarnings(listings['Symbol'][ind], excelOutput)
    break # BREAK PREVENTS ME FROM OVER-QUERYING API

print("Execution time: %s seconds" % (time.time() - start_time))


# How to structure screens? 

# Some times given sector/industry is not 1 1:1 with the actual sector
# e.g. Life Sciences versus Life