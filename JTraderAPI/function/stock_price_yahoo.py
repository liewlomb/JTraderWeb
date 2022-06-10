import yfinance as yf
import json
from datetime import datetime
import pandas as pd

def inquiry_stock_price(quote,startDate,endDate):
    #Logic
    quote = quote.upper()
    
    if quote == 'SET':
        quote = '^SET'
    
    stock_price = yf.download(quote+'.bk', start = startDate, stop = endDate)

    #Cleaning Data
    stock_price.reset_index(inplace=True)
    stock_price['Date'] = stock_price['Date'].astype(str)
    if quote == '^SET':
        quote = 'SET'
    stock_price.insert(loc=0, column='Quote', value=quote)
    record_num = []
    for i in range(len(stock_price)):
        record_num.append(str(i+1))
    stock_price.insert(loc=0, column='No', value=record_num)
    stock_price = stock_price.set_index('No')

    #export json
    jsData = stock_price.to_json(orient="index")
    result = json.loads(jsData)
    

    return result
    
    #check json
    #parsed = json.loads(result)
    #test = json.dumps(parsed, indent = 4)
    #print(test)
