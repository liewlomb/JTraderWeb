from JTraderAPI.function.daily_change import *
import requests
import pandas as pd

def call_api(quote,date):
    response = requests.get('http://127.0.0.1:8000/dailychange',params={'quote': quote,'date': date})
    result = response.text
    #df = pd.read_json(result, orient ='index')
    #df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    return result

df = pd.read_csv('/home/liewlom/Desktop/JTrader/Data-batch/JTraderAPI/set100/set100_q1_2022.csv')

test = {}
for i in range(len(df)):
    quote = df.iloc[i]['Quote']
    quote = quote.upper()
    quote = quote.strip()
    print(quote)
    res = call_api(quote,'2022-06-10')
    test.update(res)
    print(res)