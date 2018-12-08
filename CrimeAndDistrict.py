####################################
# Author: Jiachi Zhang
# E-mail: zhangjiachi1007@gmail.com
####################################


import pandas as pd
import numpy as np

import plotly
plotly.tools.set_credentials_file(username='milliondegree', api_key='PginxqCthBUcEn7bDhIp')

import plotly.plotly as py
import pandas as pd
import plotly.graph_objs as go


File = './dataset/crime2017_cleaned_preprocessed.csv'


def drawBar(data, title, xtitle, ytitle, filename):
    '''
    given data and text information, draw bar in plotly
    '''
    myLayout = go.Layout(
        barmode='group',
        title = title,
        xaxis = dict(
            title = xtitle
        ),
        yaxis = dict(
            title = ytitle
        )
    )
    myFigure = go.Figure(data=data, layout=myLayout)
    py.iplot(myFigure, filename=filename)


def safety(mydata, weight):
    safety = []
    for d in range(1, 8):
        s = 0.0;
        data = mydata[mydata['DISTRICT']==d]
        count = data['OFFENSE'].value_counts()
        for k in count.index:
            s += count[k]*weight[k-1]
        safety.append(-np.log(1.0/s))
    l = [safety[d-1] for d in mydata['DISTRICT'].values.astype('uint8')]
    mydata['SAFETY'] = pd.Series(l)
    return mydata


def draw(mydata):
    gr = mydata.groupby('DISTRICT')

    # draw number of countries of different income group in different region
    # use bar
    x = [key for key, _ in gr]
    vl = ['ARSON', 'ASSAULT W/DANGEROUS WEAPON', 'BURGLARY', 'HOMICIDE', 'MOTOR VEHICLE THEFT',
          'ROBBERY', 'SEX ABUSE', 'THEFT F/AUTO', 'THEFT/OTHER']
    yl = [[sum(group['OFFENSE']==v) for _, group in gr] for v in vl]
    data = [go.Bar(x=x, y=y, name=v) for y, v in zip(yl, vl)]
    drawBar(data, title='Crime type and districts',
            xtitle='District',
            ytitle='Number of crimes',
            filename='Crime and district'
            )


def main():
    mydata = pd.read_csv(File, sep=',', encoding='latin1')
    weight = [0.1, 0.1, 0.2, 0.5, 1.0, 0.9, 0.7, 0.7, 0.5]
    mydata = safety(mydata, weight)
    mydata.to_csv('./dataset/crime2017_safety.csv')

    data = pd.read_csv('./dataset/crime2017_cleaned.csv', sep=',', encoding='latin1')
    draw(data)


if __name__ == '__main__':
    main()
