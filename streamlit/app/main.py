from st_pages import Page, show_pages, add_page_title
import streamlit as st
# streamlit run main.py
# yay its so easy to use
# Note: this web page will only call API
# DO NOT INTERACT WITH: Database,MQTT,ESP32
if __name__ == "__main__":
    show_pages(
    [
        Page("src/pages/landing.py", "Home", ":sweat_drops:"),
        Page("src/pages/index.py", "Take a Picture", ":camera_with_flash:"),
        Page("src/pages/waterlevels.py", "Overall-Water-Levels", ":ocean:"),
        Page("src/pages/analytic.py", "Data-Analytics", ":chart_with_upwards_trend:"),
        Page("src/pages/dbstat.py", "DB&API", ":keyboard:")
    ]
)
