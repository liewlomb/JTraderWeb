import pandas as pd
import requests
import plotly.graph_objects as go
import plotly as plt

def call_api(ema_length,beginDate,endDate):
    response = requests.get('http://127.0.0.1:8000/aboveema',params={'emaLength': ema_length,'beginDate': beginDate,'endDate': endDate})
    result = response.text
    df = pd.read_json(result, orient ='index')
    df = pd.DataFrame(df)
    df.reset_index(inplace=True)
    df.rename(columns= {'index':'Date'}, inplace = True)
    df['Date'] = df['Date'].dt.strftime('%Y/%m/%d')
    return df

res = call_api(5,'2022-06-10','2022-06-14')
print(res)

fig = go.Figure([go.Bar(x = res['Date'], y = res['Above EMA(5)'])])
fig.show()
