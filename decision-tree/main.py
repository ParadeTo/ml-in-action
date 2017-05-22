# -*- coding: utf-8 -*-
import tree
import treePlotter

myDat, labels = tree.createDataSet()

print myDat, labels

print tree.calcShannonEnt([
            [1, 1, 'yes'],
            [1, 1, 'yes'],
            [1, 0, 'no'],
            [0, 1, 'no'],
            [0, 1, 'no']])

print tree.calcShannonEnt([
            [1, 1, 'yes'],
            [1, 1, 'yes'],
            [1, 0, 'yes'],
            [0, 1, 'yes'],
            [0, 1, 'yes']])

print tree.splitDataSet([
            [1, 1, 'yes'],
            [1, 1, 'yes'],
            [1, 0, 'no'],
            [0, 1, 'no'],
            [0, 1, 'no']], 0 ,1)

print tree.chooseBestFeatureToSplit([
            [1, 1, 'yes'],
            [1, 1, 'yes'],
            [1, 0, 'no'],
            [0, 1, 'no'],
            [0, 1, 'no']])

print tree.createTree([
            [1, 1, 'yes'],
            [1, 1, 'yes'],
            [1, 0, 'no'],
            [0, 1, 'no'],
            [0, 1, 'no']],['No Surfacing?', 'Flippers?'])


t = {'No Surfacing?': {0: 'no', 1: {'Flippers?': {0: 'no', 1: 'yes'}}}}
print treePlotter.getNumLeafs(t)
print treePlotter.getTreeDepth(t)

treePlotter.createPlot(t)

print tree.classify({'No Surfacing?': {0: 'no', 1: {'Flippers?': {0: 'no', 1: 'yes'}}}}, ['No Surfacing?', 'Flippers?'], [1,0])