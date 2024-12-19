import streamlit as st
import numpy as np

def predict_car_price(kilometrage, vitesse, puissance, condition):
    price = 20000 - (kilometrage * 0.05) + (vitesse * 150) + (puissance * 100)
    if condition == 'Neuf':
        price += 5000
    return price

background_image_path = 'bmwBraga-InChaALLAH.jpg'

background_style = f"""
<style>
body {{
background-image: url("file://{background_image_path}");
background-size: cover;
background-repeat: no-repeat;
background-attachment: fixed;
}}
</style>
"""

st.markdown(background_style, unsafe_allow_html=True)


st.title('Car Price Prediction Model')
st.write('Please enter the specifications of the car.')

col1, col2, col3 = st.columns(3)
with col1:
    kilometrage = st.number_input('Kilometrage', min_value=0, value=100000, step=1000)
with col2:
    vitesse = st.slider('Vitesse', min_value=0, max_value=300, value=150, step=10)
with col3:
    puissance = st.slider('Puissance', min_value=0, max_value=500, value=100, step=10)

condition = st.radio("Condition of the car:", ('Neuf', 'Occasion'))

if st.button('Predict Price'):
    st.spinner(text='Calculating...')
    predicted_price = predict_car_price(kilometrage, vitesse, puissance, condition)
    st.success(f"The predicted price of the car is ${predicted_price:.2f}")
else:
    st.write('Enter the car details to see the prediction.')
