import streamlit as st

st.set_page_config(page_title="Period Pal")
st.title("Period Pal")
menu = ["Home", "New Entry"]
choice = st.sidebar.selectbox("Menu", menu)

