import yfinance as yf
import pandas as pd
import talib as ta
from datetime import timedelta
import numpy as np

quotes = ['ACE','KKP','ADVANC']
#quotes = ['ACE']


beginDate = '2022-04-07'
endDate = '2022-06-07'
for quote in quotes:
    startDate = pd.to_datetime(beginDate) - timedelta(days=365)
    startDate = startDate.strftime("%Y-%m-%d")
    stock_price = yf.download(quote+'.bk', start = startDate, stop = endDate)
    stock_price.reset_index(inplace=True)
    df = stock_price['Close']

    ema = ta.EMA(df,20)
    ema = pd.DataFrame(ema)
    ema = ema.rename(columns={0:"EMA Value"})

    merge_df = stock_price[['Date','Close']]
    merge_df = pd.concat([merge_df,ema], axis="columns")
    merge_df = merge_df.set_index('Date')
    
    filter_df = merge_df.loc[beginDate:endDate]
    filter_df.reset_index(inplace=True)
    
    compare = np.where(filter_df['Close'] > filter_df['EMA Value'], 'Above','Under')

    filter_df['Direction'] = compare

    print(quote)
    print(filter_df)