import streamlit as st
import streamlit_authenticator as stauth
from page.home_page import *

st.set_page_config(
   page_title="JTrader: The Journey of Trader"
)

names = ['John Smith','Rebecca Briggs']
usernames = ['jsmith','rbriggs']
passwords = ['123','456']

hashed_passwords = stauth.Hasher(passwords).generate()
authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)

col1, col2 = st.columns(2)

with col1:
    name, authentication_status, username = authenticator.login('Login to JTrader','main')
    if authentication_status == False:
        st.error('Username/password is incorrect')
        with col2:
            with st.form(key='Register'):
                st.subheader("Register to JTrader")
                RegUserName = st.text_input("Username", placeholder= 'Username')
                RegEmail = st.text_input("Email", placeholder= 'Email')
                RegPassword = st.text_input("Password", placeholder= 'Password',type='password')
                RegConfirmPassword = st.text_input("Confirm Password", placeholder= 'Confirm Password',type='password')
                register_button = st.form_submit_button(label='Register')
    if authentication_status == None:
        st.warning('Please enter your username and password')
        with col2:
            with st.form(key='Register'):
                st.subheader("Register to JTrader")
                RegUserName = st.text_input("Username", placeholder= 'Username')
                RegEmail = st.text_input("Email", placeholder= 'Email')
                RegPassword = st.text_input("Password", placeholder= 'Password',type='password')
                RegConfirmPassword = st.text_input("Confirm Password", placeholder= 'Confirm Password',type='password')
                register_button = st.form_submit_button(label='Register')
if authentication_status == True:
    home_page(name)
    logout = authenticator.logout("Log out","sidebar")