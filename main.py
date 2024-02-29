import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load model and data
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv('Cleaned_Car_data (1).csv')

# Get unique values for dropdown options
companies = sorted(car['company'].unique())
car_models = sorted(car['name'].unique())
year = sorted(car['year'].unique(), reverse=True)
fuel_type = car['fuel_type'].unique()

# Set page title and background color
st.set_page_config(page_title="Car Price Prediction", page_icon="🚗", layout="centered", initial_sidebar_state="collapsed")
st.markdown(
    """
    <style>
    .reportview-container {
        background: #624f9c;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.title('Car Price Prediction')
st.write("Welcome to the Car Price Prediction App! Select the car details below and click 'Predict' to see the estimated price.")

# Dropdown widgets for selecting car details
selected_company = st.selectbox('Select Company', companies[1:], help="Select the manufacturer company of the car.")
selected_car_model = st.selectbox('Select Car Model', car_models, help="Select the model of the car.")
selected_year = st.selectbox('Select Year', year, help="Select the manufacturing year of the car.")
selected_fuel_type = st.selectbox('Select Fuel Type', fuel_type, help="Select the fuel type of the car.")
kilo_driven = st.number_input('Enter Kilometers Driven', value=1000, help="Enter the total kilometers driven by the car.")

# Prediction button with some style enhancements
btn_predict = st.button('Predict')
if btn_predict:
    prediction = model.predict(pd.DataFrame({'name': [selected_car_model],
                                              'company': [selected_company],
                                              'year': [selected_year],
                                              'kms_driven': [kilo_driven],
                                              'fuel_type': [selected_fuel_type]}))
    st.success(f'Predicted Price: {np.round(prediction[0], 2)}')
