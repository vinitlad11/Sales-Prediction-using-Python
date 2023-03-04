import numpy as np
import streamlit as st
import pickle
from warnings import filterwarnings
filterwarnings('ignore')

model = pickle.load(open('model.pkl', 'rb'))

st.title("Sales Prediction")

TV = st.number_input("Enter the advertising through TV: ")

radio = st.number_input("Enter the advertising through radio: ")

newspaper = st.number_input("Enter the advertising through newspaper: ")

if st.button('Predict'):
    # 1. predict
    result = float(model.predict(np.array([[TV, radio, newspaper]])))
    result = round(result, 3)
    # 2. Display
    st.header(f"Sales: {result}")
