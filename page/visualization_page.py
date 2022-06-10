import streamlit as st
from logic.buying_recovery import *
from logic.stock_price import *
from logic.set100_above_ema import *
from logic.set100_daily_change import *

def tiles():
    st.header("Visualization")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        menu_1 = st.button('Buying Recovery')
    with col2:
        menu_2 = st.button('SET100 Above EMA')
    with col3:
        menu_3 = st.button('SET100 Change(%)')
    with col4:
        menu_4 = st.button('Stock Price Trend')

    if menu_1 == True:
        buying_recovery() 
    elif menu_2:
        above_ema()
    elif menu_3:
        set100_change()
    elif menu_4:
        stock_price_visualize()