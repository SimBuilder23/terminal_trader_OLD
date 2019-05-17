#!/usr/bin/env python3

import csv

import numpy as np
import pandas as pd


df = pd.read_csv('UBER.csv')

"""print(df.shape)
print(df.describe())
print (df)"""

df1 = pd.DataFrame({'date':[1., 2., 3., 4.],
                    'open':[1., 2., 3., 4.],
                    'high':[1., 2., 3., 4.],
                    'low':[1., 2., 3., 4.],
                    'close':[1., 2., 3., 4.],
                    'adj_close':[1., 2., 3., 4.],
                    'volume':[1., 2., 3., 4.]})
#print (df1.describe())

d = {'date':[],
    'open':[],
    'high':[],
    'low':[],
    'close':[],
    'adj_close':[],
    'volume':[]}

with open ("UBER.csv", "r") as f:
    rows = csv.reader(f)
    next(rows)
    for row in rows:
        d['date'].append(row[0])
        d['open'].append(row[1])
        d['high'].append(row[2])
        d['low'].append(row[3])
        d['close'].append(row[4])
        d['adj_close'].append(row[5])
        d['volume'].append(row[6])



df2 = pd.DataFrame(d, index=list('xyza'))

if __name__ == '__main__':
    print (df2)


