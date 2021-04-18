import pandas as pd
import time


def predict(user_name,recom_df):
    predict_df=pd.read_csv('preprocessing_sample30.csv',index_col='Product')
    dataframe_df=predict_df[predict_df.index.isin(recom_df.loc[user_name].sort_values(ascending=False)[0:20].index)]
    time.sleep(6)
    return dataframe_df 
