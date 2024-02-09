import pandas as pd
import numpy as np
import os

from etl.extract import Extracts
from etl.transform import Transforms

#############################################################################
###                                                                       ###
###                             Extracts data                             ###
###                                                                       ###
#############################################################################

data = Extracts(os.getcwd() +'/data/ikea.csv','csv').load_data()

def fix_old_price(df):
    
    # fill in price to old_price for No old price
    if df['old_price']  == 'No old price':              
        return df['price']

    # remove SR and , from old_price                            
    elif df['old_price'][-4:] != 'pack':                
        return float(str(df['old_price'])[3:].replace(',','')) 
                                                               
    else:
        return np.nan

#############################################################################
###                                                                       ###
###                            Transform Data                             ###
###                                                                       ###
#############################################################################
def factTable(ikea):
    ikea=ikea.drop(['Unnamed: 0'],axis=1)
    median_depth=ikea.groupby('category')['depth'].median().reset_index()
    median_depth.columns = ['category','medianDepth']

    median_height=ikea.groupby('category')['height'].median().reset_index()
    median_height.columns = ['category','medianHeight']

    median_width=ikea.groupby('category')['width'].median().reset_index()
    median_width.columns = ['category','medianWidth']

    #median_size = pd.merge(pd.merge(median_depth,median_height,on='category'),median_width,on='category')
    median_size = Transforms(Transforms(median_depth,median_height,'category').transform_state(),median_width,'category').transform_state()

    #ikea=pd.merge(ikea,median_size,on='category')
    ikea=Transforms(ikea,median_size,'category').transform_state()
    ikea['depth']=ikea['depth'].fillna(ikea['medianDepth'])
    ikea['height']=ikea['height'].fillna(ikea['medianHeight'])
    ikea['width']=ikea['width'].fillna(ikea['medianWidth'])

    ikea.drop(['medianDepth','medianHeight','medianWidth'],axis=1 ,inplace=True)
    # create new colum price_diff to help identified is there any different
    # between price and old_price

    ikea['price_diff']=(ikea['old_price']!='no old price')

    #apply the function 
    ikea['old_price']=ikea.apply(fix_old_price,axis=1)
    ikea[['price','old_price','price_diff']]
    ikea['old_price']=ikea['old_price'].fillna(ikea['price'])
    
    return ikea



