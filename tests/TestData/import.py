from pandas_datareader import data as wb
import yfinance as yfin


yfin.pdr_override()
data = wb.get_data_yahoo('PG', start='1995-1-1', end='2022-12-23').head()

data.to_csv('tests/TestData/yahoo_data.csv')