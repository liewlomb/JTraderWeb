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

def generate_plot_data():
    res = call_api()


def buying_recovery_page():
    
    #Tile
    st.title("SET100: Buying Recovery")
    
    with st.form(key='visualizeform'):
    #EMA Length
        endDate = st.date_input("Date", value=pd.to_datetime("today", format="%Y-%m-%d"))
        setRange = st.selectbox('SET Data',('SET100','SET50','SET51-100'))
        submit_visualize = st.form_submit_button(label='Visualize')
    if submit_visualize:
        res = call_api(endDate,setRange)
        if setRange == 'SET100':
            w_size = 1800
        else:
            w_size = 1000
        trace0 = go.Bar(
            x = res['Quote'],
            y = res['%Change '+res['Begin Month'].iloc[0]],
            marker_color='rgba(0,128,0, 0.6)',
            name="%Change "+res['Begin Month'].iloc[0]
        )
        trace1 = go.Bar(
            x = res['Quote'],
            y=res['%Change '+res['End Month'].iloc[0]],
            marker_color='rgba(0,0,255, 0.6)',
            name="%Change "+res['End Month'].iloc[0],
            text = res['Quote']
        )
        data = [trace0,trace1]
        layout = go.Layout(title='Buying Recovery', barmode='relative')
        figure = go.Figure(data = data, layout = layout)
        figure.update_layout(
            yaxis = dict(title_text="% Change"),
            xaxis = dict(title_text="Quote"),
            title = {
                    'text': "Buying-Recovery "+str(setRange),
                    'y':0.96,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
            autosize = False,
            width = w_size,
            height = 500,
            paper_bgcolor = 'rgba(255,255,255)',
            plot_bgcolor = 'rgba(0,0,0,0)'
            )
        config = {
            'toImageButtonOptions': {
                'format': 'png',
                'filename': '('+setRange+')-Buying-Recovery-('+str(endDate)+')',
                'height': 500,
                'width': 800,
                'scale': 6
                }
            }
        figure.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
        figure.update_xaxes(tickfont=dict(size=7))

        st.plotly_chart(figure, use_container_width=False,config=config)
        st.dataframe(res)
        csv = res.to_csv().encode('utf-8')
        st.download_button(label='Export to CSV',data=csv,file_name = '('+setRange+')-Buying-Recovery-('+str(endDate)+').csv')