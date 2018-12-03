####################################
# Author: Jiachi Zhang
# E-mail: zhangjiachi1007@gmail.com
####################################


import pandas as pd
import numpy as np

File = './dataset/crime2017_cleaned_preprocessed.csv'

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


def main():
    mydata = pd.read_csv(File, sep=',', encoding='latin1')
    weight = [0.1, 0.1, 0.2, 0.5, 1.0, 0.9, 0.7, 0.7, 0.5]
    mydata = safety(mydata, weight)
    mydata.to_csv('./dataset/crime2017_safety.csv')


if __name__ == '__main__':
    main()
