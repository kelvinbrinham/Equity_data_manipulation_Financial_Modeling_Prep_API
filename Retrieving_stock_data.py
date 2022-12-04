import pandas as pd
import numpy as np
import requests as rq
import json
from os.path import exists


universe_df = pd.read_excel(r'/Users/kelvinbrinham/Desktop/Python_practice/Aperture_Task_1/Universe.xlsx')

Ticker_list = list(universe_df['Ticker']) #List of Tickers from spreadsheet
Ticker_list_stripped = []

#Strip the ticker symbols to the base tickers
for Ticker in Ticker_list:
    Ticker_list_stripped.append(Ticker.split()[0])

#------------------------


#Trim Ticker list because only allowed 250 API requests per day on free subscription
Ticker_list_stripped = Ticker_list_stripped[:37]

time_window = 5 #years

if __name__ == '__main__':
    for ticker in Ticker_list_stripped:
        Stock_data = rq.get(f'https://financialmodelingprep.com/api/v3/income-statement/{ticker}?limit={time_window}&apikey=8a7b6a9b1759870d086b6a0773d1ce8f')
        Stock_data = Stock_data.json()
        if 'Error Message' in Stock_data:
            if Stock_data['Error Message'].startswith('Limit Reach'):
                print('No requests left on API free trial')
                continue

        with open(f"/Users/kelvinbrinham/Desktop/Python_practice/Aperture_Task_1/Data/{ticker}.json", 'w') as f:
            json.dump(Stock_data, f)
