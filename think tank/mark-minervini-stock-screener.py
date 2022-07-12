import datetime as dt
from re import S
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
from pandas import ExcelWriter

def get_stocklist(filepath): 
    stocklist = pd.read_excel(filepath)
    return stocklist.head(1000)


def apply_mark_minervi(stock, close, sma_50, sma_150, sma_200, sma_200_adj, 
                       wk52_low, wk52_high, rs_rating, exportlist):
    cond1 = False    
    cond2 = False
    cond3 = False
    cond4 = False
    cond5 = False
    cond6 = False
    cond7 = False
    cond8 = False

    # Check a given stock with the data we collected and apply Mark Minervi logic
    if close > sma_150 and close > sma_200:
        cond1 = True
    if sma_150 > sma_200:
        cond2 = True
    if sma_200 > sma_200_adj:
        cond3 = True
    if sma_50 > sma_150 and sma_50 < sma_200:
        cond4 = True
    if close > sma_50:
        cond5 = True
    if close >= 1.3 * wk52_low: # Current price is at least 30% above 52 wk low 
        cond6 = True
    if close >= .75 * wk52_high:
        cond7 = True
    if (rs_rating > 70):
        cond8 = True
    
    if cond1 and cond2 and cond3 and cond4 and cond5 and cond6 and cond7 and cond8:
        return exportlist.append({'Stock': stock, "RS_Rating": rs_rating, "50 Day MA": sma_50, 
                                  "150 Day Ma": sma_150, "200 Day MA": sma_200, "52 Week Low": wk52_low, 
                                  "52 week High": wk52_high}, ignore_index=True)
    else:
        return exportlist

def process_stocklist(stocklist, exportlist, start, end):
    for n in stocklist.index:
        stock = str(stocklist["Symbol"][n])
        rs_rating = str(stocklist["RS Rating"][n])

        try:
            yahoo_df = pdr.get_data_yahoo(stock, start, end)

            sma_arr = [50, 150, 200]
            for sma in sma_arr:
                # add SMA columns for each SMA to the data frame
                yahoo_df["SMA_" + str(sma)] = round(yahoo_df.iloc[:,4].rolling(window = sma).mean(), 2)
            
            #-1 is most recent value in yahoo dataframe
            close = yahoo_df["Adj Close"][-1] 
            sma_50 = yahoo_df["SMA_50"][-1]
            sma_150 = yahoo_df["SMA_150"][-1]
            sma_200 = yahoo_df["SMA_200"][-1]

            # min value of the previous 260 trading days (52 weeks)
            wk52_low = min(yahoo_df["Adj Close"][-260:])
            wk52_high = max(yahoo_df["Adj Close"][-260:])

            try:
                # Grab the sma 200 that has been trending upward for at least 20 days per the Mark Minervi algo
                sma_200_adj = yahoo_df["SMA_200"][-20]
            except Exception:
                sma_200_adj = 0 

            apply_mark_minervi(stock, sma_50, sma_150, sma_200, sma_200_adj, 
                            wk52_low, wk52_high, rs_rating, exportlist)
            
        except Exception:
            print("No data on " + stock + "\n")

# main
yf.pdr_override()
start = dt.datetime(2017, 1, 1) 
end = dt.datetime.now()

filepath = r"C:\Users\Andrew Canaan\Documents\repos\Fintech-Project\think tank\RichardStocks.xlsx"
stocklist = get_stocklist(filepath)

exportlist = pd.DataFrame(columns=['Stock', "RS_Rating", "50 Day MA", "150 Day MA", "200 Day MA", 
                                    "200 Day MA", "52 Week Low", "52 Week High"])

exportlist = process_stocklist(stocklist, exportlist, start, end)

print(exportlist.head())



