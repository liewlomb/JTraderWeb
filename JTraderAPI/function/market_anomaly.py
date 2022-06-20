import yfinance as yf
import pandas as pd
import json

def market_anomaly(quote,beginYear,endYear,period):
    # Set Date
    begin_date = f'{beginYear}-01-01'
    end_date = f'{endYear}-12-31'
    
    # Set Interval
    if period == 'Week' or '2 Weeks':
        tf = '1wk'
    if period == 'Month':
        tf = '1mo'
    
    # Set Quote
    quote = quote.upper()
    if quote == 'SET':
        quote = f'^{quote}.BK'
    else:
        quote = f'{quote}.BK'
        
    # Download Data
    data = yf.download(quote, start = begin_date, end = end_date, interval = tf)
    data.reset_index(inplace=True)
    data['Date'] = data['Date'].astype(str)
    data = data.set_index('Date')
    res = data.to_json(orient='index')
    res = json.loads(res)
    return res