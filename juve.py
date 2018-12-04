# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 22:44:07 2018

@author: Riven
"""

import pandas as pd
import numpy as np
import d3py

filename = "./dataset/juvenilearrests.csv"
#read the csv file into panda
df = pd.read_csv(filename, sep=',', encoding='latin1')

df["District"] = 0
d_index = list(df.columns).index('District')

for index, row in df.iterrows():
    a =  str(row["CRIME_PSA"])[0]
    for d in range(1, 8):
        if a == str(d):
            df.iloc[index,d_index] = str(d)


df = df[df["CRIME_PSA"]!="JPC"]
df.to_csv('./dataset/juvenile_district.csv')
