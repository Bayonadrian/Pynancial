from pandas_datareader import data as wb
import pandas as pd
import yfinance as yfin

# Data interest
yfin.pdr_override()
data_interest = wb.get_data_yahoo('PG', start='1995-1-1', end='2022-12-23').head()

# Data risk
tickers = ['PG', 'BEI.DE']

data_risk = pd.DataFrame()

for t in tickers:
    data_risk[t] = wb.get_data_yahoo(t, start='2007-1-1')['Adj Close']

data_risk = data_risk.head()

# Saving csv
data_interest.to_csv('tests/TestData/yahoo_data_interest.csv')
data_risk.to_csv('tests/TestData/yahoo_data_risk.csv')