##########################################
# Author: Zheyi Wang
# E-mail: zeyikwong@gmail.com
##########################################

import plotly
plotly.tools.set_credentials_file(username='zeyikwong', api_key='AZ7Nv2rY5JYPvXGyA3Zb')

import plotly.plotly as py
import pandas as pd
import plotly.graph_objs as go

import numpy as np
import argparse
import pandas as pd

def getArguments():
    # get and parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', type=str, default='./dataset/juvenilearrests_tableau.csv', help='the file path')
    return parser.parse_args()


#############################
# determine the mean (mode if categorical), median, 
# and standard deviation of attributes in the dataset
def describe(data):
    # describe the nominal attributes, including the mode
    print(data.describe(include=[np.object]))
    # describe the numeric attributes, including the mean, median, std
    print(data.describe())

def clean(data):
    return data.dropna(axis = 0)

#############################
# draw the line plot trying to find out the relationship between Month and the number of juvenile crime
def drawLinePlot(myData):
    MONTHS = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    YEARS = {2011, 2012, 2013, 2014, 2015, 2016, 2017}

    data = []
    number = []

    for month in MONTHS:
        df = myData[myData['MONTH'] == month]
        grouped = df.groupby(['YEAR']).size().mean()
        number.append(grouped)

    # Create a trace for a scatterplot
    trace = go.Scatter(
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        y = number
    )
    # Assign it to an iterable object named myData
    data.append(trace)

    myLayout = go.Layout(
        title = "Juvenile Crime by Month",
        xaxis=dict(
            title = 'Month'
        ),
        yaxis=dict(
            title='Average number of crime',
            range = [200,300],
        )
    )

    # Setup figure
    myFigure = go.Figure(data=data, layout=myLayout)
    # Create the boxplot
    py.iplot(myFigure, filename = 'lineplot')

    
def main():
    args = getArguments()
    myData = pd.read_csv(args.f, sep=',', encoding='latin1')
    # summary of the data
    clean(myData)
    drawLinePlot(myData)


if __name__ == '__main__':
    main()
