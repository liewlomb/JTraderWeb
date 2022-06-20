import yfinance as yf
from datetime import datetime
from datetime import timedelta
import pandas as pd

def daily_change(date):
    df = pd.read_csv('/home/liewlom/Desktop/JTrader/Data-batch/JTraderAPI/set100/set100_q1_2022.csv')
    tmp={}
    for i in range(len(df)):
        quote = df.iloc[i]['Quote']
        quote = quote.upper()
        quote = quote.strip()
        dayCheck = pd.Timestamp(date)

        if dayCheck.dayofweek == 0:
            startDate = pd.to_datetime(date) - timedelta(days=3)
            startDate = startDate.strftime("%Y-%m-%d")
        else:
            startDate = pd.to_datetime(date) - timedelta(days=1)
            startDate = startDate.strftime("%Y-%m-%d")
        
        endDate = date
        
        stock_price = yf.download(quote+'.bk', start = startDate, stop = endDate)
        stock_price.reset_index(inplace=True)
        stock_price['Date'] = stock_price['Date'].astype(str)
        stock_price = stock_price.set_index('Date')
        stock_price = stock_price.filter(items = [startDate,endDate], axis=0)
        
        x = stock_price.iloc[0]['Close']
        y = stock_price.iloc[1]['Close']
                
        pc = float('{:.2f}'.format(((y-x)/x)*100))
        
        x = float('{:.2f}'.format(x))
        y = float('{:.2f}'.format(y))
        
        if pc > 0:
            change = 'Increase'
        elif pc == 0:
            change = 'No Change'
        elif pc < 0:
            change = 'Decrease' 

        result = {i+1:{'Quote': quote,'startDate': startDate,'close: '+startDate: x,'endDate': date,'close: '+endDate: y,'closeDirection': change,'percentChange': float('{:.2f}'.format(pc))}}
        tmp.update(result)
        
    return tmp



