import streamlit as st
import plotly_express as px
from plotly.subplots import make_subplots
import pandas as pd
import yfinance as yf
from datetime import datetime
import requests

def call_api(ema_length,beginDate,endDate):
    response = requests.get('http://127.0.0.1:8000/aboveema',params={'emaLength': ema_length,'beginDate': beginDate,'endDate': endDate})
    result = response.text
    df = pd.read_json(result, orient ='index')
    return df


def above_ema():
    #Tile
    st.title("SET100: Above EMA")
    
    with st.form(key='visualizeform'):
    #EMA Length
        ema_length = st.selectbox('EMA Length',('5','20','60'))
        beginDate = st.date_input("Begin Date", value=pd.to_datetime("today", format="%Y-%m-%d"))
        endDate = st.date_input("End Date", value=pd.to_datetime("today", format="%Y-%m-%d"))
        submit_visualize = st.form_submit_button(label='Visualize')
    if submit_visualize:
        result = call_api(ema_length,beginDate,endDate)
        subfig = make_subplots(specs=[[{'secondary_y': True}]])
        fig_number_above = px.bar(
            result,
            y = 'Above EMA('+str(ema_length)+')'
        )
        fig_set100 = px.line(
            result,
            y = 'SET Close Price'
        )

        fig_number_above.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.6)
        fig_set100.update_traces(yaxis='y2')
        fig_number_above.update_layout(yaxis2 = dict(range=[1500,1700]))
        subfig.add_traces(fig_number_above.data + fig_set100.data)
        st.plotly_chart(subfig)
        st.dataframe(result)