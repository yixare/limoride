import streamlit as st
import csv
from datetime import datetime

# ---------- CSS + ANIMATION ---------- #
st.markdown("""
<style>
body {
    background: linear-gradient(-45deg, #1f1c2c, #928dab, #414345, #232526);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
    color: white;
}
@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
h1, h2, h3 {
    text-align: center;
    color: #ffffff;
    font-family: 'Segoe UI', sans-serif;
}
.stButton>button {
    background-color: #FF6F61;
    color: white;
    font-weight: bold;
    padding: 0.6em 1.2em;
    border-radius: 12px;
    border: none;
}
.stTextInput>div>input {
    background-color: #ffffff10;
    color: white;
}
.stTextInput>div>input::placeholder {
    color: #dddddd;
}
</style>
""", unsafe_allow_html=True)

# ---------- CORE APP ---------- #

CSV_FILE = "rides.csv"

def save_ride(client, date, time, pickup, dropoff, cost):
    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([client, date, time, pickup, dropoff, cost])

def load_rides():
    try:
        with open(CSV_FILE, 'r') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return []

st.markdown("<h1>🚘 Seaside Limo Tracker</h1>", unsafe_allow_html=True)

with st.container():
    st.markdown("### 📋 Add a New Ride")
    with st.form("ride_form"):
        client = st.text_input("Client Name")
        date = st.date_input("Pickup Date")
        time = st.text_input("Pickup Time (e.g., 10:00 AM)")

        pickup = st.text_input("Pickup Location")
        dropoff = st.text_input("Dropoff Location")
        cost = st.text_input("Estimated Cost ($)")

        submitted = st.form_submit_button("➕ Add Ride")

        if submitted:
            if not client or not pickup or not dropoff or not cost:
                st.error("Please fill in all required fields.")
            else:
                save_ride(client, date.strftime("%Y-%m-%d"), time, pickup, dropoff, cost)
                st.success("✅ Ride added successfully!")

# ---------- Display Rides ---------- #
st.markdown("### 📅 Upcoming Rides")
rides = load_rides()

if rides:
    for ride in rides:
        st.markdown(f"""
        <div style='padding: 10px; background-color: #ffffff10; border-radius: 10px; margin-bottom: 10px;'>
        <b>{ride[0]}</b> — {ride[1]} {ride[2]} <br>
        From: <i>{ride[3]}</i> → <i>{ride[4]}</i><br>
        💲 <b>${ride[5]}</b>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("No rides found.")
