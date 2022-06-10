import streamlit as st
from streamlit_option_menu import option_menu
import plotly_express as px
import pandas as pd
import yfinance as yf
from datetime import datetime

def buying_recovery():
    
    #Tile
    st.title("SET100: Buying Recovery")
        
    # Set current Date
    currentDate = datetime.today().strftime('%Y-%m-%d')

    #Set current Date
    year = st.selectbox('SET100: Month',('January','February','March','April','May','June','July','August','September','October','November','December'))