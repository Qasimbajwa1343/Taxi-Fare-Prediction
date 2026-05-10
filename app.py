import streamlit as st
import joblib
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Taxi Fare Predictor",
    page_icon="🚖",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 900;
    color: #00ffd5;
    margin-top: 20px;
    margin-bottom: 30px;
    text-shadow: 0 0 20px rgba(0,255,213,0.6);
}

/* Labels fix (IMPORTANT) */
label {
    color: white !important;
    font-weight: 600;
}

/* Card style */
.block-container {
    padding: 2rem 2rem;
}

/* Buttons */
.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #00c9ff, #92fe9d);
    color: black;
    font-weight: bold;
    border-radius: 10px;
    height: 45px;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.03);
}

/* Input box styling */
div[data-baseweb="input"] {
    background-color: rgba(255,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
model = joblib.load("fare_model.pkl")

# ---------------- TITLE ----------------
st.markdown('<div class="main-title">🚖 Taxi Fare Prediction System</div>', unsafe_allow_html=True)

# ---------------- INPUTS ----------------
hour = st.selectbox("Pickup Hour", list(range(1, 13)))
am_pm = st.radio("AM / PM", ["AM", "PM"], horizontal=True)

pickup_hour = hour
if am_pm == "PM" and hour != 12:
    pickup_hour += 12
elif am_pm == "AM" and hour == 12:
    pickup_hour = 0

days = {
    "Monday": 0, "Tuesday": 1, "Wednesday": 2,
    "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6
}

pickup_weekday = st.selectbox("Pickup Day", list(days.keys()))
pickup_weekday = days[pickup_weekday]

passenger_count = st.slider("Passengers", 1, 6, 1)
distance_km = st.number_input("Distance (KM)", min_value=0.0, step=0.1)

# ---------------- PREDICTION ----------------
if st.button("Predict Fare 🚕"):

    input_data = np.array([[
        pickup_hour,
        pickup_weekday,
        passenger_count,
        distance_km
    ]])

    prediction = model.predict(input_data)

    # Professional feedback instead of balloons
    st.success(f"Estimated Fare: ${prediction[0]:.2f}")
    st.toast("Prediction completed successfully 🚕", icon="🚖")
  
