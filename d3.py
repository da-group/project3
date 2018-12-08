####################################
# Author: Jiachi Zhang
# E-mail: zhangjiachi1007@gmail.com
####################################


import d3py
import pandas as pd
import numpy as np


def draw(mydata):
    x = [i for i in range(2011, 2018)]
    y = [mydata[mydata['YEAR']==i].shape[0] for i in x]
    df = pd.DataFrame({'x':x, 'y':y})
    fig = d3py.PandasFigure(df, name="Juvenile Arrest 2011-2017", width=1800, height=1200)
    fig += d3py.geoms.Line(x="x", y="y")
    fig += d3py.xAxis('x')
    fig += d3py.yAxis('y')
    fig.show()

    try:
        print "ctrl+c to exit"
        while(True):
            pass
    except KeyboardInterrupt:
        pass


def main():
    mydata = pd.read_csv('./dataset/juvenilearrests_tableau.csv', sep=',', encoding='latin1')
    draw(mydata)


if __name__ == '__main__':
    main()
