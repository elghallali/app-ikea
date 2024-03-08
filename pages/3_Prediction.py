import streamlit as st
import numpy as np
import joblib
import os
from PIL import Image

from utils.style import style
path_file = os.getcwd() + '/images/logo ikea.webp'
logo = Image.open(path_file)
st.set_page_config(
    page_title='Ikea | Prediction',
    page_icon=logo,
    layout='wide'
)

style()
st.markdown('# <img src="https://raw.githubusercontent.com/IssamELMEHDI/Application-using-streamlit-Ikea-case/master/images/ikea%20logo.png" alt="Ikea Logo" width=100/> Prediction',unsafe_allow_html=True)
st.markdown('<style> div.block-container {padding-top: 0.1rem;}</style>',unsafe_allow_html=True)
st.markdown("""
<div class="espace_1"></div>
""",unsafe_allow_html=True)
insert_cols = st.columns(3, gap="large")
with insert_cols[0]:
    width = st.number_input('Insert a width (cm)')
with insert_cols[1]:
    height = st.number_input('Insert a height (cm)')
with insert_cols[2]:
    depth = st.number_input('Insert a depth (cm)')



mul_reg=open(os.getcwd() + "/utils/linear_regression_model_ikea.pkl","rb")
ml_model=joblib.load(mul_reg)
volume=width*height*depth
pred_args = [volume]
pred_arr = np.array(pred_args)
preds = pred_arr.reshape(1,-1)
model_prediction = ml_model.predict(preds)
model_prediction = round(float(model_prediction), 2)
st.markdown("""
<div class="espace_2"></div>
""",unsafe_allow_html=True)
prediction_col=st.columns([2,3,2])
with prediction_col[1]:
    prediction= st.button('Prediction',use_container_width=True)

st.markdown("""
<div class="espace_2"></div>
""",unsafe_allow_html=True)
if prediction:
    if volume == 0:
        st.markdown(f"""
<center>
                    
<div style="font-size: 900 !important;"> SR 0 </div>
                    
</center>
""",unsafe_allow_html=True)
    else:
        st.markdown(f"""
<center>
                    
SR {model_prediction}
                    
</center>
""",unsafe_allow_html=True)
        
        

