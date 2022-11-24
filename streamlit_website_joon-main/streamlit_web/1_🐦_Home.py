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



#----USE AYTHENTICATION --
# 
# names = ["Lee Joonho", "Park Soyoung"]
# usernames = ["ghwnsgkgk", "eotkdch1993"]
#load hashed passwords

hashed_passwords = stauth.Hasher(["wnsgh774","eotksch1993"]).generate()

with open('../config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
   
)


# file_path = Path(__file__).parent / "hashed_pw.pkl"

# with file_path.open("rb") as file:
#     hashed_passwords = pickle.load(file)


# authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
#     'multipage_app','abcdef',cookie_expiry_days=30)

name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
    st.title('Some content')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

# Creating a password reset widget
if authentication_status:
    try:
        if authenticator.reset_password(username, 'Reset password'):
            st.success('Password modified successfully')
    except Exception as e:
        st.error(e)

# Creating a new user registration widget
try:
    if authenticator.register_user('Register user', preauthorization=False):
        st.success('User registered successfully')
except Exception as e:
    st.error(e)

# Creating a forgot password widget
try:
    username_forgot_pw, email_forgot_password, random_password = authenticator.forgot_password('Forgot password')
    if username_forgot_pw:
        st.success('New password sent securely')
        # Random password to be transferred to user securely
    elif username_forgot_pw == False:
        st.error('Username not found')
except Exception as e:
    st.error(e)

# Creating a forgot username widget
try:
    username_forgot_username, email_forgot_username = authenticator.forgot_username('Forgot username')
    if username_forgot_username:
        st.success('Username sent securely')
        # Username to be transferred to user securely
    elif username_forgot_username == False:
        st.error('Email not found')
except Exception as e:
    st.error(e)

# Creating an update user details widget
if authentication_status:
    try:
        if authenticator.update_user_details(username, 'Update user details'):
            st.success('Entries updated successfully')
    except Exception as e:
        st.error(e)

# Saving config file
with open('../config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)


    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""


    my_input = st.text_input("Input a text here", st.session_state["my_input"])
    submit = st.button("입력")

    if submit:
        st.session_state["my_input"] = my_input
        st.write("입력된 내용 : ", my_input)
        
