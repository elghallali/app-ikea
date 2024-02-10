import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import os
import io
import warnings
from etl.data import factTable

from etl.loads import Loads

warnings.filterwarnings('ignore')

path_file = os.getcwd() + '/images/logo ikea.webp'
logo = Image.open(path_file)

path_location = os.getcwd() + '/images/ikea place.webp'
location = Image.open(path_location)

st.set_page_config(
    page_title='Ikea | Home',
    page_icon=logo,
    layout='wide'
)

st.markdown('# <img src="https://raw.githubusercontent.com/IssamELMEHDI/Application-using-streamlit-Ikea-case/master/images/ikea%20logo.png" alt="Ikea Logo" width=100/> Application',unsafe_allow_html=True)
st.markdown('<style> div.block-container {padding-top: 0.1rem;}</style>',unsafe_allow_html=True)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            /*footer {visibility: hidden;}*/
            header {visibility: hidden;}
            </style>
            """
            
st.markdown(hide_st_style, unsafe_allow_html=True)
st.image("https://www.ikea.com/images/13/b5/13b5ceaa3d91329b9172ee94b8684a63.jpg?f=sg")

with st.container():
    
    col_team0, col_team1, col_team2, col_team3 = st.columns([1,4,4,1])
    with col_team1:
        st.markdown("""
                <style>
                    .centered-header {
                        text-align: center;
                    }
                </style>
            """, unsafe_allow_html=True)
        st.markdown('<h2 class="centered-header">Team</h2>', unsafe_allow_html=True)
        team = pd.DataFrame({'Name':['Yassine EL GHALLALI', 'Rabia SLAOUI', 'Issam EL MEHDI', 'Said SEHLALI']})
        fig = ff.create_table(team, height_constant=60, colorscale=[[0, '#e5989b'],[.5, '#ffddd2'],[1, '#ffffff']])
        fig.update_layout(font=dict(size=30))
        st.plotly_chart(fig, use_container_width=True)
    with col_team2:
        st.markdown("""
                <style>
                    .centered-header {
                        text-align: center;
                    }
                </style>
            """, unsafe_allow_html=True)
        st.markdown('<h2 class="centered-header">Proposed by</h2>', unsafe_allow_html=True)
        team = pd.DataFrame({'Prof':['Mohamed Bakhat']})
        fig = ff.create_table(team, height_constant=60, colorscale=[[0, '#e5989b'],[.5, '#ffddd2'],[1, '#ffffff']])
        fig.update_layout(font=dict(size=30))
        st.plotly_chart(fig, use_container_width=True)
    st.header('Description')


    st.markdown("""
                <footer>
                <h2 class="centered-header">Realised by slaoui rabia</h2>
                </footer>
                """, unsafe_allow_html=True)
    # pour etre tjrs sur le footer

    df = pd.read_csv(os.getcwd() + '/data/ikea.csv')
    st.dataframe(df)
    
# test load

data_load=st.button('data load')
if data_load:
    Loads(factTable(df),'data/','ikeaLoad.csv').send_to_csv()

