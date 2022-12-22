# Equity_data_manipulation_Financial_Modeling_Prep_API

My code consists of 2 scripts:
main.py
Retrieving_stock_data.py

NB: THIS IS AN EXERCISE IN DATA MANIPULATION (USING A FREE API) AND API USAGE, HENCE THE MISSING DATA ETC.
---
Instructions:

1. Create a folder to hold the equity data we will retrieve from the
API. It is currently called 'Data' in my code.


2. Run Retrieving_stock_data.py. Ensure to change the API key in the
URL on line 26 and the time_window (number of years of data you want)
on line 23. Also ensure to rename the file paths.

Retrieving_stock_data.py pulls the stock tickers from the universe
Excel sheet and then saves data for each of these stocks as json files
from the API.


3. Run main.py or main_Dates.py. Ensure to change the file paths for the excel sheets
(both the universe being read, and the output file 'Universe_revenues'/'Universe_earning_report_dates'
in my code).
IMPORTANT: ENSURE THE HYPERLINK 'link' IS SET TO THE SAME WORKBOOK AS THE FINAL SAVED ONE TO AVOID EXCEL 
OPENING SEPERATE SHEETS.

main.py adds annual revenue for each calendar year to the universe spreadsheet
main_Dates.py adds the annual earning report dates for each calendar year to the universe spreadsheet

Key:
N/D = No Data. These stocks have no data, either because the API
doesn't have the data or because it is a non-US stock in which case
my free trial of the API won't allow data to be retrieved

N/A = Not Available. My free trial of the API prevents more than 250
requests per day. Therefore, I was unable to fill in this data. My
code fills these cells with 'N/A' by recognising these stock's data
json files are missing.
