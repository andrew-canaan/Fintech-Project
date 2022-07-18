import yfinance as yf
import yahoo_fin.stock_info as si

yf.pdr_override()

aapl = yf.Ticker("AAPL")

aapl_quoteTable = si.get_quote_table("AAPL", dict_result = False)

aapl_statsValuation = si.get_stats_valuation("AAPL")

print('Sector: ' + aapl.info['sector'] + '\nIndustry: ' + aapl.info['industry'] + '\n')
print(aapl_quoteTable)
print("\n")
print(aapl_statsValuation)