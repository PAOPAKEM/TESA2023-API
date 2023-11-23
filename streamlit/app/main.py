from st_pages import Page, show_pages, add_page_title

# streamlit run main.py
# yay its so easy to use
# Note: this web page will only call API
# DO NOT INTERACT WITH: Database, ESP32, BlaBlaBla
if __name__ == "__main__":
    show_pages(
    [
        Page("src/pages/index.py", "Take a Picture", ":camera_with_flash:"),
        Page("src/pages/analytic.py", "Data Analytics", ":chart_with_upwards_trend:"),
    ]
)
