import streamlit as st
import requests
import time
import datetime

API_ADDRESS = "127.0.0.1"
BROKER_ADDRESS = "127.0.0.1"


st.set_page_config(page_title="Water: Picture", page_icon=":droplet:")
st.title("Take a Picture.....")
st.write("Politely ask the sensor device to take a picture")
if st.button("Please take a Picture"):
    try:
        response = requests.get(f"http://{API_ADDRESS}/mqtt/cap")
        st.markdown(f"Sent {':white_check_mark:' if response.json()['result'] == True else 'probable API error :no_entry_sign:'} : {response.json()['message']}")
        
        st.markdown("#### Latest Data :camera_with_flash: (wait a bit...)")
        with st.spinner('Wait for it...'):
            time.sleep(3)
        response = requests.get(f"http://{API_ADDRESS}/water/latest-add/1")
        st.write("Captured:", datetime.datetime.fromtimestamp(response.json()["data"][0][0]["timestamp"]))
        st.write(response.json()["data"][0][0])

    except Exception as e:
        st.markdown(f"ERROR on  :no_entry_sign: \n error message : *{e}*")
