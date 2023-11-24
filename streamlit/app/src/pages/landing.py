import streamlit as st
import time 
import json
from pprint import pprint

from src.pages.pageconf import(
    API_ADDRESS,
    BROKER_ADDRESS
)
import requests

st.set_page_config(page_icon=":droplet:")

"""
    ### Water Level Monitoring System :sweat_drops: 
    
    Team: T44 - บ้านเเละสวน  
    University: **Mahidol University, Faculty of ICT**

    #### Component Status
"""
with st.spinner(f'Checking FastAPI ({API_ADDRESS}:80)...'):
    try:
        req = requests.get(f'http://{API_ADDRESS}:80/')
        if req.status_code == 200:
            st.write(":white_check_mark: API SERVER ON :white_check_mark:")
        else:
            st.write(":sos: error :sos:")
    except Exception as e:
        st.write(":sos: Exception Real Bad :sos:")
time.sleep(0.5)
with st.spinner(f'Checking MongoDB ({API_ADDRESS}:27017)...'):
    try:
        req = requests.get(f'http://{API_ADDRESS}:27017/')
        if req.status_code == 200:
            st.write(":white_check_mark: MONGODB ON :white_check_mark:")
        else:
            st.write(":sos: error :sos:")
    except Exception as e:
        st.write(":sos: Exception Real Bad :sos:")
time.sleep(0.5)
with st.spinner(f'Checking MQTT Broker({BROKER_ADDRESS}:1883)...'):
    try:
        req = requests.get(f'http://{API_ADDRESS}:80/')
        if "200" in req.text:
            st.write(":white_check_mark: MQTT BROKER ON (via API) :white_check_mark:")
        else:
            st.write(":sos: error :sos:")
    except Exception as e:
        st.write(":sos: Exception Real Bad :sos:")
time.sleep(0.5)

"""    
    #### Important Page List
    1. [Take a Picture](http://localhost:8501/Take%20a%20Picture)
    2. [Overall-Water-Levels](http://localhost:8501/Overall-Water-Levels)
    3. [Data-Analytics](http://localhost:8501/Data-Analytics)
    4. [DB&API](http://localhost:8501/DB%26API)
"""