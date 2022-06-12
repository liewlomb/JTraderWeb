import yfinance as yf
from datetime import datetime
from datetime import timedelta
import pandas as pd
import talib as ta

def above_ema(emaLength,beginDate,endDate):
    #set variable
    startDate = beginDate
    quotes = pd.read_csv('/home/liewlom/Desktop/JTrader/Data-batch/JTraderAPI/set100/set100_q1_2022.csv')
    above=0
    
    for i in range(len(quotes)):
        quote = quotes.iloc[i]['Quote']
        quote = quote.upper()
        quote = quote.strip()
        
        #download data
        stock_price = yf.download(quote+'.bk', start = startDate, stop = endDate)

        df = stock_price['Close'].values[-int(emaLength):]


        ema = ta.EMA(df,int(emaLength))
        ema_value = ema[-1]

        close_price = stock_price.iloc[-1]['Close']

        if close_price > ema_value:
            direction = 'Above'
            above = above + 1
        else:
            direction = 'Under'

    setClosePrice = yf.download('^SET.BK', start = endDate, stop = endDate)
    setClosePrice.reset_index(inplace=True)
    setClosePrice ['Date'] = setClosePrice ['Date'].astype(str)
    setClosePrice = setClosePrice.loc[setClosePrice['Date'] == endDate]
    set_close = setClosePrice['Close'].values[-1]
    result_date = setClosePrice['Date'].values[-1]
    result = {result_date:{'date':result_date,'SET Close Price':set_close,'Above EMA('+emaLength+')':above}}
        
    return result

