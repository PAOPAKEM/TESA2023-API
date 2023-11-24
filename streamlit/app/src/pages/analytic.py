import streamlit as st
import requests
import time
import datetime
from pprint import pprint
import pandas as pd

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from src.pages.pageconf import( 
    API_ADDRESS,
    BROKER_ADDRESS,
)

st.set_page_config(page_title="Water: Analytics", page_icon=":droplet:")
st.title("MatLab Analytics")
st.write("This page is for basic data analytics via <b>matlab</b>")
option = st.selectbox(
    "Select a Analytics",
    ("Height/Discharge-S1", "Height/Discharge-S3", "Everything")
)
def genfig(name:str, df:pd.DataFrame, xx:str, yy:str, yy2:str):
    fig = make_subplots(specs=[[{"secondary_y": True}]])
        # Add traces
    fig.add_trace(
        go.Scatter(x=df[xx], y=df[yy], name="Water Height"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=df[xx], y=df[yy2], name="Water Drain Rate"),
        secondary_y=True,
    )
    # Add figure title
    fig.update_layout(title_text=name)
    # Set x-axis title
    fig.update_xaxes(title_text="Days")
    # Set y-axes titles
    fig.update_yaxes(title_text=f"<b>{yy}</b> (m)", secondary_y=False)
    fig.update_yaxes(title_text=f"<b>{yy2}</b> rate (m^3)", secondary_y=True)

    fig.for_each_trace(lambda t: t.update(textfont_color=t.marker.color, textposition='top center'))

    return fig

match option:
    case "Height/Discharge-S1":
        name = "Correlation Between Water Height and Discharge Rate on S1"

        response = requests.get(f"http://{API_ADDRESS}/matlab/1")
        df = pd.DataFrame(response.json()["data"][0][0])
        df["day"] = df.index + 1

        fig = genfig(name, df, "day", "Height_S1", "Discharge_S1")

        st.plotly_chart(fig)

    case "Height/Discharge-S3":
        name = "Correlation Between Water Height and Discharge Rate on S3"
        
        response = requests.get(f"http://{API_ADDRESS}/matlab/1")
        df = pd.DataFrame(response.json()["data"][0][0])
        df["day"] = df.index + 1

        fig = genfig(name, df, "day", "Height_3", "Discharge_S3")
        st.plotly_chart(fig)

    case "Everything":
        st.write("All 5 data in one graph")
        st.write(r"This is not a good idea, data does not make sense ¯\\_(ツ)_/¯")