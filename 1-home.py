import streamlit as st
import main

st.markdown("<h3 style='text-align: center;color: white; font-size: 48px; font-family: Modern Sans-Serif;'>Welcome to the Airbnb Data Analysis Web App</h3>", unsafe_allow_html=True)

url = "https://www.airbnb.co.in/"

st.write('''
**Airbnb, Inc**. is an American company. Headquartered in San Francisco, California, the platform is accessible through both its website and mobile application. Founded in 2008 the company’s name is derived from its original title 
[**Air Bed and Breakfast**](%s)

**What it is**: An online marketplace for lodging and travel experiences.

**Core Function**: Connects "hosts" (people who rent out their space) with "guests" (travelers seeking accommodation).

**Key Feature**: Offers a wide variety of stays, emphasizing local and authentic travel as an alternative to hotels.

**Platform Role**: Manages bookings, facilitates secure payments, and builds a community based on user reviews
'''% url)

st.markdown("<h3 style='text-align: center;color: grey;'>About Dataset</h3>", unsafe_allow_html=True)

st.write('''
This dataset contains information about Airbnb listings, including:
- **Host details** (host verification, host listings count, etc.)
- **Property information** (neighbourhood, room type, construction year, availability)
- **Pricing** (price per night, service fee, total cost of stay)
- **Booking patterns** (minimum nights, number of reviews, review scores)
- **Geographical info** (latitude, longitude for mapping)
---
## 🗂️ Dataset Source
This dataset is publicly available.  
(Source: [Inside Airbnb](https://www.kaggle.com/datasets/arianazmoudeh/airbnbopendata) / Kaggle)
## 📐 Data Summary
- **Rows (observations):** ~100,000+  
- **Columns (features):** ~15 - 20  
- **Data type:** Structured tabular data (CSV)
''')

st.markdown("<h3 style='text-align: center;color: grey;'>Dataset Preview </h3>", unsafe_allow_html=True)

st.dataframe(main.df)
st.markdown("---")
st.write("*Note*: Use the **sidebar** to navigate to `Dashboard`.")



