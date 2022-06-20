import yfinance as yf
from datetime import datetime
from datetime import timedelta
import pandas as pd
import talib as ta
import numpy as np

def loop_create_dict(emaLength,startDate,endDate):
    result={}
    setclose = yf.download('^SET.BK', start = startDate, stop = endDate)
    setclose = setclose.loc[startDate:endDate]
    setclose.reset_index(inplace=True)

    for i in range(len(setclose)):
        date = setclose['Date'][i].strftime("%Y-%m-%d")
        close = setclose['Close'][i]
        genDict = {date:{'SET Close Price': close,'Above EMA('+str(emaLength)+')': 0}}
        result.update(genDict)
    return(result)

def above_ema(emaLength,beginDate,endDate):
    startDate = beginDate
    # Get SET100
    quotes = pd.read_csv('/home/liewlom/Desktop/JTrader/Data-batch/JTraderAPI/set100/set100_q1_2022.csv')
    # Get Data Dict
    res = loop_create_dict(emaLength,beginDate,endDate)
    for i in range(len(quotes)):
        quote = quotes.iloc[i]['Quote']
        quote = quote.upper()
        quote = quote.strip()
        # Get Stock Data
        startDate = pd.to_datetime(beginDate) - timedelta(days=365)
        stock_price = yf.download(quote+'.bk', start = startDate, stop = endDate)
        stock_price.reset_index(inplace=True)
        df = stock_price['Close']

        # Get EMA
        ema = ta.EMA(df,int(emaLength))
        ema = pd.DataFrame(ema)
        ema = ema.rename(columns={0:"EMA Value"})

        merge_df = stock_price[['Date','Close']]
        merge_df = pd.concat([merge_df,ema], axis="columns")
        merge_df = merge_df.set_index('Date')
        
        filter_df = merge_df.loc[beginDate:endDate]
        filter_df.reset_index(inplace=True)
        
        compare = np.where(filter_df['Close'] > filter_df['EMA Value'], 'Above','Under')

        filter_df['Direction'] = compare
        
        # Update Dict
        for i in range(len(filter_df)):
            date = filter_df['Date'][i].strftime("%Y-%m-%d")
            dir = filter_df.loc[filter_df['Date'] == date, 'Direction'].iloc[0]
            if dir == 'Above':
                x = res[date]['Above EMA('+str(emaLength)+')']
                x = x+1
                res[date]['Above EMA('+str(emaLength)+')'] = x
    return res

