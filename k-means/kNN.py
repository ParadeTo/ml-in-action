# -*- coding:utf-8 -*-
from numpy import tile, zeros, shape
import operator


def classify0(inX, dataSet, labels, k):
    """
    knn分类函数
    :param inX: 待分类的向量
    :param dataSet: 样本数据集
    :param labels: 样本数据对应的分类向量
    :param k: 最近邻数目
    :return: 类别标签
    """
    # 得到数据大小
    dataSetSize = dataSet.shape[0]

    # 欧氏距离
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5

    # [-1 -1 -7] => [2 0 1]
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        """
            {
                "label1": 34,
                 "label2": 23,
                 "label3": 35
            }
        """
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1

    """
        [('label3', 35), ('label1', 34), ('label2', 23)]
    """
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
    pass

def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())         #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

def autoNorm(dataSet):
    """
    [
        [ 1  1 -2]
        [-2 -2 -5]
    ]
    
    [-2 -2 -5]
    [ 1  1 -2]
    """
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet / tile(ranges, (m,1))   #element wise divide
    return normDataSet, ranges, minVals