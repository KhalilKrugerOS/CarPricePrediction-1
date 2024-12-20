import streamlit as st
import numpy as np
import pickle
import os
import base64
import sklearn
print(sklearn.__version__)


def load_model(model_path):
    if not os.path.exists(model_path):
        st.error(f"Model file not found at: {model_path}")
        st.stop()
    try:
        with open(model_path, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        st.stop()


def get_base64_encoded_image(image_path):
    if not os.path.exists(image_path):
        return None
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


# Load model
model = load_model('best_gb_reg.pkl')

# Set background
background_image = get_base64_encoded_image('bmwBraga-InChaALLAH.jpg')
if background_image:
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{background_image}");
            background-size: cover;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.title('Car Price Prediction Model')
st.write('Please enter the specifications of the car.')

col1, col2, col3 = st.columns(3)
with col1:
    kilometrage = st.number_input(
        'Kilometrage', min_value=0, max_value=1000000, value=100000, step=1000)
with col2:
    vitesse = st.slider('Vitesse', min_value=0,
                        max_value=300, value=150, step=10)
with col3:
    puissance = st.slider('Puissance', min_value=0,
                          max_value=500, value=100, step=10)

condition = st.radio("Condition of the car:", ('Neuf', 'Occasion'))

if st.button('Predict Price'):
    with st.spinner('Calculating...'):
        X = np.array(
            [[kilometrage, vitesse, puissance, 1 if condition == 'Neuf' else 0]])
        predicted_price = model.predict(X)[0]
    st.success(f"The predicted price of the car is ${predicted_price:,.2f}")
else:
    st.write('Enter the car details to see the prediction.')
