import yfinance as yf
from datetime import datetime
from datetime import timedelta
import pandas as pd
import talib as ta
import requests

def call_api(ema_length,beginDate,endDate):
    response = requests.get('http://127.0.0.1:8000/aboveema',params={'emaLength': ema_length,'beginDate': beginDate,'endDate': endDate})
    result = response.text
    df = pd.read_json(result, orient ='index')
    df = pd.DataFrame(df)
    df.reset_index(inplace=True)
    print(df)
    df.rename(columns= {'index':'Date'}, inplace = True)
    df['Date'] = df['Date'].dt.strftime('%d/%m/%Y')
    return df

ema_length = 5
beginDate = '2022-06-20'
endDate = '2022-06-17'

print(call_api(ema_length,beginDate,endDate))