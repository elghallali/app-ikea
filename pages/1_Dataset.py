import streamlit as st
from PIL import Image
import pandas as pd
import os
import glob
import io
import warnings


from etl.data import *
from utils.style import style

warnings.filterwarnings('ignore')

path_file = os.getcwd()+ '/images/logo ikea.webp'
logo = Image.open(path_file)

st.set_page_config(
    page_title='IKEA | Dataset',
    page_icon=logo,
    layout='wide'
)
style()
st.markdown('# <img src="https://raw.githubusercontent.com/IssamELMEHDI/Application-using-streamlit-Ikea-case/master/images/ikea%20logo.png" alt="Ikea Logo" width=100/> Dataset',unsafe_allow_html=True)
st.markdown('<style> div.block-container {padding-top: 0.1rem;}</style>',unsafe_allow_html=True)



def visualDataFrame(df):
    options = st.multiselect(
        'Dataset columns',
        list(df.columns),list(df.columns), label_visibility="hidden")
    tab1, tab2, tab3, tab4 = st.tabs([":card_file_box: Data", "Types", 'NAN', 'Info'])
    with tab1:

        st.dataframe(df[options])
    with tab2:

        st.text(df[options].dtypes)
    with tab3:

        st.text(df[options].isna().sum())
    with tab4:

        buffer = io.StringIO()
        df[options].info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

st.subheader('Dataset before ETL Process')
visualDataFrame(data)

st.subheader('Dataset after ETL Process')
visualDataFrame(factTable(data))