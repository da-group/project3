# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 22:44:07 2018

@author: Riven
"""
import plotly
plotly.tools.set_credentials_file(username='rivenseiun',api_key='NffxDyNVpgZAIDLPueWY')

import plotly.plotly as py
import pandas as pd
import plotly.graph_objs as go

import pandas as pd
import numpy as np


filename = "./dataset/juvenilearrests.csv"
#read the csv file into panda
df = pd.read_csv(filename, sep=',', encoding='latin1')

#add a new column district 
df["District"] = 0
d_index = list(df.columns).index('District')

for index, row in df.iterrows():
    a =  str(row["CRIME_PSA"])[0]
    for d in range(1, 8):
        if a == str(d):
            df.iloc[index,d_index] = str(d)




#add a new column year

df["Year"] = "2011"
d_index = list(df.columns).index('Year')

for index, row in df.iterrows():
    a =  str(row["ARREST_DATE"])[0:4]
    for d in range(2010, 2018):
        if a == str(d):
            df.iloc[index,d_index] = a


#remove the rows with psa = jpc
df = df[df["CRIME_PSA"]!="JPC"]


counts = df['Year'].value_counts(sort = False)
counts = counts.sort_index()


# Create a trace for a scatterplot
trace = go.Scatter(
	x = ["2011","2012","2013","2014","2015","2016","2017"],
	y = counts,
	mode = 'lines'
)

# Assign it to an iterable object named myData
myData = [trace]

# Add axes and title
myLayout = go.Layout(
	title = "Juvenile Arrests 2011-2017",
	xaxis=dict(
		title = 'Year'
	),
	yaxis=dict(
		title = 'Num of Juvenile Arrests'
	)
)

# Setup figure
myFigure = go.Figure(data=myData, layout=myLayout)

# Create the scatterplot
py.iplot(myFigure, filename='Juvenile Arrests 2011-2017')



df.to_csv('./dataset/juvenile_district.csv')


