import streamlit as st
import pandas as pd
from src.utils import load_model
from src.Config.configuration import *
import pickle

preprocessor = load_model(preproceesing_obj_path)
model = load_model(model_trainer_path)

st.title("Delivery Time Prediction App 🚀")
st.sidebar.header("Enter Delivery Details")


df = pd.read_csv("train_data.csv")  
#st.write(df.columns)

Type_of_order = st.sidebar.selectbox("Type of Order", df["Type_of_order"].unique())
Type_of_vehicle = st.sidebar.selectbox("Type of Vehicle", df["Type_of_vehicle"].unique())
Delivery_city = st.sidebar.selectbox("Delivery City", df["Delivery_city"].unique())

Road_traffic_density = st.sidebar.selectbox("Road Traffic Density", df["Road_traffic_density"].unique())
Weather_conditions = st.sidebar.selectbox("Weather Conditions",df["Weather_conditions"].unique())
Delivery_person_Age = st.sidebar.number_input("Delivery Person Age", df["Delivery_person_Age"].min(), df["Delivery_person_Age"].max(), df["Delivery_person_Age"].median())
Delivery_person_Ratings = st.sidebar.slider("Delivery Person Ratings", df["Delivery_person_Ratings"].min(), df["Delivery_person_Ratings"].max(), df["Delivery_person_Ratings"].median())
Vehicle_condition = st.sidebar.selectbox("Vehicle Condition", df["Vehicle_condition"].unique())
multiple_deliveries = st.sidebar.slider("Multiple Deliveries", df["multiple_deliveries"].min(), df["multiple_deliveries"].max(), df["multiple_deliveries"].median())
Time_Orderd_hour = st.sidebar.slider("Time Ordered (Hour)", df["Time_Orderd_hour"].min(), df["Time_Orderd_hour"].max(), df["Time_Orderd_hour"].median())
distance = st.sidebar.slider("Distance (km)", df["distance"].min(), df["distance"].max(), df["distance"].median())
Festival = st.sidebar.selectbox("Is it a Festival?", options=["Yes","No"])
City = st.sidebar.selectbox("City Type",options=["Metropolitian","Urban","Semi-Urban"])

data = {
    "Type_of_order": [Type_of_order],
    "Type_of_vehicle": [Type_of_vehicle],
    "Festival": [Festival],
    "City": [City],
    "Delivery_city": [Delivery_city],
    "Road_traffic_density": [Road_traffic_density],
    "Weather_conditions": [Weather_conditions],
    "Delivery_person_Age": [Delivery_person_Age],
    "Delivery_person_Ratings": [Delivery_person_Ratings],
    "Vehicle_condition": [Vehicle_condition],
    "multiple_deliveries": [multiple_deliveries],
    "Time_Orderd_hour": [Time_Orderd_hour],
    "distance": [distance]
}

df = pd.DataFrame(data)

# Predict Button
if st.button("Predict Delivery Time"):
    try:
        # Apply the same preprocessing
        data_scaled = preprocessor.transform(df)
        prediction = model.predict(data_scaled)

        st.success(f"Estimated Delivery Time: {round(prediction[0], 2)} minutes ⏳")
    except Exception as e:
        st.error(f"Error: {e}")