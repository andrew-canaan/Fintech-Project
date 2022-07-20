This directory holds files that demonstrate how we can access/process data to satisfy V1 requirements for our application.
V1 requirements:
    A stock screener that shall screen NASDAQ listings with the following screening functionality:

    1. Market Cap 

    2. Current Price 

    3. Volume

    4. Dividends Y/N 

    5. Earnings Per Share (EPS (TTM): Yahoo_fin->get_quote_table())

    6. Price to Earnings Ratio (PE (TTM): Yahoo_fin->get_quote_table())

    7. Price to Earnings to Growth Ratio (5 yr expected: Yahoo_fin->get_stats_valuation())

    8. Beta (5Y Monthly: Yahoo_fin->get_quote_table())

    9. Sector 

    10. Industry

    11. Earnings Date

# Description

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
<<<<<<< HEAD
zip                                                                      100022
sector                                                       Consumer Defensive
fullTimeEmployees                                                           584
longBusinessSummary           ATA Creativity Global, together with its subsi...
city                                                                    Beijing
phone                                                           86 10 6518 1133
country                                                                   China
companyOfficers                                                              []
website                                                 https://www.atai.net.cn
maxAge                                                                        1
address1                                                         Building No. 2
fax                                                             86 10 6517 9517
industry                                          Education & Training Services
address2                      East Gate, Floor 1 Jian Wai Soho No.39 Dong Sa...
ebitdaMargins                                                          -0.19653
profitMargins                                                          -0.14732
grossMargins                                                            0.52812
operatingCashflow                                                          None
revenueGrowth                                                             0.121
operatingMargins                                                       -0.29956
ebitda                                                                -40633820
targetLowPrice                                                               22
recommendationKey                                                    strong_buy
grossProfits                                                          104795550
freeCashflow                                                               None
targetMedianPrice                                                            22
currentPrice                                                               1.38
earningsGrowth                                                             None
currentRatio                                                              0.253
returnOnAssets                                                         -0.07383
numberOfAnalystOpinions                                                       1
targetMeanPrice                                                              22
debtToEquity                                                             22.648
returnOnEquity                                                         -0.16249
targetHighPrice                                                              22
totalCash                                                              62413832
totalDebt                                                              39557444
totalRevenue                                                          206758544
totalCashPerShare                                                         1.988
financialCurrency                                                           CNY
revenuePerShare                                                           6.459
quickRatio                                                                0.229
recommendationMean                                                            1
exchange                                                                    NGM
shortName                                                 ATA Creativity Global
longName                                                  ATA Creativity Global
exchangeTimezoneName                                           America/New_York
exchangeTimezoneShortName                                                   EDT
isEsgPopulated                                                            False
gmtOffSetMilliseconds                                                 -14400000
quoteType                                                                EQUITY
symbol                                                                     AACG
messageBoardId                                                   finmb_39920439
market                                                                us_market
annualHoldingsTurnover                                                     None
enterpriseToRevenue                                                       0.095
beta3Year                                                                  None
enterpriseToEbitda                                                       -0.482
52WeekChange                                                          -0.595611
morningStarRiskRating                                                      None
forwardEps                                                                -1.32
revenueQuarterlyGrowth                                                     None
sharesOutstanding                                                      31598600
fundInceptionDate                                                          None
annualReportExpenseRatio                                                   None
totalAssets                                                                None
bookValue                                                                 5.481
sharesShort                                                                4076
sharesPercentSharesOut                                                   0.0001
fundFamily                                                                 None
lastFiscalYearEnd                                                    1640908800
heldPercentInstitutions                                                  0.1697
netIncomeToCommon                                                     -32742800
trailingEps                                                              -0.153
lastDividendValue                                                             6
SandP52WeekChange                                                     -0.096818
priceToBook                                                            0.251779
heldPercentInsiders                                                     0.05489
nextFiscalYearEnd                                                    1703980800
yield                                                                      None
mostRecentQuarter                                                    1648684800
shortRatio                                                                 0.51
sharesShortPreviousMonthDate                                         1653955200
floatShares                                                             8808642
beta                                                                   0.912303
enterpriseValue                                                        19587230
priceHint                                                                     4
threeYearAverageReturn                                                     None
lastSplitDate                                                              None
lastSplitFactor                                                            None
legalType                                                                  None
lastDividendDate                                                     1535328000
morningStarOverallRating                                                   None
earningsQuarterlyGrowth                                                    None
priceToSalesTrailing12Months                                           0.210903
dateShortInterest                                                    1656547200
pegRatio                                                                  -0.04
ytdReturn                                                                  None
forwardPE                                                             -1.045454
lastCapGain                                                                None
shortPercentOfFloat                                                        None
sharesShortPriorMonth                                                       746
impliedSharesOutstanding                                                      0
category                                                                   None
fiveYearAverageReturn                                                      None
previousClose                                                               1.3
regularMarketOpen                                                           1.3
twoHundredDayAverage                                                    1.50985
trailingAnnualDividendYield                                                   0
payoutRatio                                                                   0
volume24Hr                                                                 None
regularMarketDayHigh                                                       1.38
navPrice                                                                   None
averageDailyVolume10Day                                                   16040
regularMarketPreviousClose                                                  1.3
fiftyDayAverage                                                          1.0912
trailingAnnualDividendRate                                                    0
open                                                                        1.3
toCurrency                                                                 None
averageVolume10days                                                       16040
expireDate                                                                 None
algorithm                                                                  None
dividendRate                                                               None
exDividendDate                                                       1535328000
circulatingSupply                                                          None
startDate                                                                  None
regularMarketDayLow                                                         1.3
currency                                                                    USD
regularMarketVolume                                                       12828
lastMarket                                                                 None
maxSupply                                                                  None
openInterest                                                               None
marketCap                                                              43606068
volumeAllCurrencies                                                        None
strikePrice                                                                None
averageVolume                                                             11736
dayLow                                                                      1.3
ask                                                                         1.4
askSize                                                                     800
volume                                                                    12828
fiftyTwoWeekHigh                                                           4.27
fromCurrency                                                               None
fiveYearAvgDividendYield                                                   None
fiftyTwoWeekLow                                                            0.88
bid                                                                        1.31
tradeable                                                                 False
dividendYield                                                              None
bidSize                                                                    4000
dayHigh                                                                    1.38
coinMarketCapLink                                                          None
regularMarketPrice                                                         1.38
preMarketPrice                                                             1.22
logo_url                                  https://logo.clearbit.com/atai.net.cn
=======
# sector
# industry
# country
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
# targetMeanPrice
# debtToEquity
# returnOnEquity
# targetHighPrice
# revenuePerShare
# quickRatio
# recommendationMean
# exchange
# shortName
# longName
# symbol
# market
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
# annualReportExpenseRatio
# bookValue
# sharesShort
# heldPercentInstitutions
# netIncomeToCommon
# trailingEps
# lastDividendValue
# priceToBook
# heldPercentInsiders
# yield
# shortRatio
# floatShares
# enterpriseValue
# threeYearAverageReturn
# lastDividendDate
# morningStarOverallRating
# earningsQuarterlyGrowth
# priceToSalesTrailing12Months
# dateShortInterest
# ytdReturn
# shortPercentOfFloat
# sharesShortPriorMonth
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
# open
# averageVolume10days
# expireDate
# algorithm
# circulatingSupply
# regularMarketDayLow
# regularMarketVolume
# currency
# dayLow 
# dayHigh
# volume
# regularMarketPrice
# preMarketPrice
>>>>>>> 43be357738aee152805ab073ee690233c3ef87ce
