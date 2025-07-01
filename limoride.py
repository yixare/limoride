import streamlit as st
import csv
from datetime import datetime

CSV_FILE = "rides.csv"

def save_ride(client, date, time, pickup, drop_off, cost):
    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([client, date, time, pickup, drop_off, cost])

def load_rides():
    try:
        with open(CSV_FILE, 'r') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return []

st.title("🚘 Limo Ride Tracker")

st.header("Add New Ride")
with st.form("ride_form"):
    client = st.text_input("Client Name")
    date = st.date_input("Pickup Date")
    time = st.text_input("Pickup Time (e.g., 10:00 AM)")
    pickup = st.text_input("Pickup Location")
    drop_off = st.text_input("Drop off Location")
    cost = st.text_input("Estimated Cost ($)")
    submitted = st.form_submit_button("Add Ride")

    if submitted:
        save_ride(client, date.strftime("%Y-%m-%d"), time, pickup, drop_off, cost)
        st.success("Ride added successfully!")

st.header("📅 Upcoming Rides")
rides = load_rides()
if rides:
    for ride in rides:
        st.write(f"**{ride[0]}** — {ride[1]} {ride[2]} | From: {ride[3]} To: {ride[4]} | ${ride[5]}")
else:
    st.info("No rides found.")