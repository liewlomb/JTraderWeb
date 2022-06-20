import streamlit as st
import plotly_express as px
import pandas as pd
from datetime import datetime
import requests

def call_api(date):
    response = requests.get('http://127.0.0.1:8000/dailychange',params={'date': date})
    result = response.text
    df = pd.read_json(result, orient ='index')
    return df

def set100_change():
    #Tile
    st.title("SET100: Daily Change(%)")
    
    with st.form(key='visualizeform'):
        #Date Select
        date = st.date_input("Date", value=pd.to_datetime("today", format="%Y-%m-%d"))
        submit_visualize = st.form_submit_button(label='Visualize')
    
    if submit_visualize:
        result = call_api(date)
        plot_data = result.sort_values(by='percentChange')
        fig_daily_percent_change = px.bar(
            plot_data,
            x = 'Quote',
            y = 'percentChange',
            color = 'closeDirection',
            color_discrete_sequence=['#E45756','#EECA3B','#54A24B'],
            orientation = 'v',
            title = '<b>SET100 Daily Percentage Change: </b>'+str(date),
            template ='plotly_white'
        )
        config = {
            'toImageButtonOptions': {
                'format': 'png',
                'filename': 'SET100_Daily_Percantage_Change('+str(date)+')',
                'height': 500,
                'width': 800,
                'scale':6
                }
            }
        st.plotly_chart(fig_daily_percent_change, use_container_width = False,config = config)
        st.dataframe(result)
        csv = result.to_csv().encode('utf-8')
        st.download_button(label='Export to CSV',data=csv,file_name='SET100_Daily_Percantage_Change('+str(date)+').csv')
            