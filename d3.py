####################################
# Author: Jiachi Zhang
# E-mail: zhangjiachi1007@gmail.com
####################################

'''
Because I cannot install d3py on python3. I only test this file in python 2.7
'''


import d3py
import pandas as pd
import numpy as np


def drawLine(mydata):
    '''
    draw a d3 graph to show every years' juvenile crime numbers
    save the snapshot as juvenile_crime_number_d3.png
    '''
    x = [i for i in range(2011, 2018)]
    y = [mydata[mydata['YEAR']==i].shape[0] for i in x]
    df = pd.DataFrame({'x':x, 'y':y})
    fig = d3py.PandasFigure(df, name="Juvenile Arrest 2011-2017", width=1200, height=900)
    fig += d3py.geoms.Line(x="x", y="y")
    fig += d3py.xAxis('x')
    fig += d3py.yAxis('y')
    fig.show()

    try:
        while(True):
            pass
    except KeyboardInterrupt:
        pass


def drawDistrict(mydata):
    '''
    draw a d3 graph to show every districts' crime number in 2017
    save the snapshot as districts_crime_number_d3.png
    '''
    x = [np.str(i) for i in range(1, 8)]
    y = [mydata[mydata['DISTRICT']==i].shape[0] for i in range(1, 8)]
    df = pd.DataFrame({'x':x, 'y':y})
    with d3py.PandasFigure(df, name='District crime number') as fig:
        fig += d3py.geoms.Line(x="x", y="y")
        fig += d3py.xAxis('x')
        fig += d3py.yAxis('y')
        fig.show()


def main():
    mydata = pd.read_csv('./dataset/juvenilearrests_tableau.csv', sep=',', encoding='latin1')
    drawLine(mydata)
    mydata = pd.read_csv('./dataset/crime2017_cleaned_preprocessed.csv', sep=',', encoding='latin1')
    drawDistrict(mydata)


if __name__ == '__main__':
    main()
