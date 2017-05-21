from numpy import tile
import operator

dataSet = [
    [1,2,3],
    [4,5,6]
]

diffMat = tile([2,3,1], (2, 1)) - dataSet

print diffMat
print diffMat.min(0)
print diffMat.max(0)

print diffMat
print diffMat.sum(axis=0)
print (diffMat.sum(axis=0)).argsort()


dict = {}
dict["label1"] = 11
dict["label2"] = 222

print (dict)
sortedClassCount = sorted(dict.iteritems(), key=operator.itemgetter(1), reverse=True)
print sortedClassCount