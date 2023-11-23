import streamlit as st
import requests
import time
import datetime

from src.pages.pageconf import( 
    API_ADDRESS,
    BROKER_ADDRESS,
)

st.set_page_config(page_title="Water: Analytics", page_icon=":droplet:")
st.title("Analytics")
st.write("This page is for basic data analytics via matlab")