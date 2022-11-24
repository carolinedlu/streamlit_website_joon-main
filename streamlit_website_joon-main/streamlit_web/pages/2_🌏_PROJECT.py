import streamlit as st

from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Project",
    page_icon="🌏",
)

st.title("Project")
st.sidebar.success("Select a page above.")

selected = option_menu( menu_title= None, options=["Web", "App","Codes","Text"], icons=["pencil-fill", "bar-chart-fill"], orientation="horizontal",)