from v1_1prototypehelpers import *
from v1_1prototypemenu import *
import time

start_time = time.time()

# Is screen greater than, less than, or equal to value 
screen_config = {
    "Current Price": {"active": False, "greater": False, "less": False, "equalto": False, "value": 0},
    "Market Cap":    {"active": False, "greater": False, "less": False, "equalto": False, "value": 0},
    "Volume":        {"active": False, "greater": False, "less": False, "equalto": False, "value": 0},
    "Dividends Y/N": {"active": False, "value": False}, 
    "EPS":           {"active": False, "greater": False, "less": False, "equalto": False, "value": 0},
    "P/E":           {"active": False, "greater": False, "less": False, "equalto": False, "value": 0},
    "P/E/G":         {"active": False, "greater": False, "less": False, "equalto": False, "value": 0},  
    "Beta":          {"active": False, "greater": False, "less": False, "equalto": False, "value": 0},
}

pd.set_option('display.width', 160)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

excelOutput = False # Does user want to generate an excel sheet?

while(True):
    exit_code = False
    display_menu()
    option = ''
    try:
        option = int(input('Enter your selection: '))
    except:
        print('Invalid input, please try again.')
    screen_config = process_options(option, screen_config)

    try:
        option = str(input('Would you like to add additional screens? Y/N: '))
    except:
        print('Invalid input...')

    if option == 'n' or option == 'N' or option == 'no' or option == 'No':
        exit_code = True

    if exit_code:
        print("Execution time: %s seconds" % (time.time() - start_time))
        break
    exit_code = False

print(screen_config)
#listings = FindActiveListings(excelOutput)

# for ind in listings.index:
    
#     company_overview = GrabCompanyOverview(listings['Symbol'][ind], excelOutput)
#     quarterly_balance_sheets, annual_balance_sheets = GrabBalanceSheet(listings['Symbol'][ind], excelOutput)
#     daily_price_history = GrabDailyPriceData(listings['Symbol'][ind], excelOutput)
#     quarterly_company_earnings, annual_company_earnings = GrabCompanyEarnings(listings['Symbol'][ind], excelOutput)
#     break # BREAK PREVENTS ME FROM OVER-QUERYING API

print("Execution time: %s seconds" % (time.time() - start_time))


# How to structure screens? 

# Some times given sector/industry is not 1 1:1 with the actual sector
# e.g. Life Sciences versus Life