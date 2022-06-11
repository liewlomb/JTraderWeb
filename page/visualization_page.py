import streamlit as st
from streamlit_option_menu import option_menu
from logic.buying_recovery import *
from logic.stock_price import *
from logic.set100_above_ema import *
from logic.set100_daily_change import *



def tiles():
    st.header("Visualization")
    type = option_menu("Menu",['Buying Recovery','SET100 Above EMA','SET100 Change(%)','Stock Price Trend'],
                    icons=['','','',''],orientation='horizontal')

    if type == 'Buying Recovery':
        buying_recovery()
    elif type == 'SET100 Above EMA':
        above_ema()
    elif type == 'SET100 Change(%)':
        set100_change()
    elif type == 'Stock Price Trend':
        stock_price_visualize()