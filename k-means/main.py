# -*- coding:utf-8 -*-
from numpy import *

import kNN as kNN
import matplotlib
import matplotlib.pyplot as plt

datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')

# print datingDataMat, datingLabels



plt.figure()
l = plt.scatter(datingDataMat[:,1], datingDataMat[:,2], 6*array(datingLabels), (datingLabels), label='1')
plt.axis([-2,25,-0.2,2.0])
plt.xlabel('Percentage of Time Spent Playing Video Games')
plt.ylabel('Liters of Ice Cream Consumed Per Week')
plt.show()
