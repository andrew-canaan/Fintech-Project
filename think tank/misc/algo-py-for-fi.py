# Libraries
import numpy as np
import pandas as pd
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr

yf.pdr_override()

# Grab input from user
stock = input("Enter a stock ticker symbol: ")

# Configure start/end dates for data range
startYear = 2021
startMonth = 1
startDay = 1

endYear = 2022
endMonth = 1
endDay = 1

# Create datetime objects
start = dt.datetime(startYear, startMonth, startDay)
end = dt.datetime(endYear, endMonth, endDay)

priceData = pdr.get_data_yahoo(stock, start, end)
# print(priceData.head(3)) Uncomment to view inital data frame object.

# 50 day moving average and a string version which we will use to add a column to the data frame object
movingAverage = 50
smaString = "SMA_" + str(movingAverage) 

# Add a 7th column to the data frame object, using the 4th column's data (close price) over a 50 day mean.
priceData[smaString] = priceData.iloc[:,4].rolling(window=movingAverage).mean()
print(priceData.head(3)) # Viewing first 3 rows from the data frame table object

# Since first 50 days of the table cannot have an associated SMA 50, delete them.
priceData = priceData.iloc[movingAverage:]
print(priceData.head(3)) # Note that the start date has now changed.

for i in priceData.index: 
    if priceData["Adj Close"][i] > priceData[smaString][i]:
        print("Buy signal! Adjusted Close: " + str(priceData["Adj Close"][i]) + " SMA_50: " + str(priceData[smaString][i]))



