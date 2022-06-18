import streamlit as st
from streamlit_option_menu import option_menu
import plotly_express as px
import plotly.graph_objs as go
import pandas as pd
import yfinance as yf
from datetime import datetime
import requests

def call_api(endDate,setRange):
    response = requests.get('http://127.0.0.1:8000/buyingRecovery',params={'endDate': endDate,'setRange': setRange})
    result = response.text
    df = pd.read_json(result, orient ='index')
    df = pd.DataFrame(df)
    df.reset_index(inplace=True)
    df.rename(columns = {'index':'Quote'}, inplace = True)
    return df

def buying_recovery(endDate,setRange):
    res = call_api(endDate,setRange)
    trace0 = go.Bar(
        x = res['Quote'],
        y=res['%Change '+res['End Month'].iloc[0]],
        marker_color='rgba(0,128,0, 0.6)',
        name="%Change "+res['End Month'].iloc[0],
    )
    trace1 = go.Bar(
        x = res['Quote'],
        y=res['%Change '+res['Begin Month'].iloc[0]],
        marker_color='rgba(0,0,255, 0.6)',
        name="%Change "+res['Begin Month'].iloc[0],
    )
    data = [trace0,trace1]
    layout = go.Layout(title='Buying Recovery', barmode='relative')
    figure = go.Figure(data = data, layout = layout)
    figure.update_layout(
        yaxis=dict(title_text="% Change"),
        xaxis=dict(title_text="Quote"),
        title={
                'text': "Buying-Recovery "+str(setRange),
                'y':0.96,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
        autosize=False,
        width=1000,
        height=500,
        paper_bgcolor='rgba(255,255,255)',
        plot_bgcolor='rgba(0,0,0,0)'
        )
    figure.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
    figure.show()
# Unit Test
endDate = '2022-06-17'
setRange = 'SET50'
print(buying_recovery(endDate,setRange))