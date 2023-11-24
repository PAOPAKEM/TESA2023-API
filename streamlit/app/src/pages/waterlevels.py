import streamlit as st
import requests
import datetime
import pandas as pd
from pprint import pprint

from src.pages.pageconf import( 
    API_ADDRESS,
    BROKER_ADDRESS,
)

st.set_page_config(page_title="Water: levels", page_icon=":droplet:")
st.title("WaterLevels data")
st.write("More like, \"data for preview\"")



# Display Data as graph
st.markdown("### N Latest Water level datapoints")
graph_container = st.container()
st.markdown("### raw data")
raw_container = st.container()

n = st.slider('set N', 0, 10, 5)
if st.button("Request data"):
    response = requests.get(f"http://{API_ADDRESS}/water/latest-add/{n}")
    # pprint(response.json())
    if response.json()["data"] != []:
        df = pd.DataFrame(response.json()["data"][0])
        df["timestamp"] = df["timestamp"].apply(lambda x: datetime.datetime.fromtimestamp(x))
        df = df.set_index("timestamp").reset_index()
        pprint(df)
        graph_container.line_chart(df, x="timestamp", y="waterlevel")
        raw_container.write(df)
    else:
        st.write("No data returned")
    
# Get data from API