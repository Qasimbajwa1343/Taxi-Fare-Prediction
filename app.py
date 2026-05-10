import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("fare_model.pkl")

# Page settings
st.set_page_config(page_title="Taxi Fare Predictor", page_icon="🚖")

# Title
st.title("🚖 Taxi Fare Prediction App")
st.markdown("Predict taxi fare using trip details")

st.divider()

# ---- Hour Selection ----
hour = st.selectbox(
    "Select Pickup Hour",
    list(range(1, 13))
)

am_pm = st.radio(
    "AM or PM",
    ["AM", "PM"],
    horizontal=True
)

# Convert to 24-hour format
pickup_hour = hour

if am_pm == "PM" and hour != 12:
    pickup_hour += 12
elif am_pm == "AM" and hour == 12:
    pickup_hour = 0

# ---- Weekday Dropdown ----
days = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}

selected_day = st.selectbox(
    "Select Pickup Day",
    list(days.keys())
)

pickup_weekday = days[selected_day]

# ---- Passenger Count ----
passenger_count = st.slider(
    "Passenger Count",
    min_value=1,
    max_value=6,
    value=1
)

# ---- Distance Input ----
distance_km = st.number_input(
    "Distance (KM)",
    min_value=0.0,
    step=0.1,
    format="%.1f"
)

st.divider()

# ---- Prediction ----
if st.button("Predict Fare"):
    
    input_data = np.array([[
        pickup_hour,
        pickup_weekday,
        passenger_count,
        distance_km
    ]])

    prediction = model.predict(input_data)

    st.success(f"💰 Estimated Fare: ${prediction[0]:.2f}")
  