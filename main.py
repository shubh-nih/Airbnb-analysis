import streamlit as st
import pandas as pd
st.set_page_config(layout = 'wide')

@st.cache_data
def load_data(file):
    df = pd.read_excel(file, index_col = 0)
    return df

df = load_data("cleaned-bnb.xlsx")

home = st.Page("1-home.py", title="Home - Airbnb")
dashboard = st.Page("2-dashboard.py", title="Dashboard - Airbnb")

st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 246px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)

pg = st.navigation([home, dashboard])

pg.run()