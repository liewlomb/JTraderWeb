import streamlit as st
from streamlit_option_menu import option_menu
from logic.buying_recovery_page import *
from logic.market_anomaly_page import *
from logic.set100_above_ema_page import *
from logic.set100_daily_change_page import *



def tiles():
    st.header("Visualization")
    type = option_menu("Menu",['Buying Recovery','SET100 Above EMA','SET100 Change(%)','Market Anomaly'],
                    icons=['','','',''],orientation='horizontal')

    if type == 'Buying Recovery':
        buying_recovery_page()
    elif type == 'SET100 Above EMA':
        above_ema()
    elif type == 'SET100 Change(%)':
        set100_change()
    elif type == 'Market Anomaly':
        market_anomaly()