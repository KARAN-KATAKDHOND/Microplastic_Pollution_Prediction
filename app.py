import streamlit as st
import pickle
import joblib
import numpy as np



with open("model.pkl", "rb") as file:
    model = joblib.load(file)

st.title("Microplastic Pollution Prediction 🌍")


industrial_activity = st.number_input("Industrial Activity Index:", min_value=0, max_value=1000, step=1)
population_density = st.number_input("Population Density:", min_value=0, max_value=1000000, step=1)
water_flow_rate = st.number_input("Water Flow Rate (m³/s):", min_value=0.0, format="%.2f")
wastewater_discharge = st.number_input("Wastewater Discharge (m³/day):", min_value=0.0, format="%.2f")
plastic_waste_production = st.number_input("Plastic Waste Production (tons/year):", min_value=0.0, format="%.2f")
temperature = st.number_input("Temperature (°C):", min_value=-50.0, max_value=50.0, format="%.2f")
ph_level = st.number_input("pH Level:", min_value=0.0, max_value=14.0, format="%.2f")

# Predict Button
if st.button("Predict Microplastic Concentration"):
    # Prepare input data as a NumPy array (reshape if needed)
    input_data = np.array([[industrial_activity, population_density, water_flow_rate, wastewater_discharge,
                             plastic_waste_production, temperature, ph_level]])

    # Make prediction
    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Microplastic Concentration: {prediction:.2f} particles/L")
