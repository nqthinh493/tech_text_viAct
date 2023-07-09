import pandas as pd
import numpy as np

hierarchy_path = 'data\hierarchy.txt'
id_to_name_path = 'data\id_to_name.txt'

def convert_df_to_np(df):
    return df.to_numpy()

def convert_np_to_df(nparray):
    dataframe = pd.DataFrame(data=nparray)
    return dataframe

df_hie = pd.read_csv(hierarchy_path, sep=" ", header=None)
df_className = pd.read_csv(id_to_name_path, sep="\t", header=None)

HIERARCHY_NUMPY = convert_df_to_np(df_hie)
ID2NAME_NUMPY = convert_df_to_np(df_className)
# print(type(ID2NAME_NUMPY))