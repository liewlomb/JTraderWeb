import streamlit as st
from streamlit_option_menu import option_menu
from page.visualization_page import *
from page.dashboard_page import *
from page.blog_page import *
from page.export_data_page import *

# Header
st.set_page_config(
   page_title="JTrader: The Journey of Trader"
)

# Sidebar
st.sidebar.header('JTrader: The Journey of Trader')
st.sidebar.subheader('Welcome:')

with st.sidebar:
    selected = option_menu("Navigation Bar", ['Dashboard','Visualization','Export Data','Blog','Log out'], 
        icons=['columns', 'bar-chart-line','file-earmark-arrow-down', 'newspaper', 'box-arrow-in-left'], menu_icon="cursor", default_index=1)

if selected == 'Dashboard':
    dashboard()
elif selected == 'Visualization':
    tiles()
elif selected == 'Export Data':
    export_data()
elif selected == 'Blog':
    blog()
