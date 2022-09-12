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

print("Collecting active stocks and ETFs standy...")
listings = FindActiveListings(excelOutput)
listingsToPop = list()
listingsToReturn = list() 

# Clean listings for null values.
for ind in listings.index:
    if not listings['Name'][ind] or not listings['Symbol'][ind] or not listings['Exchange'][ind] or not listings['Asset Type'][ind]:
        listingsToPop.append(ind)

for ind in listingsToPop:
    listings.drop([ind])
    print(f"Removing bad element with index {ind}")

count = 0
for ind in listings.index:
    if count >= 50:
        break

    print(f"Grabbing fundamental data for {listings['Symbol'][ind]}...")
    company_overview = GrabCompanyOverview(listings['Symbol'][ind], excelOutput)
    daily_price_history = GrabDailyPriceData(listings['Symbol'][ind], excelOutput)
    quarterly_company_earnings = GrabCompanyEarnings(listings['Symbol'][ind], excelOutput)

    count = count + 3

    # Check if each of our 8 potential criteria are active, if they are compare them in prio highest to lowest probability of filtering a asset.
    # E.g. if price active, it is a high prio to filter.
    if screen_config['Current Price']['active'] == True:
        print("Checking most recent Closing Price against filter...")
        asset_price = float(daily_price_history['4. close'].iloc[0]) # Grab most recent (0th) closing price of given asset.
        if screen_config['Current Price']['greater'] == True and asset_price < screen_config['Current Price']['value']:
            continue
        elif screen_config['Current Price']['less'] == True and asset_price > screen_config['Current Price']['value']:
            continue
        elif screen_config['Current Price']['equalto'] == True and asset_price != screen_config['Current Price']['value']:
            continue
    
    # This asset passed the first check, continue to check first if filter is active, then if asset passes that active filter. Add to subset at the end of all checks.

    if screen_config['Volume']['active'] == True:
        print("Checking Volume against filter...")
        asset_volume = float(daily_price_history['5. volume]'].iloc[0])
        if screen_config['Volume']['greater'] == True and asset_volume < screen_config['Volume']['value']:
            continue
        elif screen_config['Volume']['less'] == True and asset_volume > screen_config['Volume']['value']:
            continue
        elif screen_config['Volume']['equalto'] == True and asset_volume != screen_config['Volume']['value']:
            continue

    if screen_config['Market Cap']['active'] == True:
        print("Checking Market Cap against filter...")
        asset_market_cap = float(company_overview.loc['MarketCapitalization', 'Value'])
        if screen_config['Market Cap']['greater'] == True and asset_market_cap < screen_config['Market Cap']['value']:
            continue
        elif screen_config['Market Cap']['less'] == True and asset_market_cap > screen_config['Market Cap']['value']:
            continue
        elif screen_config['Market Cap']['equalto'] == True and asset_market_cap != screen_config['Market Cap']['value']:
            continue

    if screen_config['EPS']['active'] == True:
        print("Checking EPS against filter...")
        asset_EPS = float(quarterly_company_earnings['reportedEPS'].iloc[0])
        if screen_config['EPS']['greater'] == True and asset_EPS < screen_config['EPS']['value']:
            continue
        elif screen_config['EPS']['less'] == True and asset_EPS > screen_config['EPS']['value']:
            continue
        elif screen_config['EPS']['equalto'] == True and asset_EPS != screen_config['EPS']['value']:
            continue

    if screen_config['P/E']['active'] == True:
        print("Checking P/E against filter...")
        asset_PEratio = float(company_overview.loc['PERatio', 'Value'])
        if screen_config['P/E']['greater'] == True and asset_PEratio < screen_config['P/E']['value']:
            continue
        elif screen_config['P/E']['less'] == True and asset_PEratio > screen_config['P/E']['value']:
            continue
        elif screen_config['P/E']['equalto'] == True and asset_PEratio != screen_config['P/E']['value']:
            continue

    if screen_config['P/E/G']['active'] == True:
        print("Checking P/E/G against filter...")
        asset_PEGratio = float(company_overview.loc['PEGRatio', 'Value'])
        if screen_config['P/E/G']['greater'] == True and asset_PEGratio < screen_config['P/E/G']['value']:
            continue
        elif screen_config['P/E/G']['less'] == True and asset_PEGratio > screen_config['P/E/G']['value']:
            continue
        elif screen_config['P/E/G']['equalto'] == True and asset_PEGratio != screen_config['P/E/G']['value']:
            continue

    if screen_config['Beta']['active'] == True:
        print("Checking Beta against filter...")
        asset_beta = float(company_overview.loc['Beta', 'Value'])
        if screen_config['Beta']['greater'] == True and asset_beta < screen_config['Beta']['value']:
            continue
        elif screen_config['Beta']['less'] == True and asset_beta > screen_config['Beta']['value']:
            continue
        elif screen_config['Beta']['equalto'] == True and asset_beta != screen_config['Beta']['value']:
            continue

    if screen_config['Dividends Y/N']['active'] == True:
        print("Checking dividend status...")
        asset_dividend_bool = company_overview.loc['DividendDate']['Value']
        if asset_dividend_bool == "" and screen_config['Dividends Y/N']['value'] == True: # If dividend bool filter is active, and we are looking for company with dividends but no date found, skip
            continue
        if asset_dividend_bool != "" and screen_config['Dividends Y/N']['value'] == False: # If dividend bool filter is active, and we are not looking for a company with dividends, and date is found, skip
            continue

    # If the asset made it this far, it passed all applicable filters. Add it to return list.
    listingsToReturn.append(listings['Symbol'][ind])

    # This call is commented because with the initial 8 critieria, we only need company overview, daily price hist, and quarterly company earnings
    # quarterly_balance_sheets, annual_balance_sheets = GrabBalanceSheet(listings['Symbol'][ind], excelOutput)
    # break # BREAK PREVENTS ME FROM OVER-QUERYING API

print(listingsToReturn)

print("Execution time: %s seconds" % (time.time() - start_time))


# How to structure screens? 

# Some times given sector/industry is not 1 1:1 with the actual sector
# e.g. Life Sciences versus Life