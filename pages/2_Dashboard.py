from functools import partial
import duckdb
import pandas as pd
import streamlit as st
import os
from PIL import Image
from etl.data import factTable,data
from utils.graphs import histogram,scatter,boxPlot,pie
from utils.style import style

path_file = os.getcwd() + '/images/logo ikea.webp'
logo = Image.open(path_file)
st.set_page_config(
    page_title='Ikea | Dashboard',
    page_icon=logo,
    layout='wide'
)
style()
st.markdown('# <img src="https://raw.githubusercontent.com/IssamELMEHDI/Application-using-streamlit-Ikea-case/master/images/ikea%20logo.png" alt="Ikea Logo" width=100/> Dashboard',unsafe_allow_html=True)
st.markdown('<style> div.block-container {padding-top: 0.1rem;}</style>',unsafe_allow_html=True)

def check_change(text,expander_label,data_unique):
    if st.session_state[f"all_option_{text}{expander_label}"]:
        st.session_state[f"selected_options_{text}{expander_label}"] = list(data_unique.unique())
    else:
        st.session_state[f"selected_options_{text}{expander_label}"] = []
    return

def multi_change(text,expander_label,data):

    if len(st.session_state[f"selected_options_{text}{expander_label}"]) == len(list(data.unique())):
        st.session_state[f"all_option_{text}{expander_label}"] = True
    else:
        st.session_state[f"all_option_{text}{expander_label}"] = False
    return

def parameterize_SQL_in_statement(items):
    return f"""('{"', '".join(items)}')"""



duckdb_connection = duckdb.connect()

data=factTable(data)

cols = st.columns(2)
where_dict = {}
for i in range(len(cols)):
    with cols[i]:
        if i == 0:
            expander_label = "Categories"
            column_data = data['category']
            text = ""
        if i == 1:
            expander_label = "Produits"
            column_data = data['name']
            text = ""
        
        with st.expander(expander_label.replace('_',' ').capitalize()):
            # Get unique items in the column
            unique_items = column_data.unique()
            # Display the selected items
            if f"all_option_{text}{expander_label}" not in st.session_state:
                st.session_state[f"all_option_{text}{expander_label}"] = True
                st.session_state[f"selected_options_{text}{expander_label}"] = list(unique_items)
            # Display the selected items
            all = st.checkbox("Select all", key=f"all_option_{text}{expander_label}",on_change= partial(check_change, text, expander_label, column_data))
            options = st.multiselect('multiselected',list(unique_items),key=f"selected_options_{text}{expander_label}", on_change=partial(multi_change, text, expander_label, column_data), label_visibility="hidden")
            
            where_dict[expander_label]= st.session_state[f'selected_options_{text}{expander_label}']
            st.markdown(
"""
<style>
    [data-testid="stExpanderDetails"] {
        max-height: 200px;
        overflow-y: auto;
    }
</style>
""", unsafe_allow_html=True)

categories = parameterize_SQL_in_statement(where_dict["Categories"])
products = parameterize_SQL_in_statement(where_dict["Produits"])

where = f"""
    category IN {categories}
"""

price=f'''
SELECT name AS Produits, price AS Price FROM data

GROUP BY name , price
'''
price_for_products=duckdb_connection.execute(price).df()
histogram(x=price_for_products['Produits'],y=price_for_products['Price'],title='prix par produit')


scatter_query= f'''
SELECT width AS Width, height AS Height, depth AS Depth, name AS Produit
FROM data

'''
nueage_du_point = duckdb_connection.execute(scatter_query).df()
scatter(nueage_du_point, 'Width', 'Height', 'Produit', 'Depth')

price=f'''
SELECT name AS Produits, category AS Category FROM data
GROUP BY name , category
'''
name_category=duckdb_connection.execute(price).df()
histogram(x=name_category['Category'],y=name_category['Produits'],title='Categorie des produits')



box=f'''
SELECT price AS prix, category AS Category FROM data
GROUP BY price , category
'''
price_for_category=duckdb_connection.execute(box).df()
boxPlot(x=price_for_category['prix'],y=price_for_category['Category'],df=price_for_category)

# Sample DuckDB query
sellable_online_category_query = f"""
SELECT sellable_online, category, COUNT(*) AS count
FROM data
GROUP BY sellable_online, category;
"""

# Execute the query and obtain a DataFrame
sellable_online_category = duckdb_connection.execute(sellable_online_category_query).fetchdf()
# Use the pie function with the DuckDB data
pie(sellable_online_category, 'count', 'category')
