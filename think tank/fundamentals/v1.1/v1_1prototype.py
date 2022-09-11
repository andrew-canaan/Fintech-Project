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
        break
    exit_code = False

# Process the screen_config, and assign conditions
screen_config_copy = screen_config.copy()
for key in screen_config_copy.keys():
    if screen_config[key]['active'] == False:
        screen_config.pop(key)

listings = FindActiveListings(excelOutput)
listingsToPop = list()

# Clean listings for null values.
for ind in listings.index:
    if not listings['Name'][ind] or not listings['Symbol'][ind] or not listings['Exchange'][ind] or not listings['Asset Type'][ind]:
        listingsToPop.append(ind)

for ind in listingsToPop:
    listings.drop([ind])

for ind in listings.index:
    company_overview = GrabCompanyOverview(listings['Symbol'][ind], excelOutput)
    daily_price_history = GrabDailyPriceData(listings['Symbol'][ind], excelOutput)
    quarterly_company_earnings = GrabCompanyEarnings(listings['Symbol'][ind], excelOutput)

    # Check if each of our 8 potential criteria are active, if they are compare them in prio highest to lowest probability of filtering a asset.
    # E.g. if price active, it is a high prio to filter.
    if screen_config['Current Price']['Active'] == True:
        asset_price = daily_price_history['4. close'].iloc[0] # Grab most recent (0th) closing price of given asset.
        if screen_config['Current Price']['greater'] == True and asset_price < screen_config['Current Price']['value']:
            continue
        elif screen_config['Current Price']['less'] == True and asset_price > screen_config['Current Price']['value']:
            continue
        elif screen_config['Current Price']['equalto'] == True and asset_price != screen_config['Current Price']['value']:
            continue
    
    # This asset passed the first check, continue to check first if filter is active, then if asset passes that active filter. Add to subset at the end of all checks.

    if screen_config['Volume']['Active'] == True:
        asset_volume = daily_price_history['5. volume]'].iloc[0]
        if screen_config['Volume']['greater'] == True and asset_volume < screen_config['Volume']['value']:
            continue
        if screen_config['Volume']['less'] == True and asset_volume > screen_config['Volume']['value']:
            continue
        if screen_config['Volume']['equalto'] == True and asset_volume != screen_config['Volume']['value']:
            continue

    # if screen_config['']['Active'] == True:
    # if screen_config['']['Active'] == True:
    # if screen_config['']['Active'] == True:
    # if screen_config['']['Active'] == True:
    # if screen_config['']['Active'] == True:
    # if screen_config['']['Active'] == True:

    # This call is commented because with the initial 8 critieria, we only need company overview, daily price hist, and quarterly company earnings
    # quarterly_balance_sheets, annual_balance_sheets = GrabBalanceSheet(listings['Symbol'][ind], excelOutput)
    break # BREAK PREVENTS ME FROM OVER-QUERYING API


print("Execution time: %s seconds" % (time.time() - start_time))


# How to structure screens? 

# Some times given sector/industry is not 1 1:1 with the actual sector
# e.g. Life Sciences versus Life