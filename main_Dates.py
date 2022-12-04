import pandas as pd
import numpy as np
import requests as rq
import json
from os.path import exists
from Retrieving_stock_data import *


time_window = 5


universe_df = pd.read_excel(r'/Users/kelvinbrinham/Desktop/Python_practice/Aperture_Task_1/Universe.xlsx')


#Years we are interested in, 2017-2021
years_allowed = set()
for i in range(2017, 2021 + 1, 1):
    years_allowed.add(str(i))


#Add new empty columns for revenue for years 2017-2021 to the spreadsheet
years_allowed_list = list(years_allowed)
years_allowed_list.sort()
years_allowed_list = years_allowed_list[::-1]

for i in range(time_window):
    year = years_allowed_list[i]
    universe_df.insert(i+2, f'{year} earnings report release date', 0, True)


# Put in the revenue for each US stock
for j in range(len(Ticker_list_stripped)):
    #Check if file exists, may not because on free trial
    file_exists = exists(f'/Users/kelvinbrinham/Desktop/Python_practice/Aperture_Task_1/Data/{Ticker_list_stripped[j]}.json')
    if file_exists:
        Stock_data = open(f'/Users/kelvinbrinham/Desktop/Python_practice/Aperture_Task_1/Data/{Ticker_list_stripped[j]}.json')
        Stock_data = json.load(Stock_data)

        if not Stock_data:
            for i in range(2, time_window + 2, 1):
                universe_df.iloc[j, i] = 'N/D'


        else:
            for i in range(len(Stock_data)):
                year = Stock_data[i].get('calendarYear')
                date = Stock_data[i].get('date')
                if year in years_allowed and year in date:
                    universe_df.at[j, f'{year} earnings report release date'] = date


    else: #No File
        for i in range(2, time_window + 2, 1):
            universe_df.iloc[j, i] = 'N/A'


#All 0 values i have left are slots where i had stock data but not for the whole 5 years (for whatever reason, see API)
#Here i replace the 0s with N/D because no data here, also good exercise for replacing all 0s in a dataframe

for i in range(len(universe_df)):
    for j in range(len(universe_df.columns)):
        if universe_df.iloc[i,j] == 0:
            universe_df.iloc[i,j] = 'N/D'




print(universe_df)
universe_df.to_excel(r'/Users/kelvinbrinham/Desktop/Python_practice/Aperture_Task_1/Universe_earning_report_dates.xlsx', sheet_name='Universe_revenues_dates_TEST')
