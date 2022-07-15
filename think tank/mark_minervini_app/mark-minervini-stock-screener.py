# https://towardsdatascience.com/making-a-stock-screener-with-python-4f591b198261
# Reverse engineered the above program. Thank you Shashank Vemuri!
from pandas_datareader import data as web
from yahoo_fin import stock_info as si
from pandas import ExcelWriter
import yfinance as yf
import pandas as pd
import numpy as np
import datetime
import time
import os
 
yf.pdr_override()

# Grab all the tickers off the NASDAQ index using stock info
tickers = si.tickers_nasdaq()

# replace any tickers that have a '.' with a '-' if they exist
tickers = [item.replace(".", "-") for item in tickers]
tickers = tickers[0:100] # grab just the first 100 tickers out of 5k+ NASDAQ listings

# variables for later
start_date = datetime.datetime.now() - datetime.timedelta(days = 365)
end_date = datetime.date.today()

exportList = pd.DataFrame(columns=['Stock', "RS_Rating","Current Close", "50 Day MA", "150 Day Ma", "200 Day MA", "52 Week Low", "52 week High"])

returns_multiples = []

# NASDAQ info
index_used = '^IXIC' # index symbol for NASDAQ
index_data = web.get_data_yahoo(index_used, start_date, end_date)
index_data["% Change"] = index_data["Adj Close"].pct_change()
index_return = (index_data["% Change"] + 1).cumprod()[-1]

for ticker in tickers:
    try:
        stock_data = web.get_data_yahoo(ticker, start_date, end_date)
        stock_data.to_csv(f'{ticker}.csv')

        # Add % change column stock data frame, based on the % change of previous adj close price to curr adj close
        stock_data["% Change"] = stock_data["Adj Close"].pct_change()

        # Calculate % return on given stock by summing the cumulative % change. Returns a scalar decimal value
        # Exclude the first day as it has no value for % change
        stock_return = (stock_data["% Change"] + 1).cumprod()[-1]

        returns_multiple = round((stock_return / index_return), 2)
        returns_multiples.extend([returns_multiple])
    except Exception as e:
        print(e)
        print(f'Failed to calculate % change on {ticker}...')

    #print(f'Ticker: {ticker}; Returns Multiple against NASDAQ: {returns_multiple}\n')
    time.sleep(0.01)

# Create dataframe of only the top 30% from the list of tickers and corresponding returns
relative_strength_data = pd.DataFrame(list(zip(tickers, returns_multiples)), columns = ['Ticker', 'Returns_multiple'])
relative_strength_data['RS_Rating'] = relative_strength_data.Returns_multiple.rank(pct = True) * 100
relative_strength_data = relative_strength_data[relative_strength_data.RS_Rating >= relative_strength_data.RS_Rating.quantile(.7)]
relative_strength_stocks = relative_strength_data['Ticker'] # Grab all the tickers that are in the top 30% for RS score

# Loop through the stocks that are in the top 30% of all stocks on NASDAQ in terms of RS score
for stock in relative_strength_stocks:
    try:
        stock_data = pd.read_csv(f'{stock}.csv', index_col = 0)
        sma = [50, 150, 200]

        # Add SMA columns to the stock_data table, and populate the value
        for i in sma:
            stock_data["SMA_" + str(i)] = round(stock_data['Adj Close'].rolling(window = i).mean(), 2)

        # Storing required values 
        currentClose = stock_data["Adj Close"][-1]
        moving_average_50 = stock_data["SMA_50"][-1]
        moving_average_150 = stock_data["SMA_150"][-1]
        moving_average_200 = stock_data["SMA_200"][-1]
        low_of_52week = round(min(stock_data["Low"][-260:]), 2)
        high_of_52week = round(max(stock_data["High"][-260:]), 2)

        # no idea what this does but it grabs the RS rating for a given ticker
        RS_Rating = round(relative_strength_data[relative_strength_data['Ticker'] == stock].RS_Rating.tolist()[0])

        try:
            sma_200_adj = stock_data['SMA_200'][-20] 
        except Exception:
            sma_200_adj = 0 # if sma_200 adjusted 20 days prev fails

        # Condition 1: Current Price > 150 SMA and > 200 SMA
        condition_1 = currentClose > moving_average_150 > moving_average_200
        
        # Condition 2: 150 SMA and > 200 SMA
        condition_2 = moving_average_150 > moving_average_200

        # Condition 3: 200 SMA trending up for at least 1 month
        condition_3 = moving_average_200 > sma_200_adj
        
        # Condition 4: 50 SMA> 150 SMA and 50 SMA> 200 SMA
        condition_4 = moving_average_50 > moving_average_150 > moving_average_200
           
        # Condition 5: Current Price > 50 SMA
        condition_5 = currentClose > moving_average_50
           
        # Condition 6: Current Price is at least 30% above 52 week low
        condition_6 = currentClose >= (1.3*low_of_52week)
           
        # Condition 7: Current Price is within 25% of 52 week high
        condition_7 = currentClose >= (.75*high_of_52week)
        
        # If all conditions above are true, add stock to exportList USE CONCAT INSTEAD OF APPEND IN FUTURE
        if condition_1 and condition_2 and condition_3 and condition_4 and condition_5 and condition_6 and condition_7:
            exportList = exportList.append({'Stock': stock, "RS_Rating": RS_Rating ,"Current Close": currentClose ,"50 Day MA": moving_average_50, "150 Day Ma": moving_average_150, "200 Day MA": moving_average_200, "52 Week Low": low_of_52week, "52 week High": high_of_52week}, ignore_index=True)
            print (stock + " made the Minervini requirements")

    except Exception as e:
        print (e)
        print(f"Could not gather data on {stock}")

# sort output table by descending RS values
exportList = exportList.sort_values(by = 'RS_Rating', ascending = False)
print('\n', exportList, f'\nParsed {len(tickers)}')

writer = ExcelWriter("mark-minervini-output.xlsx")
exportList.to_excel(writer, "Output")
writer.save()