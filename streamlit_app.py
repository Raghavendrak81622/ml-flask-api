
import streamlit as st
import joblib
import numpy as np

# Load trained ML model
model = joblib.load("model.pkl")
print("Model loaded successfully.")
print("Model coefficients:", model.coef_)
# Application title
st.title("House Price Prediction")
st.write("Enter the house details to predict its price.")

# Input features
MedInc = st.number_input("Median Income", min_value=0.0, value=3.5)
HouseAge = st.number_input("House Age", min_value=0.0, value=20.0)
AveRooms = st.number_input("Average Rooms", min_value=0.0, value=5.0)
AveBedrms = st.number_input("Average Bedrooms", min_value=0.0, value=1.0)
Population = st.number_input("Population", min_value=0.0, value=1000.0)
AveOccup = st.number_input("Average Occupancy", min_value=0.0, value=3.0)
Latitude = st.number_input("Latitude", value=34.0)
Longitude = st.number_input("Longitude", value=-118.0)

# Predict button
if st.button("Predict House Price"):

    # Prepare input data
    features = np.array([[
        MedInc,
        HouseAge,
        AveRooms,
        AveBedrms,
        Population,
        AveOccup,
        Latitude,
        Longitude
    ]])

    # Generate prediction
    prediction = model.predict(features)

    # Display result
    st.success("Predicted House Price:")
    st.write(f"${prediction[0] * 100000:,.2f}")
