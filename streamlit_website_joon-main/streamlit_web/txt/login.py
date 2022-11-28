import yaml
from yaml.loader import SafeLoader
import streamlit.components.v1 as components

import streamlit as st # pip install streamlit
from streamlit_option_menu import option_menu # pip install streamlit_option_menu
import streamlit_authenticator as stauth #pip install streamlit_authenticator



st.set_page_config(
        page_title="Multipage App",
        page_icon="👋",
        layout="wide",
    )

with open('../config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
   
)

name, authentication_status, username = authenticator.login('Login', 'sidebar')
if authentication_status:
    authenticator.home()

    
    
    
    
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
