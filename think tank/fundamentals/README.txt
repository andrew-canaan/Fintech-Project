This directory holds files that demonstrate how we can access/process data to satisfy V1 requirements for our application.
V1 requirements:
    A stock screener that shall screen NASDAQ listings with the following screening functionality:

    1. Market Cap 
        (yfinance->tickerVariable.info['marketCap'])

    2. Current Price 
        (yfinance->tickerVariable.info['currentPrice'])

    3. Volume
        (yfinance->tickerVariable.info['volume24Hr'])
        (yfinance->tickerVariable.info['volume'])
        (yfinance->tickerVariable.info['volume24Hr'])
        (df = web.get_data_yahoo('IBM', start_date, end_date) -> df['Volume'])

    4. Dividends Y/N 
        (yfinance->tickerVariable.info['dividendRate ']) != 0 ?

    5. Earnings Per Share (EPS (TTM): Yahoo_fin->get_quote_table())
        (yfinance->tickerVariable.info['trailingEps'])
        (yfinance->tickerVariable.info['forwardEps'])

    6. Price to Earnings Ratio (PE (TTM): Yahoo_fin->get_quote_table())
        (yfinance->tickerVariable.info['trailingPE'])
        (yfinance->tickerVariable.info['forwardPE'])
        (yfinance->tickerVariable.info['forwardEps'])

    7. Price to Earnings to Growth Ratio (5 yr expected: Yahoo_fin->get_stats_valuation())
        (yfinance->tickerVariable.info['pegRatio'])

    8. Beta (5Y Monthly: Yahoo_fin->get_quote_table())
        (yfinance->tickerVariable.info['beta'])
        (yfinance->tickerVariable.info['beta3year'])

    9. Sector 
        (yfinance->tickerVariable.info['sector'])

    10. Industry
        (yfinance->tickerVariable.info['industry'])

    11. Earnings Date
        (Yahoo_fin->stockinfo -> data = get_quote_table("ticker", dict_result = False) -> data["Earnings Date"])

# Description

# si.get_quote_table("ticker", dict_result = False) returns the following (names match column names verbatum):
# 1y Target Est
# 52 Week Range
# Ask
# Avg. Volume
# Beta (5Y Monthly)
# Bid
# Day's Range
# EPS (TTM)
# Earnings Date
# Ex-Divident Date
# Forward Dividend & Yield
# Market Cap
# Open
# PE Ratio
# Previous Close
# Quote Price
# Volume

# si.get_stats_valuation("ticker") returns the following (names match column names verbatum):
# Market Cap (intraday)
# Enterprise Value
# Trailing P/E
# Forward P/E
# PEG Ratio (5 yr expected)
# Price/Sales (ttm)
# Price/Book (mrq)
# Enterprise Value/Revenue
# Enterprise Value/EBITDA

# .info() returns the following information (names match column names verbatum):
# zip
# sector
# industry
# fullTimeEmployees
# longBusinessSummary (description of business)
# city
# phone
# state
# country
# companyOfficers (lst)
# wesbsite
# maxAge (idek) 
# address1
# ebitdaMargins
# profitMargins
# trailingPE
# trailingPegRatio
# grossMargins
# operatingCashflow
# revenueGrowth
# operatingMargins
# dividendRate
# exDividendDate
# ebitda
# pegRatio
# beta
# forwardPE
# averageVolume
# marketCap
# targetLowPrice
# recommendationKey (returns string: buy or sell)
# grossProfits
# freeCashFlow
# targetMedianPrice
# currentPrice (CURRENT PRICE)
# earningsGrowth
# currentRatio
# returnOnAssets
# numberOfAnalystOpinions
# targetMeanPrice
# debtToEquity
# returnOnEquity
# targetHighPrice
# totalCash
# totalDebt
# totalRevenue
# totalCashPerShare
# financialCurrency
# revenuePerShare
# quickRatio
# recommendationMean
# exchange
# shortName
# longName
# exchangeTimezoneName
# exchangeTimezoneShortName
# isesgPopulated
# gmtOffSetMilliseconds
# quoteType
# symbol
# messageBoardId
# market
# annualHoldingsTurnover
# enterpriseToRevenue
# beta3year
# enterpriseToEbitda
# 52WeekChange
# fiftyTwoWeekHigh
# fiftyTwoWeekLow
# morningStarRiskRating
# forwardEps
# revenueQuarterlyGrowth
# sharesOutstanding
# fundInceptionDate
# annualReportExpenseRatio
# totalAssets
# bookValue
# sharesShort
# sharesPercentSharesOut
# fundFamily
# lastFiscalYearEnd
# heldPercentInstitutions
# netIncomeToCommon
# trailingEps
# lastDividendValue
# SandP52WeekChange
# priceToBook
# heldPercentInsiders
# nextFiscalYearEnd
# yield
# mostRecentQuarter
# shortRatio
# sharesShortPreviousMonthDate
# floatShares
# enterpriseValue
# priceHint
# threeYearAverageReturn
# lastSplitDate
# lastSplitFactor
# legalType
# lastDividendDate
# morningStarOverallRating
# earningsQuarterlyGrowth
# priceToSalesTrailing12Months
# dateShortInterest
# ytdReturn
# lastCapGain
# shortPercentOfFloat
# sharesShortPriorMonth
# impliedSharesOutstanding
# category
# fiveYearAverageReturn
# previousClose
# regularMarketOpen
# twoHundredDayAverage
# trailingAnnualDividendYield
# fiveYearAvgDividendYield
# payoutRatio
# volume24Hr
# regularMarketDayHigh
# navPrice
# averageDailyVolume10Day
# regularMarketPreviousClose
# fiftyDayAverage
# trailingAnnualDividendRate
# open
# toCurrency
# averageVolume10days
# expireDate
# algorithm
# circulatingSupply
# regularMarketDayLow
# regularMarketVolume
# currency
# dayLow 
# dayHigh
# ask
# askSize 
# volume
# regularMarketPrice
# preMarketPrice