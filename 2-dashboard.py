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
        if 'filtered_data' not in st.session_state:
            st.session_state.filtered_data = main.df.copy()
        if 'filters_applied' not in st.session_state:
            st.session_state.filters_applied = False
            
        self.setup_sidebar()
    
    def setup_sidebar(self):
        st.sidebar.header("General")
        self.neighbour_group = st.sidebar.selectbox(
            "Neighbourhood Group", 
            ["All"] + list(main.df["neighbourhood group"].unique()),
            index=0
        )
        
        if self.neighbour_group != "All":
            available_neighbourhoods = main.df[main.df["neighbourhood group"] == self.neighbour_group]["neighbourhood"].unique()
        else:
            available_neighbourhoods = main.df["neighbourhood"].unique()

        self.neighbourhood = st.sidebar.selectbox(
            "Neighbourhood", 
            ["All"] + list(available_neighbourhoods),
            index=0
        )
        
        self.room_type = st.sidebar.selectbox(
            "Room Type", 
            ["All"] + list(main.df["room type"].unique()),
            index=0
        )

        self.apartment = st.sidebar.checkbox("Only Apartment")
        
        col1, col2 = st.sidebar.columns(2)
        with col1:
            general_filter = st.button("Apply General", key="general_apply")
        with col2:
            general_reset = st.button("Reset General", key="general_reset")
            
        st.sidebar.markdown("---")
        
        st.sidebar.header("Host & Booking")
        self.host = st.sidebar.radio(
            "Host Identity Verified?", 
            options=["All", "Yes", "No"], 
            index=0
        )
        
        self.booking = st.sidebar.radio(
            "Instant Bookable?", 
            options=["All", "Yes", "No"], 
            index=0
        )
        
        self.cancel_policy = st.sidebar.selectbox(
            "Cancellation Policy", 
            ["All"] + list(main.df["cancellation_policy"].unique()),
            index=0
        )
        
        col1, col2 = st.sidebar.columns(2)
        with col1:
            host_filter = st.button("Apply Host", key="host_apply")
        with col2:
            host_reset = st.button("Reset Host", key="host_reset")
            
        st.sidebar.markdown("---")

        st.sidebar.header("Price & Cost")
        price_min, price_max = int(main.df["price"].min()), int(main.df["price"].max())
        self.price_range = st.sidebar.slider(
            "Price Range ($)", 
            price_min, price_max, 
            (price_min, price_max)
        )
        
        service_fee_min, service_fee_max = int(main.df["service fee"].min()), int(main.df["service fee"].max())
        self.service_fee_range = st.sidebar.slider(
            "Service Fee Range ($)",
            service_fee_min, service_fee_max,
            (service_fee_min, service_fee_max)    
        )
        
        cost_min, cost_max = int(main.df["total stay cost"].min()), int(main.df["total stay cost"].max())
        self.stay_range = st.sidebar.slider(
            "Total Stay Cost ($)", 
            cost_min, cost_max, 
            (cost_min, cost_max)
        )

        col1, col2 = st.sidebar.columns(2)
        with col1:
            price_filter = st.button("Apply Price", key="price_apply")
        with col2:
            price_reset = st.button("Reset Price", key="price_reset")

        st.sidebar.markdown("---")
        
        st.sidebar.header("Stay & Availability")
        nights_min, nights_max = int(main.df["minimum nights"].min()), int(main.df["minimum nights"].max())
        self.nights = st.sidebar.slider(
            "Minimum Nights", 
            nights_min, nights_max, 
            (nights_min, nights_max) 
        )
        
        avail_min, avail_max = int(main.df["availability 365"].min()), int(main.df["availability 365"].max())
        self.availability = st.sidebar.slider(
            "Availability (days)", 
            avail_min, avail_max, 
            (avail_min, avail_max)
        )
        
        self.availability_category = st.sidebar.selectbox(
            "Availability Category", 
            ["All"] + list(main.df["availability category"].unique()),
            index=0
        )
        
        col1, col2 = st.sidebar.columns(2)
        with col1:
            stay_filter = st.button("Apply Stay", key="stay_apply")
        with col2:
            stay_reset = st.button("Reset Stay", key="stay_reset")
            
        st.sidebar.markdown("---")
        
        st.sidebar.header("Reviews & Ratings")
        reviews_min, reviews_max = int(main.df["number of reviews"].min()), int(main.df["number of reviews"].max())
        self.numb_of_reviews = st.sidebar.slider(
            "Number of Reviews", 
            reviews_min, reviews_max, 
            (reviews_min, reviews_max)
        )
        
        rate_min, rate_max = int(main.df["review rate number"].min()), int(main.df["review rate number"].max())
        self.review_rate_number = st.sidebar.slider(
            "Review Rate Number", 
            rate_min, rate_max, 
            (rate_min, rate_max),
        )

        col1, col2 = st.sidebar.columns(2)
        with col1:
            review_filter = st.button("Apply Reviews", key="review_apply")
        with col2:
            review_reset = st.button("Reset Reviews", key="review_reset")
            
        st.sidebar.markdown("---")
        
        st.sidebar.header("Location")
        lat_min, lat_max = float(main.df['lat'].min()), float(main.df['lat'].max())
        self.min_lat, self.max_lat = st.sidebar.slider(
            "Latitude Range", 
            lat_min, lat_max, 
            (lat_min, lat_max),
            step=0.01
        )
        
        lon_min, lon_max = float(main.df['long'].min()), float(main.df['long'].max())
        self.min_lon, self.max_lon = st.sidebar.slider(
            "Longitude Range", 
            lon_min, lon_max, 
            (lon_min, lon_max),
            step=0.01
        )
        
        col1, col2 = st.sidebar.columns(2)
        with col1:
            location_filter = st.button("Apply Location", key="location_apply")
        with col2:
            location_reset = st.button("Reset Location", key="location_reset")
            
        st.sidebar.markdown("---")
        
        col1, col2 = st.sidebar.columns(2)
        with col1:
            self.apply_all = st.button("Apply All Filters", key="apply_all", type="primary")
        with col2:
            self.reset_all = st.button("Reset All", key="reset_all")
        
        self.handle_button_clicks(
            general_filter, general_reset, host_filter, host_reset,
            price_filter, price_reset, stay_filter, stay_reset,
            review_filter, review_reset, location_filter, location_reset
        )
        
    def handle_button_clicks(self, general_filter, general_reset, host_filter, host_reset, price_filter, price_reset, stay_filter, stay_reset, review_filter, review_reset, location_filter, location_reset):
        
        if general_filter:
            pass
        if general_reset:
            pass
        if host_filter:
            pass
        if host_reset:
            pass
        if price_filter:
            pass
        if price_reset:
            pass
        if stay_filter:
            pass
        if stay_reset:
            pass
        if review_filter:
            pass
        if review_reset:
            pass
        if location_filter:
            pass
        if location_reset:
            pass
        
    def apply_general_filter(self):
        filered_data = main.df.copy()
        if self.neighbour_group != "All":
            pass
                    
        


        


        







Dashboard()



        
    