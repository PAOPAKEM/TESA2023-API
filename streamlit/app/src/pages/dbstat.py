import streamlit as st
import requests
import time
import datetime

st.set_page_config(page_title="Water: dbapi", page_icon=":droplet:")
st.title("DB & API Status")

option = st.selectbox(
    "Select a Functionality",
    ("DB-Raw", "DB-Processed(Matlab)", "API")
)

match option:
    case "DB-Raw":
        st.write("Raw Data Query, from ESP32")
        # TODO: Do some API Query
    case "DB-Processed(Matlab)":
        st.write("Processed Data Query, from Matlab")
        # TODO: Do some API Query
    case "API":
        st.write("Other API Stuffs")
        # TODO: Do some API Query