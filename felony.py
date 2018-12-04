# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 21:06:15 2018

@author: Riven
"""

import pandas as pd
import numpy as np

filename = "./dataset/felony2016.csv"
#read the csv file into panda
df = pd.read_csv(filename, sep=',', encoding='latin1')

df["IsJuvenile"] = 0
d_index = list(df.columns).index('IsJuvenile')

for index, row in df.iterrows():
    if row["AGE"]>0 and row["AGE"]<20:
       df.iloc[index,d_index] = '1'

df.to_csv('./dataset/felony2016_IsJuvenile.csv')
