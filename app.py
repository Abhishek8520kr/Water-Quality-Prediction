import pandas as pd
import numpy as np
import joblib
import pickle
import streamlit as st

model = joblib.load("pollution_model.pkl")
model_cols = joblib.load("model_columns.pkl")

st.title("water pollutants predictor")
st.write("predict the water pollutants based on year and station ID")

year_input = st.number_input("enter year")
station_id = st.text_input("enter station ID")
