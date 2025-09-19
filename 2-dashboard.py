import streamlit as st
import main
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib as plt
import seaborn as sns

st.markdown("<h3 style='text-align: center;color: white; font-size:     50px; font-family: Modern Sans-Serif;'>Airbnb Insights Dashboard</h3>", unsafe_allow_html=True)

class Dashboard:
    def __init__(self):
        
        st.sidebar.header("General")
        self.neighbour_group = st.sidebar.selectbox("Neighbourhood Group", main.df["neighbourhood group"].unique(), placeholder = "Select Group")
        
        self.neighbourhood = st.sidebar.selectbox("Neighbourhood", main.df["neighbourhood"].unique(), placeholder = "Select Neighbourhood")
        
        self.room_type = st.sidebar.selectbox("Room Type", main.df["room type"].unique(), placeholder = "Select Room Type")
        
        self.apartment = st.sidebar.checkbox("Only Apartments")
        
        st.sidebar.markdown("---")
        st.sidebar.header("Host & Booking")
        self.host = st.sidebar.radio("Host Identity Verified?", options = ["Yes", "No"], index = None)
        
        self.booking = st.sidebar.radio("Instant Bookable?", options = ["Yes", "No"], index = None)
        
        self.cancel_policy = st.sidebar.selectbox("Cancellation policy", main.df["cancellation_policy"].unique(), placeholder = "Select Policy")

        st.sidebar.markdown("---")
        st.sidebar.header("Price & Cost")
        self.price_range = st.sidebar.slider("Price Range", main.df["price"].min(), main.df["price"].max(), (347, 654))
        
        self.fee_range = st.sidebar.slider("Service Fee Range", main.df["service fee"].min(), main.df["service fee"].max(), (34, 71))
        
        self.stay_range = st.sidebar.slider("Total Stay Cost", main.df["total stay cost"].min(), main.df["total stay cost"].max(), (100, 700))
        
        st.sidebar.markdown("---")
        st.sidebar.header("Stay & Availability")
        self.nights = st.sidebar.slider("Minimum Nights", main.df["minimum nights"].min(), main.df["minimum nights"].max(), (2, 200))
        
        self.availability = st.sidebar.slider("Availability", main.df["availability 365"].min(), main.df["availability 365"].max(), (10, 250))
        
        self.availability_category = st.sidebar.selectbox("Availability Category", main.df["availability category"].unique(), placeholder = "Select category")
        
        st.sidebar.markdown("---")
        st.sidebar.header("Reviews & Ratings")
        self.numb_of_reviews = st.sidebar.slider("Number Of Reviews", main.df["number of reviews"].min(), main.df["number of reviews"].max(), (10, 300))
        
        self.review_rate_number = st.sidebar.slider("Review Rate Number", main.df["review rate number"].min(), main.df["review rate number"].max())
        
        st.sidebar.markdown("---")
        st.sidebar.header("Location")
        self.min_lat, self.max_lat = st.sidebar.slider(
            "Select Latitude Range", main.df['lat'].min(), main.df['lat'].max(), (40.65, 40.70)
        )
        
        self.min_lon, self.max_lon = st.sidebar.slider(
            "Select Longitude Range", main.df['long'].min(), main.df['long'].max(), (-74.1, -73.8)
        )
        
        st.sidebar.markdown("---")
        col1, col2 = st.sidebar.columns(2)
        
        with col1:
            self.filter = st.button("Apply Filter")
        with col2:
            self.reset = st.button("Reset Filter")
    

    def fetch_data(self):
        if self.neighbourhood_group:
            pass
            

obj = Dashboard()
obj.fetch_data()
