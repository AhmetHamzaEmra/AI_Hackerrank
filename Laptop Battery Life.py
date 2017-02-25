#!/bin/python3

import sys
from numpy import genfromtxt
import numpy as np
data = genfromtxt('trainingdata.txt', delimiter=',')

train=[]
label=[]
for i in range(len(data)):
    if data[i][0]<=4:

        a=[]
        a.append(float(data[i][0]))
        train.append(a)
        label.append(float(data[i][1]))

from sklearn import linear_model
clf = linear_model.LinearRegression()
clf.fit(train,label)

timeCharged = float(input().strip())
if timeCharged>4:
    print("8.00")
else:
    print((clf.predict(timeCharged))[0])
