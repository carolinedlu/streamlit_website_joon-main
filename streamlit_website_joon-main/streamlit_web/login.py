import pickle
from pathlib import Path

import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth
# ----USE AYTHENTICATION --
#
names = ["Lee Joonho", "Park Soyoung"]
usernames = ["ghwnsgkgk", "eotkdch1993"]
# load hashed passwords

file_path = Path(__file__).parent / "hashed_pw.pkl"


with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)


authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
                                    'multipage_app', 'abcdef', cookie_expiry_days=30)

name, authenication_status, username = authenticator.login("Login", "main")

if authenication_status == False:
    st.error("Username and password is incorrect")

if authenication_status == None:
    st.warning("Please enter your username and password")

if authenication_status:
    st.success("Successfully logged in")
    st.write(name)
