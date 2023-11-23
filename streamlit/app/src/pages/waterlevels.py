import streamlit as st
import requests
import time
import datetime

from src.pages.pageconf import( 
    API_ADDRESS,
    BROKER_ADDRESS,
)

st.set_page_config(page_title="Water: levels", page_icon=":droplet:")
st.title("WaterLevels data")
st.write("More like, \"data for preview\"")

requests = requests.get("https:///api/locations")

# Display Data as graph
st.markdown("### 5 Latest Water level datapoints")

st.markdown("### raw data")

if st.button("Request data"):
    pass
# Get data from API