import streamlit as st


def style():
    st.markdown("""
        <style>

            @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap')

            .poppins-thin {
                font-family: "Poppins", sans-serif;
                font-weight: 100;
                font-style: normal;
            }

            .poppins-extralight {
                font-family: "Poppins", sans-serif;
                font-weight: 200;
                font-style: normal;
            }

            .poppins-light {
                font-family: "Poppins", sans-serif;
                font-weight: 300;
                font-style: normal;
            }

            .poppins-regular {
                font-family: "Poppins", sans-serif;
                font-weight: 400;
                font-style: normal;
            }

            .poppins-medium {
                font-family: "Poppins", sans-serif;
                font-weight: 500;
                font-style: normal;
            }

            .poppins-semibold {
                font-family: "Poppins", sans-serif;
                font-weight: 600;
                font-style: normal;
            }

            .poppins-bold {
                font-family: "Poppins", sans-serif;
                font-weight: 700;
                font-style: normal;
            }

            .poppins-extrabold {
                font-family: "Poppins", sans-serif;
                font-weight: 800;
                font-style: normal;
            }

            .poppins-black {
                font-family: "Poppins", sans-serif;
                font-weight: 900;
                font-style: normal;
            }

            .poppins-thin-italic {
                font-family: "Poppins", sans-serif;
                font-weight: 100;
                font-style: italic;
            }

            .poppins-extralight-italic {
                font-family: "Poppins", sans-serif;
                font-weight: 200;
                font-style: italic;
            }

            .poppins-light-italic {
                font-family: "Poppins", sans-serif;
                font-weight: 300;
                font-style: italic;
            }

            .poppins-regular-italic {
                font-family: "Poppins", sans-serif;
                font-weight: 400;
                font-style: italic;
            }

            .poppins-medium-italic {
                font-family: "Poppins", sans-serif;
                font-weight: 500;
                font-style: italic;
            }

            .poppins-semibold-italic {
                font-family: "Poppins", sans-serif;
                font-weight: 600;
                font-style: italic;
            }

            .poppins-bold-italic {
                font-family: "Poppins", sans-serif;
                font-weight: 700;
                font-style: italic;
            }

            .poppins-extrabold-italic {
                font-family: "Poppins", sans-serif;
                font-weight: 800;
                font-style: italic;
            }

            .poppins-black-italic {
                font-family: "Poppins", sans-serif;
                font-weight: 900;
                font-style: italic;
            }

            .espace_1{
                height: 200px;
            }

            .espace_2{
                height: 50px;
            }

            label p{
                font-family: "Poppins", sans-serif;
                font-weight: 900;
                font-style: normal;
                font-size: 1.5em !important;
            }

            button p{

                font-family: "Poppins", sans-serif;
                font-weight: 900;
                font-style: normal;
                font-size: 2em !important;
            }

            tr th {
                background-color: purple;
                color: white;
            }

            th, td {
                text-align: center !important;
            }

            th {
                font-weight: bold !important;
                font-size: 30px;
            }

            tr:hover {
                background-color: #07F;
            }

            td:hover {
                background-color: rgba(0, 230, 250, 0.89);
                color: blue;
            }

            tr {
                font-family: math;
                font-size: 24px;
            }

            h1, h2, h3, h4, h5, h6, button p, a p {
                font-family: "Poppins", sans-serif;
            }
            div.block-container {padding-top: 0.1rem;}

            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}

            .main-title {
                    text-align: center
            }

            .logos {
                background-color: #fff;
                height: 6em;
                display: flex;
                justify-content: space-between;
                align-items: center;
                box-shadow: 0 4px 8px 0 rgba(0, 230, 250, 0.89), 0 6px 20px 0 rgba(255, 0, 240, 0.7);
                border-radius: 5px 5px 5px 5px;
                margin-bottom: 30px;
            }

            .logos img:nth-child(odd) {
                width:5em;
                height: 90%;

            }

            .logos img:nth-child(even) {
                width:8em;
                height: 90%;
            }

            @media screen and (min-width: 780px) {
                .logos {
                    height: 8em;

                }
                .logos img:nth-child(odd) {
                    width:7em;


                }

                .logos img:nth-child(even) {
                    width:15em;

                }
            }

            @media screen and (min-width: 992px) {
                .logos {

                    height: 10em;

                }
                .logos img:nth-child(odd) {
                    width:9em;

                }

                .logos img:nth-child(even) {
                    width:22em;

                }
            }

            @media screen and (min-width: 1200px) {
                .logos {
                    height: 12em;

                }
                .logos img:nth-child(odd) {
                    width:9em;
                    height: 80%;
                }

                .logos img:nth-child(even) {
                    width:20em;
                    height: 70%;

                }
            }

        </style>
    """,unsafe_allow_html=True)