import streamlit as st
import numpy as np
import joblib
import os
from PIL import Image
path_file = os.getcwd() + '/images/logo ikea.webp'
logo = Image.open(path_file)
st.set_page_config(
    page_title='Ikea | Prediction',
    page_icon=logo,
    layout='wide'
)

st.markdown('# <img src="https://raw.githubusercontent.com/RabiaaSL00/app-ikea/main/images/logo%20ikea.webp" alt="Ikea Logo" width=100/> Ikea Prediction',unsafe_allow_html=True)
st.markdown('<style> div.block-container {padding-top: 0.1rem;}</style>',unsafe_allow_html=True)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            /*footer {visibility: hidden;}*/
            header {visibility: hidden;}
            </style>
            """
            
st.markdown(hide_st_style, unsafe_allow_html=True)
width = st.number_input('Insert a width')
height = st.number_input('Insert a height')
depth = st.number_input('Insert a depth')
# Définir la largeur souhaitée du bouton (en pixels)
largeur_bouton = 200

# Utiliser st.markdown pour intégrer du code HTML/CSS
st.markdown(
    f"""
    <style>
        .custom-button {{
            width: {largeur_bouton}px;
        }}
    </style>
    """,
    unsafe_allow_html=True
)
mul_reg=open(os.getcwd() + "/utils/linear_regression_model_ikea.pkl","rb") # linux /
ml_model=joblib.load(mul_reg) 
volume=width*height*depth
pred_args = [volume]
pred_arr = np.array(pred_args)
preds = pred_arr.reshape(1,-1)
model_prediction = ml_model.predict(preds)
model_prediction = round(float(model_prediction), 2)
prediction_col=st.columns([2,1,2])
with prediction_col[1]:
    prediction= st.button('Prediction',use_container_width=True,key="custom-button")
if prediction:
    st.write(model_prediction)
####"#
    
