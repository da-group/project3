# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 22:09:06 2018

@author: Riven
"""

import plotly
plotly.tools.set_credentials_file(username='rivenseiun',api_key='NffxDyNVpgZAIDLPueWY')

import plotly.plotly as py
import pandas as pd
import plotly.graph_objs as go



meta1= pd.read_csv('./dataset/crime2017_safety.csv')


#1.Pie chart
#get value counts for every income group

counts = meta1['METHOD'].value_counts(sort = False)

print(counts)





#put these groups into a plot 
methods = go.Pie(labels =["Others","Knife","Gun"],
	values = counts,
    hoverinfo='label+percent', 
    textinfo='value', 
	name = "Methods of Crime"
)


myData = [methods]



# Setup figure
myFigure = go.Figure(data=myData)

# Create the scatterplot
py.iplot(myFigure, filename='CrimeMethods')




