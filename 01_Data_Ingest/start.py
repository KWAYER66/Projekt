import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
from datetime import date
from datetime import timedelta

def get_assets_list_from_wikipedia():
	payload=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
	first_table = payload[0]
	df = first_table
	symbols = df['Symbol'].values.tolist()

	return symbols


def create_stocks_pd(assets):
	count = 0
	for stock in assets:
		dataframe = create_stock_pd(stock)

		if count == 0:
			dataframe_merged = dataframe
			count = 1
		else:
			dataframe_merged = pd.merge(dataframe_merged, dataframe, left_index=True, right_index=True)
	return dataframe_merged


def create_stock_pd(stock):
	stock_yf_ticker = yf.Ticker(stock)
	return stock_yf_ticker.history(period='730d', interval="60m")['Close'].rename(stock)

assets = get_assets_list_from_wikipedia()
assets = ['TSLA']
print(create_stocks_pd(assets))