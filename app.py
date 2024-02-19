#!/usr/bin/env python
# coding: utf-8

# In[43]:


#pip install streamlit


# In[44]:


#pip install joblib


# In[45]:


#!pip install --upgrade scikit-learn


# In[46]:


import streamlit as st
import joblib
from joblib import load


# In[47]:


# Write the title of the application on the UI
st.write("""
# Used Car Price Predictor
""")

# Specify the absolute path to the model file
model_path = 'C:/Users/PC/Atomcamp/Project/compressed.model.joblib'

# Load the model
try:
    reg_model = joblib.load(model_path)
    st.write("Model loaded successfully!")
except FileNotFoundError:
    st.error(f"Model file not found at: {model_path}")
except Exception as e:
    st.error(f"Error loading model: {e}")


# Input fields for numerical variables
years_used = st.slider("Years Used", min_value=0, max_value=20, step=1)
kilometers_driven = st.number_input("Kilometers Driven", value=0)
mileage = st.number_input("Mileage (kmpl)", value=0.0)
engine_cc = st.number_input("Engine (CC)", value=0)
power_bhp = st.number_input("Power (bhp)", value=0.0)
seats = st.slider("Seats", min_value=2, max_value=10, step=1)
number_of_owners = st.selectbox("Number of Owners", [1, 2, 3, 4])

# Dropdowns for categorical variables
fuel_type = st.selectbox("Fuel Type", ["Diesel", "Petrol", "CNG", "LPG"])
transmission_type = st.selectbox("Transmission Type", ["Manual", "Automatic"])

# Create a button to trigger the prediction
if st.button("Predict Price"):
    # Prepare the input features
    input_features = [[years_used, kilometers_driven, mileage, engine_cc, power_bhp, seats, number_of_owners]]
    
    # Make the prediction 
    predicted_price = reg_model.predict(input_features)

    # Display the result on the UI
    st.text("Predicted price of the car: " + str(predicted_price) + " Lakh INR")


# In[ ]:





# In[ ]:


#model_path = r"C:/Users/PC/Atomcamp/Project/compressed.model.joblib"
#with open(model_path, "rb") as file:
    #reg_model = joblib.load(file)
    

