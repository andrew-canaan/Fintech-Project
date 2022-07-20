from yahoo_fin import stock_info as si
import yfinance as yf
import pandas as pd

# def initialize():
#     yf.pdr_override()
#     pd.set_option('display.width', 160)
#     pd.set_option('display.max_columns', None)
#     pd.set_option('display.max_rows', None)

def grab_fundamentals(tickerObj, screenedList):
    tickerData = tickerObj.info

    if "trailingEps" in tickerData.keys():
        trailing_eps = tickerData['trailingEps']
    else:
        trailing_eps = None

    if "priceToSalesTrailing12Months" in tickerData.keys():
        trailing_ps = tickerData['priceToSalesTrailing12Months']
    else:
        trailing_ps = None

    if "currentPrice" in tickerData.keys():
        price = tickerData['currentPrice']
    else:
        price = None

    if price != None and trailing_eps != None:
        trailing_pe = price / trailing_eps
    else:
        trailing_pe = None
    
    if "averageVolume" in tickerData.keys():
        avg_volume = tickerData['averageVolume']
    else:
        avg_volume = None

    if "volume" in tickerData.keys():
        volume = tickerData['volume']

    if "industry" in tickerData.keys():
        industry = tickerData['industry']
    else:
        industry = None

    if "sector" in tickerData.keys():
        sector = tickerData['sector']
    else:
        sector = None

    if "marketCap" in tickerData.keys():
        market_cap = tickerData['marketCap']
    else:
        market_cap = None

    if "pegRatio" in tickerData.keys():
        PEG_ratio = tickerData['pegRatio']
    else:
        PEG_ratio = None

    if "beta" in tickerData.keys():
        beta = tickerData['beta']
    else:
        beta = None

    return screenedList.append({'Stock': tickerObj.info['symbol'], 'Industry': industry, 'Sector': sector, 'Price': price, 
                                        'Avg. Volume': avg_volume, 'Volume': volume, 'Market Cap': market_cap, 'Trailing P/E Ratio': trailing_pe, 
                                        'P/EG Ratio': PEG_ratio, 'Beta': beta, 'Trailing E/PS': trailing_eps, '12 mo Trailing P/S': trailing_ps},
                                        ignore_index = True)