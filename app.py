import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from model import load_data, process_data

st.title("🚦 Traffic Congestion Dashboard")

df = load_data()
df = process_data(df)

st.subheader("Dataset")
st.write(df)

area = st.selectbox("Select Area", df['area'].unique())
filtered = df[df['area'] == area]

st.subheader("Filtered Data")
st.write(filtered)

st.subheader("Vehicle Count Graph")
fig, ax = plt.subplots()
ax.plot(filtered['time'], filtered['vehicle_count'], marker='o')
ax.set_xlabel("Time")
ax.set_ylabel("Vehicle Count")
ax.set_title(f"Traffic in {area}")

st.pyplot(fig)

st.subheader("Traffic Level Count")
st.write(filtered['traffic_level'].value_counts())
